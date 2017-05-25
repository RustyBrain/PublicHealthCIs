from scipy.special import ndtri
from math import sqrt


norm_cum_dist = ndtri((100 + 95) / 200)
z = 1.96

def wilson_lower(value, count, denominator, rate):
    lower_ci = ((2 * count + norm_cum_dist ** 2 - norm_cum_dist * sqrt(norm_cum_dist ** 2 + 4 * count * ((rate -
                    value) / rate))) / 2 / (denominator + norm_cum_dist ** 2)) * rate
    return lower_ci


def wilson_higher(value, count, denominator, rate):
    upper_ci = (2 * count + norm_cum_dist ** 2 + norm_cum_dist * sqrt(norm_cum_dist ** 2 + 4 * count * ((rate - value)
                / rate))) / 2 / (denominator + norm_cum_dist ** 2) * rate

    return upper_ci


def byars_lower(count, denominator, rate):
    c = 1 / (9 * count)
    b = 3 * sqrt(count)
    lower_o = count * ((1 - c - (z / b)) ** 3)
    lower_ci = (lower_o / denominator) * rate
    return lower_ci


def byars_higher(count, denominator, rate):
    c = 1 / (9 * (count + 1))
    b = 3 * (sqrt(count) + 1)
    upper_o = (count + 1) * ((1 - c + (z / b)) ** 3)
    upper_ci = (upper_o / denominator) * rate
    return upper_ci
