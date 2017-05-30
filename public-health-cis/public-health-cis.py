from scipy.special import ndtri
from scipy.stats import chi2
from math import sqrt

alpha = 0.05
norm_cum_dist = ndtri((100 + 95) / 200)
z = ndtri(1 - alpha / 2)


def wilson_lower(value, count, denominator, rate):
    lower_ci = ((2 * count + norm_cum_dist ** 2 - norm_cum_dist * sqrt(norm_cum_dist ** 2 + 4 * count * ((rate -
                    value) / rate))) / 2 / (denominator + norm_cum_dist ** 2)) * rate
    return lower_ci


def wilson_upper(value, count, denominator, rate):
    upper_ci = (2 * count + norm_cum_dist ** 2 + norm_cum_dist * sqrt((norm_cum_dist) ** 2 + 4 * count * ((rate - value)
                / rate))) / 2 / (denominator + norm_cum_dist ** 2) * rate

    return upper_ci


def byars_lower(count, denominator, rate):
    if count < 389:
        b = (chi2.ppf((alpha * 2), (count * 2)) / 2)
        c = b / denominator
        lower_ci = c * rate
        return lower_ci
    else:
        c = 1 / (9 * count)
        b = sqrt(count)
        d = z / (3 * b)
        lower_o = (1 - c - d) ** 3
        e = count * lower_o
        lower_ci = (e / denominator) * rate
        return lower_ci


def byars_upper(count, denominator, rate):
    if count < 389:
        b = chi2.ppf(1 - (alpha / 2), 2 * count + 2) / 2
        c = b / denominator
        upper_ci = c * rate
        return upper_ci
    else:
        c = 1 / (9 * (count + 1))
        b = sqrt(count + 1)
        d = z / (3 * b)
        upper_o = (1 - c + d) ** 3
        e = (count + 1) * upper_o
        upper_ci = (e / denominator) * rate
        return upper_ci