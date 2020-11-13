
        package generated.Python
        
        sealed class expr(open val lineno: int, open val col_offset: int, open val end_lineno: int?, open val end_col_offset: int?)
        
        
        data class BoolOp(val op: boolop, val values: kotlin.collections.List<expr>, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class NamedExpr(val target: expr, val value: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class BinOp(val left: expr, val op: operator, val right: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class UnaryOp(val op: unaryop, val operand: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Lambda(val args: arguments, val body: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class IfExp(val test: expr, val body: expr, val orelse: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Dict(val keys: kotlin.collections.List<expr>, val values: kotlin.collections.List<expr>, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Set(val elts: kotlin.collections.List<expr>, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class ListComp(val elt: expr, val generators: kotlin.collections.List<comprehension>, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class SetComp(val elt: expr, val generators: kotlin.collections.List<comprehension>, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class DictComp(val key: expr, val value: expr, val generators: kotlin.collections.List<comprehension>, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class GeneratorExp(val elt: expr, val generators: kotlin.collections.List<comprehension>, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Await(val value: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Yield(val value: expr?, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class YieldFrom(val value: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Compare(val left: expr, val ops: kotlin.collections.List<cmpop>, val comparators: kotlin.collections.List<expr>, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Call(val func: expr, val args: kotlin.collections.List<expr>, val keywords: kotlin.collections.List<keyword>, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class FormattedValue(val value: expr, val conversion: int?, val format_spec: expr?, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class JoinedStr(val values: kotlin.collections.List<expr>, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Constant(val value: constant, val kind: string?, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Attribute(val value: expr, val attr: identifier, val ctx: expr_context, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Subscript(val value: expr, val slice: expr, val ctx: expr_context, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Starred(val value: expr, val ctx: expr_context, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Name(val id: identifier, val ctx: expr_context, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class List(val elts: kotlin.collections.List<expr>, val ctx: expr_context, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Tuple(val elts: kotlin.collections.List<expr>, val ctx: expr_context, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        

        data class Slice(val lower: expr?, val upper: expr?, val step: expr?, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : expr(lineno, col_offset, end_lineno, end_col_offset) 
        
    