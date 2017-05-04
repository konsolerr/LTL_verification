# Generated from ltlGrammar.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("T\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\fA\n\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\7\17I\n\17\f\17\16\17L\13")
        buf.write("\17\3\20\6\20O\n\20\r\20\16\20P\3\20\3\20\2\2\21\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\2\33")
        buf.write("\2\35\16\37\17\3\2\5\5\2\62;aac|\3\2c|\5\2\13\f\16\17")
        buf.write("\"\"\2T\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t(\3\2\2")
        buf.write("\2\13+\3\2\2\2\r-\3\2\2\2\17/\3\2\2\2\21\61\3\2\2\2\23")
        buf.write("\63\3\2\2\2\25\65\3\2\2\2\27@\3\2\2\2\31B\3\2\2\2\33D")
        buf.write("\3\2\2\2\35F\3\2\2\2\37N\3\2\2\2!\"\7*\2\2\"\4\3\2\2\2")
        buf.write("#$\7+\2\2$\6\3\2\2\2%&\7(\2\2&\'\7(\2\2\'\b\3\2\2\2()")
        buf.write("\7~\2\2)*\7~\2\2*\n\3\2\2\2+,\7#\2\2,\f\3\2\2\2-.\7Z\2")
        buf.write("\2.\16\3\2\2\2/\60\7H\2\2\60\20\3\2\2\2\61\62\7I\2\2\62")
        buf.write("\22\3\2\2\2\63\64\7W\2\2\64\24\3\2\2\2\65\66\7T\2\2\66")
        buf.write("\26\3\2\2\2\678\7V\2\289\7T\2\29:\7W\2\2:A\7G\2\2;<\7")
        buf.write("H\2\2<=\7C\2\2=>\7N\2\2>?\7U\2\2?A\7G\2\2@\67\3\2\2\2")
        buf.write("@;\3\2\2\2A\30\3\2\2\2BC\t\2\2\2C\32\3\2\2\2DE\t\3\2\2")
        buf.write("E\34\3\2\2\2FJ\5\33\16\2GI\5\31\r\2HG\3\2\2\2IL\3\2\2")
        buf.write("\2JH\3\2\2\2JK\3\2\2\2K\36\3\2\2\2LJ\3\2\2\2MO\t\4\2\2")
        buf.write("NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\b")
        buf.write("\20\2\2S \3\2\2\2\6\2@JP\3\b\2\2")
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
    BoolConst = 11
    ID = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'&&'", "'||'", "'!'", "'X'", "'F'", "'G'", "'U'", 
            "'R'" ]

    symbolicNames = [ "<INVALID>",
            "BoolConst", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "BoolConst", "ValidNameSymbol", 
                  "Letter", "ID", "WS" ]

    grammarFileName = "ltlGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


