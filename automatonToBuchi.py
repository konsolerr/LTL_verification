from ltlFormula.formulas import *
from buchiAutomata.buchiAutomata import LabeledGeneralisedBuchiAutomaton, BuchiAutomaton
from automaton import Automaton


def automaton_to_buchi(automaton):

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

    starts = []
    nodes = {}
    aps = []
    for k, v in automaton.states.items():
        name = v.name.lower()
        if v.type == 1:
            start = Node("pre__" + name)
            starts.append(start)
            nodes[k] = [start, Node(name)]
        else:
            nodes[k] = [Node("pre__" + name), Node(name)]
        aps.append(name)

    aps.extend(map(lambda x: x.lower(), automaton.events))
    for k, v in automaton.transitions.items():
        for action in v.actions:
            aps.append(action.name.lower())

    aps = set(map(lambda x: PropFormula(x), aps))


    nn = []
    delta = {}

    def add_edge(a, b, edge):
        default = delta.get(a, {})
        default[frozenset(edge)] = default.get(frozenset(edge), [])
        default[frozenset(edge)].append(b)
        delta[a] = default

    for k, dnode in nodes.items():
        add_edge(dnode[0], dnode[1], {PropFormula(dnode[1].name)})

    for transition in automaton.transitions:
        actions = automaton.transitions[transition].actions
        event = automaton.transitions[transition].event.lower()

        props = list(map(lambda action: PropFormula(action.name), actions))

        node_end = [x for x in nodes if transition in automaton.states[x].incoming][0]
        node_start = [x for x in nodes if transition in automaton.states[x].outgoing][0]

        node_start = nodes[node_start][1]
        node_end = nodes[node_end][0]

        node_event = Node("Tr {}: {}".format(transition, event))

        edges = []
        edges.append({PropFormula(node_start.name),
                      PropFormula(event)})

        for action in actions:
            action = action.name.lower()
            edges.append({PropFormula(node_start.name),
                          PropFormula(event),
                          PropFormula(action)})

        new_nodes = [Node("tmp") for i in range(len(edges) - 1)]
        new_nodes.append(node_end)
        nn.extend(new_nodes)

        last = node_start
        for i, edge in enumerate(edges):
            add_edge(last, new_nodes[i], edge)
            last = new_nodes[i]


    nodes_total = set()
    for k, v in nodes.items():
        nodes_total.update(set(v))

    nodes_total.update(set(nn))
    return BuchiAutomaton(nodes_total, aps, delta, starts, [])
