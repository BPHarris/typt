"""listener.py -- provides the custom listener for Typt."""

from antlr.TyptParser import TyptParser
from antlr.TyptVisitor import TyptVisitor

# Import Typt types
from typt.typt_types import NameSuperPair, NameTypePair, TestSuitePair
from typt.typt_types import Type
from typt.typt_types import NoneType
from typt.typt_types import BoolType
from typt.typt_types import IntType
from typt.typt_types import FloatType
from typt.typt_types import StringType
from typt.typt_types import ObjectBaseType
from typt.typt_types import ListType
from typt.typt_types import TupleType
from typt.typt_types import SetType
from typt.typt_types import DictType
from typt.typt_types import FunctionType
from typt.typt_types import ObjectType
from typt.typt_types import is_int, is_float

# Import Type AST nodes
from typt.node import NodeMetadata
from typt.program_node import ProgramNode
from typt.using_node import UsingNode
from typt.func_def_node import FuncDefNode
from typt.func_signature_node import FuncSignatureNode

from typt.argument_list_node import ArgumentListNode

from typt.stmt_node import StmtNode

from typt.expr_stmt_node import ExprStmtNode
from typt.assignment_expr_stmt_node import AssignmentExprStmtNode
from typt.var_dec_stmt_node import VarDecStmtNode
from typt.del_stmt_node import DelStmtNode
from typt.pass_stmt_node import PassStmtNode
from typt.break_stmt_node import BreakStmtNode
from typt.continue_stmt_node import ContinueStmtNode
from typt.return_stmt_node import ReturnStmtNode

from typt.if_stmt_node import IfStmtNode
from typt.while_stmt_node import WhileStmtNode
from typt.for_stmt_node import ForStmtNode

from typt.class_node import ClassNode
from typt.class_method_node import ClassMethodNode

from typt.suite_node import SuiteNode

from typt.test_node import TestNode
from typt.test.test_op_node import TestOpNode
from typt.test.comp_op_node import CompOpNode
from typt.test.expr_op_node import ExprOpNode
from typt.test.unary_expr_op_node import UnaryExprOpNode

from typt.test.atom_expr_node import AtomExprNode, TrailerType
from typt.test.atom_node import AtomNode
from typt.test.var_ref_node import VarRefNode
from typt.test.literal_node import LiteralNode
from typt.subscript_node import SubscriptNode

from typing import Iterable, List

# Todo:
#   TODO: How to handle self?


# HACK ANTLR's Context::getText() returns the repr of each token without
#   preserving spacing. This method is hack-y, but preserves spaceing.
class SourceGetter:
    """Get the source code of a given line number range."""

    source_code = list()    # type: List[str]

    @staticmethod
    def get(start_line: int, end_line: int = None):
        """Return the source code of the given lines."""
        # Change from file line number to index (i.e. start 1 to start 0)
        start_line -= 1

        # If not end_line, then only get one line
        if not end_line:
            end_line = start_line + 1

        return ''.join(SourceGetter.source_code[start_line:end_line])


