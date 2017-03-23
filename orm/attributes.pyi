# Stubs for sqlalchemy.orm.attributes (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import interfaces
from . import exc as orm_exc
from .base import instance_state as instance_state, instance_dict as instance_dict, manager_of_class as manager_of_class
from .base import PASSIVE_NO_RESULT as PASSIVE_NO_RESULT, ATTR_WAS_SET as ATTR_WAS_SET, ATTR_EMPTY as ATTR_EMPTY, NO_VALUE as NO_VALUE, NEVER_SET as NEVER_SET, NO_CHANGE as NO_CHANGE, CALLABLES_OK as CALLABLES_OK, SQL_OK as SQL_OK, RELATED_OBJECT_OK as RELATED_OBJECT_OK, INIT_OK as INIT_OK, NON_PERSISTENT_OK as NON_PERSISTENT_OK, LOAD_AGAINST_COMMITTED as LOAD_AGAINST_COMMITTED, PASSIVE_OFF as PASSIVE_OFF, PASSIVE_RETURN_NEVER_SET as PASSIVE_RETURN_NEVER_SET, PASSIVE_NO_INITIALIZE as PASSIVE_NO_INITIALIZE, PASSIVE_NO_FETCH as PASSIVE_NO_FETCH, PASSIVE_NO_FETCH_RELATED as PASSIVE_NO_FETCH_RELATED, PASSIVE_ONLY_PERSISTENT as PASSIVE_ONLY_PERSISTENT, NO_AUTOFLUSH as NO_AUTOFLUSH
from .base import state_str as state_str, instance_str as instance_str
from collections import namedtuple

class QueryableAttribute(interfaces._MappedAttribute, interfaces.InspectionAttr, interfaces.PropComparator):
    is_attribute = ...  # type: bool
    class_ = ...  # type: Any
    key = ...  # type: Any
    impl = ...  # type: Any
    comparator = ...  # type: Any
    def __init__(self, class_, key, impl: Optional[Any] = ..., comparator: Optional[Any] = ..., parententity: Optional[Any] = ..., of_type: Optional[Any] = ...) -> None: ...
    def get_history(self, instance, passive: Any = ...): ...
    def __selectable__(self): ...
    def info(self): ...
    def parent(self): ...
    @property
    def expression(self): ...
    def __clause_element__(self): ...
    def adapt_to_entity(self, adapt_to_entity): ...
    def of_type(self, cls): ...
    def label(self, name): ...
    def operate(self, op, *other, **kwargs): ...
    def reverse_operate(self, op, other, **kwargs): ...
    def hasparent(self, state, optimistic: bool = ...): ...
    def __getattr__(self, key): ...
    def property(self): ...

class InstrumentedAttribute(QueryableAttribute):
    def __set__(self, instance, value): ...
    def __delete__(self, instance): ...
    def __get__(self, instance, owner): ...

def create_proxied_attribute(descriptor): ...

OP_REMOVE = ...  # type: Any
OP_APPEND = ...  # type: Any
OP_REPLACE = ...  # type: Any

class Event:
    impl = ...  # type: Any
    op = ...  # type: Any
    parent_token = ...  # type: Any
    def __init__(self, attribute_impl, op) -> None: ...
    def __eq__(self, other): ...
    @property
    def key(self): ...
    def hasparent(self, state): ...

class AttributeImpl:
    class_ = ...  # type: Any
    key = ...  # type: Any
    callable_ = ...  # type: Any
    dispatch = ...  # type: Any
    trackparent = ...  # type: Any
    parent_token = ...  # type: Any
    send_modified_events = ...  # type: Any
    is_equal = ...  # type: Any
    expire_missing = ...  # type: Any
    def __init__(self, class_, key, callable_, dispatch, trackparent: bool = ..., extension: Optional[Any] = ..., compare_function: Optional[Any] = ..., active_history: bool = ..., parent_token: Optional[Any] = ..., expire_missing: bool = ..., send_modified_events: bool = ..., **kwargs) -> None: ...
    active_history = ...  # type: Any
    def hasparent(self, state, optimistic: bool = ...): ...
    def sethasparent(self, state, parent_state, value): ...
    def get_history(self, state, dict_, passive: Any = ...): ...
    def get_all_pending(self, state, dict_, passive: Any = ...): ...
    def initialize(self, state, dict_): ...
    def get(self, state, dict_, passive: Any = ...): ...
    def append(self, state, dict_, value, initiator, passive: Any = ...): ...
    def remove(self, state, dict_, value, initiator, passive: Any = ...): ...
    def pop(self, state, dict_, value, initiator, passive: Any = ...): ...
    def set(self, state, dict_, value, initiator, passive: Any = ..., check_old: Optional[Any] = ..., pop: bool = ...): ...
    def get_committed_value(self, state, dict_, passive: Any = ...): ...
    def set_committed_value(self, state, dict_, value): ...

