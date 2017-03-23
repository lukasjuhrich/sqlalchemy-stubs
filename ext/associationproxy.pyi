# Stubs for sqlalchemy.ext.associationproxy (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import interfaces
from ..orm import collections as collections, interfaces as interfaces
from ..sql import not_ as not_, or_ as or_

def association_proxy(target_collection, attr, **kw): ...

ASSOCIATION_PROXY = ...  # type: Any

class AssociationProxy(interfaces.InspectionAttrInfo):
    is_attribute = ...  # type: bool
    extension_type = ...  # type: Any
    target_collection = ...  # type: Any
    value_attr = ...  # type: Any
    creator = ...  # type: Any
    getset_factory = ...  # type: Any
    proxy_factory = ...  # type: Any
    proxy_bulk_set = ...  # type: Any
    owning_class = ...  # type: Any
    key = ...  # type: Any
    collection_class = ...  # type: Any
    info = ...  # type: Any
    def __init__(self, target_collection, attr, creator: Optional[Any] = ..., getset_factory: Optional[Any] = ..., proxy_factory: Optional[Any] = ..., proxy_bulk_set: Optional[Any] = ..., info: Optional[Any] = ...) -> None: ...
    @property
    def remote_attr(self): ...
    @property
    def local_attr(self): ...
    @property
    def attr(self): ...
    def target_class(self): ...
    def scalar(self): ...
    def __get__(self, obj, class_): ...
    def __set__(self, obj, values): ...
    def __delete__(self, obj): ...
    def any(self, criterion: Optional[Any] = ..., **kwargs): ...
    def has(self, criterion: Optional[Any] = ..., **kwargs): ...
    def contains(self, obj): ...
    def __eq__(self, obj): ...
    def __ne__(self, obj): ...

class _lazy_collection:
    ref = ...  # type: Any
    target = ...  # type: Any
    def __init__(self, obj, target) -> None: ...
    def __call__(self): ...

class _AssociationCollection:
    lazy_collection = ...  # type: Any
    creator = ...  # type: Any
    getter = ...  # type: Any
    setter = ...  # type: Any
    parent = ...  # type: Any
    def __init__(self, lazy_collection, creator, getter, setter, parent) -> None: ...
    col = ...  # type: Any
    def __len__(self): ...
    def __bool__(self): ...
    __nonzero__ = ...  # type: Any

class _AssociationList(_AssociationCollection):
    def __getitem__(self, index): ...
    def __setitem__(self, index, value): ...
    def __delitem__(self, index): ...
    def __contains__(self, value): ...
    def __getslice__(self, start, end): ...
    def __setslice__(self, start, end, values): ...
    def __delslice__(self, start, end): ...
    def __iter__(self): ...
    def append(self, value): ...
    def count(self, value): ...
    def extend(self, values): ...
    def insert(self, index, value): ...
    def pop(self, index: int = ...): ...
    def remove(self, value): ...
    def reverse(self): ...
    def sort(self): ...
    def clear(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __cmp__(self, other): ...
    def __add__(self, iterable): ...
    def __radd__(self, iterable): ...
    def __mul__(self, n): ...
    __rmul__ = ...  # type: Any
    def __iadd__(self, iterable): ...
    def __imul__(self, n): ...
    def copy(self): ...
    def __hash__(self): ...

class _AssociationDict(_AssociationCollection):
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    def __contains__(self, key): ...
    def has_key(self, key): ...
    def __iter__(self): ...
    def clear(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __cmp__(self, other): ...
    def get(self, key, default: Optional[Any] = ...): ...
    def setdefault(self, key, default: Optional[Any] = ...): ...
    def keys(self): ...
    def iteritems(self): ...
    def itervalues(self): ...
    def iterkeys(self): ...
    def values(self): ...
    def items(self): ...
    def items(self): ...
    def values(self): ...
    def pop(self, key, default: Any = ...): ...
    def popitem(self): ...
    def update(self, *a, **kw): ...
    def copy(self): ...
    def __hash__(self): ...

class _AssociationSet(_AssociationCollection):
    def __len__(self): ...
    def __bool__(self): ...
    __nonzero__ = ...  # type: Any
    def __contains__(self, value): ...
    def __iter__(self): ...
    def add(self, value): ...
    def discard(self, value): ...
    def remove(self, value): ...
    def pop(self): ...
    def update(self, other): ...
    def __ior__(self, other): ...
    def union(self, other): ...
    __or__ = ...  # type: Any
    def difference(self, other): ...
    __sub__ = ...  # type: Any
    def difference_update(self, other): ...
    def __isub__(self, other): ...
    def intersection(self, other): ...
    __and__ = ...  # type: Any
    def intersection_update(self, other): ...
    def __iand__(self, other): ...
    def symmetric_difference(self, other): ...
    __xor__ = ...  # type: Any
    def symmetric_difference_update(self, other): ...
    def __ixor__(self, other): ...
    def issubset(self, other): ...
    def issuperset(self, other): ...
    def clear(self): ...
    def copy(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __hash__(self): ...
