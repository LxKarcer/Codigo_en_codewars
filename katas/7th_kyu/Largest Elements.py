def largest(n, xs):
    ord_xs = sorted(xs)
    if n==0:
        return [] 
    return ord_xs[-(n):]