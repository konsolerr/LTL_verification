from ltlFormula.formulas import  UntilFormula
from utils import powerset
from ltlFormula.formulas import *


def curr1(f: Formula):
    if isinstance(f, UntilFormula):
        return {f.children[0]}
    elif isinstance(f, (OrFormula, ReleaseFormula)):
        return {f.children[1]}


def next1(f: Formula):
    if isinstance(f, (UntilFormula, ReleaseFormula)):
        return {f}
    if isinstance(f, OrFormula):
        return set()


def curr2(f: Formula):
    if isinstance(f, UntilFormula):
        return {f.children[1]}
    if isinstance(f, ReleaseFormula):
        return {f.children[0], f.children[1]}
    if isinstance(f, OrFormula):
        return {f.children[0]}


class LabeledGeneralisedBuchiAutomaton(object):
    def __init__(self, qu, sigma, delta, qu0, f, aps):
        self.qu = qu
        self.sigma = sigma
        self.delta = delta
        self.qu0 = qu0
        self.f = f
        self.aps = aps

    @classmethod
    def from_nodes(cls, formula, nodes, now, incoming, init, aps=None):

        qu = nodes
        if not aps:
            aps = formula.get_ap()
        neg_aps = {ap.negative_propagation() for ap in aps}

        sigma = {}
        for node in nodes:
            z0 = now[node] & aps
            z1 = {ap.negative_propagation() for ap in neg_aps - now[node]}
            sigma[node] = (z0, z1)

        delta = {}
        for q1 in nodes:
            for q2 in nodes:
                if q1 in incoming[q2]:
                    delta[q1] = delta.get(q1, [])
                    delta[q1].append(q2)

        qu0 = set()
        for q in nodes:
            if init in incoming[q]:
                qu0 = qu0 | {q}

        closure = formula.get_closure()

        f = [
            {q for q in nodes if g.children[1] in now[q] or g not in now[q]}
            for g in closure if isinstance(g, UntilFormula)
        ]

        return LabeledGeneralisedBuchiAutomaton(qu, sigma, delta, qu0, f, aps)

    @classmethod
    def from_formula(cls, formula: Formula, aps=None):

        class Node(object):
            total = 0

            def __init__(self, name=None):
                self.name = name
                self.id = Node.total
                Node.total += 1
                super().__init__()

            def __repr__(self):
                if self.name:
                    return "<Node #{} \"{}\">".format(self.id, self.name)
                return "<Node #{}>".format(self.id)

        NODES = set()
        INCOMING = {}
        NOW = {}
        NEXT = {}

        def expand(curr: set,
                   old: set,
                   next: set,
                   incoming: set):

            nonlocal NODES
            nonlocal INCOMING
            nonlocal NOW
            nonlocal NEXT

            if len(curr) == 0:
                q_exists = False
                for q in NODES:
                    if NEXT[q] == next and NOW[q] == old:
                        INCOMING[q] = INCOMING[q] | incoming
                        q_exists = True
                        break
                if not q_exists:
                    q = Node()
                    NODES.add(q)
                    INCOMING[q] = incoming
                    NOW[q] = old | set()
                    NEXT[q] = next | set()
                    expand(NEXT[q], set(), set(), {q})
            else:
                f = iter(curr).__next__()
                curr = curr - {f}
                old = old | {f}

                if isinstance(f, (TerminalFormula, NotFormula)):
                    if f == Formula.FALSE or f.negative_propagation() in old:
                        pass
                    else:
                        expand(curr, old, next, incoming)
                elif isinstance(f, AndFormula):
                    expand(curr | ({f.children[0], f.children[1]} - old), old, next, incoming)
                elif isinstance(f, NextFormula):
                    expand(curr, old, next | {f.children[0]}, incoming)
                elif isinstance(f, (OrFormula, UntilFormula, ReleaseFormula)):
                    expand(curr | (curr1(f) - old), old, next | next1(f), incoming)
                    expand(curr | (curr2(f) - old), old, next, incoming)

        def create_graph():
            init = Node("init")
            expand({formula}, set(), set(), {init})
            return NODES, NOW, INCOMING, init

        nodes, now, incoming, init = create_graph()
        return LabeledGeneralisedBuchiAutomaton.from_nodes(formula, nodes, now, incoming, init, aps)


class BuchiAutomaton(object):
    def __init__(self, nodes, aps, delta, starts, ends):
        self.nodes = nodes
        self.aps = aps
        self.delta = delta
        self.starts = starts
        self.ends = ends

    @classmethod
    def from_labeled(cls, labeled_automaton: LabeledGeneralisedBuchiAutomaton):

        class CountingNode(object):
            def __init__(self, node, i):
                self.node = node
                self.i = i

            def __repr__(self):
                return "{} - {}".format(self.node, self.i)

            def __eq__(self, other):
                return self.node is other.node and self.i == other.i

            def __hash__(self):
                return hash(self.node) + hash(self.i)

        n = len(labeled_automaton.f)
        nodes = set()
        starts = set()
        for q in labeled_automaton.qu:
            for i in range(n):
                cn = CountingNode(q, i + 1)
                if q in labeled_automaton.qu0 and i == 0:
                    starts.add(cn)
                nodes.add(cn)

        delta = {}
        for node in labeled_automaton.sigma:
            aps = labeled_automaton.sigma[node]
            outgoing = labeled_automaton.delta[node]

            for i, f in enumerate(labeled_automaton.f):
                a = i + 1
                if node in f:
                    b = a % n + 1
                else:
                    b = a

                for out_node in outgoing:
                    kek = delta.get(CountingNode(node, a), {})
                    kek[CountingNode(out_node, b)] = aps
                    delta[CountingNode(node, a)] = kek

        ends = [CountingNode(node, 1) for node in labeled_automaton.f[0]]
        return BuchiAutomaton(nodes, labeled_automaton.aps, delta, starts, ends)





