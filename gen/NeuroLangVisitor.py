# Generated from NeuroLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .NeuroLangParser import NeuroLangParser
else:
    from NeuroLangParser import NeuroLangParser

# This class defines a complete generic visitor for a parse tree produced by NeuroLangParser.

class NeuroLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NeuroLangParser#program.
    def visitProgram(self, ctx:NeuroLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuroLangParser#statement.
    def visitStatement(self, ctx:NeuroLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuroLangParser#channelDecl.
    def visitChannelDecl(self, ctx:NeuroLangParser.ChannelDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuroLangParser#thresholdDecl.
    def visitThresholdDecl(self, ctx:NeuroLangParser.ThresholdDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuroLangParser#whenStmt.
    def visitWhenStmt(self, ctx:NeuroLangParser.WhenStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuroLangParser#outputStmt.
    def visitOutputStmt(self, ctx:NeuroLangParser.OutputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuroLangParser#signal.
    def visitSignal(self, ctx:NeuroLangParser.SignalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuroLangParser#expression.
    def visitExpression(self, ctx:NeuroLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeuroLangParser#signalType.
    def visitSignalType(self, ctx:NeuroLangParser.SignalTypeContext):
        return self.visitChildren(ctx)



del NeuroLangParser