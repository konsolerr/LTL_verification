from antlr4 import *
from LTL_parser.ltlGrammarLexer import ltlGrammarLexer
from LTL_parser.ltlGrammarParser import ltlGrammarParser


class Formula(object):

    def __init__(self, *args):
        self.children = list(args)
        self.text = None

    def get_text(self):
        raise NotImplemented


    # def __init__(self, line):
    #     data = InputStream(line)
    #     lexer = ltlGrammarLexer(data)
    #     stream = CommonTokenStream(lexer)
    #     parser = ltlGrammarParser(stream)
    #     self.tree = parser.formula()
    #     self.text = line

    @classmethod
    def _parse_context(cls, context):
        if context.__class__.__name__ == "BracketsContext":
            return Formula._parse_context(context.children[1])

        if context.__class__.__name__ == "BoolContext":
            if context.children[0].getText() == "FALSE":
                return ConstFormula(False)
            else:
                return ConstFormula(True)

        if context.__class__.__name__ == "PropContext":
            return PropFormula(context.children[0].getText())

        # UNARY

        if context.__class__.__name__ == "NotContext":
            return NotFormula(Formula._parse_context(context.children[1]))
        if context.__class__.__name__ == "NextContext":
            return NextFormula(Formula._parse_context(context.children[1]))
        if context.__class__.__name__ == "FutureContext":
            return FutureFormula(Formula._parse_context(context.children[1]))
        if context.__class__.__name__ == "GlobalContext":
            return GlobalFormula(Formula._parse_context(context.children[1]))

        # Binary

        if context.__class__.__name__ == "AndContext":
            return AndFormula(
                Formula._parse_context(context.children[0]),
                Formula._parse_context(context.children[2])
            )

        if context.__class__.__name__ == "OrContext":
            return OrFormula(
                Formula._parse_context(context.children[0]),
                Formula._parse_context(context.children[2])
            )

        if context.__class__.__name__ == "UntilContext":
            return UntilFormula(
                Formula._parse_context(context.children[0]),
                Formula._parse_context(context.children[2])
            )

        if context.__class__.__name__ == "ReleaseContext":
            return ReleaseFormula(
                Formula._parse_context(context.children[0]),
                Formula._parse_context(context.children[2])
            )





    @classmethod
    def from_string(cls, input_string: str):
        data = InputStream(input_string)
        lexer = ltlGrammarLexer(data)
        stream = CommonTokenStream(lexer)
        parser = ltlGrammarParser(stream)
        tree = parser.formula()
        return Formula._parse_context(tree)

    @classmethod
    def from_filename(cls, file_name: str):
        with open(file_name, "r") as f:
            data = f.read()
        return Formula.from_string(data)

    def __repr__(self):
        return "{} : [{}]".format(
            self.__class__.__name__,
            "; ".join(map(repr, self.children))
        )

    def negative_propagation(self):
        raise NotImplemented

    def negative_check(self):
        raise NotImplemented

    def normality(self):
        if isinstance(self, FutureFormula):
            return UntilFormula(
                ConstFormula(True),
                self.children[0].normality()
            )

        if isinstance(self, GlobalFormula):
            return ReleaseFormula(
                ConstFormula(False),
                self.children[0].normality()
            )

        for i, child in enumerate(self.children):
            self.children[i] = child.normality()

        return self

    def normal_form(self):
        tree = self.negative_propagation()
        tree_norm = tree.normality()
        return tree_norm

    def __hash__(self):
        return hash(self.get_text())

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        eqs = [child == other.children[i] for i, child in enumerate(self.children)]
        return all(eqs)



class TerminalFormula(Formula):
    pass


class ConstFormula(TerminalFormula):
    def __init__(self, val: bool, *args):
        self.value = val
        super().__init__(*args)

    def __repr__(self):
        return str(self.value)

    def negative_propagation(self):
        return ConstFormula(not self.value)

    def negative_check(self):
        return ConstFormula(self.value)

    def get_text(self):
        if self.text is None:
            self.text = str(self.value)
        return self.text

    def __hash__(self):
        return hash(self.get_text())

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.value == other.value


