# Stubs for sqlalchemy.orm.deprecated_interfaces (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .interfaces import EXT_CONTINUE as EXT_CONTINUE

class MapperExtension(object):
    def instrument_class(self, mapper, class_): ...
    def init_instance(self, mapper, class_, oldinit, instance, args, kwargs): ...
    def init_failed(self, mapper, class_, oldinit, instance, args, kwargs): ...
    def reconstruct_instance(self, mapper, instance): ...
    def before_insert(self, mapper, connection, instance): ...
    def after_insert(self, mapper, connection, instance): ...
    def before_update(self, mapper, connection, instance): ...
    def after_update(self, mapper, connection, instance): ...
    def before_delete(self, mapper, connection, instance): ...
    def after_delete(self, mapper, connection, instance): ...

class SessionExtension(object):
    def before_commit(self, session): ...
    def after_commit(self, session): ...
    def after_rollback(self, session): ...
    def before_flush(self, session, flush_context, instances): ...
    def after_flush(self, session, flush_context): ...
    def after_flush_postexec(self, session, flush_context): ...
    def after_begin(self, session, transaction, connection): ...
    def after_attach(self, session, instance): ...
    def after_bulk_update(self, session, query, query_context, result): ...
    def after_bulk_delete(self, session, query, query_context, result): ...

class AttributeExtension(object):
    active_history = ...  # type: bool
    def append(self, state, value, initiator): ...
    def remove(self, state, value, initiator): ...
    def set(self, state, value, oldvalue, initiator): ...