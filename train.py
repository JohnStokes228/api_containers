"""
'Train' the model and send to pkl.

In the name of 'failing left' I believe data quality can be assumed prior to hitting this stage, so no DQ checks are
applied during model training. This may be incredibly dumb but who's to say...
"""
from src.utils.io_manager import IOManager
from src.utils.model import NonsenseModel


def main():
    model = NonsenseModel(extra_colname='elaborate_transformation', extra_colval='lol jk its crap')
    IOManager().save(model)


if __name__ == '__main__':
    main()
