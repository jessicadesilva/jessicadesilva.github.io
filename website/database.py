# -*- coding: utf-8 -*-
"""Database module, including the SQLAlchemy database object and DB-related utilities."""
from sqlalchemy.orm import Mapped, mapped_column

from website.extensions import database


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit: bool = True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            return self.save()
        return self

    def save(self, commit: bool = True):
        database.session.add(self)
        if commit:
            database.session.commit()
        return self

    def delete(self, commit: bool = True) -> None:
        database.session.delete(self)
        if commit:
            database.session.commit()
        return


class Model(CRUDMixin, database.Model):
    """Base `Model` class that includes CRUD convenience methods."""

    __abstract__ = True


class PkModel(Model):
    """Base `Model` class that includes CRUD convenience methods and a primary key."""

    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @classmethod
    def get_by_id(cls, record_id):
        if any(
            (
                isinstance(record_id, str) and record_id.isdigit(),
                isinstance(record_id, (int, float)),
            )
        ):
            return database.session.get(cls, record_id)
        return None
