# -*- coding: utf-8 -*-
"""Research models."""
from __future__ import annotations
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from website.extensions import database
from website.database import PkModel


class Project(PkModel):
    __tablename__ = "projects"

    type_id: Mapped[int] = mapped_column(ForeignKey("project_type.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("undergrad_status.id"))
    image: Mapped[str] = mapped_column()
    advisors: Mapped[Optional[str]] = mapped_column()
    students: Mapped[str] = mapped_column()
    majors: Mapped[Optional[str]] = mapped_column()
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    link: Mapped[Optional[str]] = mapped_column()

    type_rel: Mapped[ProjectType] = relationship()
    status_rel: Mapped[UndergradStatus] = relationship()

    def __repr__(self):
        return f"<Project: {self.id} - {self.title}>"


class ProjectType(PkModel):
    __tablename__ = "project_type"

    type: Mapped[str] = mapped_column(unique=True)

    @classmethod
    def return_type_id(self, type: str) -> int:
        return database.session.execute(
            database.select(ProjectType.id).where(ProjectType.type == type)
        ).scalar_one()

    def __repr__(self):
        return f"<ProjectType: {self.id} - {self.type}>"


class UndergradStatus(PkModel):
    __tablename__ = "undergrad_status"

    status: Mapped[str] = mapped_column(unique=True)

    @classmethod
    def return_status_id(self, status: str) -> int:
        return database.session.execute(
            database.select(UndergradStatus.id).where(UndergradStatus.status == status)
        ).scalar_one()

    def __repr__(self):
        return f"<UndergradStatus: {self.id} - {self.u_status}>"
