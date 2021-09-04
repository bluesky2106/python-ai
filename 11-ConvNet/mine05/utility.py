from typing import List, Tuple

import cv2
import dlib

from exception import InvalidImage
from validator import is_valid_img

def convert_to_rgb(image):
    """Converts an image to RGB format.

    Args:
        image (numpy array): [description]

    Raises:
        InvalidImage: [description]

    Returns:
        [type]: [description]
    """
    if not is_valid_img(image):
        raise InvalidImage
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def draw_bounding_box(image, bbox: List[int], color: Tuple = (0, 255, 0)):
    """Used for drawing bounding box on an image

    Args:
        image (numpy array): [description]
        bbox (List[int]): Bounding box coordinates
        color (Tuple, optional): [description]. Defaults to (0,255,0).

    Returns:
        [type]: [description]
    """
    x1, y1, x2, y2 = bbox
    cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
    return image