"""
Models for data provided to API endpoint.
"""
from pydantic import (
    BaseModel,
    validator,
    Field,
)
from datetime import datetime
from typing import (
    List,
    Optional,
)

from utils.custom_errors import (
    DateNotInPeriodError,
    ValueNotInSetError,
)
from utils.helper_funcs import str_to_dt
import utils.params as params


class Clothes(BaseModel):
    """Clothing datatype."""
    brand: str
    cost: foat
    where_worn: Optional[str]

    class Config:
        validate_assignment = True

    @validator('where_worn', pre=True)
    def clothes_on_acceptable_bodypart(cls, value) -> Optional[str]:
        acceptable_bodyparts = ['legs', 'hands', 'body', 'head', ]

        if value not in acceptable_bodyparts:
            raise ValueNotInSetError(value=value, list_of_vals=acceptable_bodyparts)

        return value


class RequestBody(BaseModel):
    """Expected structure of requests to API endpoint."""
    name: str
    age: int
    date_of_accident: str
    number_of_limbs_before_accident: float
    clothes: Optional[List[Clothes]] = None

    class Config:
        validate_assignment = True

    @validator('date_of_accident', pre=True)
    def check_accident_in_period(cls, value) -> Optional[str]:
        if params.PERIOD_UPPER_BOUND >= str_to_dt(value) >= params.PERIOD_LOWER_BOUND:
            raise DateNotInPeriodError(
                date=value,
                upper_bound=params.PERIOD_UPPER_BOUND,
                lower_bound=params.PERIOD_LOWER_BOUND
            )

        return value
