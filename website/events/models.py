# -*- coding: utf-8 -*-
"""Event models."""
from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from website.extensions import database
from website.database import PkModel


class Event(PkModel):
    __tablename__ = "events"

    status_id: Mapped[int] = mapped_column(ForeignKey("event_status.id"))
    start_date: Mapped[str] = mapped_column()
    end_date: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    status_rel: Mapped[EventStatus] = relationship()

    @classmethod
    def search_for_event(self, event: Event) -> Event | None:
        return database.session.execute(
            database.select(Event).where(
                Event.name == event.name,
                Event.description == event.description,
                Event.start_date == event.start_date,
                Event.end_date == event.end_date,
            )
        ).scalar_one_or_none()

    def __repr__(self):
        return f"<Event: {self.id} - {self.name}>"


class EventStatus(PkModel):
    __tablename__ = "event_status"

    status: Mapped[str] = mapped_column(unique=True)

    @classmethod
    def return_status_id(self, status: str) -> int:
        return database.session.execute(
            database.select(EventStatus.id).where(EventStatus.status == status)
        ).scalar_one()

    def __repr__(self):
        return f"<EventStatus: {self.id} - {self.status}>"
