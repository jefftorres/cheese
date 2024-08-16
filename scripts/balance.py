import numpy as np

DEMANDA = 40
capacidades = np.array([4, 8, 20, 20, 12])

X = np.array([[0, 0, 20, 20, 0], [0, 8, 15, 5, 12]])
N = X.shape[1]


def alter_lower(single, idx_mut, capacidades):
    delta = capacidades[idx_mut]
    ca = list(np.nonzero(single)[0])
    idx = -1

    single[idx_mut] = delta

    while np.sum(single) != DEMANDA:
        if len(ca) > 0:
            idx = np.random.choice(ca)
            ca.remove(idx)

        if single[idx] - delta >= 0:
            single[idx] -= delta
        else:
            delta -= single[idx]
            single[idx] = 0


def alter_upper(single, idx_mut, capacidades):
    delta = single[idx_mut]
    ca = list(np.where(single == 0)[0])
    idx = -1

    single[idx_mut] = 0

    while np.sum(single) != DEMANDA:
        if len(ca) > 0:
            idx = np.random.choice(ca)
            ca.remove(idx)

        if capacidades[idx] == single[idx]:
            continue

        if single[idx] + delta > capacidades[idx]:
            delta -= capacidades[idx] - single[idx]
            single[idx] = capacidades[idx]
        else:
            single[idx] += delta
            delta = 0


def mutar_cap(individuo, idx_mut):
    delta = capacidades[idx_mut]
    individuo[idx_mut] = delta

    return igualar(individuo)


def igualar(individuo):
    ca = list(np.nonzero(individuo)[0])

    while np.sum(individuo) != DEMANDA and len(ca) > 0:
        idx = np.random.choice(ca)
        ca.remove(idx)

        if capacidades[idx] == individuo[idx]:
            continue

        # if np.sum(individuo) < DEMANDA:
        #
        # elif np.sum(individuo) > DEMANDA:



# def mutar_cero(individuo, idx_mut, capacidades):


print(f'Iniciales')
print(X[0])
print(X[1])

for _ in range(1000):
    print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
    for i in range(len(X)):
        dx = np.random.randint(X.shape[1])

        if X[i][dx] == 0:
            alter_lower(X[i], dx, capacidades)
        else:
            alter_upper(X[i], dx, capacidades)
        # if X[i][idx] != 0:
        #     mutar_cap(X[i], idx)

        print(f'Vector: {X[i]}, Suma: {np.sum(X[i])}')
