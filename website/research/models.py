# -*- coding: utf-8 -*-
"""Research models."""
from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from website.database import PkModel
from website.extensions import database


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

    @classmethod
    def search_for_project(self, search: Project) -> Project | None:
        return database.session.execute(
            database.select(Project).where(
                Project.type_id == search.type_id,
                Project.status_id == search.status_id,
                Project.students == search.students,
                Project.title == search.title,
                Project.description == search.description,
            )
        ).scalar_one_or_none()

    def __repr__(self):
        return f"<Project: {self.id} - {self.title}>"


class ProjectType(PkModel):
    __tablename__ = "project_type"

    type: Mapped[str] = mapped_column(unique=True)

    @classmethod
    def get_id(self, type: str) -> int:
        return database.session.execute(
            database.select(self.id).where(self.type == type)
        ).scalar_one_or_none()

    def __repr__(self):
        return f"<ProjectType: {self.id} - {self.type}>"


class UndergradStatus(PkModel):
    __tablename__ = "undergrad_status"

    status: Mapped[str] = mapped_column(unique=True)

    @classmethod
    def get_id(self, status: str) -> int:
        return database.session.execute(
            database.select(self.id).where(self.status == status)
        ).scalar_one_or_none()

    def __repr__(self):
        return f"<UndergradStatus: {self.id} - {self.u_status}>"
