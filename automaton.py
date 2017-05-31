from lxml import etree
from ltlFormula.formulas import *
from pprint import pprint

NOT_SET = "not set"


class Inc():
    def __init__(self):
        self.val = 0

    def __call__(self, *args, **kwargs):
        let = chr(ord('a') + self.val)
        self.val += 1
        return let


class CodeAction:
    def __init__(self, var, val):
        self.var = var
        self.val = val


class Action:
    def __init__(self, name, comment, synchro):
        self.name = name
        self.comment = comment
        self.synchro = synchro


class Event:
    def __init__(self):
        self.name = NOT_SET
        self.comment = NOT_SET


class Variable:
    def __init__(self):
        self.name = NOT_SET
        self.value = NOT_SET
        self.volatile = False
        self.pseudoname = NOT_SET


class State:
    def __init__(self):
        self.id = -1
        self.name = NOT_SET
        self.type = -1
        self.outgoing = []
        self.incoming = []

    def __repr__(self):
        return "State \"{}\" with incoming edges: {} \n and outgoing edges: {}".format(
            self.name, self.incoming, self.outgoing
        )


class Transition:
    def __init__(self):
        self.id = -1
        self.event = NOT_SET
        self.actions = []
        self.code = NOT_SET
        self.guard = NOT_SET

    def __repr__(self):
        return "Transition happens with event {}".format(self.event)


class Automaton:
    def __init__(self):
        self.events = {}
        self.variables = {}
        self.pseudoname_to_name = {}
        self.name_to_pseudoname = {}
        self.states = {}
        self.transitions = {}
        self.current_state = None
        self.inc = Inc()

    def __parse_event(self, root):
        event = Event()
        event.name = root.get("name")
        event.comment = root.get("comment")
        return event

    def __parse_variable(self, root):
        val = root.get("decl")
        var = Variable()
        var.volatile = "volatile" in val
        val = val.replace("volatile ", "")
        var.name = val.split(" ")[1]
        var.value = int(val.split(" ")[3].split(";")[0]) == 1
        var.pseudoname = self.inc()
        return var

    def __parse_state(self, root):
        state = State()
        state.id = int(root.get("id"))
        root = root.find("attributes")
        state.name = root.find("name").text
        state.type = int(root.find("type").text)
        state.outgoing = [int(transition.get("id")) for transition in root.findall("outgoing")]
        state.incoming = [int(transition.get("id")) for transition in root.findall("incoming")]
        return state

    def __parse_code(self, code):
        lines = code.split(";")
        lines.pop()
        code_actions = []
        for line in lines:
            code_line = line.strip()
            code_actions.append(CodeAction(code_line.split(" ")[0], int(code_line.split(" ")[2]) == 1))
        return code_actions

    def __parse_transition(self, root):
        transition = Transition()
        transition.id = int(root.get("id"))
        root = root.find("attributes")
        transition.event = root.find("event").get("name")
        transition.actions = [Action(action.get("name"), action.get("comment"), action.get("synchro"))
                              for action in root.findall("action")]
        code = root.find("code").text
        transition.code = self.__parse_code(code) if code is not None else []
        guard = root.find("guard").text
        transition.guard = guard  # Formula.from_string(guard) if guard is not None else True
        return transition

    def read(self, text):
        text = text.strip()
        root = etree.fromstring(text)
        data = root.find("data")
        statemachine = data.find("Statemachine")
        for entry in statemachine.findall("event"):
            event = self.__parse_event(entry)
            self.events[event.name] = event
        for entry in statemachine.findall("variable"):
            var = self.__parse_variable(entry)
            self.variables[var.name] = var
            self.pseudoname_to_name[var.pseudoname] = var.name
            self.name_to_pseudoname[var.name] = var.pseudoname
        for entry in root.findall("widget"):
            if entry.get("type") == "State":
                state = self.__parse_state(entry)
                self.states[state.id] = state
            elif entry.get("type") == "Transition":
                transition = self.__parse_transition(entry)
                self.transitions[transition.id] = transition
        self.current_state = self.get_start_state_id()

    def get_start_state_id(self):
        for id in self.states:
            if self.states[id].type == 1:
                return id

    def get_parsed_formula(self, id):
        guard_text = self.transitions[id].guard
        for name in self.name_to_pseudoname:
            guard_text = guard_text.replace(name, self.name_to_pseudoname[name])
        formula = Formula.from_string(guard_text)
        return formula

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, "r") as f:
            text = f.read()
            aut = Automaton()
            aut.read(text.replace('<?xml version="1.0" encoding="utf-8"?>', ''))
            return aut

