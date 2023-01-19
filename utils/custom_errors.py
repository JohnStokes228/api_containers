"""
All custom errors requried throughout the project to ensure readability of error trace. Especially useful during data
validation.
"""
from typing import (
    Any,
    List,
)


class DateNotInPeriodError(Exception):
    """Exception raised when date is not within bounds.

    Parameters
    ----------
    date: Provided date which caused the error.
    lower_bound: Lower bound of exceptable dates.
    upper_bound: Upper bound of exceptable dates.
    """

    def __init__(
        self,
        date: str,
        lower_bound: str = '01/01/2015',
        upper_bound: str = '01/01/2023'
    ):
        self.message = f"provided date {date} is not within the acceptable period of {lower_bound} - {upper_bound}"
        super().__init__(self.message)


class PenisError(Exception):
    """Exception Raised if someone uses 'penis' as an input - grow up."""

    def __init__(self):
        super().__init__("DO NOT USE 'penis' AS A VALUE HERE.")


class ValueNotInSetError(Exception):
    """Exception raised when a value isn't in the set of acceptable values.

    Parameters
    ----------
    value: Provided value which caused the error.
    list_of_vals: List of values that 'value' is sadly inequal to.
    """

    def __init__(
        self,
        value: Any,
        list_of_vals: List[Any],
    ):
        if value == 'penis':
            raise PenisError

        self.message = f"provided value {value} is not within the acceptable set of values :{list_of_vals}"
        super().__init__(self.message)
