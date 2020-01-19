# Generated from .\antlr\Typt.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TyptParser import TyptParser
else:
    from TyptParser import TyptParser

# This class defines a complete generic visitor for a parse tree produced by TyptParser.

class TyptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TyptParser#program.
    def visitProgram(self, ctx:TyptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#using.
    def visitUsing(self, ctx:TyptParser.UsingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#stmt.
    def visitStmt(self, ctx:TyptParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#parameter_list.
    def visitParameter_list(self, ctx:TyptParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#parameter.
    def visitParameter(self, ctx:TyptParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#argument_list.
    def visitArgument_list(self, ctx:TyptParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#argument.
    def visitArgument(self, ctx:TyptParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#simple_stmt.
    def visitSimple_stmt(self, ctx:TyptParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#small_stmt.
    def visitSmall_stmt(self, ctx:TyptParser.Small_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#expr_stmt.
    def visitExpr_stmt(self, ctx:TyptParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#anassign.
    def visitAnassign(self, ctx:TyptParser.AnassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#augassign.
    def visitAugassign(self, ctx:TyptParser.AugassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#var_dec_stmt.
    def visitVar_dec_stmt(self, ctx:TyptParser.Var_dec_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#del_stmt.
    def visitDel_stmt(self, ctx:TyptParser.Del_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#pass_stmt.
    def visitPass_stmt(self, ctx:TyptParser.Pass_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#flow_stmt.
    def visitFlow_stmt(self, ctx:TyptParser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#break_stmt.
    def visitBreak_stmt(self, ctx:TyptParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#continue_stmt.
    def visitContinue_stmt(self, ctx:TyptParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#return_stmt.
    def visitReturn_stmt(self, ctx:TyptParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#compound_stmt.
    def visitCompound_stmt(self, ctx:TyptParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#if_stmt.
    def visitIf_stmt(self, ctx:TyptParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#while_stmt.
    def visitWhile_stmt(self, ctx:TyptParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#for_stmt.
    def visitFor_stmt(self, ctx:TyptParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#suite.
    def visitSuite(self, ctx:TyptParser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#func_def.
    def visitFunc_def(self, ctx:TyptParser.Func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#func_signature.
    def visitFunc_signature(self, ctx:TyptParser.Func_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#func_parameter_list.
    def visitFunc_parameter_list(self, ctx:TyptParser.Func_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#class_def.
    def visitClass_def(self, ctx:TyptParser.Class_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#class_dec.
    def visitClass_dec(self, ctx:TyptParser.Class_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#class_method.
    def visitClass_method(self, ctx:TyptParser.Class_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#class_static_method.
    def visitClass_static_method(self, ctx:TyptParser.Class_static_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#test.
    def visitTest(self, ctx:TyptParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#or_test.
    def visitOr_test(self, ctx:TyptParser.Or_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#and_test.
    def visitAnd_test(self, ctx:TyptParser.And_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#not_test.
    def visitNot_test(self, ctx:TyptParser.Not_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#comparison.
    def visitComparison(self, ctx:TyptParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#comp_op.
    def visitComp_op(self, ctx:TyptParser.Comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#expr.
    def visitExpr(self, ctx:TyptParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#xor_expr.
    def visitXor_expr(self, ctx:TyptParser.Xor_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#and_expr.
    def visitAnd_expr(self, ctx:TyptParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#shift_expr.
    def visitShift_expr(self, ctx:TyptParser.Shift_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#arith_expr.
    def visitArith_expr(self, ctx:TyptParser.Arith_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#term.
    def visitTerm(self, ctx:TyptParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#factor.
    def visitFactor(self, ctx:TyptParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#power.
    def visitPower(self, ctx:TyptParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#atom_expr.
    def visitAtom_expr(self, ctx:TyptParser.Atom_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#atom.
    def visitAtom(self, ctx:TyptParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#trailer.
    def visitTrailer(self, ctx:TyptParser.TrailerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#subscriptlist.
    def visitSubscriptlist(self, ctx:TyptParser.SubscriptlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#subscript.
    def visitSubscript(self, ctx:TyptParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#sliceop.
    def visitSliceop(self, ctx:TyptParser.SliceopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#exprlist.
    def visitExprlist(self, ctx:TyptParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#testlist.
    def visitTestlist(self, ctx:TyptParser.TestlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#name.
    def visitName(self, ctx:TyptParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#value.
    def visitValue(self, ctx:TyptParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyptParser#typt_type.
    def visitTypt_type(self, ctx:TyptParser.Typt_typeContext):
        return self.visitChildren(ctx)



del TyptParser