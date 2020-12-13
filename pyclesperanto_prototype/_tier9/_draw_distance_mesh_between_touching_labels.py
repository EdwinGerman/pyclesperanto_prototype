from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function

@plugin_function
def draw_distance_mesh_between_touching_labels(labels : Image, distance_mesh_destination : Image = None):
    from .._tier9 import centroids_of_labels
    from .._tier1 import generate_distance_matrix
    from .._tier1 import generate_touch_matrix
    from .._tier1 import touch_matrix_to_mesh
    from .._tier1 import multiply_images

    centroids = centroids_of_labels(labels)
    distance_matrix = generate_distance_matrix(centroids, centroids)
    touch_matrix = generate_touch_matrix(labels)
    touch_distance_matrix = multiply_images(touch_matrix, distance_matrix)

    from .._tier1 import set
    set(distance_mesh_destination, 0)

    distance_mesh_destination = touch_matrix_to_mesh(centroids, touch_distance_matrix, distance_mesh_destination)
    return distance_mesh_destination
