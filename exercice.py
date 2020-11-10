#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([(np.sqrt(c[0]**2+c[1]**2), np.arctan2(c[1], c[0])) for c in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    diff = [abs(i-number) for i in values]
    return diff.index(min(diff))


def graph_test():
    x = np.linspace(-1, 1, num=250)
    y = x**2*np.sin(1/x**2)+x
    plt.plot(x,y)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    graph_test()
    pass
