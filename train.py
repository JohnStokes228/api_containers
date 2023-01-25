"""
'Train' the model and send to pkl.

In the name of 'failing left' I believe data quality can be assumed prior to hitting this stage, so no DQ checks are
applied during model training. This may be incredibly dumb but who's to say...
"""
import random
from typing import Any
from utils.io_manager import IOManager


class NonsenseModel:
    def __init__(
        self,
        extra_colname: str,
        extra_colval: str,
    ) -> None:
        self.extra_colname = extra_colname
        self.extra_colval = extra_colval

    def predict(self, X: Any):
        X[self.extra_colname] = self.extra_colval
        X['prediction'] = random.random()

        return X

    def fit(self, X: Any, y: Any):
        print(f"you'll do nuttin!... except provide me with the colname {self.extra_colname}")


def main():
    model = NonsenseModel(extra_colname='elaborate_transformation', extra_colval='lol jk its crap')
    IOManager().save(model)


if __name__ == '__main__':
    main()
