import matplotlib.pyplot as plt
from numpy import *

L1, L2 = 10.0, 10.0

x = float(input('x = '))
y = float(input('y = '))

try:
    Q2 = rad2deg(-arccos((x ** 2 + y ** 2 - L1 ** 2 - L2 ** 2) / (2 * L1 * L2)))
    Q1 = rad2deg(arctan(y / x)) + rad2deg(arctan(L2 * sin(Q2) / (L1 + L2 * cos(Q2))))
    print(Q1, Q2)

    x0 = L1 * rad2deg(cos(Q1))
    y0 = L1 * rad2deg(sin(Q1))
    x1 = L2 * rad2deg(cos(Q2))
    y1 = L2 * rad2deg(sin(Q2))

    plt.title('This is it folk')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot([0, x0], [0, y0])
    plt.plot([x0, x0 + x1], [y0, y0 + y1])
    plt.grid(True)
    plt.show()

except ZeroDivisionError:
    print('Zero is invalid')
