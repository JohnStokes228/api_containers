import random
from typing import Any


class NonsenseModel:
    def __init__(
        self,
        extra_colname: str,
        extra_colval: str,
    ) -> None:
        self.extra_colname = extra_colname
        self.extra_colval = extra_colval

    def predict(self, X: Any) -> Any:
        preds = {
            self.extra_colname: self.extra_colval,
            'prediction': random.random()
        }

        return preds

    def fit(self, X: Any, y: Any) -> None:
        print(f"you'll do nuttin!... except provide me with the colname {self.extra_colname}")
