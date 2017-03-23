# Stubs for sqlalchemy.orm.exc (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import sa_exc
from .. import exc as sa_exc

NO_STATE = ...  # type: Any

class StaleDataError(sa_exc.SQLAlchemyError): ...

ConcurrentModificationError = ...  # type: Any

class FlushError(sa_exc.SQLAlchemyError): ...
class UnmappedError(sa_exc.InvalidRequestError): ...
class ObjectDereferencedError(sa_exc.SQLAlchemyError): ...
class DetachedInstanceError(sa_exc.SQLAlchemyError): ...

class UnmappedInstanceError(UnmappedError):
    def __init__(self, base, obj, msg: Optional[Any] = ...) -> None: ...
    def __reduce__(self): ...

class UnmappedClassError(UnmappedError):
    def __init__(self, cls, msg: Optional[Any] = ...) -> None: ...
    def __reduce__(self): ...

class ObjectDeletedError(sa_exc.InvalidRequestError):
    def __init__(self, base, state, msg: Optional[Any] = ...) -> None: ...
    def __reduce__(self): ...

class UnmappedColumnError(sa_exc.InvalidRequestError): ...
class NoResultFound(sa_exc.InvalidRequestError): ...
class MultipleResultsFound(sa_exc.InvalidRequestError): ...
