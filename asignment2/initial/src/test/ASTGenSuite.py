import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = str(Program([VarDecl(Id("x"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program_with_call_stmt(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            printLn(x);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_function_main302(self):
        input = """
        Function: main
            Body:
                x = 10;
                printLn(x);
            EndBody.
        """
        expect = str(Program([
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")])]))
                ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_empty_program303(self):
        input = """**Function: main
            Body:
                x = 10;
                fact (x);
            EndBody.**"""
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_globalvardecl304(self):
        input = """
        Var: a = 10.;
        Var: b[5];
        Var: c[2][3],d = 6, e;"""
        expect = str(Program([
            VarDecl(Id("a"),[],FloatLiteral(10.)),
            VarDecl(Id("b"), [5], None),
            VarDecl(Id("c"), [2,3], None),
            VarDecl(Id("d"), [], IntLiteral(6)),
            VarDecl(Id("e"), [], None)
                            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_converthex_int305(self):
        input = """
        Var: b[0xFFFF];
        Var: m[4][9];"""
        expect = str(Program([
            VarDecl(Id("b"), [65535], None),
            VarDecl(Id("m"), [4,9], None),
                            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_convertoct_int306(self):
        input = """
                Var: b[0xFFFF];
                Var: c[0O77][9];"""
        expect = str(Program([
            VarDecl(Id("b"), [65535], None),
            VarDecl(Id("c"), [63, 9], None),
                                ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_function307(self):
        input = """
        Var: a = 5;
        Var: b[0xFFFF];
        Var: c[0O77][9];
        
        Function: main
            Body:
                x = 10;
                printLn (x);
            EndBody."""
        expect = str(Program([
            VarDecl(Id("a"),[],IntLiteral(5)),
            VarDecl(Id("b"), [65535], None),
            VarDecl(Id("c"), [63,9], None),
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("x"), IntLiteral(10)),
                CallStmt(Id("printLn"), [Id("x")])]))
                            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))



    def test_var308(self):
        input = """Var: a, b[5], c = 2;
        Function: main
            Body:
                x = 10;
                printLn (x);
            EndBody."""
        expect = str(Program([
            VarDecl(Id("a"),[],None),
            VarDecl(Id("b"), [5], None),
            VarDecl(Id("c"), [], IntLiteral(2)),
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("x"), IntLiteral(10)),
                CallStmt(Id("printLn"), [Id("x")])]))
                            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_funcdecl309(self):
        input = """Var: a;

        Function: main
        Parameter: b[5],c = 2,x
             Body:
                 x = 10;
                 printLn (x);
             EndBody."""
        expect = str(Program([
            VarDecl(Id("a"),[],None),
            FuncDecl(Id("main"),
                [VarDecl(Id("b"), [5], None),VarDecl(Id("c"), [], IntLiteral(2)),VarDecl(Id("x"), [], None)],
                ([], [Assign(Id("x"), IntLiteral(10)),CallStmt(Id("printLn"), [Id("x")])]))
                            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_stringlit310(self):
        input = """Var: a;

        Function: main
             Body:
                 Var: name;
                 printLn("Enter your name:");
                 read(name);
             EndBody."""
        expect = str(Program([
            VarDecl(Id("a"), [], None),
            FuncDecl(Id("main"),
                     [],
                     ([VarDecl(Id("name"), [], None)], [CallStmt(Id("printLn"), [StringLiteral("\"Enter your name:\"")]),
                                                        CallStmt(Id("read"), [Id("name")])]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_funcemptybody311(self):
        input = """Var: a;

                Function: main
                Parameter: b[5],c = 2.,x
                     Body:

                     EndBody."""
        expect = str(Program([
            VarDecl(Id("a"), [], None),
            FuncDecl(Id("main"),
                     [VarDecl(Id("b"), [5], None), VarDecl(Id("c"), [], FloatLiteral(2.)), VarDecl(Id("x"), [], None)],
                     ([], []))
                    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))


    def test_equal312(self):
        input ="""Var: n;

        Function: main
            Body:
               l=2;
               n=k[5]==k[3];
            EndBody.
        """
        expect = str(Program([
            VarDecl(Id("n"), [], None),
            FuncDecl(Id("main"),
                     [],
                     ([], [Assign(Id("l"), IntLiteral(2)), Assign(Id("n"), BinaryOp("==",ArrayCell(Id("k"),[IntLiteral("5")]),ArrayCell(Id("k"),[IntLiteral("3")]))) ]))
                    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_equal313(self):
        input ="""Var: n;

        Function: main
            Body:
               k[5]=l +. 1.0;
            EndBody.
        """
        expect = str(Program([
            VarDecl(Id("n"), [], None),
            FuncDecl(Id("main"),
                     [],
                     ([], [ Assign(ArrayCell(Id("k"),[IntLiteral("5")]), BinaryOp("+.",Id("l"),FloatLiteral(1.0))) ]))
                    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_equal314(self):
        input ="""Var: n;

        Function: main
            Body:
               n=k[5]||k[3] ;
            EndBody.
        """
        expect = str(Program([
            VarDecl(Id("n"), [], None),
            FuncDecl(Id("main"),
                     [],
                     ([], [ Assign(Id("n"), BinaryOp("||",ArrayCell(Id("k"),[IntLiteral("5")]),ArrayCell(Id("k"),[IntLiteral("3")]))) ]))
                    ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_twofunctions315(self):
        input ="""Var: x;
        Function: fact
            Body:
     
            EndBody.
        Function: main
            Body:
               x = 10;
               fact(x);
               
            EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"), [], None),
            FuncDecl(Id("fact"),
                     [],
                     ([], [])
                     ),
            FuncDecl(Id("main"),
                     [],
                     ([], [Assign(Id("x"), IntLiteral(10)), CallStmt(Id("fact"),[Id("x")]) ]  ))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_array_in_body316(self):
        input = """Var: n[10];

        Function: main
            Body:
               Var: i = 3 ;
               n[i] = 10; 
               printLn (n [ i ] ) ;
            EndBody.
        """
        expect = str(Program([
            VarDecl(Id("n"), [10], None),
            FuncDecl(Id("main"),
                     [],
                     ([VarDecl(Id("i"), [], IntLiteral(3))], [Assign(ArrayCell(Id("n"),[Id("i")]), IntLiteral(10)),
                           CallStmt(Id("printLn"), [ ArrayCell(Id("n"),[Id("i")]) ])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_exp317(self):
        input = """
        Function: main

             Body:
                 x = x * 10;
                 printLn (x);
             EndBody."""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                ([], [Assign(Id("x"), BinaryOp ("*", Id("x"), IntLiteral(10))) ,
                      CallStmt(Id("printLn"), [Id("x")])]))
                            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_array_exp318(self):
        input = """Var: n[10],x=5;

        Function: main
            Body:
               Var: i = 1 ;
               n[x + i] = x - i; 
               printLn (n [ x + i] ) ;
            EndBody.
        """
        expect = str(Program([
            VarDecl(Id("n"), [10], None),
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [],
                     ([VarDecl(Id("i"), [], IntLiteral(1))],
                      [Assign(ArrayCell(Id("n"), [BinaryOp ("+", Id("x"), Id("i"))]), BinaryOp ("-", Id("x"), Id("i"))),
                       CallStmt(Id("printLn"),  [ArrayCell(Id("n"), [BinaryOp ("+", Id("x"), Id("i"))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_array_exp319(self):
        input = """Var: n[10][10],x=5;

        Function: main
            Body:
               Var: i = 2 ;
               n[x + i][x-i] = x * i; 
               printLn (n [ x + i][x - i] ) ;
            EndBody.
        """
        expect = str(Program([
            VarDecl(Id("n"), [10,10], None),
            VarDecl(Id("x"), [], IntLiteral(5)),
            FuncDecl(Id("main"),
                     [],
                     ([VarDecl(Id("i"), [], IntLiteral(2))],
                      [Assign(ArrayCell(Id("n"), [BinaryOp ("+", Id("x"), Id("i")),BinaryOp ("-", Id("x"), Id("i"))]), BinaryOp ("*", Id("x"), Id("i"))),
                       CallStmt(Id("printLn"),  [ArrayCell(Id("n"), [BinaryOp ("+", Id("x"), Id("i")), BinaryOp ("-", Id("x"), Id("i"))])])]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))


    def test_ifstmt320(self):
        input = """Var: n = 9 ;
                Function: main
                     Body:
                         If (n == 0) Then
                                Return 1;
                         EndIf.
                     EndBody."""
        expect = str(Program([
            VarDecl(Id("n"), [], IntLiteral(9)),
            FuncDecl(Id("main"),
                     [],
                     ([], [ If ( [ ( BinaryOp("==", Id("n"), IntLiteral(0)), [], [Return(IntLiteral(1))]) ],
                                    ([], []) )] ))

                     ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_ifstmt_elseif321(self):
        input = """
                Function: main
                     Parameter: n
                     Body:
                         If (n == 0) Then
                                Return 1;
                         ElseIf (n == 1) Then 
                                Return 2;
                         EndIf.
                     EndBody."""
        expect = str(Program([
            FuncDecl(Id("main"),
                     [VarDecl(Id("n"), [], None)],
                     ([], [ If ( [ ( BinaryOp("==", Id("n"), IntLiteral(0)), [], [Return(IntLiteral(1))]),
                                    (BinaryOp("==", Id("n"), IntLiteral(1)), [], [Return(IntLiteral(2))]) ],
                                    ([], []) )] ))

                     ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_ifstmt_else322(self):
        input = """Var: n = 9 ;
                Function: main
                     Body:
                         If (n != 9) Then
                                printLn (n);
                         Else 
                                printLn (n \ 3);
                         EndIf.
                     EndBody."""
        expect = str(Program([
            VarDecl(Id("n"), [], IntLiteral(9)),
            FuncDecl(Id("main"),
                     [],
                     ([], [ If ( [ ( BinaryOp("!=", Id("n"), IntLiteral(9)), [], [CallStmt(Id("printLn"), [Id("n")])])] ,
                                    ([], [CallStmt(Id("printLn"), [BinaryOp("\\", Id("n"), IntLiteral(3))]) ]
                                     ))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_ifstmt_full323(self):
        input = """Var: n = 9 ;
                Function: main
                     Body:
                         If (n != 9) Then
                                printLn (n);
                         ElseIf (n % 3 == 0) Then
                                printLn ((((((((n \ 3)))))))) ;
                         Else 
                                Return 0;
                         EndIf.
                     EndBody."""
        expect = str(Program([
            VarDecl(Id("n"), [], IntLiteral(9)),
            FuncDecl(Id("main"),
                     [],
                     ([], [ If ( [ ( BinaryOp("!=", Id("n"), IntLiteral(9)), [], [CallStmt(Id("printLn"), [Id("n")])]),
                                    (BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(3)), IntLiteral(0)), [], [CallStmt(Id("printLn"), [BinaryOp("\\", Id("n"), IntLiteral(3))])])] ,
                                    ([], [ Return(IntLiteral(0)) ]
                                     ))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_if_stmt324(self):
        input = """Var: a;
                Function: fact
                    Parameter: n
                    Body:
                            If (n == 0) Then
                                Return 1;
                            Else
                                Return n * fact (n - 1);
                            EndIf.
                    EndBody.       
                                 
                Function: main
                Parameter: n[10],m=0,x
                     Body:
                         x = 10;
                         printLn (x);
                     EndBody."""
        expect = str(Program([
            VarDecl(Id("a"), [], None),
            FuncDecl(Id("fact"),
                     [VarDecl(Id("n"), [], None)],
                     ([], [ If ( [ ( BinaryOp("==", Id("n"), IntLiteral(0)), [], [Return(IntLiteral(1))]) ],
                                    ([], [Return (BinaryOp ("*", Id("n"),
                                                            CallExpr(Id("fact"), [BinaryOp("-", Id("n"), IntLiteral(1))]))
                                                  )]) )] )),
            FuncDecl(Id("main"),
                     [VarDecl(Id("n"), [10], None), VarDecl(Id("m"), [], IntLiteral(0)), VarDecl(Id("x"), [], None)],
                     ([], [Assign(Id("x"), IntLiteral(10)),CallStmt(Id("printLn"), [Id("x")])]))

                     ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_unaryexp325(self):
        input = """Var: x
        Function: main
        Parameter: x
             Body:
                 x = 10;
                 printLn (-x);
                 
             EndBody."""
        expect = str(Program([
            VarDecl(Id("x"),[],None),
            FuncDecl(Id("main"),
                [VarDecl(Id("x"), [], None)],
                ([], [Assign(Id("x") , IntLiteral(10)),
                      CallStmt(Id("printLn"), [UnaryOp("-",Id("x"))])])  )
                            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))



    def test_whilestmt327(self):
        input = """Var: i;
          Function: main
            Body:
                i = 0;
                While i < 5 Do
                    printLn (i);
                    i = i + 1 ;
                EndWhile.
            EndBody."""
        expect = str(Program([
            VarDecl(Id("i"), [], None),
            FuncDecl(Id("main"),
                     [],
                     ([], [
                         Assign(Id("i"),IntLiteral(0)),
                         While( BinaryOp("<", Id("i"), IntLiteral(5)),
                                ( [],
                                  [ CallStmt (Id("printLn"),
                                              [Id("i")]),
                                    Assign(Id("i"),BinaryOp("+", Id("i"),IntLiteral(1)))] )
                                )

                            ]))
                             ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_Dowhile328(self):
        input = """Var: i;
          Function: main
            Body:
                i = 0;
                Do
                    printLn (i);
                    i = i + 1 ;
                While i < 5;
            EndBody."""
        expect = str(Program([
            VarDecl(Id("i"), [], None),
            FuncDecl(Id("main"),
                     [],
                     ([], [
                         Assign(Id("i"),IntLiteral(0)),
                         Dowhile(
                                ( [],
                                  [ CallStmt (Id("printLn"),
                                              [Id("i")]),
                                    Assign(Id("i"),BinaryOp("+", Id("i"),IntLiteral(1)))] ),
                                BinaryOp("<", Id("i"), IntLiteral(5))
                                )

                            ]))
                             ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))



    def test_assign330(self):
        input = """
        Function: main
            Body:
                d = a[b] == b + 5;
            EndBody.
                """
        expect = str(
            Program([
                FuncDecl(
                    Id("main"),
                    [],
                    ([],[Assign(Id("d"), BinaryOp("==", ArrayCell(Id("a"), [Id("b")]), BinaryOp("+",Id("b"),IntLiteral(5))))])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_whilestmtcomplex331(self):
        input = """
        Function: main
        Parameter: k[5], l;
            Body:
                Var: i = 0;
                While (i < 5)
                k[i] = l +. 1.0;
                i = i + 1;
                EndWhile.
            EndBody.
                """
        expect = str(
            Program([
                FuncDecl(
                    Id("main"),
                    [VarDecl(Id("k"), [5], None),VarDecl(Id("l"), [], None)],
                    ([VarDecl(Id("i"), [], IntLiteral(0))],[While( BinaryOp("<", Id("i"), IntLiteral(5)),
                                ( [],
                                  [ Assign(ArrayCell(Id("k"), [Id("i")]),BinaryOp("+.", Id("l"),FloatLiteral(1.0))),
                                    Assign(Id("i"),BinaryOp("+", Id("i"),IntLiteral(1)))] )
                                )])
                )
            ])
        )
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))
