import pyclesperanto_prototype as cle
import numpy as np

def test_average_distance_of_n_far_off_distances():

    labels = cle.push_zyx(np.asarray([
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [1, 1, 1, 3, 3, 3],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2],
                    [0, 0, 0, 2, 2, 2]
    ]))

    reference = cle.push_zyx(np.asarray(
                    [[0, 4.2426, 4.2426, 3]]
    ))

    centroids = cle.centroids_of_labels(labels)
    distance_matrix = cle.generate_distance_matrix(centroids, centroids)

    average_distance_of_n_far_off_distances = cle.average_distance_of_n_far_off_distances(distance_matrix, n=1)

    a = cle.pull_zyx(average_distance_of_n_far_off_distances)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)


    assert (np.allclose(a, b, 0.01))
