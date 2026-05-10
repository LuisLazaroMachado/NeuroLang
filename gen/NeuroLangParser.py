# Generated from NeuroLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,5,4,50,8,4,10,4,12,4,53,9,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,
        9,0,2,4,6,8,10,12,14,16,0,2,2,0,16,16,18,18,1,0,6,8,66,0,21,1,0,
        0,0,2,29,1,0,0,0,4,31,1,0,0,0,6,37,1,0,0,0,8,43,1,0,0,0,10,56,1,
        0,0,0,12,62,1,0,0,0,14,67,1,0,0,0,16,69,1,0,0,0,18,20,3,2,1,0,19,
        18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,
        0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,30,3,4,2,0,27,30,3,
        6,3,0,28,30,3,8,4,0,29,26,1,0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,
        3,1,0,0,0,31,32,5,1,0,0,32,33,5,18,0,0,33,34,5,10,0,0,34,35,3,16,
        8,0,35,36,5,11,0,0,36,5,1,0,0,0,37,38,5,2,0,0,38,39,5,18,0,0,39,
        40,5,10,0,0,40,41,5,16,0,0,41,42,5,11,0,0,42,7,1,0,0,0,43,44,5,3,
        0,0,44,45,3,12,6,0,45,46,5,9,0,0,46,47,3,14,7,0,47,51,5,14,0,0,48,
        50,3,10,5,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,
        0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,15,0,0,55,9,1,0,0,0,56,57,
        5,4,0,0,57,58,5,12,0,0,58,59,5,17,0,0,59,60,5,13,0,0,60,61,5,11,
        0,0,61,11,1,0,0,0,62,63,5,5,0,0,63,64,5,12,0,0,64,65,5,18,0,0,65,
        66,5,13,0,0,66,13,1,0,0,0,67,68,7,0,0,0,68,15,1,0,0,0,69,70,7,1,
        0,0,70,17,1,0,0,0,3,21,29,51
    ]

