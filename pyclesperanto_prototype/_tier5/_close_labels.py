from .._tier0 import plugin_function, Image
from .._tier0 import create_like, create_labels_like
from .._tier1 import erode_sphere, erode_box, multiply_images, copy
from .._tier4 import dilate_labels


@plugin_function(categories=['label processing', 'in assistant'], output_creator=create_labels_like)
def close_labels(labels_input: Image, labels_destination: Image = None, radius: int = 0) -> Image:
    """Apply a morphological closing operation to a label image.

    The operation consists of iterative dilation and erosion of the labels.
    With every iteration, box and diamind/sphere structuring elements are used
    and thus, the operation has an octagon as structuring element.

    Parameters
    ----------
    labels_input: Image
    labels_destination: Image
    radius: int

    Returns
    -------
    labels_destination: Image
    """
    if radius == 0:
        return copy(labels_input, labels_destination)

    temp = dilate_labels(labels_input, radius=radius)

    flip = temp > 0
    flop = create_like(temp)
    for i in range(radius):
        if i % 2 == 0:
            erode_sphere(flip, flop)
        else:
            erode_box(flop, flip)
    if radius % 2 == 0:
        return multiply_images(flip, temp, labels_destination)
    else:
        return multiply_images(flop, temp, labels_destination)
