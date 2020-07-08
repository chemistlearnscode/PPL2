# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#glovardeclprt.
    def visitGlovardeclprt(self, ctx:BKITParser.GlovardeclprtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardecl.
    def visitVardecl(self, ctx:BKITParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varlist.
    def visitVarlist(self, ctx:BKITParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vari.
    def visitVari(self, ctx:BKITParser.VariContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vari_array.
    def visitVari_array(self, ctx:BKITParser.Vari_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vari_scalar.
    def visitVari_scalar(self, ctx:BKITParser.Vari_scalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#indexop.
    def visitIndexop(self, ctx:BKITParser.IndexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#lit.
    def visitLit(self, ctx:BKITParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcdeclprt.
    def visitFuncdeclprt(self, ctx:BKITParser.FuncdeclprtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcdecl.
    def visitFuncdecl(self, ctx:BKITParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parafun.
    def visitParafun(self, ctx:BKITParser.ParafunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paralist.
    def visitParalist(self, ctx:BKITParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para.
    def visitPara(self, ctx:BKITParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bodyfun.
    def visitBodyfun(self, ctx:BKITParser.BodyfunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmttype.
    def visitStmttype(self, ctx:BKITParser.StmttypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#nulstmtlst.
    def visitNulstmtlst(self, ctx:BKITParser.NulstmtlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varstmt.
    def visitVarstmt(self, ctx:BKITParser.VarstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#asstmt.
    def visitAsstmt(self, ctx:BKITParser.AsstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#value.
    def visitValue(self, ctx:BKITParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifthenStmt.
    def visitIfthenStmt(self, ctx:BKITParser.IfthenStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseStmt.
    def visitElseStmt(self, ctx:BKITParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifstmt.
    def visitIfstmt(self, ctx:BKITParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmtlst.
    def visitStmtlst(self, ctx:BKITParser.StmtlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forstmt.
    def visitForstmt(self, ctx:BKITParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scava.
    def visitScava(self, ctx:BKITParser.ScavaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#inex.
    def visitInex(self, ctx:BKITParser.InexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#conExp.
    def visitConExp(self, ctx:BKITParser.ConExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#upex.
    def visitUpex(self, ctx:BKITParser.UpexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#whilestmt.
    def visitWhilestmt(self, ctx:BKITParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhistmt.
    def visitDowhistmt(self, ctx:BKITParser.DowhistmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#breakstmt.
    def visitBreakstmt(self, ctx:BKITParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#contstmt.
    def visitContstmt(self, ctx:BKITParser.ContstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callstmt.
    def visitCallstmt(self, ctx:BKITParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bet.
    def visitBet(self, ctx:BKITParser.BetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnstmt.
    def visitReturnstmt(self, ctx:BKITParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funccall.
    def visitFunccall(self, ctx:BKITParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#explist.
    def visitExplist(self, ctx:BKITParser.ExplistContext):
        return self.visitChildren(ctx)



del BKITParser