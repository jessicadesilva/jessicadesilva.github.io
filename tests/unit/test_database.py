# -*- coding: utf-8 -*-
"""Database unit tests."""
import pytest
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm.exc import ObjectDeletedError

from website.database import PkModel
from website.extensions import database


class ExampleEventModel(PkModel):
    __tablename__ = "test_events"

    status_id = database.Column(
        database.Integer, ForeignKey("test_event_status.id"), nullable=False
    )
    start_date = database.Column(database.String, nullable=False)
    end_date = database.Column(database.String, nullable=False)
    name = database.Column(database.String, nullable=False)
    description = database.Column(database.String, nullable=False)

    status_rel = database.relationship("ExampleEventStatusModel")

    def __init__(self, status_id, start_date, end_date, name, description):
        super().__init__(
            status_id=status_id,
            start_date=start_date,
            end_date=end_date,
            name=name,
            description=description,
        )


class ExampleEventStatusModel(PkModel):
    __tablename__ = "test_event_status"

    status = database.Column(database.String, unique=True, nullable=False)

    def __init__(self, status):
        super().__init__(status=status)


@pytest.mark.usefixtures("database")
class TestCRUDMixin:
    def setup_test_event(self):
        self._test_event_status = ExampleEventStatusModel("scheduled")
        self._test_event_status.save()
        self._test_event = ExampleEventModel(
            self._test_event_status.id,
            "2024-01-01",
            "2024-01-01",
            "Test Event",
            "Test Description",
        )
        return self._test_event

    def test_method_save_with_valid_data_saves_record(self):
        event = self.setup_test_event()
        event.save()

        assert isinstance(event, ExampleEventModel)
        assert ExampleEventModel.get_by_id(event.id) is not None
        assert ExampleEventModel.get_by_id(event.id).name == "Test Event"
        assert ExampleEventModel.get_by_id(event.id).description == "Test Description"

    def test_method_create_with_valid_data_creates_record(self):
        event = ExampleEventModel.create(
            status_id=1,
            start_date="2024-01-01",
            end_date="2024-01-01",
            name="Test Event",
            description="Test Description",
        )

        assert isinstance(event, ExampleEventModel)
        assert ExampleEventModel.get_by_id(event.id) is not None
        assert ExampleEventModel.get_by_id(event.id).name == "Test Event"
        assert ExampleEventModel.get_by_id(event.id).description == "Test Description"

    @pytest.mark.parametrize(
        "commit, expected", [(True, "Edited Event"), (False, "Test Event")]
    )
    def test_method_update_with_valid_data_updates_record(
        self, commit, expected, database
    ):
        event = self.setup_test_event()
        event.save()
        event.update(commit=commit, name="Edited Event")
        query = text("SELECT * FROM test_events")
        result = database.session.execute(query).first()

        assert result.name == expected

    def test_method_delete_with_commit_deletes_record(self):
        event = self.setup_test_event()
        event.save()
        event.delete(commit=True)

        assert ExampleEventModel.get_by_id(event.id) is None

    def test_method_save_without_commit_is_not_saved(self):
        event = self.setup_test_event()
        event.save(commit=False)

        assert ExampleEventModel.get_by_id(event.id) is None

    def test_method_delete_without_commit_raises_object_deleted_error(self):
        event = self.setup_test_event()
        event.save()
        event.delete(commit=False)
        with pytest.raises(ObjectDeletedError):
            ExampleEventModel.get_by_id(event.id)


@pytest.mark.usefixtures("database")
class TestPkModel:
    def test_method_get_by_id_returns_record_when_found(self):
        event = ExampleEventModel.create(
            status_id=1,
            start_date="2024-01-01",
            end_date="2024-01-01",
            name="Test Event",
            description="Test Description",
        )

        assert ExampleEventModel.get_by_id(event.id) == event

    def test_method_get_by_id_returns_none_when_no_record_found(self):
        assert ExampleEventModel.get_by_id(0) is None

    def test_method_get_by_id_returns_none_with_invalid_id(self):
        assert ExampleEventModel.get_by_id("invalid") is None
