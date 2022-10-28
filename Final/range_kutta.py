import numpy as np

def dydt(t, y): 
    return np.sin(t)**2*y

def f(t): return 2*np.exp(0.5*(t-np.sin(t)*np.cos(t)))


def RK3(t, y, h):
    # compute approximations
    k_1 = dydt(t, y)
    k_2 = dydt(t+h/2, y+(h/2)*k_1)
    k_3 = dydt(t+h/2, y+h*(-k_1 + 2*k_2))

    # calculate new y estimate
    y = y + h * (1/6) * (k_1 + 4 * k_2 + k_3)
    return y


def RK4(t, y, h):
    # compute approximations
    k_1 = dydt(t, y)
    k_2 = dydt(t+h/2, y+(h/2)*k_1)
    k_3 = dydt(t+h/2, y+(h/2)*k_2)
    k_4 = dydt(t+h, y+h*k_3)

    # calculate new y estimate
    y = y + h * (1/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
    return y


# Initialization
ti = 0
tf = 5
h = 0.5
n = int((tf-ti)/h)
t = 0
y = 2
y_rk3 = 2

print("t \t\t yRK3 \t\t yRK4 \t\t f(t)")
print(f"{t:.1f} \t\t {y_rk3:4f} \t\t {y:4f} \t\t {f(t):.4f}")

t_plot = []
y_RK3 = []
y_RK4 = []
y_analytical = []


##
for i in range(1, n+1):
    t_plot.append(t)
    y_RK4.append(y)
    y_RK3.append(y_rk3)
    y_analytical.append(f(t))

    # calculate new y estimate
    y = RK4(t, y, h)
    y_rk3 = RK3(t, y_rk3, h)

    t += h
    print(f"{t:.1f} \t\t {y_rk3:4f} \t\t {y:4f} \t\t {f(t):.4f}")
    
    def dydx(x, y):
    return x+y
 
def dydx(x, y):
    return x+y
 
# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def rungeKutta4(x0, y0, x, h):
    # Count number of iterations using step size or
    # step height h
    n = (int)((x - x0)/h)
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)
 
        # Update next value of y
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
 
        # Update next value of x
        x0 = x0 + h
    return y
 
# Driver method
x0 = 0
y = 1
x = 0.2
h = 0.2
print ('The value of y at x is:', rungeKutta4(x0, y, x, h))
