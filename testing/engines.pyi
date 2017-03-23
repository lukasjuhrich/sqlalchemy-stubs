# Stubs for sqlalchemy.testing.engines (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .util import decorator as decorator

class ConnectionKiller:
    proxy_refs = ...  # type: Any
    testing_engines = ...  # type: Any
    conns = ...  # type: Any
    def __init__(self) -> None: ...
    def add_engine(self, engine): ...
    def connect(self, dbapi_conn, con_record): ...
    def checkout(self, dbapi_con, con_record, con_proxy): ...
    def invalidate(self, dbapi_con, con_record, exception): ...
    def rollback_all(self): ...
    def close_all(self): ...
    def assert_all_closed(self): ...

testing_reaper = ...  # type: Any

def drop_all_tables(metadata, bind): ...
def assert_conns_closed(fn, *args, **kw): ...
def rollback_open_connections(fn, *args, **kw): ...
def close_first(fn, *args, **kw): ...
def close_open_connections(fn, *args, **kw): ...
def all_dialects(exclude: Optional[Any] = ...): ...

class ReconnectFixture:
    dbapi = ...  # type: Any
    connections = ...  # type: Any
    def __init__(self, dbapi) -> None: ...
    def __getattr__(self, key): ...
    def connect(self, *args, **kwargs): ...
    def shutdown(self): ...

def reconnecting_engine(url: Optional[Any] = ..., options: Optional[Any] = ...): ...
def testing_engine(url: Optional[Any] = ..., options: Optional[Any] = ...): ...
def mock_engine(dialect_name: Optional[Any] = ...): ...

class DBAPIProxyCursor:
    engine = ...  # type: Any
    connection = ...  # type: Any
    cursor = ...  # type: Any
    def __init__(self, engine, conn, *args, **kwargs) -> None: ...
    def execute(self, stmt, parameters: Optional[Any] = ..., **kw): ...
    def executemany(self, stmt, params, **kw): ...
    def __getattr__(self, key): ...

class DBAPIProxyConnection:
    conn = ...  # type: Any
    engine = ...  # type: Any
    cursor_cls = ...  # type: Any
    def __init__(self, engine, cursor_cls) -> None: ...
    def cursor(self, *args, **kwargs): ...
    def close(self): ...
    def __getattr__(self, key): ...

def proxying_engine(conn_cls: Any = ..., cursor_cls: Any = ...): ...
