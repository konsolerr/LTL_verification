from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def verification(auto, ltl):

    class DoubleNode(object):
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __repr__(self):
            return "Double node for {} and {}".format(self.a, self.b)

        def __hash__(self):
            return hash(self.a) + hash(self.b)

        def __eq__(self, other):
            if type(self) == type(other):
                return self.a == other.a and self.b == other.b
            else:
                return False

    def pairs(alist, blist):
        for a in alist:
            for b in blist:
                yield DoubleNode(a, b)

    used = set()
    usedStack = []
    used2 = set()

    stack = []
    cycle = []

    pos = None
    ansStack = []
    ansCycle = []
    answer = False

    def accepted(q):
        return q.b in ltl.ends

    def dfs1(q):
        used.add(q)
        usedStack.append(q)

        if accepted(q):
            used2.clear()
            dfs2(q)

        for edge in auto.delta[q.a]:
            deltas = ltl.delta[q.b]

            good_nodes = [
                nd for nd in deltas
                if deltas[nd][0].issubset(edge) and edge.issubset(deltas[nd][1])
            ]

            for q1 in pairs(auto.delta[q.a][edge], good_nodes):
                if q1 not in used:

                    if answer:
                        return

                    stack.append(edge)
                    dfs1(q1)
                    stack.pop()

        usedStack.pop()
        used.remove(q)



    def dfs2(q):
        nonlocal answer
        nonlocal ansCycle
        nonlocal ansStack
        nonlocal pos
        used2.add(q)

        for edge in auto.delta[q.a]:

            deltas = ltl.delta[q.b]
            good_nodes = [
                nd for nd in deltas
                if deltas[nd][0].issubset(edge) and edge.issubset(deltas[nd][1])
            ]

            for q1 in pairs(auto.delta[q.a][edge], good_nodes):

                if answer:
                    return

                if q1 in used:
                    cycle.append(edge)
                    answer = True
                    pos = usedStack.index(q1)
                    ansStack = [qq for qq in stack]
                    ansCycle = [qq for qq in cycle]

                    return

                if q1 not in used2:
                    cycle.append(edge)
                    dfs2(q1)
                    cycle.pop()

    kek = [dfs1(q) for q in pairs(auto.starts, ltl.starts)]
    if answer:
        path = ansStack[:pos]
        cycle = ansStack[pos:] + ansCycle
        return answer, path, cycle
    else:
        return answer, [], []
