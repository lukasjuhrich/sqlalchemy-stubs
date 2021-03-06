# Stubs for sqlalchemy.dialects.mssql.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from sqlalchemy.sql import compiler
from ... import schema as sa_schema
from ...sql import compiler as compiler, expression as expression
from ...sql import util as sql_util
from ...engine import reflection as reflection, default as default
from ... import types as sqltypes
from ...types import INTEGER as INTEGER, BIGINT as BIGINT, SMALLINT as SMALLINT, DECIMAL as DECIMAL, NUMERIC as NUMERIC, FLOAT as FLOAT, TIMESTAMP as TIMESTAMP, DATETIME as DATETIME, DATE as DATE, BINARY as BINARY, TEXT as TEXT, VARCHAR as VARCHAR, NVARCHAR as NVARCHAR, CHAR as CHAR, NCHAR as NCHAR
from . import information_schema as ischema

MS_2016_VERSION = ...  # type: Any
MS_2014_VERSION = ...  # type: Any
MS_2012_VERSION = ...  # type: Any
MS_2008_VERSION = ...  # type: Any
MS_2005_VERSION = ...  # type: Any
MS_2000_VERSION = ...  # type: Any
RESERVED_WORDS = ...  # type: Any

class REAL(sqltypes.REAL):
    __visit_name__ = ...  # type: str
    def __init__(self, **kw) -> None: ...

class TINYINT(sqltypes.Integer):
    __visit_name__ = ...  # type: str

class _MSDate(sqltypes.Date):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class TIME(sqltypes.TIME):
    precision = ...  # type: Any
    def __init__(self, precision: Optional[Any] = ..., **kwargs) -> None: ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

_MSTime = TIME

class _DateTimeBase(object):
    def bind_processor(self, dialect): ...

class _MSDateTime(_DateTimeBase, sqltypes.DateTime): ...

class SMALLDATETIME(_DateTimeBase, sqltypes.DateTime):
    __visit_name__ = ...  # type: str

class DATETIME2(_DateTimeBase, sqltypes.DateTime):
    __visit_name__ = ...  # type: str
    precision = ...  # type: Any
    def __init__(self, precision: Optional[Any] = ..., **kw) -> None: ...

