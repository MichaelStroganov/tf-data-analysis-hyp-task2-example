import pandas as pd
import numpy as np
import math
from scipy.stats import ks_2samp


chat_id = 1004085803 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    statistic, pvalue = ks_2samp(x, y)
    alpha = 0.02
    if pvalue > alpha:
        return False
    else:
        True

    
