
        package generated.Python
        
        sealed class excepthandler(open val lineno: int, open val col_offset: int, open val end_lineno: int?, open val end_col_offset: int?)
        
        
        data class ExceptHandler(val type: expr?, val name: identifier?, val body: kotlin.collections.List<stmt>, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : excepthandler(lineno, col_offset, end_lineno, end_col_offset) 
        
    