import random
from typing import Any
import time


class NonsenseModel:
    def predict(self, X: Any) -> float:
        time.sleep(random.random())

        return random.random()

    def fit(self, X: Any, y: Any) -> None:
        print(f"you'll do nuttin!... except provide me with the colname {self.extra_colname}")
