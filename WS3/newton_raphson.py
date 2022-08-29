def f(x):
    return x * x * x - x * x + 2

def df(x):
    return 3 * x * x - 2 * x

def newtonRaphson( x ):
    h = f(x) / df(x)
    while abs(h) >= 0.0001:
        h = f(x)/df(x)
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
    print("The value of the root is : ", "%.4f"% x)
 
x0 = 0.1 # Initial value
newtonRaphson(x0)

------------------------------------------
def newton_raphson(f, limit):
    a = limit[0]
    b = limit[1]
    t = float(a + b) / 2

    while f.subs(x, t) > 0.001 or f.subs(x, t) < -0.001:
        print("t =", t, "\nf(t) =", f.subs(x, t), end = "\n\n")
        t = t - f.subs(x, t) / diff(f, x).subs(x, t)

    print("SOLUTION\nx = {x}\nf(x) = {fx}".format(x = t, fx = f.subs(x, t)))

newton_raphson(f,limit)
