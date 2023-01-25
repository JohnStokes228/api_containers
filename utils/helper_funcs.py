"""
Functions used to provide standard utility in multiple places throughout.
"""
from datetime import datetime
from typing import Optional


def str_to_dt(date: str) -> Optional[datetime]:
    """Attempt to convert to DT or raise error.

    Parameters
    ----------
    date: the string to be ideally converted, if it's not shit.

    Returns
    -------
    Optional[datetime]
        If the string was valid you'll get your DT, elsewise it's the bin with you and your dreams.
    """
    try:
        return datetime.strptime(date, '%Y/%m/%d')
    except ValueError:
        raise
