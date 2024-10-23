import numpy as np


def sa(t_max=1, t_min=1e-8, e_th=1e-5, alpha=0.91):
    np.random.seed(1)
    t = t_max
    x = gen()
    e = f(x)

    while t > t_min and e > e_th:
        print(f'f(x): {e}\t\t\tx: {x}')
        dx = gen()
        de = f(dx)

        delta = de-e

        if delta < 0:
            x = dx
            e = de
        else:
            p = np.exp(-delta/t)
            r = np.random.rand()

            if r < p:
                x = dx
                e = de

        t *= alpha


def f(x):
    return x[0]**2 + x[1]**2


def gen():
    return np.random.uniform(-1, size=2)


if __name__ == '__main__':
    sa()
