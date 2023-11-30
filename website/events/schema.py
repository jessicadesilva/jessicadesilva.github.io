from pydantic import BaseModel, ConfigDict


class EventSchema(BaseModel):
    model_config: ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        extra="forbid",
    )

    id: int
    status: str
    start_date: str
    end_date: str
    name: str
    description: str


class EventsListSchema(BaseModel):
    model_config: ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        extra="forbid",
    )

    updated: str
    events: list[EventSchema]
