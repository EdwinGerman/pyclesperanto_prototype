def test_maximum_of_touch_portion_within_range_neighbors_map():
    import numpy as np
    import pyclesperanto_prototype as cle

    labels = cle.asarray([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 2, 2, 0],
        [0, 1, 1, 1, 2, 2, 0],
        [0, 0, 3, 3, 3, 3, 0],
        [0, 0, 4, 4, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ])

    reference = cle.replace_intensities(cle.asarray([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 2, 2, 0],
        [0, 1, 1, 1, 2, 2, 0],
        [0, 0, 3, 3, 3, 3, 0],
        [0, 0, 4, 4, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]), [0, 3, 3, 4, 4])

    result = cle.maximum_of_touch_portion_within_range_neighbors_map(labels, labels, minimum_touch_portion=0.09)

    print(result)
    print(reference)

    assert np.allclose(result, reference, 0.01)

