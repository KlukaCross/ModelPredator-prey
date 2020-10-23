import numpy as np
import matplotlib.pyplot as plt

LIMIT_PREY = 100

FACTOR_PREY_GROWTH = 0.6  # is K
FACTOR_PREDATOR_FALL = 0.8  # is D

FACTOR_PREY_FALL = 0.01  # is bN
FACTOR_PREDATOR_GROWTH = 0.015  # is bZ

ITERATIONS = 100

START_POP_PREYS = 70
START_POP_PREDATORS = 5


def get_prey(count_prey, count_predator):
    return (1+FACTOR_PREY_GROWTH*(LIMIT_PREY-count_prey)/LIMIT_PREY-FACTOR_PREY_FALL*count_predator)*count_prey


def get_predator(count_prey, count_predator):
    return (1-FACTOR_PREDATOR_FALL+FACTOR_PREDATOR_GROWTH*count_prey)*count_predator


x = np.arange(0, ITERATIONS, 1)
y1 = np.arange(0, ITERATIONS, 1)
y2 = np.arange(0, ITERATIONS, 1)

y1[0] = START_POP_PREYS
y2[0] = START_POP_PREDATORS
for i in range(1, ITERATIONS):
    y1[i] = get_prey(y1[i-1], y2[i-1])
    y2[i] = get_predator(y1[i-1], y2[i-1])
    print("{0}: {1} - {2}".format(i, y1[i], y2[i]))

fig, ax = plt.subplots(figsize=(5, 3))

ax.plot(x, y1, x, y2)
ax.set_title("model predator-prey")
ax.legend(labels=["prey", "predator"], loc="upper right")
ax.set_ylabel("population")
ax.set_xlabel("time")
ax.set_xlim(xmin=x[0], xmax=ITERATIONS-1)
fig.tight_layout()

plt.show()