class ScalarAttributeImpl(AttributeImpl):
    accepts_scalar_loader = ...  # type: bool
    uses_objects = ...  # type: bool
    supports_population = ...  # type: bool
    collection = ...  # type: bool
    def __init__(self, *arg, **kw) -> None: ...
    def delete(self, state, dict_): ...
    def get_history(self, state, dict_, passive: Any = ...): ...
    def set(self, state, dict_, value, initiator, passive: Any = ..., check_old: Optional[Any] = ..., pop: bool = ...): ...
    def fire_replace_event(self, state, dict_, value, previous, initiator): ...
    def fire_remove_event(self, state, dict_, value, initiator): ...
    @property
    def type(self): ...

class ScalarObjectAttributeImpl(ScalarAttributeImpl):
    accepts_scalar_loader = ...  # type: bool
    uses_objects = ...  # type: bool
    supports_population = ...  # type: bool
    collection = ...  # type: bool
    def delete(self, state, dict_): ...
    def get_history(self, state, dict_, passive: Any = ...): ...
    def get_all_pending(self, state, dict_, passive: Any = ...): ...
    def set(self, state, dict_, value, initiator, passive: Any = ..., check_old: Optional[Any] = ..., pop: bool = ...): ...
    def fire_remove_event(self, state, dict_, value, initiator): ...
    def fire_replace_event(self, state, dict_, value, previous, initiator): ...

class CollectionAttributeImpl(AttributeImpl):
    accepts_scalar_loader = ...  # type: bool
    uses_objects = ...  # type: bool
    supports_population = ...  # type: bool
    collection = ...  # type: bool
    copy = ...  # type: Any
    collection_factory = ...  # type: Any
    def __init__(self, class_, key, callable_, dispatch, typecallable: Optional[Any] = ..., trackparent: bool = ..., extension: Optional[Any] = ..., copy_function: Optional[Any] = ..., compare_function: Optional[Any] = ..., **kwargs) -> None: ...
    def get_history(self, state, dict_, passive: Any = ...): ...
    def get_all_pending(self, state, dict_, passive: Any = ...): ...
    def fire_append_event(self, state, dict_, value, initiator): ...
    def fire_pre_remove_event(self, state, dict_, initiator): ...
    def fire_remove_event(self, state, dict_, value, initiator): ...
    def delete(self, state, dict_): ...
    def initialize(self, state, dict_): ...
    def append(self, state, dict_, value, initiator, passive: Any = ...): ...
    def remove(self, state, dict_, value, initiator, passive: Any = ...): ...
    def pop(self, state, dict_, value, initiator, passive: Any = ...): ...
    def set(self, state, dict_, value, initiator: Optional[Any] = ..., passive: Any = ..., pop: bool = ..., _adapt: bool = ...): ...
    def set_committed_value(self, state, dict_, value): ...
    def get_collection(self, state, dict_, user_data: Optional[Any] = ..., passive: Any = ...): ...

def backref_listeners(attribute, key, uselist): ...

History = namedtuple('History', ['added', 'unchanged', 'deleted'])

class History(History):
    def __bool__(self): ...
    __nonzero__ = ...  # type: Any
    def empty(self): ...
    def sum(self): ...
    def non_deleted(self): ...
    def non_added(self): ...
    def has_changes(self): ...
    def as_state(self): ...
    @classmethod
    def from_scalar_attribute(cls, attribute, state, current): ...
    @classmethod
    def from_object_attribute(cls, attribute, state, current): ...
    @classmethod
    def from_collection(cls, attribute, state, current): ...

HISTORY_BLANK = ...  # type: Any

def get_history(obj, key, passive: Any = ...): ...
def get_state_history(state, key, passive: Any = ...): ...
def has_parent(cls, obj, key, optimistic: bool = ...): ...
def register_attribute(class_, key, **kw): ...
def register_attribute_impl(class_, key, uselist: bool = ..., callable_: Optional[Any] = ..., useobject: bool = ..., impl_class: Optional[Any] = ..., backref: Optional[Any] = ..., **kw): ...
def register_descriptor(class_, key, comparator: Optional[Any] = ..., parententity: Optional[Any] = ..., doc: Optional[Any] = ...): ...
def unregister_attribute(class_, key): ...
def init_collection(obj, key): ...
def init_state_collection(state, dict_, key): ...
def set_committed_value(instance, key, value): ...
def set_attribute(instance, key, value): ...
def get_attribute(instance, key): ...
def del_attribute(instance, key): ...
def flag_modified(instance, key): ...
