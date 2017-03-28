# Stubs for sqlalchemy.sql.elements (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from . import operators
from sqlalchemy import util
from .visitors import Visitable as Visitable, cloned_traverse as cloned_traverse, traverse as traverse
from .annotation import Annotated as Annotated
from .base import Executable as Executable, PARSE_AUTOCOMMIT as PARSE_AUTOCOMMIT, Immutable as Immutable, NO_ARG as NO_ARG

def collate(expression, collation): ...
def between(expr, lower_bound, upper_bound, symmetric: bool = ...): ...
def literal(value, type_: Optional[Any] = ...): ...
def outparam(key, type_: Optional[Any] = ...): ...
def not_(clause): ...

class ClauseElement(Visitable):
    __visit_name__ = ...  # type: str
    supports_execution = ...  # type: bool
    bind = ...  # type: Any
    is_selectable = ...  # type: bool
    is_clause_element = ...  # type: bool
    description = ...  # type: Any
    def unique_params(self, *optionaldict, **kwargs): ...
    def params(self, *optionaldict, **kwargs): ...
    def compare(self, other, **kw): ...
    def get_children(self, **kwargs): ...
    def self_group(self, against: Optional[Any] = ...): ...
    def compile(self, bind: Optional[Any] = ..., dialect: Optional[Any] = ..., **kw): ...
    def __and__(self, other): ...
    def __or__(self, other): ...
    def __invert__(self): ...
    def __bool__(self): ...
    __nonzero__ = ...  # type: Any

class ColumnElement(operators.ColumnOperators, ClauseElement):
    __visit_name__ = ...  # type: str
    primary_key = ...  # type: Any
    foreign_keys = ...  # type: Any
    key = ...  # type: Any
    def self_group(self, against: Optional[Any] = ...): ...
    @property
    def type(self): ...
    def comparator(self): ...
    def __getattr__(self, key): ...
    def operate(self, op, *other, **kwargs): ...
    def reverse_operate(self, op, other, **kwargs): ...
    @property
    def expression(self): ...
    def base_columns(self): ...
    def proxy_set(self): ...
    def shares_lineage(self, othercolumn): ...
    def compare(self, other, **kw): ...
    def cast(self, type_): ...
    def label(self, name): ...
    def anon_label(self): ...

class BindParameter(ColumnElement):
    __visit_name__ = ...  # type: str
    key = ...  # type: Any
    unique = ...  # type: Any
    value = ...  # type: Any
    callable = ...  # type: Any
    isoutparam = ...  # type: Any
    required = ...  # type: Any
    type = ...  # type: Any
    def __init__(self, key, value: Any = ..., type_: Optional[Any] = ..., unique: bool = ..., required: Any = ..., quote: Optional[Any] = ..., callable_: Optional[Any] = ..., isoutparam: bool = ..., _compared_to_operator: Optional[Any] = ..., _compared_to_type: Optional[Any] = ...) -> None: ...
    @property
    def effective_value(self): ...
    def compare(self, other, **kw): ...

class TypeClause(ClauseElement):
    __visit_name__ = ...  # type: str
    type = ...  # type: Any
    def __init__(self, type) -> None: ...

class TextClause(Executable, ClauseElement):
    __visit_name__ = ...  # type: str
    @property
    def selectable(self): ...
    key = ...  # type: Any
    text = ...  # type: Any
    def __init__(self, text, bind: Optional[Any] = ...) -> None: ...
    def bindparams(self, *binds, **names_to_values): ...
    def columns(self, *cols, **types): ...
    @property
    def type(self): ...
    @property
    def comparator(self): ...
    def self_group(self, against: Optional[Any] = ...): ...
    def get_children(self, **kwargs): ...
    def compare(self, other): ...

class Null(ColumnElement):
    __visit_name__ = ...  # type: str
    @property
    def type(self): ...
    def compare(self, other): ...

class False_(ColumnElement):
    __visit_name__ = ...  # type: str
    @property
    def type(self): ...
    def compare(self, other): ...

class True_(ColumnElement):
    __visit_name__ = ...  # type: str
    @property
    def type(self): ...
    def compare(self, other): ...

class ClauseList(ClauseElement):
    __visit_name__ = ...  # type: str
    operator = ...  # type: Any
    group = ...  # type: Any
    group_contents = ...  # type: Any
    clauses = ...  # type: Any
    def __init__(self, *clauses, **kwargs) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    def append(self, clause): ...
    def get_children(self, **kwargs): ...
    def self_group(self, against: Optional[Any] = ...): ...
    def compare(self, other, **kw): ...

