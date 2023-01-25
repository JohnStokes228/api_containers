"""
Custom datatypes for use in typehints.
"""
from typing import(
    Any,
    Protocol,
)


class LegitSKLModel(Protocol):
    """Anything which can fit and predict on X must surely be a legitimate SKLearn model right?"""
    def predict(self, X: Any):
        ...

    def fit(self, X: Any, y: Any, *args, **kwargs):
        ...
