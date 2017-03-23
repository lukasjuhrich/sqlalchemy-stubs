# Stubs for sqlalchemy.dialects.mssql.zxjdbc (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from ...connectors.zxJDBC import ZxJDBCConnector as ZxJDBCConnector
from .base import MSDialect as MSDialect, MSExecutionContext as MSExecutionContext

class MSExecutionContext_zxjdbc(MSExecutionContext):
    def pre_exec(self): ...
    def post_exec(self): ...

class MSDialect_zxjdbc(ZxJDBCConnector, MSDialect):
    jdbc_db_name = ...  # type: str
    jdbc_driver_name = ...  # type: str
    execution_ctx_cls = ...  # type: Any

dialect = ...  # type: Any
