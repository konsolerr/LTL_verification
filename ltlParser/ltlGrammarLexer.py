# Generated from ltlGrammar.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("Y\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\rF\n\r\3\16\3\16\3\17\3\17\3\20\3\20\7")
        buf.write("\20N\n\20\f\20\16\20Q\13\20\3\21\6\21T\n\21\r\21\16\21")
        buf.write("U\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\2\35\2\37\17!\20\3\2\5\5\2\62")
        buf.write(";aac|\3\2c|\5\2\13\f\16\17\"\"\2Y\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3")
        buf.write("\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t*\3\2\2\2\13-\3\2\2\2\r")
        buf.write("\60\3\2\2\2\17\62\3\2\2\2\21\64\3\2\2\2\23\66\3\2\2\2")
        buf.write("\258\3\2\2\2\27:\3\2\2\2\31E\3\2\2\2\33G\3\2\2\2\35I\3")
        buf.write("\2\2\2\37K\3\2\2\2!S\3\2\2\2#$\7*\2\2$\4\3\2\2\2%&\7+")
        buf.write("\2\2&\6\3\2\2\2\'(\7(\2\2()\7(\2\2)\b\3\2\2\2*+\7~\2\2")
        buf.write("+,\7~\2\2,\n\3\2\2\2-.\7/\2\2./\7@\2\2/\f\3\2\2\2\60\61")
        buf.write("\7#\2\2\61\16\3\2\2\2\62\63\7Z\2\2\63\20\3\2\2\2\64\65")
        buf.write("\7H\2\2\65\22\3\2\2\2\66\67\7I\2\2\67\24\3\2\2\289\7W")
        buf.write("\2\29\26\3\2\2\2:;\7T\2\2;\30\3\2\2\2<=\7V\2\2=>\7T\2")
        buf.write("\2>?\7W\2\2?F\7G\2\2@A\7H\2\2AB\7C\2\2BC\7N\2\2CD\7U\2")
        buf.write("\2DF\7G\2\2E<\3\2\2\2E@\3\2\2\2F\32\3\2\2\2GH\t\2\2\2")
        buf.write("H\34\3\2\2\2IJ\t\3\2\2J\36\3\2\2\2KO\5\35\17\2LN\5\33")
        buf.write("\16\2ML\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P \3\2\2")
        buf.write("\2QO\3\2\2\2RT\t\4\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2U")
        buf.write("V\3\2\2\2VW\3\2\2\2WX\b\21\2\2X\"\3\2\2\2\6\2EOU\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class ltlGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    BoolConst = 12
    ID = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'&&'", "'||'", "'->'", "'!'", "'X'", "'F'", "'G'", 
            "'U'", "'R'" ]

    symbolicNames = [ "<INVALID>",
            "BoolConst", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "BoolConst", "ValidNameSymbol", 
                  "Letter", "ID", "WS" ]

    grammarFileName = "ltlGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


