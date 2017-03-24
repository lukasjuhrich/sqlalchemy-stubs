# Stubs for sqlalchemy.dialects.sybase.pysybase (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from sqlalchemy.sql import sqltypes
from sqlalchemy import types as sqltypes
from sqlalchemy.dialects.sybase.base import SybaseDialect, SybaseExecutionContext, SybaseSQLCompiler

class _SybNumeric(sqltypes.Numeric):
    def result_processor(self, dialect, type_): ...

class SybaseExecutionContext_pysybase(SybaseExecutionContext):
    def set_ddl_autocommit(self, dbapi_connection, value): ...
    def pre_exec(self): ...

class SybaseSQLCompiler_pysybase(SybaseSQLCompiler):
    def bindparam_string(self, name, **kw): ...

class SybaseDialect_pysybase(SybaseDialect):
    driver = ...  # type: str
    execution_ctx_cls = ...  # type: Any
    statement_compiler = ...  # type: Any
    colspecs = ...  # type: Any
    @classmethod
    def dbapi(cls): ...
    def create_connect_args(self, url): ...
    def do_executemany(self, cursor, statement, parameters, context: Optional[Any] = ...): ...
    def is_disconnect(self, e, connection, cursor): ...

dialect = ...  # type: Any