class NeuroLangParser ( Parser ):

    grammarFileName = "NeuroLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'channel'", "'threshold'", "'when'", 
                     "'output'", "'signal'", "'eeg'", "'emg'", "'eog'", 
                     "<INVALID>", "':'", "';'", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "CHANNEL", "THRESHOLD", "WHEN", "OUTPUT", 
                      "SIGNAL", "EEG", "EMG", "EOG", "RELOP", "COLON", "SEMI", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "NUMBER", 
                      "STRING_LIT", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_channelDecl = 2
    RULE_thresholdDecl = 3
    RULE_whenStmt = 4
    RULE_outputStmt = 5
    RULE_signal = 6
    RULE_expression = 7
    RULE_signalType = 8

    ruleNames =  [ "program", "statement", "channelDecl", "thresholdDecl", 
                   "whenStmt", "outputStmt", "signal", "expression", "signalType" ]

    EOF = Token.EOF
    CHANNEL=1
    THRESHOLD=2
    WHEN=3
    OUTPUT=4
    SIGNAL=5
    EEG=6
    EMG=7
    EOG=8
    RELOP=9
    COLON=10
    SEMI=11
    LPAREN=12
    RPAREN=13
    LBRACE=14
    RBRACE=15
    NUMBER=16
    STRING_LIT=17
    ID=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(NeuroLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NeuroLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(NeuroLangParser.StatementContext,i)


        def getRuleIndex(self):
            return NeuroLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = NeuroLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(NeuroLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def channelDecl(self):
            return self.getTypedRuleContext(NeuroLangParser.ChannelDeclContext,0)


        def thresholdDecl(self):
            return self.getTypedRuleContext(NeuroLangParser.ThresholdDeclContext,0)


        def whenStmt(self):
            return self.getTypedRuleContext(NeuroLangParser.WhenStmtContext,0)


        def getRuleIndex(self):
            return NeuroLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = NeuroLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.channelDecl()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.thresholdDecl()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.whenStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChannelDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHANNEL(self):
            return self.getToken(NeuroLangParser.CHANNEL, 0)

        def ID(self):
            return self.getToken(NeuroLangParser.ID, 0)

        def COLON(self):
            return self.getToken(NeuroLangParser.COLON, 0)

        def signalType(self):
            return self.getTypedRuleContext(NeuroLangParser.SignalTypeContext,0)


        def SEMI(self):
            return self.getToken(NeuroLangParser.SEMI, 0)

        def getRuleIndex(self):
            return NeuroLangParser.RULE_channelDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChannelDecl" ):
                listener.enterChannelDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChannelDecl" ):
                listener.exitChannelDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChannelDecl" ):
                return visitor.visitChannelDecl(self)
            else:
                return visitor.visitChildren(self)




    def channelDecl(self):

        localctx = NeuroLangParser.ChannelDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_channelDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(NeuroLangParser.CHANNEL)
            self.state = 32
            self.match(NeuroLangParser.ID)
            self.state = 33
            self.match(NeuroLangParser.COLON)
            self.state = 34
            self.signalType()
            self.state = 35
            self.match(NeuroLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThresholdDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THRESHOLD(self):
            return self.getToken(NeuroLangParser.THRESHOLD, 0)

        def ID(self):
            return self.getToken(NeuroLangParser.ID, 0)

        def COLON(self):
            return self.getToken(NeuroLangParser.COLON, 0)

        def NUMBER(self):
            return self.getToken(NeuroLangParser.NUMBER, 0)

        def SEMI(self):
            return self.getToken(NeuroLangParser.SEMI, 0)

        def getRuleIndex(self):
            return NeuroLangParser.RULE_thresholdDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThresholdDecl" ):
                listener.enterThresholdDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThresholdDecl" ):
                listener.exitThresholdDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThresholdDecl" ):
                return visitor.visitThresholdDecl(self)
            else:
                return visitor.visitChildren(self)




    def thresholdDecl(self):

        localctx = NeuroLangParser.ThresholdDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_thresholdDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(NeuroLangParser.THRESHOLD)
            self.state = 38
            self.match(NeuroLangParser.ID)
            self.state = 39
            self.match(NeuroLangParser.COLON)
            self.state = 40
            self.match(NeuroLangParser.NUMBER)
            self.state = 41
            self.match(NeuroLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhenStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(NeuroLangParser.WHEN, 0)

        def signal(self):
            return self.getTypedRuleContext(NeuroLangParser.SignalContext,0)


        def RELOP(self):
            return self.getToken(NeuroLangParser.RELOP, 0)

        def expression(self):
            return self.getTypedRuleContext(NeuroLangParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(NeuroLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(NeuroLangParser.RBRACE, 0)

        def outputStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NeuroLangParser.OutputStmtContext)
            else:
                return self.getTypedRuleContext(NeuroLangParser.OutputStmtContext,i)


        def getRuleIndex(self):
            return NeuroLangParser.RULE_whenStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhenStmt" ):
                listener.enterWhenStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhenStmt" ):
                listener.exitWhenStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhenStmt" ):
                return visitor.visitWhenStmt(self)
            else:
                return visitor.visitChildren(self)




    def whenStmt(self):

        localctx = NeuroLangParser.WhenStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whenStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(NeuroLangParser.WHEN)
            self.state = 44
            self.signal()
            self.state = 45
            self.match(NeuroLangParser.RELOP)
            self.state = 46
            self.expression()
            self.state = 47
            self.match(NeuroLangParser.LBRACE)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 48
                self.outputStmt()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(NeuroLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(NeuroLangParser.OUTPUT, 0)

        def LPAREN(self):
            return self.getToken(NeuroLangParser.LPAREN, 0)

        def STRING_LIT(self):
            return self.getToken(NeuroLangParser.STRING_LIT, 0)

        def RPAREN(self):
            return self.getToken(NeuroLangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(NeuroLangParser.SEMI, 0)

        def getRuleIndex(self):
            return NeuroLangParser.RULE_outputStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputStmt" ):
                listener.enterOutputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputStmt" ):
                listener.exitOutputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputStmt" ):
                return visitor.visitOutputStmt(self)
            else:
                return visitor.visitChildren(self)




    def outputStmt(self):

        localctx = NeuroLangParser.OutputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_outputStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(NeuroLangParser.OUTPUT)
            self.state = 57
            self.match(NeuroLangParser.LPAREN)
            self.state = 58
            self.match(NeuroLangParser.STRING_LIT)
            self.state = 59
            self.match(NeuroLangParser.RPAREN)
            self.state = 60
            self.match(NeuroLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGNAL(self):
            return self.getToken(NeuroLangParser.SIGNAL, 0)

        def LPAREN(self):
            return self.getToken(NeuroLangParser.LPAREN, 0)

        def ID(self):
            return self.getToken(NeuroLangParser.ID, 0)

        def RPAREN(self):
            return self.getToken(NeuroLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return NeuroLangParser.RULE_signal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignal" ):
                listener.enterSignal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignal" ):
                listener.exitSignal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignal" ):
                return visitor.visitSignal(self)
            else:
                return visitor.visitChildren(self)




    def signal(self):

        localctx = NeuroLangParser.SignalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_signal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(NeuroLangParser.SIGNAL)
            self.state = 63
            self.match(NeuroLangParser.LPAREN)
            self.state = 64
            self.match(NeuroLangParser.ID)
            self.state = 65
            self.match(NeuroLangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(NeuroLangParser.NUMBER, 0)

        def ID(self):
            return self.getToken(NeuroLangParser.ID, 0)

        def getRuleIndex(self):
            return NeuroLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = NeuroLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not(_la==16 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignalTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EEG(self):
            return self.getToken(NeuroLangParser.EEG, 0)

        def EMG(self):
            return self.getToken(NeuroLangParser.EMG, 0)

        def EOG(self):
            return self.getToken(NeuroLangParser.EOG, 0)

        def getRuleIndex(self):
            return NeuroLangParser.RULE_signalType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignalType" ):
                listener.enterSignalType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignalType" ):
                listener.exitSignalType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignalType" ):
                return visitor.visitSignalType(self)
            else:
                return visitor.visitChildren(self)




    def signalType(self):

        localctx = NeuroLangParser.SignalTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_signalType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





