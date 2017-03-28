# Stubs for sqlalchemy.dialects.postgresql.zxjdbc (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from ...connectors.zxJDBC import ZxJDBCConnector as ZxJDBCConnector
from .base import PGDialect as PGDialect, PGExecutionContext as PGExecutionContext

class PGExecutionContext_zxjdbc(PGExecutionContext):
    def create_cursor(self): ...

class PGDialect_zxjdbc(ZxJDBCConnector, PGDialect):
    jdbc_db_name = ...  # type: str
    jdbc_driver_name = ...  # type: str
    execution_ctx_cls = ...  # type: Any
    supports_native_decimal = ...  # type: bool
    DataHandler = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...

dialect = ...  # type: Any