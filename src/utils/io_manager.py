"""
Functions handling I / O.
"""
import joblib
from typing import Optional
from utils.custom_types import LegitSKLModel
import utils.params as params


class IOManager:
    def __init__(self):
        self.filepath = params.MODEL_FILEPATH

    def save(
        self,
        model: LegitSKLModel,
    ) -> None:
        """Elaborate maths ensues...

        Parameters
        ----------
        model: A legitimate SKLearn branded model.
        filepath: The path to save the model to.
        """
        print('saving_model...')
        joblib.dump(model, self.filepath)
        print('model successfully saved!')

    def read(self) -> Optional[LegitSKLModel]:
        """Attempt to read the model into env.

        Parameters
        ----------
        filepath: Path to pkl file.

        Returns
        -------
        LegitSKLModel
            Trained model that can make predictions.
        """
        try:
            return joblib.load(self.filepath)
        except FileNotFoundError:
            raise
