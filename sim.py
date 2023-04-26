import random
import numpy as np
from scipy.stats import norm

# TEST DATA: Investing $500 in NASDAQ composite index each month for 40 years
# TODO add history to SQLite db to incorporate varied risk based on asset
today = 11944.06
investment = 500.0
inv_frequency = 30
time = 365 * 40

"""
run through a single random simulation

Args:
    asset_value: float
        current value of the asset
    investment: float
        amount invested each investment period
    inv_frequency: int
        frequency of investment (in days)
    time: int
        time of investment (in days)

Returns: float
    investment value after time
"""
def run_sim(asset_value, investment, inv_frequency, time):
    bal = [investment]
    ret_history = []
    val = asset_value
    val_yesterday = asset_value

    while len(bal) < time:
        ret_history.append(np.log(val / val_yesterday))
        rand = np.std(ret_history) * norm.ppf(random.random())
        val_yesterday = val
        val = val * np.exp(rand)
        bal.append(val)

    return bal[time - 1]

print(run_sim(today, investment, inv_frequency, time))
print(run_sim(today, investment, inv_frequency, time))
print(run_sim(today, investment, inv_frequency, time))
print(run_sim(today, investment, inv_frequency, time))
print(run_sim(today, investment, inv_frequency, time))
print(run_sim(today, investment, inv_frequency, time))
print(run_sim(today, investment, inv_frequency, time))
