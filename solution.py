import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 560481426 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    l = (-min(-x)-1/2)/(32**2/2)
    r = (-np.log(alpha)/ n -min(-x)-1/2)/ (32**2/2)
    return l, \
           r
