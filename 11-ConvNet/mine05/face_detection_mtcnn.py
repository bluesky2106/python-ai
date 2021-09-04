from typing import List

import cv2
from mtcnn import MTCNN

from exception import InvalidImage
from face_detector import FaceDetector
from utility import convert_to_rgb, draw_bounding_box
from validator import is_valid_img

class FaceDetectorMTCNN(FaceDetector):
    """Class for face detection. Uses a MTCNN
    based neural network to get the bounding box coordinates
    for a human face.
    """

    def __init__(self):
        """Constructor
        """
        try:
            # load the model
            self.face_detector = MTCNN()
        except Exception as e:
            raise e

    def detect_faces(self, image, conf_threshold: float = 0.7) -> List[List[int]]:
        """Performs facial detection on an image. Uses MTCNN.
        Args:
            image (numpy array):
            conf_threshold (float, optional): Threshold confidence to consider
        Raises:
            InvalidImage: When the image is either None or
            with wrong number of channels.

        Returns:
            List[List[int]]: List of bounding box coordinates
        """
        if not is_valid_img(image):
            raise InvalidImage

        # Do a forward propagation with the blob created from input img
        detections = self.face_detector.detect_faces(image)
        # Bounding box coordinates of faces in image
        bboxes = []
        for _, detection in enumerate(detections):
            conf = detection["confidence"]
            if conf >= conf_threshold:
                x, y, w, h = detection["box"]
                x1, y1, x2, y2 = x, y, x + w, y + h
                bboxes.append([x1, y1, x2, y2])

        return bboxes

    def __repr__(self):
        return "FaceDetectorMTCNN"


if __name__ == "__main__":

    # Sample Usage
    ob = FaceDetectorMTCNN()
    img = cv2.imread("faces/Akagi/Akagi_1.jpg")

    bboxes = ob.detect_faces(convert_to_rgb(img))
    print(bboxes)
    print(ob)
    print(img.shape)
    for bbox in bboxes:
        cv2.imwrite('out/Akagi_1.jpg', draw_bounding_box(img, bbox))
        cv2.imshow("Test", draw_bounding_box(img, bbox))
        cv2.waitKey(0)
