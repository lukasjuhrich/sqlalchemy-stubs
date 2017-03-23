# Stubs for sqlalchemy.orm.descriptor_props (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .interfaces import MapperProperty as MapperProperty, PropComparator as PropComparator
from .util import _none_set as _none_set
from .. import exc as sa_exc
from ..sql import expression as expression
import query

class DescriptorProperty(MapperProperty):
    doc = ...  # type: Any
    key = ...  # type: Any
    descriptor = ...  # type: Any
    def instrument_class(self, mapper): ...

class CompositeProperty(DescriptorProperty):
    attrs = ...  # type: Any
    composite_class = ...  # type: Any
    active_history = ...  # type: Any
    deferred = ...  # type: Any
    group = ...  # type: Any
    comparator_factory = ...  # type: Any
    info = ...  # type: Any
    def __init__(self, class_, *attrs, **kwargs) -> None: ...
    def instrument_class(self, mapper): ...
    def do_init(self): ...
    def props(self): ...
    @property
    def columns(self): ...
    def get_history(self, state, dict_, passive: Any = ...): ...
    class CompositeBundle(query.Bundle):
        property = ...  # type: Any
        def __init__(self, property, expr) -> None: ...
        def create_row_processor(self, query, procs, labels): ...
    class Comparator(PropComparator):
        __hash__ = ...  # type: Any
        @property
        def clauses(self): ...
        def __clause_element__(self): ...
        def __eq__(self, other): ...
        def __ne__(self, other): ...

class ConcreteInheritedProperty(DescriptorProperty):
    descriptor = ...  # type: Any
    def __init__(self) -> None: ...

class SynonymProperty(DescriptorProperty):
    name = ...  # type: Any
    map_column = ...  # type: Any
    descriptor = ...  # type: Any
    comparator_factory = ...  # type: Any
    doc = ...  # type: Any
    info = ...  # type: Any
    def __init__(self, name, map_column: Optional[Any] = ..., descriptor: Optional[Any] = ..., comparator_factory: Optional[Any] = ..., doc: Optional[Any] = ..., info: Optional[Any] = ...) -> None: ...
    parent = ...  # type: Any
    def set_parent(self, parent, init): ...

class ComparableProperty(DescriptorProperty):
    descriptor = ...  # type: Any
    comparator_factory = ...  # type: Any
    doc = ...  # type: Any
    info = ...  # type: Any
    def __init__(self, comparator_factory, descriptor: Optional[Any] = ..., doc: Optional[Any] = ..., info: Optional[Any] = ...) -> None: ...