def get_metadata(ctx):
    """Return the NodeMetadata for the given context."""
    start_line, end_line = ctx.start.line, ctx.stop.line
    start_column = ctx.start.column

    return NodeMetadata(
        start_line,
        start_column,
        SourceGetter.get(start_line, end_line)
    )


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
            self.program.using_list += [self.visitUsing(using_ctx)]

        # Add stmts to program
        for stmt_ctx in ctx.stmt():
            self.program.stmt_list += [self.visitStmt(stmt_ctx)]

        return self.program

    def visitUsing(self, ctx: TyptParser.UsingContext) -> UsingNode:
        """Visit a UsingNode."""
        library_name = self.visitName(ctx.library_name)

        using = UsingNode(library_name, meta=get_metadata(ctx))

        # Add function signatures to using-declaration
        for fs_ctx in ctx.func_signature():
            using.function_signature_list += [self.visitFunc_signature(fs_ctx)]

        return using

    def visitStmt(self, ctx: TyptParser.StmtContext) -> StmtNode:
        """Visit `stmt' rule."""
        # If simple statment, visit child
        if ctx.simple_stmt():
            return self.visitSimple_stmt(ctx.simple_stmt())

        # Otherwise (is compound stmt), visit child
        return self.visitCompound_stmt(ctx.compound_stmt())

    def visitArgument_list(self, ctx: TyptParser.Argument_listContext) -> ArgumentListNode:
        """Return argument_list."""
        argument_list_node = ArgumentListNode()

        # Add arguments
        for argument in ctx.argument():
            argument_list_node.argument_list += [self.visitArgument(argument)]

        return argument_list_node

    def visitArgument(self, ctx: TyptParser.ArgumentContext) -> TestNode:
        """Delegate to test."""
        return self.visitTest(ctx.test())

    def visitSimple_stmt(self, ctx: TyptParser.Simple_stmtContext) -> StmtNode:
        """Visit `simple_stmt' rule."""
        # Visit the child small_stmt
        return self.visitSmall_stmt(ctx.small_stmt())

    def visitSmall_stmt(self, ctx: TyptParser.Small_stmtContext) -> StmtNode:
        """Visit `small_stmt' rule."""
        # Return the child statement
        if ctx.expr_stmt():
            return self.visitExpr_stmt(ctx.expr_stmt())
        if ctx.var_dec_stmt():
            return self.visitVar_dec_stmt(ctx.var_dec_stmt())
        if ctx.del_stmt():
            return self.visitDel_stmt(ctx.del_stmt())
        if ctx.pass_stmt():
            return self.visitPass_stmt(ctx.pass_stmt())
        if ctx.flow_stmt():
            return self.visitFlow_stmt(ctx.flow_stmt())

        raise NotImplementedError('Small statment type not implemented yet.')

    def visitExpr_stmt(self, ctx: TyptParser.Expr_stmtContext) -> StmtNode:
        """Visit `expr_stmt' rule.

        Args:
            ctx (Expr_stmtContext) : ...

        expr_stmt ::= ...

        """
        # If no right-hand side (i.e. not an assignment expression)
        if not ctx.rhs:
            return ExprStmtNode(self.visitTest(ctx.lhs))

        # Otherwise (i.e. is assignment expression), get type of assignment
        if ctx.anassign():
            assignment_type = ctx.anassign().getText()
        if ctx.augassign():
            assignment_type = ctx.augassign().getText()

        return AssignmentExprStmtNode(
            self.visitTest(ctx.lhs),
            assignment_type,
            self.visitTest(ctx.rhs)
        )

    def visitAnassign(self, ctx: TyptParser.AnassignContext) -> None:
        """Dead method (never called)."""
        raise NotImplementedError('Should not be reached (anassign).')

    def visitAugassign(self, ctx: TyptParser.AugassignContext) -> None:
        """Dead method (never called)."""
        raise NotImplementedError('Should not be reached (augassign).')

    def visitVar_dec_stmt(self, ctx: TyptParser.Var_dec_stmtContext) -> VarDecStmtNode:
        """Visit `var_dec_stmt' rule.

        Args:
            ctx (Var_dec_stmtContext) : ...

        var_dec_stmt ::= ...

        """
        # If no initial value given, set to None
        if not ctx.rhs:
            return VarDecStmtNode(
                self.visitName(ctx.lhs),
                self.visitTypt_type(ctx.typt_type())
            )

        # Otherwise, parse intial value
        return VarDecStmtNode(
            self.visitName(ctx.lhs),
            self.visitTypt_type(ctx.typt_type()),
            self.visitTest(ctx.rhs)
        )

    def visitDel_stmt(self, ctx: TyptParser.Del_stmtContext) -> DelStmtNode:
        """Visit `del_stmt' rule."""
        # Get expr_list
        expr_list = self.visitExprlist(ctx.exprlist())

        return DelStmtNode(expr_list)

    def visitPass_stmt(self, ctx: TyptParser.Pass_stmtContext) -> PassStmtNode:
        """Visit `pass_stmt' rule."""
        return PassStmtNode(meta=get_metadata(ctx))

    def visitFlow_stmt(self, ctx: TyptParser.Flow_stmtContext) -> StmtNode:
        """Visit `flow_stmt' rule."""
        # Return relevant flow-stmt
        if ctx.break_stmt():
            return self.visitBreak_stmt(ctx.break_stmt())
        if ctx.continue_stmt():
            return self.visitContinue_stmt(ctx.continue_stmt())
        if ctx.return_stmt():
            return self.visitReturn_stmt(ctx.return_stmt())

        raise NotImplementedError('Flow statement type not implemented.')

    def visitBreak_stmt(self, ctx: TyptParser.Break_stmtContext) -> BreakStmtNode:
        """Visit `break_stmt' rule."""
        return BreakStmtNode(meta=get_metadata(ctx))

    def visitContinue_stmt(self, ctx: TyptParser.Continue_stmtContext) -> ContinueStmtNode:
        """Visit `continue_stmt' rule."""
        # Return a new continue statement
        return ContinueStmtNode(meta=get_metadata(ctx))

    def visitReturn_stmt(self, ctx: TyptParser.Return_stmtContext) -> ReturnStmtNode:
        """Visit `return_stmt' rule."""
        # Return statement with return value
        if ctx.test():
            return ReturnStmtNode(self.visitTest(ctx.test()))

        # 'Empty' return statement
        return ReturnStmtNode()

    def visitCompound_stmt(self, ctx: TyptParser.Compound_stmtContext) -> StmtNode:
        """Visit `compound_stmt' rule.

        Args:
            ctx (Compound_stmtContext) : ...

        compound_stmt ::= if_stmt
                        | while_stmt
                        | for_stmt
                        | func_def
                        | class_def

        """
        # Return relevant child statement
        if ctx.if_stmt():
            return self.visitIf_stmt(ctx.if_stmt())
        if ctx.while_stmt():
            return self.visitWhile_stmt(ctx.while_stmt())
        if ctx.for_stmt():
            return self.visitFor_stmt(ctx.for_stmt())
        if ctx.func_def():
            return self.visitFunc_def(ctx.func_def())
        if ctx.class_def():
            return self.visitClass_def(ctx.class_def())

        raise NotImplementedError('That compound statement is not implemented')

    def visitIf_stmt(self, ctx: TyptParser.If_stmtContext) -> IfStmtNode:
        """Visit `if_stmt' rule.

        Args:
            ctx (If_stmtContext) : ...

        if_stmt ::= 'if'    test ':' suite
                    ('elif' test ':' suite)*
                    ('else'      ':' suite)?

        """
        # Get if branch
        if_branch = TestSuitePair(
            self.visitTest(ctx.if_test), self.visitSuite(ctx.if_suite)
        )

        if_stmt_node = IfStmtNode(if_branch, meta=get_metadata(ctx))

        # Get the elif branches
        # HACK if there is an else branch, then len(suites) = len(tests)+1
        #   but the final suite is discarded from the elif branches in the zip
        # HACK the [1:] removes the if branch's test+suite from being in the
        #   elif branch
        tests = [self.visitTest(test) for test in ctx.test()[1:]]
        suites = [self.visitSuite(suite) for suite in ctx.suite()[1:]]
        if_stmt_node.elif_branches = [
            TestSuitePair(t, s) for (t, s) in zip(tests, suites)
        ]

        # Get the else branch
        if ctx.else_suite:
            if_stmt_node.else_branch = self.visitSuite(ctx.else_suite)

        return if_stmt_node

    def visitWhile_stmt(self, ctx: TyptParser.While_stmtContext) -> WhileStmtNode:
        """Visit `while_stmt' rule.

        Args:
            ctx (While_stmtContext) : ...

        while_stmt ::=  'while' test ':' suite
                        ('else'      ':' suite)?

        """
        # Get while branch
        while_branch = TestSuitePair(
            self.visitTest(ctx.while_test), self.visitSuite(ctx.while_suite)
        )

        # Get else branch
        else_branch = None
        if ctx.else_suite:
            else_branch = self.visitSuite(ctx.else_suite)

        return WhileStmtNode(while_branch, else_branch, meta=get_metadata())

    def visitFor_stmt(self, ctx: TyptParser.For_stmtContext) -> ForStmtNode:
        """Visit `for_stmt' rule.

        Args:
            ctx (For_stmtContext) : ...

        for_stmt ::= 'for' exprlist 'in' testlist   ':' suite
                     ('else'                        ':' suite)?

        """
        # Get for condition and body
        expr_list = self.visitExprlist(ctx.expr_list)
        test_list = self.visitTestlist(ctx.test_list)
        for_branch = self.visitSuite(ctx.for_suite)

        # Get else branch
        else_branch = None
        if ctx.else_suite:
            else_branch = self.visitSuite(ctx.else_suite)

        return ForStmtNode(
            expr_list, test_list, for_branch, else_branch, meta=get_metadata()
        )

    def visitSuite(self, ctx: TyptParser.SuiteContext) -> SuiteNode:
        """Visit `suite' rule.

        Args:
            ctx (SuiteContext) : ...

        suite ::= simple_stmt | NEWLINE INDENT stmt+ DEDENT

        """
        suite_node = SuiteNode(meta=get_metadata(ctx))

        # If the suite is just a simple statement, add it
        if ctx.simple_stmt():
            suite_node.stmt_list = [self.visitSimple_stmt(ctx.simple_stmt())]

        # Otherwise, it is a block => add each stmt in the block
        for s in ctx.stmt():
            suite_node.stmt_list += [self.visitStmt(s)]

        return suite_node

    def visitFunc_def(self, ctx: TyptParser.Func_defContext) -> FuncDefNode:
        """Visit `func_def' rule."""
        # Get function signature
        func_signature = self.visitFunc_signature(ctx.func_signature())

        # Get suite
        suite = self.visitSuite(ctx.suite())

        # Return FuncDefNode
        return FuncDefNode(func_signature, suite)

    def visitFunc_signature(self, ctx: TyptParser.Func_signatureContext) -> FuncSignatureNode:
        """Visit `func_signature' rule."""
        func_signature = FuncSignatureNode(
            self.visitName(ctx.name()),
            self.visitTypt_type(ctx.typt_type()),
            meta=get_metadata(ctx)
        )

        # If parameters non-empty, get parameter nodes
        if ctx.func_parameter_list():
            func_signature.parameter_list = \
                self.visitFunc_parameter_list(ctx.func_parameter_list())

        return func_signature

    def visitFunc_parameter_list(self, ctx: TyptParser.Func_parameter_listContext) -> Iterable[NameTypePair]:
        """Visit `func_parameter_list' rule."""
        # Return the parameter list as a list of tuples of form (id, type)
        names = [self.visitName(name) for name in ctx.name()]
        types = [self.visitTypt_type(type) for type in ctx.typt_type()]

        return [NameTypePair(n, t) for (n, t) in zip(names, types)]

    def visitClass_def(self, ctx: TyptParser.Class_defContext) -> ClassNode:
        """Parse a class definition."""
        # TODO: visitCompound_stmt returns StmtNode but ClassNode is sub of
        #       Node. Change ClassNode or change visitCompund_stmt?
        name_super_pair = self.visitClass_dec(ctx.class_dec())

        # Handle the empty class
        if ctx.the_empty_class:
            return ClassNode(name_super_pair)

        # Get initialiser, if has one
        initialiser_parameters = None
        initialiser_suite = None
        if ctx.initialiser:
            # Get parameters if there are any
            if ctx.func_parameter_list():
                initialiser_parameters = self.visitFunc_parameter_list(
                    ctx.func_parameter_list()
                )
            initialiser_suite = self.visitSuite(ctx.suite())

        class_node = ClassNode(
            name_super_pair,
            initialiser_parameters,
            initialiser_suite
        )

        # Add class variables
        # TODO

        # Add methods
        for method in ctx.class_method():
            class_node.class_methods += [self.visitClass_method(method)]

        return class_node

    def visitClass_dec(self, ctx: TyptParser.Class_decContext) -> NameSuperPair:
        """Return the NameSuperPair of the class declaration."""
        # Get class name and set super name to default
        class_name = self.visitName(ctx.class_name)
        super_name = 'Object'

        # If super provided, set it
        if ctx.super_name:
            super_name = self.visitName(ctx.super_name)

        return NameSuperPair(class_name, super_name)

    def visitClass_method(self, ctx: TyptParser.Class_methodContext) -> ClassMethodNode:
        """Return a ClassMethodNode for the given context."""
        # Function (method) signature
        function_signature = FuncSignatureNode(
            self.visitName(ctx.name()),
            self.visitTypt_type(ctx.typt_type())
        )

        if ctx.func_parameter_list():
            function_signature.parameter_list = self.visitFunc_parameter_list(
                ctx.func_parameter_list()
            )

        # Method suite
        method_suite = self.visitSuite(ctx.suite())

        return ClassMethodNode(function_signature, method_suite)

    def visitClass_static_method(self, ctx: TyptParser.Class_static_methodContext) -> None:
        """Return a static class method."""
        # TODO static methods
        raise NotImplementedError('Static methods not yet implemented.')

    def visitTest(self, ctx: TyptParser.TestContext) -> TestNode:
        """Delegate to or_test (test ::= or_test)."""
        return self.visitOr_test(ctx.or_test())

    def visitOr_test(self, ctx: TyptParser.Or_testContext) -> TestNode:
        """Get node for or_test; delegates to and_test if needed.

        or_test ::= and_test ('or' and_test)*

        """
        # Get LHS
        lhs = self.visitAnd_test(ctx.lhs)

        # If only lhs => delegate (no or_test occuring)
        if not ctx.op:
            return lhs

        test_op_node = TestOpNode(ctx.op.text, lhs)

        # Add remaining operators
        # NOTE [0] == lhs, so skip it with [1:]
        for rhs in ctx.and_test()[1:]:
            test_op_node.operands += [self.visitAnd_test(rhs)]

        return test_op_node

    def visitAnd_test(self, ctx: TyptParser.And_testContext) -> TestNode:
        """Get node for and_test; delegates to not_test if needed.

        and_test ::= not_test ('and' not_test)*

        """
        # Get LHS
        lhs = self.visitNot_test(ctx.lhs)

        # If only lhs => delegate (no or_test occuring)
        if not ctx.op:
            return lhs

        test_op_node = TestOpNode(ctx.op.text, lhs)

        # Add remaining operators
        # NOTE [0] == lhs, so skip it with [1:]
        for rhs in ctx.not_test()[1:]:
            test_op_node.operands += [self.visitNot_test(rhs)]

        return test_op_node

    def visitNot_test(self, ctx: TyptParser.Not_testContext) -> TestNode:
        """Get node for not_test; delegates to comparison if needed.

        not_test ::= 'not' not_test | comparison

        """
        # If rule is: 'not' (not_test), recurse
        if ctx.lhs:
            return TestOpNode(ctx.op.text, self.visitNot_test(ctx.lhs))

        # Otherwise, delegate to comparison
        return self.visitComparison(ctx.comparison())

    def visitComparison(self, ctx: TyptParser.ComparisonContext) -> TestNode:
        """Get sub tree of CompOpNodes."""
        # Get lhs
        lhs = self.visitExpr(ctx.lhs)

        # If no RHS operands, delegate to Expr
        if not ctx.op:
            return lhs

        # Foreach operator and operand, lhs' = (lhs OP rhs)
        # i.e. left-associative
        # NOTE [1:] to skip lhs
        for op, rhs in zip(ctx.comp_op(), ctx.expr()[1:]):
            rhs = self.visitExpr(rhs)
            lhs = CompOpNode(op.getText(), lhs, rhs)

        return lhs

    def visitComp_op(self, ctx: TyptParser.Comp_opContext) -> None:
        """Will not be reached. Use <op_ctx>.getText() instead."""
        raise NotImplementedError('Should not reach visitComp_op.')

    def visitExpr(self, ctx: TyptParser.ExprContext) -> TestNode:
        """Delegate to or_expr."""
        return self.visitOr_expr(ctx.or_expr())

    def visitOr_expr(self, ctx: TyptParser.Or_exprContext) -> TestNode:
        """Get sub tree of ExprOpNode."""
        # Get lhs
        lhs = self.visitXor_expr(ctx.lhs)

        # If no RHS operands, delegate
        if not ctx.op:
            return lhs

        # Foreach operator and operand, lhs' = (lhs OP rhs)
        # i.e. left-associative
        # NOTE [1:] to skip lhs
        for rhs in ctx.xor_expr()[1:]:
            rhs = self.visitXor_expr(rhs)
            lhs = ExprOpNode(ctx.op.text, lhs, rhs)

        return lhs

    def visitXor_expr(self, ctx: TyptParser.Xor_exprContext) -> TestNode:
        """Get sub tree of ExprOpNode."""
        # Get lhs
        lhs = self.visitAnd_expr(ctx.lhs)

        # If no RHS operands, delegate
        if not ctx.op:
            return lhs

        # Foreach operator and operand, lhs' = (lhs OP rhs)
        # i.e. left-associative
        # NOTE [1:] to skip lhs
        for rhs in ctx.and_expr()[1:]:
            rhs = self.visitAnd_expr(rhs)
            lhs = ExprOpNode(ctx.op.text, lhs, rhs)

        return lhs

    def visitAnd_expr(self, ctx: TyptParser.And_exprContext) -> TestNode:
        """Get sub tree of ExprOpNode."""
        # Get lhs
        lhs = self.visitShift_expr(ctx.lhs)

        # If no RHS operands, delegate
        if not ctx.op:
            return lhs

        # Foreach operator and operand, lhs' = (lhs OP rhs)
        # i.e. left-associative
        # NOTE [1:] to skip lhs
        for rhs in ctx.shift_expr()[1:]:
            rhs = self.visitShift_expr(rhs)
            lhs = ExprOpNode(ctx.op.text, lhs, rhs)

        return lhs

    def visitShift_expr(self, ctx: TyptParser.Shift_exprContext) -> TestNode:
        """Get sub tree of ExprOpNode."""
        # Get lhs
        lhs = self.visitArith_expr(ctx.lhs)

        # If no RHS operands, delegate to Expr
        if not ctx.op:
            return lhs

        # Foreach operator and operand, lhs' = (lhs OP rhs)
        # i.e. left-associative
        # NOTE [1:] to skip lhs
        for op, rhs in zip(ctx.shift_op(), ctx.arith_expr()[1:]):
            rhs = self.visitArith_expr(rhs)
            lhs = ExprOpNode(op.getText(), lhs, rhs)

        return lhs

    def visitShift_op(self, ctx: TyptParser.Shift_opContext) -> None:
        """Will not be reached. Use <op_ctx>.getText() instead."""
        raise NotImplementedError('Should not reach visitShift_op.')

    def visitArith_expr(self, ctx: TyptParser.Arith_exprContext) -> TestNode:
        """Get sub tree of ExprOpNode."""
        # Get lhs
        lhs = self.visitTerm(ctx.lhs)

        # If no RHS operands, delegate to Expr
        if not ctx.op:
            return lhs

        # Foreach operator and operand, lhs' = (lhs OP rhs)
        # i.e. left-associative
        # NOTE [1:] to skip lhs
        for op, rhs in zip(ctx.arith_op(), ctx.term()[1:]):
            rhs = self.visitTerm(rhs)
            lhs = ExprOpNode(op.getText(), lhs, rhs)

        return lhs

    def visitArith_op(self, ctx: TyptParser.Arith_opContext) -> None:
        """Will not be reached. Use <op_ctx>.getText() instead."""
        raise NotImplementedError('Should not reach visitArith_op.')

    def visitTerm(self, ctx: TyptParser.TermContext) -> TestNode:
        """Get sub tree of ExprOpNode."""
        # Get lhs
        lhs = self.visitFactor(ctx.lhs)

        # If no RHS operands, delegate to Expr
        if not ctx.op:
            return lhs

        # Foreach operator and operand, lhs' = (lhs OP rhs)
        # i.e. left-associative
        # NOTE [1:] to skip lhs
        for op, rhs in zip(ctx.term_op(), ctx.factor()[1:]):
            rhs = self.visitFactor(rhs)
            lhs = ExprOpNode(op.getText(), lhs, rhs)

        return lhs

    def visitTerm_op(self, ctx: TyptParser.Term_opContext) -> None:
        """Will not be reached. Use <op_ctx>.getText() instead."""
        raise NotImplementedError('Should not reach visitTerm_op.')

    def visitFactor(self, ctx: TyptParser.FactorContext) -> TestNode:
        """Return UnaryExprOpNode or delegate."""
        # If no op, just delegate
        if not ctx.op:
            return self.visitPower(ctx.power())

        # Otherwise, get factor as unary op
        return UnaryExprOpNode(
            ctx.op.getText(), self.visitFactor(ctx.factor())
        )

    def visitFactor_op(self, ctx: TyptParser.Factor_opContext) -> None:
        """Will not be reached. Use <op_ctx>.getText() instead."""
        raise NotImplementedError('Should not reach visitFactor_op.')

    def visitPower(self, ctx: TyptParser.PowerContext) -> TestNode:
        """Get sub tree of ExprOpNode."""
        # Get lhs
        lhs = self.visitAtom_expr(ctx.lhs)

        # If no RHS operands, delegate to atom_expr
        if not ctx.op:
            return lhs

        # Otherwise, get factor
        return ExprOpNode(ctx.op.text, lhs, self.visitFactor(ctx.factor()))

    def visitAtom_expr(self, ctx: TyptParser.Atom_exprContext) -> TestNode:
        """Return atom expression node -- with trailers."""
        atom_expr = AtomExprNode(self.visitAtom(ctx.atom()))

        # Add trailers
        for trailer in ctx.trailer():
            atom_expr.trailer_list += [self.visitTrailer(trailer)]

        return atom_expr

    def visitAtom(self, ctx: TyptParser.AtomContext) -> AtomNode:
        """Return VarRefNode or LiteralNode, depending on atom."""
        # If the atom is a variable reference, return a new VarRefNode
        if ctx.name():
            return VarRefNode(self.visitName(ctx.name()), meta=get_metadata(ctx))

        atom_type = None
        atom_text = ctx.getText()

        if ctx.string_literal:                          # String
            atom_type = StringType()
        if is_int(atom_text):                           # Int
            atom_type = IntType()
        if is_float(atom_text):                         # Float
            atom_type = FloatType()
        if atom_text == 'None':                         # None
            atom_type = NoneType()
        if atom_text in (repr(True), repr(False)):      # Boolean
            atom_type = BoolType()

        # TODO List, tuple, set, dict

        if atom_text == 'self':                         # Self
            # TODO self references
            print('\x1b[1;37;41mvisitAtom: self not implemented\x1b[0m')
            atom_type = 'SelfType'

        if not atom_type:
            raise NotImplementedError(f'Atom {atom_text} is not implemented.')

        return LiteralNode(atom_type, atom_text, meta=get_metadata(ctx))

    def visitTrailer(self, ctx: TyptParser.TrailerContext) -> TrailerType:
        """Delegate da trailer."""
        # Is argument_list?
        if ctx.argument_list():
            return self.visitArgument_list(ctx.argument_list())

        # HACK Is empty argument_list
        if ctx.getText() == '()':
            return ArgumentListNode()

        # Is subscriptlist?
        if ctx.subscriptlist():
            return self.visitSubscriptlist(ctx.subscriptlist())

        # Is name?
        if ctx.name():
            return self.visitName(ctx.name())

        raise NotImplementedError('Invalid trailer type.')

    def visitSubscriptlist(self, ctx: TyptParser.SubscriptlistContext) -> SubscriptNode:
        """Delegate to subscript."""
        return self.visitSubscript(ctx.subscript())

    def visitSubscript(self, ctx: TyptParser.SubscriptContext) -> SubscriptNode:
        """Get the subscript."""
        # Get start:upto:step
        start = None if not ctx.start else self.visitTest(ctx.start)
        upto = None if not ctx.upto else self.visitTest(ctx.upto)
        step = None if not ctx.step else self.visitSliceop(ctx.step)

        return SubscriptNode(start, upto, step)

    def visitSliceop(self, ctx: TyptParser.SliceopContext):
        """DELEGATE HAHAHAHAHA."""
        if ctx.test():
            return self.visitTest(ctx.test())

        raise NotImplementedError('Should not reach me.')

    def visitExprlist(self, ctx: TyptParser.ExprlistContext) -> List[ExprOpNode]:
        """Return list of expression operation nodes, length >= 1."""
        expr_list = list()

        for expr in ctx.expr():
            expr_list += [self.visitExpr(expr)]

        return expr_list

    def visitTestlist(self, ctx: TyptParser.TestlistContext) -> List[TestNode]:
        """Return list of expression operation nodes, length >= 1."""
        test_list = list()

        for test in ctx.test():
            test_list += [self.visitTest(test)]

        return test_list

    def visitName(self, ctx: TyptParser.NameContext) -> str:
        """Return the contents."""
        return ctx.getText()

    def visitTypt_type(self, ctx: TyptParser.Typt_typeContext) -> Type:
        """Temporary visit for typt_type."""
        text = ctx.getText()

        # Base Types (None, Bool, Int, Float, String, ObjectBaseType)
        if ctx.none_type:
            return NoneType()
        if ctx.bool_type:
            return BoolType()
        if ctx.int_type:
            return IntType()
        if ctx.float_type:
            return FloatType()
        if ctx.string_type:
            return StringType()
        if ctx.object_base_type:
            return ObjectBaseType()

        # Object Type
        if ctx.object_type:
            # Get members names, types
            names = [self.visitName(name) for name in ctx.name()]
            types = [self.visitTypt_type(t) for t in ctx.typt_type()]

            # Create NameTypePairs
            members = list()
            for (n, t) in zip(names, types):
                members += [NameTypePair(n, t)]

            return ObjectType(members)

        # Function Type
        if ctx.function_type:
            return_type = self.visitTypt_type(ctx.return_type)

            # Get parameter types
            # NOTE [:-1] to skip return type in param types -- duh!
            parameter_types = list()
            for ctx_type in ctx.typt_type()[:-1]:
                parameter_types += [self.visitTypt_type(ctx_type)]

            return FunctionType(parameter_types, return_type)

        # List, Tuple, Set, Dict
        if ctx.list_type:
            return ListType(self.visitTypt_type(ctx.element_type))
        if ctx.tuple_type:
            # Get type list
            element_types = list()
            for ctx_typt_type in ctx.typt_type():
                element_types += [self.visitTypt_type(ctx_typt_type)]

            return TupleType(element_types)
        if ctx.set_type:
            return SetType(self.visitTypt_type(ctx.element_type))
        if ctx.dict_type:
            return DictType(
                self.visitTypt_type(ctx.key_type),
                self.visitTypt_type(ctx.value_type)
            )

        raise NotImplementedError(f'The type \'{text}\' is not implemented.')