class PropFormula(TerminalFormula):
    def __init__(self, name: str, *args):
        self.name = name
        super().__init__(*args)

    def __repr__(self):
        return "Prop: \"{}\"".format(self.name)

    def negative_propagation(self):
        return NotFormula(self)

    def negative_check(self):
        return PropFormula(self.name)

    def get_text(self):
        if self.text is None:
            self.text = str(self.name)
        return self.text

    def __hash__(self):
        return hash(self.get_text())

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.name == other.name


class NotFormula(Formula):
    def negative_propagation(self):
        return self.children[0].negative_check()

    def negative_check(self):
        if isinstance(self.children[0], PropFormula):
            return self
        else:
            return self.children[0].negative_propagation()

    def get_text(self):
        if self.text is None:
            self.text = "!({})".format(self.children[0].get_text())
        return self.text


class AndFormula(Formula):
    def negative_propagation(self):
        return OrFormula(
            self.children[0].negative_propagation(),
            self.children[1].negative_propagation()
        )

    def negative_check(self):
        return AndFormula(
            self.children[0].negative_check(),
            self.children[1].negative_check()
        )

    def get_text(self):
        if self.text is None:
            self.text = "({}) && ({})".format(
                self.children[0].get_text(),
                self.children[1].get_text()
            )
        return self.text


class OrFormula(Formula):
    def negative_propagation(self):
        return AndFormula(
            self.children[0].negative_propagation(),
            self.children[1].negative_propagation()
        )

    def negative_check(self):
        return OrFormula(
            self.children[0].negative_check(),
            self.children[1].negative_check()
        )

    def get_text(self):
        if self.text is None:
            self.text = "({}) || ({})".format(
                self.children[0].get_text(),
                self.children[1].get_text()
            )
        return self.text


class NextFormula(Formula):
    def negative_propagation(self):
        return NextFormula(self.children[0].negative_propagation())

    def negative_check(self):
        return NextFormula(self.children[0].negative_check())

    def get_text(self):
        if self.text is None:
            self.text = "X ({})".format(self.children[0].get_text())
        return self.text


class FutureFormula(Formula):
    def negative_propagation(self):
        return GlobalFormula(self.children[0].negative_propagation())

    def negative_check(self):
        return FutureFormula(self.children[0].negative_check())

    def get_text(self):
        if self.text is None:
            self.text = "F ({})".format(self.children[0].get_text())
        return self.text


class GlobalFormula(Formula):
    def negative_propagation(self):
        return FutureFormula(self.children[0].negative_propagation())

    def negative_check(self):
        return GlobalFormula(self.children[0].negative_check())

    def get_text(self):
        if self.text is None:
            self.text = "G ({})".format(self.children[0].get_text())
        return self.text


class ReleaseFormula(Formula):
    def negative_propagation(self):
        return UntilFormula(
            self.children[0].negative_propagation(),
            self.children[1].negative_propagation()
        )

    def negative_check(self):
        return ReleaseFormula(
            self.children[0].negative_check(),
            self.children[1].negative_check()
        )

    def get_text(self):
        if self.text is None:
            self.text = "({}) R ({})".format(
                self.children[0].get_text(),
                self.children[1].get_text()
            )
        return self.text


class UntilFormula(Formula):
    def negative_propagation(self):
        return ReleaseFormula(
            self.children[0].negative_propagation(),
            self.children[1].negative_propagation()
        )

    def negative_check(self):
        return UntilFormula(
            self.children[0].negative_check(),
            self.children[1].negative_check()
        )

    def get_text(self):
        if self.text is None:
            self.text = "({}) U ({})".format(
                self.children[0].get_text(),
                self.children[1].get_text()
            )
        return self.text


class FormulaSet(object):
    def __init__(self, *args):
        self.formulas = set()
        for arg in args:
            self.formulas.add(arg)

    def add_formula(self, formula: Formula):
        self.formulas.add(formula)

    def __len__(self):
        return len(self.formulas)

    def __iter__(self):
        return iter(self.formulas)

    def is_empty(self):
        return len(self) == 0

    @classmethod
    def from_filename(cls, file_name: str):
        formula_set = FormulaSet()
        with open(file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                f = Formula.from_string(line)
                formula_set.add_formula(f)
        return formula_set

    def __eq__(self, other):
        return self.formulas == other.formulas
