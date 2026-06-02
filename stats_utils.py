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

def prop1(x, n, p1 = 0.5, alt='two-sided'):
    ph = x/n
    sd = math.sqrt(p1*(1-p1)/n)
    z_score = (ph-p1)/sd
    if alt == 'larger':
        p = stats.norm.sf(z_score)
    elif alt == 'two-sided':
        p = 2*stats.norm.sf(abs(z_score))
    else:
        p = stats.norm.cdf(z_score)
    return {'statistic': float(z_score),'p_value': float(p)}

def prop2(x1, n1, x2, n2, alt='two-sided'):
    ph1 = x1/n1
    ph2 = x2/n2
    pc = (x1+x2)/(n1+n2)
    sd = math.sqrt(pc*(1-pc)*(1/n1 + 1/n2))
    z = (ph1-ph2)/sd
    if alt == 'larger':
        p = stats.norm.sf(z)
    elif alt == 'two-sided':
        p = 2*stats.norm.sf(abs(z))
    else:
        p = stats.norm.cdf(z)
    return {'statistic': float(z),'p_value': float(p)}

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
