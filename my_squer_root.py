def my_s_root(p):
    s = 1
    while abs(s*s - p)>0.0000000000001:
        # s**2=p -> s**2-p=0
        # Newton's method
        s = s - (s*s - p)/(2*s)
        
    return s
