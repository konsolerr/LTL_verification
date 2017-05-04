# Generated from ltlGrammar.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("\'\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\5\2\24\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\7\2\"\n\2\f\2\16\2%\13\2\3\2\2")
        buf.write("\3\2\3\2\2\2\2/\2\23\3\2\2\2\4\5\b\2\1\2\5\6\7\3\2\2\6")
        buf.write("\7\5\2\2\2\7\b\7\4\2\2\b\24\3\2\2\2\t\24\7\16\2\2\n\24")
        buf.write("\7\r\2\2\13\f\7\7\2\2\f\24\5\2\2\b\r\16\7\b\2\2\16\24")
        buf.write("\5\2\2\7\17\20\7\t\2\2\20\24\5\2\2\6\21\22\7\n\2\2\22")
        buf.write("\24\5\2\2\5\23\4\3\2\2\2\23\t\3\2\2\2\23\n\3\2\2\2\23")
        buf.write("\13\3\2\2\2\23\r\3\2\2\2\23\17\3\2\2\2\23\21\3\2\2\2\24")
        buf.write("#\3\2\2\2\25\26\f\n\2\2\26\27\7\5\2\2\27\"\5\2\2\13\30")
        buf.write("\31\f\t\2\2\31\32\7\6\2\2\32\"\5\2\2\n\33\34\f\4\2\2\34")
        buf.write("\35\7\13\2\2\35\"\5\2\2\5\36\37\f\3\2\2\37 \7\f\2\2 \"")
        buf.write("\5\2\2\4!\25\3\2\2\2!\30\3\2\2\2!\33\3\2\2\2!\36\3\2\2")
        buf.write("\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\3\3\2\2\2%#\3\2\2\2")
        buf.write("\5\23!#")
        return buf.getvalue()


class ltlGrammarParser ( Parser ):

    grammarFileName = "ltlGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'&&'", "'||'", "'!'", "'X'", 
                     "'F'", "'G'", "'U'", "'R'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BoolConst", 
                      "ID", "WS" ]

    RULE_formula = 0

    ruleNames =  [ "formula" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    BoolConst=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ltlGrammarParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NotContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ltlGrammarParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(ltlGrammarParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)


    class OrContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ltlGrammarParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ltlGrammarParser.FormulaContext)
            else:
                return self.getTypedRuleContext(ltlGrammarParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)


    class BracketsContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ltlGrammarParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(ltlGrammarParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackets" ):
                listener.enterBrackets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackets" ):
                listener.exitBrackets(self)


    class PropContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ltlGrammarParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ltlGrammarParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProp" ):
                listener.enterProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProp" ):
                listener.exitProp(self)


    class BoolContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ltlGrammarParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BoolConst(self):
            return self.getToken(ltlGrammarParser.BoolConst, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)


    class AndContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ltlGrammarParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ltlGrammarParser.FormulaContext)
            else:
                return self.getTypedRuleContext(ltlGrammarParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)


    class NextContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ltlGrammarParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(ltlGrammarParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNext" ):
                listener.enterNext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNext" ):
                listener.exitNext(self)


    class FutureContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ltlGrammarParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(ltlGrammarParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuture" ):
                listener.enterFuture(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuture" ):
                listener.exitFuture(self)


    class GlobalContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ltlGrammarParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(ltlGrammarParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal" ):
                listener.enterGlobal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal" ):
                listener.exitGlobal(self)


    class ReleaseContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ltlGrammarParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ltlGrammarParser.FormulaContext)
            else:
                return self.getTypedRuleContext(ltlGrammarParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelease" ):
                listener.enterRelease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelease" ):
                listener.exitRelease(self)


    class UntilContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ltlGrammarParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ltlGrammarParser.FormulaContext)
            else:
                return self.getTypedRuleContext(ltlGrammarParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUntil" ):
                listener.enterUntil(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUntil" ):
                listener.exitUntil(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ltlGrammarParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_formula, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ltlGrammarParser.T__0]:
                localctx = ltlGrammarParser.BracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(ltlGrammarParser.T__0)
                self.state = 4
                self.formula(0)
                self.state = 5
                self.match(ltlGrammarParser.T__1)
                pass
            elif token in [ltlGrammarParser.ID]:
                localctx = ltlGrammarParser.PropContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(ltlGrammarParser.ID)
                pass
            elif token in [ltlGrammarParser.BoolConst]:
                localctx = ltlGrammarParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(ltlGrammarParser.BoolConst)
                pass
            elif token in [ltlGrammarParser.T__4]:
                localctx = ltlGrammarParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(ltlGrammarParser.T__4)
                self.state = 10
                self.formula(6)
                pass
            elif token in [ltlGrammarParser.T__5]:
                localctx = ltlGrammarParser.NextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(ltlGrammarParser.T__5)
                self.state = 12
                self.formula(5)
                pass
            elif token in [ltlGrammarParser.T__6]:
                localctx = ltlGrammarParser.FutureContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(ltlGrammarParser.T__6)
                self.state = 14
                self.formula(4)
                pass
            elif token in [ltlGrammarParser.T__7]:
                localctx = ltlGrammarParser.GlobalContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(ltlGrammarParser.T__7)
                self.state = 16
                self.formula(3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 31
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ltlGrammarParser.AndContext(self, ltlGrammarParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 19
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 20
                        self.match(ltlGrammarParser.T__2)
                        self.state = 21
                        self.formula(9)
                        pass

                    elif la_ == 2:
                        localctx = ltlGrammarParser.OrContext(self, ltlGrammarParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 22
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 23
                        self.match(ltlGrammarParser.T__3)
                        self.state = 24
                        self.formula(8)
                        pass

                    elif la_ == 3:
                        localctx = ltlGrammarParser.UntilContext(self, ltlGrammarParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 25
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 26
                        self.match(ltlGrammarParser.T__8)
                        self.state = 27
                        self.formula(3)
                        pass

                    elif la_ == 4:
                        localctx = ltlGrammarParser.ReleaseContext(self, ltlGrammarParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 28
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 29
                        self.match(ltlGrammarParser.T__9)
                        self.state = 30
                        self.formula(2)
                        pass

             
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




