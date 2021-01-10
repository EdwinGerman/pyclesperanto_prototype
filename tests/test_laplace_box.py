import pyclesperanto_prototype as cle
import numpy as np


def test_laplace_box():
    test1 = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [0, -1, -1, -1, 0],
        [0, -1, 8, -1, 0],
        [0, -1, -1, -1, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test1)
    cle.laplace_box(test1, result)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)

    assert (np.array_equal(a, b))

