# Generated from .\antlr\Typt.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TyptParser import TyptParser
else:
    from TyptParser import TyptParser

# This class defines a complete listener for a parse tree produced by TyptParser.
class TyptListener(ParseTreeListener):

    # Enter a parse tree produced by TyptParser#program.
    def enterProgram(self, ctx:TyptParser.ProgramContext):
        pass

    # Exit a parse tree produced by TyptParser#program.
    def exitProgram(self, ctx:TyptParser.ProgramContext):
        pass


    # Enter a parse tree produced by TyptParser#using.
    def enterUsing(self, ctx:TyptParser.UsingContext):
        pass

    # Exit a parse tree produced by TyptParser#using.
    def exitUsing(self, ctx:TyptParser.UsingContext):
        pass


    # Enter a parse tree produced by TyptParser#stmt.
    def enterStmt(self, ctx:TyptParser.StmtContext):
        pass

    # Exit a parse tree produced by TyptParser#stmt.
    def exitStmt(self, ctx:TyptParser.StmtContext):
        pass


    # Enter a parse tree produced by TyptParser#argument_list.
    def enterArgument_list(self, ctx:TyptParser.Argument_listContext):
        pass

    # Exit a parse tree produced by TyptParser#argument_list.
    def exitArgument_list(self, ctx:TyptParser.Argument_listContext):
        pass


    # Enter a parse tree produced by TyptParser#argument.
    def enterArgument(self, ctx:TyptParser.ArgumentContext):
        pass

    # Exit a parse tree produced by TyptParser#argument.
    def exitArgument(self, ctx:TyptParser.ArgumentContext):
        pass


    # Enter a parse tree produced by TyptParser#simple_stmt.
    def enterSimple_stmt(self, ctx:TyptParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#simple_stmt.
    def exitSimple_stmt(self, ctx:TyptParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#small_stmt.
    def enterSmall_stmt(self, ctx:TyptParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#small_stmt.
    def exitSmall_stmt(self, ctx:TyptParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#expr_stmt.
    def enterExpr_stmt(self, ctx:TyptParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#expr_stmt.
    def exitExpr_stmt(self, ctx:TyptParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#anassign.
    def enterAnassign(self, ctx:TyptParser.AnassignContext):
        pass

    # Exit a parse tree produced by TyptParser#anassign.
    def exitAnassign(self, ctx:TyptParser.AnassignContext):
        pass


    # Enter a parse tree produced by TyptParser#augassign.
    def enterAugassign(self, ctx:TyptParser.AugassignContext):
        pass

    # Exit a parse tree produced by TyptParser#augassign.
    def exitAugassign(self, ctx:TyptParser.AugassignContext):
        pass


    # Enter a parse tree produced by TyptParser#var_dec_stmt.
    def enterVar_dec_stmt(self, ctx:TyptParser.Var_dec_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#var_dec_stmt.
    def exitVar_dec_stmt(self, ctx:TyptParser.Var_dec_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#del_stmt.
    def enterDel_stmt(self, ctx:TyptParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#del_stmt.
    def exitDel_stmt(self, ctx:TyptParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#pass_stmt.
    def enterPass_stmt(self, ctx:TyptParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#pass_stmt.
    def exitPass_stmt(self, ctx:TyptParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#flow_stmt.
    def enterFlow_stmt(self, ctx:TyptParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#flow_stmt.
    def exitFlow_stmt(self, ctx:TyptParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#break_stmt.
    def enterBreak_stmt(self, ctx:TyptParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#break_stmt.
    def exitBreak_stmt(self, ctx:TyptParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#continue_stmt.
    def enterContinue_stmt(self, ctx:TyptParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#continue_stmt.
    def exitContinue_stmt(self, ctx:TyptParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#return_stmt.
    def enterReturn_stmt(self, ctx:TyptParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#return_stmt.
    def exitReturn_stmt(self, ctx:TyptParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#compound_stmt.
    def enterCompound_stmt(self, ctx:TyptParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#compound_stmt.
    def exitCompound_stmt(self, ctx:TyptParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#if_stmt.
    def enterIf_stmt(self, ctx:TyptParser.If_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#if_stmt.
    def exitIf_stmt(self, ctx:TyptParser.If_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#while_stmt.
    def enterWhile_stmt(self, ctx:TyptParser.While_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#while_stmt.
    def exitWhile_stmt(self, ctx:TyptParser.While_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#for_stmt.
    def enterFor_stmt(self, ctx:TyptParser.For_stmtContext):
        pass

    # Exit a parse tree produced by TyptParser#for_stmt.
    def exitFor_stmt(self, ctx:TyptParser.For_stmtContext):
        pass


    # Enter a parse tree produced by TyptParser#suite.
    def enterSuite(self, ctx:TyptParser.SuiteContext):
        pass

    # Exit a parse tree produced by TyptParser#suite.
    def exitSuite(self, ctx:TyptParser.SuiteContext):
        pass


    # Enter a parse tree produced by TyptParser#func_def.
    def enterFunc_def(self, ctx:TyptParser.Func_defContext):
        pass

    # Exit a parse tree produced by TyptParser#func_def.
    def exitFunc_def(self, ctx:TyptParser.Func_defContext):
        pass


    # Enter a parse tree produced by TyptParser#func_signature.
    def enterFunc_signature(self, ctx:TyptParser.Func_signatureContext):
        pass

    # Exit a parse tree produced by TyptParser#func_signature.
    def exitFunc_signature(self, ctx:TyptParser.Func_signatureContext):
        pass


    # Enter a parse tree produced by TyptParser#func_parameter_list.
    def enterFunc_parameter_list(self, ctx:TyptParser.Func_parameter_listContext):
        pass

    # Exit a parse tree produced by TyptParser#func_parameter_list.
    def exitFunc_parameter_list(self, ctx:TyptParser.Func_parameter_listContext):
        pass


    # Enter a parse tree produced by TyptParser#class_def.
    def enterClass_def(self, ctx:TyptParser.Class_defContext):
        pass

    # Exit a parse tree produced by TyptParser#class_def.
    def exitClass_def(self, ctx:TyptParser.Class_defContext):
        pass


    # Enter a parse tree produced by TyptParser#class_dec.
    def enterClass_dec(self, ctx:TyptParser.Class_decContext):
        pass

    # Exit a parse tree produced by TyptParser#class_dec.
    def exitClass_dec(self, ctx:TyptParser.Class_decContext):
        pass


    # Enter a parse tree produced by TyptParser#class_method.
    def enterClass_method(self, ctx:TyptParser.Class_methodContext):
        pass

    # Exit a parse tree produced by TyptParser#class_method.
    def exitClass_method(self, ctx:TyptParser.Class_methodContext):
        pass


    # Enter a parse tree produced by TyptParser#class_static_method.
    def enterClass_static_method(self, ctx:TyptParser.Class_static_methodContext):
        pass

    # Exit a parse tree produced by TyptParser#class_static_method.
    def exitClass_static_method(self, ctx:TyptParser.Class_static_methodContext):
        pass


    # Enter a parse tree produced by TyptParser#test.
    def enterTest(self, ctx:TyptParser.TestContext):
        pass

    # Exit a parse tree produced by TyptParser#test.
    def exitTest(self, ctx:TyptParser.TestContext):
        pass


    # Enter a parse tree produced by TyptParser#or_test.
    def enterOr_test(self, ctx:TyptParser.Or_testContext):
        pass

    # Exit a parse tree produced by TyptParser#or_test.
    def exitOr_test(self, ctx:TyptParser.Or_testContext):
        pass


    # Enter a parse tree produced by TyptParser#and_test.
    def enterAnd_test(self, ctx:TyptParser.And_testContext):
        pass

    # Exit a parse tree produced by TyptParser#and_test.
    def exitAnd_test(self, ctx:TyptParser.And_testContext):
        pass


    # Enter a parse tree produced by TyptParser#not_test.
    def enterNot_test(self, ctx:TyptParser.Not_testContext):
        pass

    # Exit a parse tree produced by TyptParser#not_test.
    def exitNot_test(self, ctx:TyptParser.Not_testContext):
        pass


    # Enter a parse tree produced by TyptParser#comparison.
    def enterComparison(self, ctx:TyptParser.ComparisonContext):
        pass

    # Exit a parse tree produced by TyptParser#comparison.
    def exitComparison(self, ctx:TyptParser.ComparisonContext):
        pass


    # Enter a parse tree produced by TyptParser#comp_op.
    def enterComp_op(self, ctx:TyptParser.Comp_opContext):
        pass

    # Exit a parse tree produced by TyptParser#comp_op.
    def exitComp_op(self, ctx:TyptParser.Comp_opContext):
        pass


    # Enter a parse tree produced by TyptParser#expr.
    def enterExpr(self, ctx:TyptParser.ExprContext):
        pass

    # Exit a parse tree produced by TyptParser#expr.
    def exitExpr(self, ctx:TyptParser.ExprContext):
        pass


    # Enter a parse tree produced by TyptParser#xor_expr.
    def enterXor_expr(self, ctx:TyptParser.Xor_exprContext):
        pass

    # Exit a parse tree produced by TyptParser#xor_expr.
    def exitXor_expr(self, ctx:TyptParser.Xor_exprContext):
        pass


    # Enter a parse tree produced by TyptParser#and_expr.
    def enterAnd_expr(self, ctx:TyptParser.And_exprContext):
        pass

    # Exit a parse tree produced by TyptParser#and_expr.
    def exitAnd_expr(self, ctx:TyptParser.And_exprContext):
        pass


    # Enter a parse tree produced by TyptParser#shift_expr.
    def enterShift_expr(self, ctx:TyptParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by TyptParser#shift_expr.
    def exitShift_expr(self, ctx:TyptParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by TyptParser#arith_expr.
    def enterArith_expr(self, ctx:TyptParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by TyptParser#arith_expr.
    def exitArith_expr(self, ctx:TyptParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by TyptParser#term.
    def enterTerm(self, ctx:TyptParser.TermContext):
        pass

    # Exit a parse tree produced by TyptParser#term.
    def exitTerm(self, ctx:TyptParser.TermContext):
        pass


    # Enter a parse tree produced by TyptParser#factor.
    def enterFactor(self, ctx:TyptParser.FactorContext):
        pass

    # Exit a parse tree produced by TyptParser#factor.
    def exitFactor(self, ctx:TyptParser.FactorContext):
        pass


    # Enter a parse tree produced by TyptParser#power.
    def enterPower(self, ctx:TyptParser.PowerContext):
        pass

    # Exit a parse tree produced by TyptParser#power.
    def exitPower(self, ctx:TyptParser.PowerContext):
        pass


    # Enter a parse tree produced by TyptParser#atom_expr.
    def enterAtom_expr(self, ctx:TyptParser.Atom_exprContext):
        pass

    # Exit a parse tree produced by TyptParser#atom_expr.
    def exitAtom_expr(self, ctx:TyptParser.Atom_exprContext):
        pass


    # Enter a parse tree produced by TyptParser#atom.
    def enterAtom(self, ctx:TyptParser.AtomContext):
        pass

    # Exit a parse tree produced by TyptParser#atom.
    def exitAtom(self, ctx:TyptParser.AtomContext):
        pass


    # Enter a parse tree produced by TyptParser#trailer.
    def enterTrailer(self, ctx:TyptParser.TrailerContext):
        pass

    # Exit a parse tree produced by TyptParser#trailer.
    def exitTrailer(self, ctx:TyptParser.TrailerContext):
        pass


    # Enter a parse tree produced by TyptParser#subscriptlist.
    def enterSubscriptlist(self, ctx:TyptParser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by TyptParser#subscriptlist.
    def exitSubscriptlist(self, ctx:TyptParser.SubscriptlistContext):
        pass


    # Enter a parse tree produced by TyptParser#subscript.
    def enterSubscript(self, ctx:TyptParser.SubscriptContext):
        pass

    # Exit a parse tree produced by TyptParser#subscript.
    def exitSubscript(self, ctx:TyptParser.SubscriptContext):
        pass


    # Enter a parse tree produced by TyptParser#sliceop.
    def enterSliceop(self, ctx:TyptParser.SliceopContext):
        pass

    # Exit a parse tree produced by TyptParser#sliceop.
    def exitSliceop(self, ctx:TyptParser.SliceopContext):
        pass


    # Enter a parse tree produced by TyptParser#exprlist.
    def enterExprlist(self, ctx:TyptParser.ExprlistContext):
        pass

    # Exit a parse tree produced by TyptParser#exprlist.
    def exitExprlist(self, ctx:TyptParser.ExprlistContext):
        pass


    # Enter a parse tree produced by TyptParser#testlist.
    def enterTestlist(self, ctx:TyptParser.TestlistContext):
        pass

    # Exit a parse tree produced by TyptParser#testlist.
    def exitTestlist(self, ctx:TyptParser.TestlistContext):
        pass


    # Enter a parse tree produced by TyptParser#name.
    def enterName(self, ctx:TyptParser.NameContext):
        pass

    # Exit a parse tree produced by TyptParser#name.
    def exitName(self, ctx:TyptParser.NameContext):
        pass


    # Enter a parse tree produced by TyptParser#value.
    def enterValue(self, ctx:TyptParser.ValueContext):
        pass

    # Exit a parse tree produced by TyptParser#value.
    def exitValue(self, ctx:TyptParser.ValueContext):
        pass


    # Enter a parse tree produced by TyptParser#typt_type.
    def enterTypt_type(self, ctx:TyptParser.Typt_typeContext):
        pass

    # Exit a parse tree produced by TyptParser#typt_type.
    def exitTypt_type(self, ctx:TyptParser.Typt_typeContext):
        pass


