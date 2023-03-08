"""
Models for data provided to API endpoint.
"""
from pydantic import (
    BaseModel,
    validator,
    Field,
    UUID4,
)
from typing import (
    List,
    Optional,
)
import os
from utils.custom_errors import (
    DateNotInPeriodError,
    ValueNotInSetError,
)
from utils.helper_funcs import str_to_dt
from utils.custom_types import AcceptableBodyParts
import utils.params as params
from datetime import datetime
from uuid import uuid4


class Clothes(BaseModel):
    """Clothing datatype."""
    brand: str
    cost: float
    where_worn: Optional[AcceptableBodyParts]

    class Config:
        validate_assignment = True


class RequestBody(BaseModel):
    """Expected structure of requests to API endpoint."""
    uuid: UUID4 = Field(default_factory=uuid4)
    timestamp_requested: datetime = Field(default_factory=datetime.now)
    name: str
    age: int = Field(..., ge=0)
    date_of_accident: str
    number_of_limbs_before_accident: float
    clothes: List[Clothes] = Field(default_factory=list)

    class Config:
        validate_assignment = True

    @validator('date_of_accident', pre=True)
    def check_accident_in_period(cls, value) -> Optional[str]:
        if not params.PERIOD_UPPER_BOUND >= str_to_dt(value) >= params.PERIOD_LOWER_BOUND:
            raise DateNotInPeriodError(
                date=value,
                upper_bound=params.PERIOD_UPPER_BOUND,
                lower_bound=params.PERIOD_LOWER_BOUND
            )

        return value


class ResponseMessage(BaseModel):
    """Expected structure of response from the ML model."""
    uuid: UUID4
    timestamp_requested: datetime
    timestamp_response: datetime = Field(default_factory=datetime.now)
    prediction: float = Field(..., ge=0.0, le=1.0)
