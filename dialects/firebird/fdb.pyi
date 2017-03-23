# Stubs for sqlalchemy.dialects.firebird.fdb (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .kinterbasdb import FBDialect_kinterbasdb as FBDialect_kinterbasdb

class FBDialect_fdb(FBDialect_kinterbasdb):
    def __init__(self, enable_rowcount: bool = ..., retaining: bool = ..., **kwargs) -> None: ...
    @classmethod
    def dbapi(cls): ...
    def create_connect_args(self, url): ...

dialect = ...  # type: Any
