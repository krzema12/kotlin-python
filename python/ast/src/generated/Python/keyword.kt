
        package generated.Python
        
        sealed class keyword(open val lineno: int, open val col_offset: int, open val end_lineno: int?, open val end_col_offset: int?)
        
        
        data class keywordImpl(val arg: identifier?, val value: expr, override val lineno: int, override val col_offset: int, override val end_lineno: int?, override val end_col_offset: int?) 
            : keyword(lineno, col_offset, end_lineno, end_col_offset) 
        
    