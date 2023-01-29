"""
Parameters that may be called throughout the project, ensuring they're easily edited.
"""

from utils.helper_funcs import str_to_dt

PERIOD_UPPER_BOUND = str_to_dt('2022/10/13')
PERIOD_LOWER_BOUND = str_to_dt('2020/08/01')
MODEL_FILEPATH = 'src/artifacts/model.pkl'
