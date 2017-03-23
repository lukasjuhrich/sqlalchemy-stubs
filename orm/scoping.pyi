# Stubs for sqlalchemy.orm.scoping (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .. import exc as sa_exc
from . import exc as orm_exc

class scoped_session:
    session_factory = ...  # type: Any
    registry = ...  # type: Any
    def __init__(self, session_factory, scopefunc: Optional[Any] = ...) -> None: ...
    def __call__(self, **kw): ...
    def remove(self): ...
    def configure(self, **kwargs): ...
    def query_property(self, query_cls: Optional[Any] = ...): ...
