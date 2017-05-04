from LTL_formula.formulas import *
from pprint import pprint


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
        return {f.children[0], f.children[0]}
    if isinstance(f, OrFormula):
        return {f.children[0]}


true_formula = Formula.from_string("TRUE")
false_formula = Formula.from_string("FALSE")


def holy_fucking_translation(formula: Formula):

    class Node(object):
        total = 0

        def __init__(self, name=None):
            Node.total += 1
            self.name = name
            self.id = Node.total
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
                    INCOMING[q] |= incoming
                    q_exists = True
                    break
            if not q_exists:
                q = Node()
                NODES.add(q)
                INCOMING[q] = incoming
                NOW[q] = old
                NEXT[q] = next
                expand(NEXT[q], set(), set(), {q})
        else:
            f = iter(curr).__next__()
            curr = curr - {f}
            old = old | {f}

            if isinstance(f, (TerminalFormula, NotFormula)):
                if f == false_formula and true_formula in old:
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
        return NODES, NOW, INCOMING

    return create_graph()