class BooleanClauseList(ClauseList, ColumnElement):
    __visit_name__ = ...  # type: str
    def __init__(self, *arg, **kw) -> None: ...
    @classmethod
    def and_(cls, *clauses): ...
    @classmethod
    def or_(cls, *clauses): ...
    def self_group(self, against: Optional[Any] = ...): ...

and_ = ...  # type: Any
or_ = ...  # type: Any

class Tuple(ClauseList, ColumnElement):
    type = ...  # type: Any
    def __init__(self, *clauses, **kw) -> None: ...

class Case(ColumnElement):
    __visit_name__ = ...  # type: str
    value = ...  # type: Any
    type = ...  # type: Any
    whens = ...  # type: Any
    else_ = ...  # type: Any
    def __init__(self, whens, value: Optional[Any] = ..., else_: Optional[Any] = ...) -> None: ...
    def get_children(self, **kwargs): ...

def literal_column(text, type_: Optional[Any] = ...): ...

class Cast(ColumnElement):
    __visit_name__ = ...  # type: str
    type = ...  # type: Any
    clause = ...  # type: Any
    typeclause = ...  # type: Any
    def __init__(self, expression, type_) -> None: ...
    def get_children(self, **kwargs): ...

class TypeCoerce(ColumnElement):
    __visit_name__ = ...  # type: str
    type = ...  # type: Any
    clause = ...  # type: Any
    def __init__(self, expression, type_) -> None: ...
    def get_children(self, **kwargs): ...
    @property
    def typed_expression(self): ...

class Extract(ColumnElement):
    __visit_name__ = ...  # type: str
    type = ...  # type: Any
    field = ...  # type: Any
    expr = ...  # type: Any
    def __init__(self, field, expr, **kwargs) -> None: ...
    def get_children(self, **kwargs): ...

class _label_reference(ColumnElement):
    __visit_name__ = ...  # type: str
    element = ...  # type: Any
    def __init__(self, element) -> None: ...

class _textual_label_reference(ColumnElement):
    __visit_name__ = ...  # type: str
    element = ...  # type: Any
    def __init__(self, element) -> None: ...

class UnaryExpression(ColumnElement):
    __visit_name__ = ...  # type: str
    operator = ...  # type: Any
    modifier = ...  # type: Any
    element = ...  # type: Any
    type = ...  # type: Any
    negate = ...  # type: Any
    wraps_column_expression = ...  # type: Any
    def __init__(self, element, operator: Optional[Any] = ..., modifier: Optional[Any] = ..., type_: Optional[Any] = ..., negate: Optional[Any] = ..., wraps_column_expression: bool = ...) -> None: ...
    def get_children(self, **kwargs): ...
    def compare(self, other, **kw): ...
    def self_group(self, against: Optional[Any] = ...): ...

class CollectionAggregate(UnaryExpression):
    def operate(self, op, *other, **kwargs): ...
    def reverse_operate(self, op, other, **kwargs): ...

class AsBoolean(UnaryExpression):
    element = ...  # type: Any
    type = ...  # type: Any
    operator = ...  # type: Any
    negate = ...  # type: Any
    modifier = ...  # type: Any
    wraps_column_expression = ...  # type: bool
    def __init__(self, element, operator, negate) -> None: ...
    def self_group(self, against: Optional[Any] = ...): ...

class BinaryExpression(ColumnElement):
    __visit_name__ = ...  # type: str
    left = ...  # type: Any
    right = ...  # type: Any
    operator = ...  # type: Any
    type = ...  # type: Any
    negate = ...  # type: Any
    modifiers = ...  # type: Any
    def __init__(self, left, right, operator, type_: Optional[Any] = ..., negate: Optional[Any] = ..., modifiers: Optional[Any] = ...) -> None: ...
    def __bool__(self): ...
    __nonzero__ = ...  # type: Any
    @property
    def is_comparison(self): ...
    def get_children(self, **kwargs): ...
    def compare(self, other, **kw): ...
    def self_group(self, against: Optional[Any] = ...): ...

class Slice(ColumnElement):
    __visit_name__ = ...  # type: str
    start = ...  # type: Any
    stop = ...  # type: Any
    step = ...  # type: Any
    type = ...  # type: Any
    def __init__(self, start, stop, step) -> None: ...
    def self_group(self, against: Optional[Any] = ...): ...

