def cohen_d(x,y):
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    return (mean(x) - mean(y)) / sqrt(((nx-1)*std(x, ddof=1) ** 2 + (ny-1)*std(y, ddof=1) ** 2) / dof)


def test_normality(x):
    """
    h0: x is normal
    ha: x is not normal
    
    if pvalue < 0.5 
        we reject the null hypothesis and our data is not normal
    if pvalue > 0.5
        we fail to rejrect the null hypothesis and our data is normal
    """
    t, p = scs.shapiro(x)
    if p < 0.5:
        print(f"Data is not normal with \npvalue={p}")
        return False
    else:
        print(f"Data is normal with \npvalue={p}")
        return True

def test_equal_variances(x1, x2):
    """
    h0: var_x1 = var_x2
    ha: var_x1 != var_x2
    
    """
    t, p = scs.levene(x1, x2)
    if p < 0.5:
        print(f"p = {p}\nThe data does not have equal variances ")
        return False
    else:
        print(f"p = {p}\nThe data have equal variances")
        return True
    
