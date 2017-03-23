# Stubs for sqlalchemy.testing.assertions (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from . import util as testutil
from sqlalchemy import types as sqltypes, exc as sa_exc
from .exclusions import db_spec as db_spec, _is_excluded as _is_excluded
from .util import fail as fail

def expect_warnings(*messages, **kw): ...
def expect_warnings_on(db, *messages, **kw): ...
def emits_warning(*messages): ...
def expect_deprecated(*messages, **kw): ...
def emits_warning_on(db, *messages): ...
def uses_deprecated(*messages): ...
def global_cleanup_assertions(): ...
def eq_regex(a, b, msg: Optional[Any] = ...): ...
def eq_(a, b, msg: Optional[Any] = ...): ...
def ne_(a, b, msg: Optional[Any] = ...): ...
def le_(a, b, msg: Optional[Any] = ...): ...
def is_true(a, msg: Optional[Any] = ...): ...
def is_false(a, msg: Optional[Any] = ...): ...
def is_(a, b, msg: Optional[Any] = ...): ...
def is_not_(a, b, msg: Optional[Any] = ...): ...
def in_(a, b, msg: Optional[Any] = ...): ...
def not_in_(a, b, msg: Optional[Any] = ...): ...
def startswith_(a, fragment, msg: Optional[Any] = ...): ...
def eq_ignore_whitespace(a, b, msg: Optional[Any] = ...): ...
def assert_raises(except_cls, callable_, *args, **kw): ...
def assert_raises_message(except_cls, msg, callable_, *args, **kwargs): ...

class AssertsCompiledSQL:
    def assert_compile(self, clause, result, params: Optional[Any] = ..., checkparams: Optional[Any] = ..., dialect: Optional[Any] = ..., checkpositional: Optional[Any] = ..., check_prefetch: Optional[Any] = ..., use_default_dialect: bool = ..., allow_dialect_select: bool = ..., literal_binds: bool = ..., schema_translate_map: Optional[Any] = ...): ...

class ComparesTables:
    def assert_tables_equal(self, table, reflected_table, strict_types: bool = ...): ...
    def assert_types_base(self, c1, c2): ...

class AssertsExecutionResults:
    def assert_result(self, result, class_, *objects): ...
    def assert_list(self, result, class_, list): ...
    def assert_row(self, class_, rowobj, desc): ...
    def assert_unordered_result(self, result, cls, *expected): ...
    def sql_execution_asserter(self, db: Optional[Any] = ...): ...
    def assert_sql_execution(self, db, callable_, *rules): ...
    def assert_sql(self, db, callable_, rules): ...
    def assert_sql_count(self, db, callable_, count): ...
    def assert_execution(self, *rules): ...
    def assert_statement_count(self, count): ...
