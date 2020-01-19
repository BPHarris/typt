"""listener.py - provides the custom listener for Typt."""

from antlr.TyptParser import TyptParser
from antlr.TyptVisitor import TyptVisitor

from typt.node import Node
from typt.program_node import ProgramNode

# Done:
#   program


class Typt(TyptVisitor):
    """Provide custom Typt listener."""

    def __init__(self):
        """Initialise custom visitor."""
        self.program = ProgramNode()

        super().__init__()

    def visitProgram(self, ctx: TyptParser.ProgramContext) -> ProgramNode:
        """Visit `program' rule.

        Args:
            ctx (ProgramContext) : The program context

        Get the child using-declarations and statements.

        program ::= using* stmt* EOF

        """

        # Add using-declarations to program
        for using_ctx in ctx.using():
            using = self.visitUsing(using_ctx)
            self.program.using_list += [using]

        # Add stmts to program
        for stmt_ctx in ctx.stmt():
            stmt = self.visitStmt(stmt_ctx)

        return self.program

    def visitUsing(self, ctx: TyptParser.UsingContext):
        """Visit `using' rule.

        Args:
            ctx (UsingContext) : ...

        using ::= ...

        """
        return self.visitChildren(ctx)

    def visitStmt(self, ctx: TyptParser.StmtContext):
        """Visit `stmt' rule.

        Args:
            ctx (StmtContext) : ...

        stmt ::= ...

        """
        return self.visitChildren(ctx)

    def visitParameter_list(self, ctx: TyptParser.Parameter_listContext):
        """Visit `parameter_list' rule.

        Args:
            ctx (Parameter_listContext) : ...

        parameter_list ::= ...

        """
        return self.visitChildren(ctx)

    def visitParameter(self, ctx: TyptParser.ParameterContext):
        """Visit `parameter' rule.

        Args:
            ctx (ParameterContext) : ...

        parameter ::= ...

        """
        return self.visitChildren(ctx)

    def visitArgument_list(self, ctx: TyptParser.Argument_listContext):
        """Visit `argument_list' rule.

        Args:
            ctx (Argument_listContext) : ...

        argument_list ::= ...

        """
        return self.visitChildren(ctx)

    def visitArgument(self, ctx: TyptParser.ArgumentContext):
        """Visit `argument' rule.

        Args:
            ctx (ArgumentContext) : ...

        argument ::= ...

        """
        return self.visitChildren(ctx)

    def visitSimple_stmt(self, ctx: TyptParser.Simple_stmtContext):
        """Visit `simple_stmt' rule.

        Args:
            ctx (Simple_stmtContext) : ...

        simple_stmt ::= ...

        """
        return self.visitChildren(ctx)

    def visitSmall_stmt(self, ctx: TyptParser.Small_stmtContext):
        """Visit `small_stmt' rule.

        Args:
            ctx (Small_stmtContext) : ...

        small_stmt ::= ...

        """
        return self.visitChildren(ctx)

    def visitExpr_stmt(self, ctx: TyptParser.Expr_stmtContext):
        """Visit `expr_stmt' rule.

        Args:
            ctx (Expr_stmtContext) : ...

        expr_stmt ::= ...

        """
        return self.visitChildren(ctx)


    def visitAnassign(self, ctx: TyptParser.AnassignContext):
        """Visit `anassign' rule.

        Args:
            ctx (AnassignContext) : ...

        anassign ::= ...

        """
        return self.visitChildren(ctx)


    def visitAugassign(self, ctx: TyptParser.AugassignContext):
        """Visit `augassign' rule.

        Args:
            ctx (AugassignContext) : ...

        augassign ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitVar_dec_stmt(self, ctx: TyptParser.Var_dec_stmtContext):
        """Visit `var_dec_stmt' rule.

        Args:
            ctx (Var_dec_stmtContext) : ...

        var_dec_stmt ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitDel_stmt(self, ctx: TyptParser.Del_stmtContext):
        """Visit `del_stmt' rule.

        Args:
            ctx (Del_stmtContext) : ...

        del_stmt ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitPass_stmt(self, ctx: TyptParser.Pass_stmtContext):
        """Visit `pass_stmt' rule.

        Args:
            ctx (Pass_stmtContext) : ...

        pass_stmt ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitFlow_stmt(self, ctx: TyptParser.Flow_stmtContext):
        """Visit `flow_stmt' rule.

        Args:
            ctx (Flow_stmtContext) : ...

        flow_stmt ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitBreak_stmt(self, ctx: TyptParser.Break_stmtContext):
        """Visit `break_stmt' rule.

        Args:
            ctx (Break_stmtContext) : ...

        break_stmt ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitContinue_stmt(self, ctx: TyptParser.Continue_stmtContext):
        """Visit `continue_stmt' rule.

        Args:
            ctx (Continue_stmtContext) : ...

        continue_stmt ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitReturn_stmt(self, ctx: TyptParser.Return_stmtContext):
        """Visit `return_stmt' rule.

        Args:
            ctx (Return_stmtContext) : ...

        return_stmt ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitCompound_stmt(self, ctx: TyptParser.Compound_stmtContext):
        """Visit `compound_stmt' rule.

        Args:
            ctx (Compound_stmtContext) : ...

        compound_stmt ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitIf_stmt(self, ctx: TyptParser.If_stmtContext):
        """Visit `if_stmt' rule.

        Args:
            ctx (If_stmtContext) : ...

        if_stmt ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitWhile_stmt(self, ctx: TyptParser.While_stmtContext):
        """Visit `while_stmt' rule.

        Args:
            ctx (While_stmtContext) : ...

        while_stmt ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitFor_stmt(self, ctx: TyptParser.For_stmtContext):
        """Visit `for_stmt' rule.

        Args:
            ctx (For_stmtContext) : ...

        for_stmt ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitSuite(self, ctx: TyptParser.SuiteContext):
        """Visit `suite' rule.

        Args:
            ctx (SuiteContext) : ...

        suite ::= ...

        """
        return self.visitChildren(ctx)
    
    def visitFunc_def(self, ctx: TyptParser.Func_defContext):
        return self.visitChildren(ctx)
    
    def visitFunc_signature(self, ctx: TyptParser.Func_signatureContext):
        return self.visitChildren(ctx)
    
    def visitFunc_parameter_list(self, ctx: TyptParser.Func_parameter_listContext):
        return self.visitChildren(ctx)
    
    def visitClass_def(self, ctx: TyptParser.Class_defContext):
        return self.visitChildren(ctx)
    
    def visitClass_dec(self, ctx: TyptParser.Class_decContext):
        return self.visitChildren(ctx)
    
    def visitClass_method(self, ctx: TyptParser.Class_methodContext):
        return self.visitChildren(ctx)
    
    def visitClass_static_method(self, ctx: TyptParser.Class_static_methodContext):
        return self.visitChildren(ctx)
    
    def visitTest(self, ctx: TyptParser.TestContext):
        return self.visitChildren(ctx)
    
    def visitOr_test(self, ctx: TyptParser.Or_testContext):
        return self.visitChildren(ctx)
    
    def visitAnd_test(self, ctx: TyptParser.And_testContext):
        return self.visitChildren(ctx)
    
    def visitNot_test(self, ctx: TyptParser.Not_testContext):
        return self.visitChildren(ctx)
    
    def visitComparison(self, ctx: TyptParser.ComparisonContext):
        return self.visitChildren(ctx)
    
    def visitComp_op(self, ctx: TyptParser.Comp_opContext):
        return self.visitChildren(ctx)
    
    def visitExpr(self, ctx: TyptParser.ExprContext):
        return self.visitChildren(ctx)
    
    def visitXor_expr(self, ctx: TyptParser.Xor_exprContext):
        return self.visitChildren(ctx)
    
    def visitAnd_expr(self, ctx: TyptParser.And_exprContext):
        return self.visitChildren(ctx)
    
    def visitShift_expr(self, ctx: TyptParser.Shift_exprContext):
        return self.visitChildren(ctx)
    
    def visitArith_expr(self, ctx: TyptParser.Arith_exprContext):
        return self.visitChildren(ctx)
    
    def visitTerm(self, ctx: TyptParser.TermContext):
        return self.visitChildren(ctx)
    
    def visitFactor(self, ctx: TyptParser.FactorContext):
        return self.visitChildren(ctx)
    
    def visitPower(self, ctx: TyptParser.PowerContext):
        return self.visitChildren(ctx)
    
    def visitAtom_expr(self, ctx: TyptParser.Atom_exprContext):
        return self.visitChildren(ctx)
    
    def visitAtom(self, ctx: TyptParser.AtomContext):
        return self.visitChildren(ctx)
    
    def visitTrailer(self, ctx: TyptParser.TrailerContext):
        return self.visitChildren(ctx)
    
    def visitSubscriptlist(self, ctx: TyptParser.SubscriptlistContext):
        return self.visitChildren(ctx)
    
    def visitSubscript(self, ctx: TyptParser.SubscriptContext):
        return self.visitChildren(ctx)
    
    def visitSliceop(self, ctx: TyptParser.SliceopContext):
        return self.visitChildren(ctx)
    
    def visitExprlist(self, ctx: TyptParser.ExprlistContext):
        return self.visitChildren(ctx)
    
    def visitTestlist(self, ctx: TyptParser.TestlistContext):
        return self.visitChildren(ctx)
    
    def visitName(self, ctx: TyptParser.NameContext):
        return self.visitChildren(ctx)
    
    def visitValue(self, ctx: TyptParser.ValueContext):
        return self.visitChildren(ctx)
    
    def visitTypt_type(self, ctx: TyptParser.Typt_typeContext):
        return self.visitChildren(ctx)