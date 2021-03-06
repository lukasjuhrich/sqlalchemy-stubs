# Stubs for sqlalchemy.sql.ddl (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .elements import ClauseElement as ClauseElement
from .base import Executable as Executable, SchemaVisitor as SchemaVisitor
from ..util import topological as topological

class _DDLCompiles(ClauseElement): ...

class DDLElement(Executable, _DDLCompiles):
    target = ...  # type: Any
    on = ...  # type: Any
    dialect = ...  # type: Any
    callable_ = ...  # type: Any
    def execute(self, *multiparams, **params): ...
    def execute_at(self, event_name, target): ...
    def against(self, target): ...
    state = ...  # type: Any
    def execute_if(self, dialect: Optional[Any] = ..., callable_: Optional[Any] = ..., state: Optional[Any] = ...): ...
    def __call__(self, target, bind, **kw): ...
    def bind(self): ...

class DDL(DDLElement):
    __visit_name__ = ...  # type: str
    statement = ...  # type: Any
    context = ...  # type: Any
    on = ...  # type: Any
    def __init__(self, statement, on: Optional[Any] = ..., context: Optional[Any] = ..., bind: Optional[Any] = ...) -> None: ...

class _CreateDropBase(DDLElement):
    element = ...  # type: Any
    on = ...  # type: Any
    bind = ...  # type: Any
    def __init__(self, element, on: Optional[Any] = ..., bind: Optional[Any] = ...) -> None: ...

class CreateSchema(_CreateDropBase):
    __visit_name__ = ...  # type: str
    quote = ...  # type: Any
    def __init__(self, name, quote: Optional[Any] = ..., **kw) -> None: ...

class DropSchema(_CreateDropBase):
    __visit_name__ = ...  # type: str
    quote = ...  # type: Any
    cascade = ...  # type: Any
    def __init__(self, name, quote: Optional[Any] = ..., cascade: bool = ..., **kw) -> None: ...

class CreateTable(_CreateDropBase):
    __visit_name__ = ...  # type: str
    columns = ...  # type: Any
    include_foreign_key_constraints = ...  # type: Any
    def __init__(self, element, on: Optional[Any] = ..., bind: Optional[Any] = ..., include_foreign_key_constraints: Optional[Any] = ...) -> None: ...

class _DropView(_CreateDropBase):
    __visit_name__ = ...  # type: str

class CreateColumn(_DDLCompiles):
    __visit_name__ = ...  # type: str
    element = ...  # type: Any
    def __init__(self, element) -> None: ...

class DropTable(_CreateDropBase):
    __visit_name__ = ...  # type: str

class CreateSequence(_CreateDropBase):
    __visit_name__ = ...  # type: str

class DropSequence(_CreateDropBase):
    __visit_name__ = ...  # type: str

class CreateIndex(_CreateDropBase):
    __visit_name__ = ...  # type: str

class DropIndex(_CreateDropBase):
    __visit_name__ = ...  # type: str

class AddConstraint(_CreateDropBase):
    __visit_name__ = ...  # type: str
    def __init__(self, element, *args, **kw) -> None: ...

class DropConstraint(_CreateDropBase):
    __visit_name__ = ...  # type: str
    cascade = ...  # type: Any
    def __init__(self, element, cascade: bool = ..., **kw) -> None: ...

class DDLBase(SchemaVisitor):
    connection = ...  # type: Any
    def __init__(self, connection) -> None: ...

class SchemaGenerator(DDLBase):
    checkfirst = ...  # type: Any
    tables = ...  # type: Any
    preparer = ...  # type: Any
    dialect = ...  # type: Any
    memo = ...  # type: Any
    def __init__(self, dialect, connection, checkfirst: bool = ..., tables: Optional[Any] = ..., **kwargs) -> None: ...
    def visit_metadata(self, metadata): ...
    def visit_table(self, table, create_ok: bool = ..., include_foreign_key_constraints: Optional[Any] = ..., _is_metadata_operation: bool = ...): ...
    def visit_foreign_key_constraint(self, constraint): ...
    def visit_sequence(self, sequence, create_ok: bool = ...): ...
    def visit_index(self, index): ...

class SchemaDropper(DDLBase):
    checkfirst = ...  # type: Any
    tables = ...  # type: Any
    preparer = ...  # type: Any
    dialect = ...  # type: Any
    memo = ...  # type: Any
    def __init__(self, dialect, connection, checkfirst: bool = ..., tables: Optional[Any] = ..., **kwargs) -> None: ...
    def visit_metadata(self, metadata): ...
    def visit_index(self, index): ...
    def visit_table(self, table, drop_ok: bool = ..., _is_metadata_operation: bool = ...): ...
    def visit_foreign_key_constraint(self, constraint): ...
    def visit_sequence(self, sequence, drop_ok: bool = ...): ...

def sort_tables(tables, skip_fn: Optional[Any] = ..., extra_dependencies: Optional[Any] = ...): ...
def sort_tables_and_constraints(tables, filter_fn: Optional[Any] = ..., extra_dependencies: Optional[Any] = ...): ...
