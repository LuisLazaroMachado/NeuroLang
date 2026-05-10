# Generated from NeuroLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .NeuroLangParser import NeuroLangParser
else:
    from NeuroLangParser import NeuroLangParser

# This class defines a complete listener for a parse tree produced by NeuroLangParser.
class NeuroLangListener(ParseTreeListener):

    # Enter a parse tree produced by NeuroLangParser#program.
    def enterProgram(self, ctx:NeuroLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by NeuroLangParser#program.
    def exitProgram(self, ctx:NeuroLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by NeuroLangParser#statement.
    def enterStatement(self, ctx:NeuroLangParser.StatementContext):
        pass

    # Exit a parse tree produced by NeuroLangParser#statement.
    def exitStatement(self, ctx:NeuroLangParser.StatementContext):
        pass


    # Enter a parse tree produced by NeuroLangParser#channelDecl.
    def enterChannelDecl(self, ctx:NeuroLangParser.ChannelDeclContext):
        pass

    # Exit a parse tree produced by NeuroLangParser#channelDecl.
    def exitChannelDecl(self, ctx:NeuroLangParser.ChannelDeclContext):
        pass


    # Enter a parse tree produced by NeuroLangParser#thresholdDecl.
    def enterThresholdDecl(self, ctx:NeuroLangParser.ThresholdDeclContext):
        pass

    # Exit a parse tree produced by NeuroLangParser#thresholdDecl.
    def exitThresholdDecl(self, ctx:NeuroLangParser.ThresholdDeclContext):
        pass


    # Enter a parse tree produced by NeuroLangParser#whenStmt.
    def enterWhenStmt(self, ctx:NeuroLangParser.WhenStmtContext):
        pass

    # Exit a parse tree produced by NeuroLangParser#whenStmt.
    def exitWhenStmt(self, ctx:NeuroLangParser.WhenStmtContext):
        pass


    # Enter a parse tree produced by NeuroLangParser#outputStmt.
    def enterOutputStmt(self, ctx:NeuroLangParser.OutputStmtContext):
        pass

    # Exit a parse tree produced by NeuroLangParser#outputStmt.
    def exitOutputStmt(self, ctx:NeuroLangParser.OutputStmtContext):
        pass


    # Enter a parse tree produced by NeuroLangParser#signal.
    def enterSignal(self, ctx:NeuroLangParser.SignalContext):
        pass

    # Exit a parse tree produced by NeuroLangParser#signal.
    def exitSignal(self, ctx:NeuroLangParser.SignalContext):
        pass


    # Enter a parse tree produced by NeuroLangParser#expression.
    def enterExpression(self, ctx:NeuroLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by NeuroLangParser#expression.
    def exitExpression(self, ctx:NeuroLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by NeuroLangParser#signalType.
    def enterSignalType(self, ctx:NeuroLangParser.SignalTypeContext):
        pass

    # Exit a parse tree produced by NeuroLangParser#signalType.
    def exitSignalType(self, ctx:NeuroLangParser.SignalTypeContext):
        pass



del NeuroLangParser