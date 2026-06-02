import math
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

def adj(stat, p_two, alt):
    if alt == 'two-sided':
        return p_two
    p_one = p_two / 2.0
    if alt == 'greater':
        if stat > 0:
            return p_one
        else:
            return 1-p_one
    else:  
        if stat < 0:
            return p_one
        else:
            return 1-p_one

def prop1(count, nobs, p1 = 0.5, alt='two-sided'):
    stat, p_two = proportions_ztest(count,nobs,p1,alt)
    return {'statistic': float(stat),'p_value': float(p)}

def prop2(count1, n1, count2, n2, alt='two-sided'):
    stat, p_two = proportions_ztest([count1, count2],[n1, n2],alt)
    return {'statistic': float(stat),'p_value': float(p)}

def t1(mean, s, n, mu = 0.0, alt = 'two-sided'):
    se = s/math.sqrt(n)
    stat = (mean - mu)/se
    df = n-1
    if alt == 'two-sided':
        p = 2 * stats.t.sf(abs(stat), df)
    elif alt == 'greater':
        p = stats.t.sf(stat, df)
    else: 
        p = stats.t.cdf(stat, df)
    return {'statistic': float(stat),'p_value': float(p),'df': int(df)}

def t2(mean1, s1, n1, mean2, s2, n2, eq=False, alt='two-sided'):
    se = math.sqrt((s1*s1)/n1 + (s2*s2)/n2)
    df = min(n1-1, n2- 1)
    stat = ((mean1 - mean2) / se)
    if alt == 'two-sided':
        p = 2 * stats.t.sf(abs(stat), df)
    elif alt == 'greater':
        p = stats.t.sf(stat, df)
    else: 
        p = stats.t.cdf(stat, df)
    return {'statistic': float(stat),'p_value': float(p),'df': float(df)}


def tp(mean_diff, s_diff, n, alt='two-sided'):

    se = s_diff / math.sqrt(n)
    stat = mean_diff/ se
    df = n -1
    if alt == 'two-sided':
        p = 2 *stats.t.sf(abs(stat), df)
    elif alt == 'greater':
        p = stats.t.sf(stat, df)
    else:
        p = stats.t.cdf(stat, df)
    return {'statistic': float(stat),'p_value': float(p),'df': int(df)}
