from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce

class ASTGeneration(BKITVisitor):
    #program  : glovardeclprt? funcdeclprt EOF ;
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        lst=[]
        if ctx.glovardeclprt():
            lst=lst+self.visit(ctx.glovardeclprt())+self.visit(ctx.funcdeclprt())
        else:
            lst=lst+self.visit(ctx.funcdeclprt())
        return Program(lst)

    #glovardeclprt: vardecl +;
    def visitGlovardeclprt(self,ctx:BKITParser.GlovardeclprtContext):
        return reduce(lambda x,y:x+y,[self.visit(x) for x in ctx.vardecl()],[])

    #vardecl : VAR COLON varlist SEMI ;
    def visitVardecl(self,ctx:BKITParser.VardeclContext):
        return self.visit(ctx.varlist())

    #varlist : vari (COMMA vari)* ;
    def visitVarlist(self,ctx:BKITParser.VarlistContext):
        return [self.visit(x) for x in ctx.vari()]
        #tra ve 1 list cac object VarDecl()

    #vari : vari_array|vari_scalar ;
    def visitVari(self,ctx:BKITParser.VariContext):
        if ctx.vari_array():
            return self.visit(ctx.vari_array())
        else:
            return self.visit(ctx.vari_scalar())


    #vari_array : ID indexop+ (ASSIGN lit)? ;
    # tra ve 1 object VarDecl()
    def visitVari_array(self,ctx:BKITParser.Vari_arrayContext):
        if ctx.lit():
            return VarDecl(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.indexop()],self.visit(ctx.lit()))
        else:
            return VarDecl(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.indexop()],None)

    #vari_scalar : ID (ASSIGN lit)? ;
    #tra ve 1 object VarDecl
    def visitVari_scalar(self,ctx:BKITParser.Vari_scalarContext):
        if ctx.lit():
            return VarDecl(Id(ctx.ID().getText()),[],self.visit(ctx.lit()))
        else:
            return VarDecl(Id(ctx.ID().getText()),[],None)

    #indexop : LS INTLIT RS ;
    def visitIndexop(self,ctx:BKITParser.IndexopContext): #tra ve kieu int
        if ctx.INTLIT().getText()[:2] in ['0x', '0X']:
            return int(ctx.INTLIT().getText(), 16)
        elif ctx.INTLIT().getText()[:2] in ['0o', '0O']:
            return int(ctx.INTLIT().getText(), 8)
        else:
            return int(ctx.INTLIT().getText())

    #lit : INTLIT|FLOATLIT|BOOLLIT
    def visitLit(self,ctx:BKITParser.LitContext):
        if ctx.INTLIT():
            if ctx.INTLIT().getText()[:2] in ['0x', '0X']:
                return IntLiteral(int(ctx.INTLIT().getText(), 16))
            elif ctx.INTLIT().getText()[:2] in ['0o', '0O']:
                return IntLiteral(int(ctx.INTLIT().getText(), 8))
            else:
                return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral('True'==ctx.BOOLLIT().getText())

    #funcdeclprt : funcdecl* ;
    def visitFuncdeclprt(self,ctx:BKITParser.FuncdeclprtContext):
        if ctx.funcdecl():
            return [self.visit(x) for x in ctx.funcdecl()]
        else:
            return []

    #funcdecl : FUNCTION COLON ID (parafun)? bodyfun ;
    def visitFuncdecl(self,ctx:BKITParser.FuncdeclContext):
        if ctx.parafun():
            return FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.parafun()),self.visit(ctx.bodyfun()))
        else:
            return FuncDecl(Id(ctx.ID().getText()),[],self.visit(ctx.bodyfun()))

    #parafun : PARA COLON paralist ;
    def visitParafun(self,ctx:BKITParser.ParafunContext):
        return self.visit(ctx.paralist())

    #paralist : para (COMMA para)* ;
    def visitParalist(self,ctx:BKITParser.ParalistContext):
        return [self.visit(x) for x in ctx.para()]

    #para : vari ;
    def visitPara(self,ctx:BKITParser.ParaContext):
        return self.visit(ctx.vari())

    #bodyfun : BODY COLON nulstmtlst ENDBODY DOT ;
    def visitBodyfun(self,ctx:BKITParser.BodyfunContext):
        return self.visit(ctx.nulstmtlst())

    #nulstmtlst : varstmt* stmttype*   ;
    def visitNulstmtlst(self, ctx:BKITParser.NulstmtlstContext):
        if ctx.varstmt() and ctx.stmttype():
            lst = reduce(lambda x, y: x + y,[self.visit(x) for x in ctx.varstmt()])
            return (lst ,[self.visit(y) for y in ctx.stmttype()])
        elif ctx.varstmt():
            lst = reduce(lambda x, y: x + y, [self.visit(x) for x in ctx.varstmt()])
            return (lst,[])
        elif ctx.stmttype():
            return ([],[self.visit(x) for x in ctx.stmttype()])
        else:
            return ([],[])

    #stmttype : asstmt|ifstmt|forstmt|whilestmt|dowhistmt|breakstmt|contstmt|callstmt|returnstmt ;
    def visitStmttype(self,ctx:BKITParser.StmttypeContext):
        return self.visitChildren(ctx)

    #varstmt : vardecl ;
    def visitVarstmt(self,ctx:BKITParser.VarstmtContext):
        return self.visit(ctx.vardecl())

    #asstmt : value ASSIGN exp SEMI ;
    def visitAsstmt(self,ctx:BKITParser.AsstmtContext):
        return Assign(self.visit(ctx.value()),self.visit(ctx.exp()))

    #value : ID (LS exp RS)* ;
    def visitValue(self,ctx:BKITParser.ValueContext):
        if ctx.exp():
            return ArrayCell(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.exp()])
        else:
            return Id(ctx.ID().getText())

    #ifthenStmt: IF exp THEN stmtlst (ELSEIF exp THEN stmtlst)* ;
    def visitIfthenStmt(self,ctx:BKITParser.IfthenStmtContext):
        lst1 = [self.visit(x) for x in ctx.exp()]  # kieu Exp
        lst2 = [self.visit(x) for x in ctx.stmtlst()]  # kieu list 2 phan tu : var , stmt

        if ctx.ELSEIF():
            return [(lst1[i],lst2[i] [0], lst2[i] [1])  for i in range(len(lst1)) ]
        else:
            return [(lst1[0],lst2[0] [0], lst2[0] [1])]

    #elseStmt: (ELSE stmtlst)? ENDIF DOT ;
    def visitElseStmt(self,ctx:BKITParser.ElseStmtContext):
        if ctx.stmtlst():
            lst = self.visit(ctx.stmtlst())
            return (lst[0],lst[1])
        else:
            return ([],[])

    #ifstmt: ifthenStmt elseStmt ;
    def visitIfstmt(self,ctx:BKITParser.IfstmtContext):
        return If(self.visit(ctx.ifthenStmt()),self.visit(ctx.elseStmt()))

    #stmtlst : varstmt* stmttype+ |  varstmt+ stmttype* ;
    def visitStmtlst(self,ctx:BKITParser.StmtlstContext):
        if ctx.stmttype() and ctx.varstmt():
            return [[self.visit(x) for x in ctx.varstmt()],[self.visit(y) for y in ctx.stmttype()]]
        elif ctx.stmttype():
            return [[],[self.visit(y) for y in ctx.stmttype()]]
        else:
            return [[self.visit(x) for x in ctx.varstmt()],[]]

    #forstmt : FOR LB scava ASSIGN inex COMMA conExp COMMA scava ASSIGN upex RB DO stmtlst ENDFOR DOT ;
    def visitForstmt(self,ctx:BKITParser.ForstmtContext):
        abc = self.visit(ctx.stmtlst())
        return For(self.visit(ctx.scava(0)),self.visit(ctx.inex()),self.visit(ctx.conExp()),self.visit(ctx.scava(1)),self.visit(ctx.upex()),(abc[0],abc[1]))

    #scava : ID ;
    def visitScava(self,ctx:BKITParser.ScavaContext):
        return Id(ctx.ID().getText())

    #inex : exp ;
    def visitInex(self,ctx:BKITParser.InexContext):
        return self.visit(ctx.exp())

    #conExp: exp ;
    def visitConExp(self,ctx:BKITParser.ConExpContext):
        return self.visit(ctx.exp())

    #upex : exp ;
    def visitUpex(self,ctx:BKITParser.UpexContext):
        return self.visit(ctx.exp())

    #whilestmt : WHILE exp DO stmtlst ENDWHILE DOT ;
    def visitWhilestmt(self,ctx:BKITParser.WhilestmtContext):
        bca = self.visit(ctx.stmtlst())
        return While(self.visit(ctx.exp()),(bca[0],bca[1]))

    #dowhistmt : DO stmtlst WHILE exp SEMI ;
    def visitDowhistmt(self,ctx:BKITParser.DowhistmtContext):
        bca = self.visit(ctx.stmtlst())
        return Dowhile((bca[0],bca[1]),self.visit(ctx.exp()))

    #breakstmt : BREAK SEMI ;
    def visitBreakstmt(self,ctx:BKITParser.BreakstmtContext):
        return Break()

    #contstmt : CONTINUE SEMI ;
    def visitContstmt(self,ctx:BKITParser.ContstmtContext):
        return Continue()

    #callstmt : ID LB bet? RB SEMI ;
    def visitCallstmt(self,ctx:BKITParser.CallstmtContext):
        if ctx.bet():
            return CallStmt(Id(ctx.ID().getText()),self.visit(ctx.bet()))
        else:
            return CallStmt(Id(ctx.ID().getText()),[])

    #bet : exp (COMMA exp)* ;
    def visitBet(self,ctx:BKITParser.BetContext):
        return [self.visit(x) for x in ctx.exp()]

    #returnstmt : RETURN exp? SEMI ;
    def visitReturnstmt(self,ctx:BKITParser.ReturnstmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        else:
            return Return(None)

    #exp : exp (EQ|NOEQ|LESS|GREAT|LEEQ|GREQ|NOEQF|LEF|GRF|LEQF|GEQF) exp1 | exp1 ;
    def visitExp(self,ctx:BKITParser.ExpContext):
        if ctx.getChildCount()==1:
            return self.visitChildren(ctx)
        elif ctx.EQ():
            op="=="
        elif ctx.getChild(1)==ctx.NOEQ():
            op="!="
        elif ctx.getChild(1)==ctx.LESS():
            op="<"
        elif ctx.getChild(1)==ctx.GREAT():
            op=">"
        elif ctx.getChild(1)==ctx.LEEQ():
            op="<="
        elif ctx.getChild(1)==ctx.GREQ():
            op=">="
        elif ctx.getChild(1)==ctx.NOEQF():
            op="=/="
        elif ctx.getChild(1)==ctx.LEF():
            op="<."
        elif ctx.getChild(1)==ctx.GRF():
            op=">."
        elif ctx.getChild(1)==ctx.LEQF():
            op="<=."
        elif ctx.getChild(1)==ctx.GEQF():
            op=">=."
        return BinaryOp(op,self.visit(ctx.exp()),self.visit(ctx.exp1()))

    #exp1 : exp1 (CONJ|DISJ) exp2|exp2 ;
    def visitExp1(self,ctx:BKITParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2()))

    #exp2 : exp2 (IADD|FADD|ISUB|FSUB) exp3|exp3 ;
    def visitExp2(self,ctx:BKITParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))

    #exp3 : exp3 (IMUL|FMUL|IDIV|FDIV|IREM) exp4|exp4 ;
    def visitExp3(self,ctx:BKITParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))

    #exp4 : NEG exp5 | exp5 ;
    def visitExp4(self, ctx: BKITParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp5()))

    #exp5 : (ISUB|FSUB) exp6 | exp6 ;
    def visitExp5(self, ctx: BKITParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
        return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp6()))

    #exp6 : value | LB exp RB| funccall |INTLIT|FLOATLIT| STRINGLIT | BOOLLIT ;
    def visitExp6(self, ctx: BKITParser.Exp6Context):
        if ctx.INTLIT():
            if ctx.INTLIT().getText()[:2] in ['0x', '0X']:
                return IntLiteral(int(ctx.INTLIT().getText(),16))
            elif ctx.INTLIT().getText()[:2] in ['0o', '0O']:
                return  IntLiteral(int(ctx.INTLIT().getText(),8))
            else:
                return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral('True'==ctx.BOOLLIT().getText())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.value():
            return self.visit(ctx.value())
        elif ctx.exp():
            return self.visit(ctx.exp())
        elif ctx.funccall():
            return self.visit(ctx.funccall())

    #explist : exp COMMA explist | exp ;
    def visitExplist(self, ctx: BKITParser.ExplistContext):
        if ctx.explist():
            return [self.visit(ctx.exp())] + self.visit(ctx.explist())
        else:
            return [self.visit(ctx.exp())]

    #funccall : ID LB explist? RB ;
    def visitFunccall(self, ctx: BKITParser.FunccallContext):
        if ctx.explist():
            return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.explist()))
        else:
            return CallExpr(Id(ctx.ID().getText()),[])













    