class DATETIMEOFFSET(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str
    precision = ...  # type: Any
    def __init__(self, precision: Optional[Any] = ..., **kwargs) -> None: ...

class _StringType(object):
    def __init__(self, collation: Optional[Any] = ...) -> None: ...

class NTEXT(sqltypes.UnicodeText):
    __visit_name__ = ...  # type: str

class VARBINARY(sqltypes.VARBINARY, sqltypes.LargeBinary):
    __visit_name__ = ...  # type: str

class IMAGE(sqltypes.LargeBinary):
    __visit_name__ = ...  # type: str

class BIT(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str

class MONEY(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str

class SMALLMONEY(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str

class UNIQUEIDENTIFIER(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str

class SQL_VARIANT(sqltypes.TypeEngine):
    __visit_name__ = ...  # type: str

MSDateTime = ...  # type: Any
MSDate = ...  # type: Any
MSReal = ...  # type: Any
MSTinyInteger = ...  # type: Any
MSTime = ...  # type: Any
MSSmallDateTime = ...  # type: Any
MSDateTime2 = ...  # type: Any
MSDateTimeOffset = ...  # type: Any
MSText = ...  # type: Any
MSNText = ...  # type: Any
MSString = ...  # type: Any
MSNVarchar = ...  # type: Any
MSChar = ...  # type: Any
MSNChar = ...  # type: Any
MSBinary = ...  # type: Any
MSVarBinary = ...  # type: Any
MSImage = ...  # type: Any
MSBit = ...  # type: Any
MSMoney = ...  # type: Any
MSSmallMoney = ...  # type: Any
MSUniqueIdentifier = ...  # type: Any
MSVariant = ...  # type: Any
ischema_names = ...  # type: Any

class MSTypeCompiler(compiler.GenericTypeCompiler):
    def visit_FLOAT(self, type_, **kw): ...
    def visit_TINYINT(self, type_, **kw): ...
    def visit_DATETIMEOFFSET(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...
    def visit_DATETIME2(self, type_, **kw): ...
    def visit_SMALLDATETIME(self, type_, **kw): ...
    def visit_unicode(self, type_, **kw): ...
    def visit_text(self, type_, **kw): ...
    def visit_unicode_text(self, type_, **kw): ...
    def visit_NTEXT(self, type_, **kw): ...
    def visit_TEXT(self, type_, **kw): ...
    def visit_VARCHAR(self, type_, **kw): ...
    def visit_CHAR(self, type_, **kw): ...
    def visit_NCHAR(self, type_, **kw): ...
    def visit_NVARCHAR(self, type_, **kw): ...
    def visit_date(self, type_, **kw): ...
    def visit_time(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_IMAGE(self, type_, **kw): ...
    def visit_VARBINARY(self, type_, **kw): ...
    def visit_boolean(self, type_, **kw): ...
    def visit_BIT(self, type_, **kw): ...
    def visit_MONEY(self, type_, **kw): ...
    def visit_SMALLMONEY(self, type_, **kw): ...
    def visit_UNIQUEIDENTIFIER(self, type_, **kw): ...
    def visit_SQL_VARIANT(self, type_, **kw): ...

class MSExecutionContext(default.DefaultExecutionContext):
    def pre_exec(self): ...
    def post_exec(self): ...
    def get_lastrowid(self): ...
    def handle_dbapi_exception(self, e): ...
    def get_result_proxy(self): ...

class MSSQLCompiler(compiler.SQLCompiler):
    returning_precedes_values = ...  # type: bool
    extract_map = ...  # type: Any
    tablealiases = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def visit_now_func(self, fn, **kw): ...
    def visit_current_date_func(self, fn, **kw): ...
    def visit_length_func(self, fn, **kw): ...
    def visit_char_length_func(self, fn, **kw): ...
    def visit_concat_op_binary(self, binary, operator, **kw): ...
    def visit_true(self, expr, **kw): ...
    def visit_false(self, expr, **kw): ...
    def visit_match_op_binary(self, binary, operator, **kw): ...
    def get_select_precolumns(self, select, **kw): ...
    def get_from_hint_text(self, table, text): ...
    def get_crud_hint_text(self, table, text): ...
    def limit_clause(self, select, **kw): ...
    def visit_select(self, select, **kwargs): ...
    def visit_table(self, *args, **kwargs): ...
    def visit_alias(self, alias, **kw): ...
    def visit_column(self, *args, **kw): ...
    def visit_extract(self, extract, **kw): ...
    def visit_savepoint(self, savepoint_stmt): ...
    def visit_rollback_to_savepoint(self, savepoint_stmt): ...
    def visit_binary(self, binary, **kwargs): ...
    def returning_clause(self, stmt, returning_cols): ...
    def get_cte_preamble(self, recursive): ...
    def label_select_column(self, select, column, asfrom): ...
    def for_update_clause(self, select): ...
    def order_by_clause(self, select, **kw): ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw): ...

class MSSQLStrictCompiler(MSSQLCompiler):
    ansi_bind_rules = ...  # type: bool
    def visit_in_op_binary(self, binary, operator, **kw): ...
    def visit_notin_op_binary(self, binary, operator, **kw): ...
    def render_literal_value(self, value, type_): ...

class MSDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column, **kwargs): ...
    def visit_create_index(self, *args, **kwargs): ...
    def visit_drop_index(self, drop): ...
    def visit_primary_key_constraint(self, constraint): ...
    def visit_unique_constraint(self, constraint): ...

class MSIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words = ...  # type: Any
    def __init__(self, dialect) -> None: ...
    def quote_schema(self, schema, force: Optional[Any] = ...): ...

class MSDialect(default.DefaultDialect):
    name = ...  # type: str
    supports_default_values = ...  # type: bool
    supports_empty_insert = ...  # type: bool
    execution_ctx_cls = ...  # type: Any
    use_scope_identity = ...  # type: bool
    max_identifier_length = ...  # type: int
    schema_name = ...  # type: str
    colspecs = ...  # type: Any
    engine_config_types = ...  # type: Any
    ischema_names = ...  # type: Any
    supports_native_boolean = ...  # type: bool
    supports_unicode_binds = ...  # type: bool
    postfetch_lastrowid = ...  # type: bool
    server_version_info = ...  # type: Any
    statement_compiler = ...  # type: Any
    ddl_compiler = ...  # type: Any
    type_compiler = ...  # type: Any
    preparer = ...  # type: Any
    construct_arguments = ...  # type: Any
    query_timeout = ...  # type: Any
    deprecate_large_types = ...  # type: Any
    legacy_schema_aliasing = ...  # type: Any
    isolation_level = ...  # type: Any
    def __init__(self, query_timeout: Optional[Any] = ..., use_scope_identity: bool = ..., max_identifier_length: Optional[Any] = ..., schema_name: str = ..., isolation_level: Optional[Any] = ..., deprecate_large_types: Optional[Any] = ..., legacy_schema_aliasing: bool = ..., **opts) -> None: ...
    def do_savepoint(self, connection, name): ...
    def do_release_savepoint(self, connection, name): ...
    def set_isolation_level(self, connection, level): ...
    def get_isolation_level(self, connection): ...
    def initialize(self, connection): ...
    def on_connect(self): ...
    def has_table(self, connection, tablename, dbname, owner, schema): ...
    def get_schema_names(self, connection, **kw): ...
    def get_table_names(self, connection, dbname, owner, schema, **kw): ...
    def get_view_names(self, connection, dbname, owner, schema, **kw): ...
    def get_indexes(self, connection, tablename, dbname, owner, schema, **kw): ...
    def get_view_definition(self, connection, viewname, dbname, owner, schema, **kw): ...
    def get_columns(self, connection, tablename, dbname, owner, schema, **kw): ...
    def get_pk_constraint(self, connection, tablename, dbname, owner, schema, **kw): ...
    def get_foreign_keys(self, connection, tablename, dbname, owner, schema, **kw): ...