class IndexExpression(BinaryExpression): ...

class Grouping(ColumnElement):
    __visit_name__ = ...  # type: str
    element = ...  # type: Any
    type = ...  # type: Any
    def __init__(self, element) -> None: ...
    def self_group(self, against: Optional[Any] = ...): ...
    def get_children(self, **kwargs): ...
    def __getattr__(self, attr): ...
    def compare(self, other, **kw): ...

RANGE_UNBOUNDED = ...  # type: Any
RANGE_CURRENT = ...  # type: Any

class Over(ColumnElement):
    __visit_name__ = ...  # type: str
    order_by = ...  # type: Any
    partition_by = ...  # type: Any
    element = ...  # type: Any
    range_ = ...  # type: Any
    rows = ...  # type: Any
    def __init__(self, element, partition_by: Optional[Any] = ..., order_by: Optional[Any] = ..., range_: Optional[Any] = ..., rows: Optional[Any] = ...) -> None: ...
    @property
    def func(self): ...
    @property
    def type(self): ...
    def get_children(self, **kwargs): ...

class WithinGroup(ColumnElement):
    __visit_name__ = ...  # type: str
    order_by = ...  # type: Any
    element = ...  # type: Any
    def __init__(self, element, *order_by) -> None: ...
    def over(self, partition_by: Optional[Any] = ..., order_by: Optional[Any] = ...): ...
    @property
    def type(self): ...
    def get_children(self, **kwargs): ...

class FunctionFilter(ColumnElement):
    __visit_name__ = ...  # type: str
    criterion = ...  # type: Any
    func = ...  # type: Any
    def __init__(self, func, *criterion) -> None: ...
    def filter(self, *criterion): ...
    def over(self, partition_by: Optional[Any] = ..., order_by: Optional[Any] = ...): ...
    @property
    def type(self): ...
    def get_children(self, **kwargs): ...

class Label(ColumnElement):
    __visit_name__ = ...  # type: str
    name = ...  # type: Any
    key = ...  # type: Any
    def __init__(self, name, element, type_: Optional[Any] = ...) -> None: ...
    def __reduce__(self): ...
    @property
    def type(self): ...
    @property
    def element(self): ...
    def self_group(self, against: Optional[Any] = ...): ...
    @property
    def primary_key(self): ...
    @property
    def foreign_keys(self): ...
    def get_children(self, **kwargs): ...

class ColumnClause(Immutable, ColumnElement):
    __visit_name__ = ...  # type: str
    onupdate = ...  # type: Any
    default = ...  # type: Any
    server_default = ...  # type: Any
    server_onupdate = ...  # type: Any
    key = ...  # type: Any
    table = ...  # type: Any
    type = ...  # type: Any
    is_literal = ...  # type: Any
    def __init__(self, text, type_: Optional[Any] = ..., is_literal: bool = ..., _selectable: Optional[Any] = ...) -> None: ...
    @property
    def description(self): ...

class _IdentifiedClause(Executable, ClauseElement):
    __visit_name__ = ...  # type: str
    ident = ...  # type: Any
    def __init__(self, ident) -> None: ...

class SavepointClause(_IdentifiedClause):
    __visit_name__ = ...  # type: str

class RollbackToSavepointClause(_IdentifiedClause):
    __visit_name__ = ...  # type: str

class ReleaseSavepointClause(_IdentifiedClause):
    __visit_name__ = ...  # type: str

class quoted_name(util.MemoizedSlots, util.text_type):
    quote = ...  # type: Any
    def __new__(cls, value, quote): ...
    def __reduce__(self): ...

class _truncated_label(quoted_name):
    def __new__(cls, value, quote: Optional[Any] = ...): ...
    def __reduce__(self): ...
    def apply_map(self, map_): ...

class conv(_truncated_label): ...

class _defer_name(_truncated_label):
    def __new__(cls, value): ...
    def __reduce__(self): ...

class _defer_none_name(_defer_name): ...

class _anonymous_label(_truncated_label):
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def apply_map(self, map_): ...

class AnnotatedColumnElement(Annotated):
    def __init__(self, element, values) -> None: ...
    @property
    def name(self): ...
    @property
    def table(self): ...
    @property
    def key(self): ...
    @property
    def info(self): ...
    @property
    def anon_label(self): ...