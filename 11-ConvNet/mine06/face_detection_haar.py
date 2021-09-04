import os
from typing import List
import cv2

from exception import InvalidImage
from face_detector import FaceDetector
from utility import convert_to_rgb, draw_bounding_box
from validator import is_valid_img

class FaceDetectorHaar(FaceDetector):
    """Class for face detection. Uses a OpenCV's CNN
    model to get the bounding box coordinates for a human face.

    """

    def __init__(self):
        """Constructor
        """
        try:
            # load the model
            path = os.path.sep.join(["cascades", "haarcascade_frontalface_default.xml"])
            self.face_detector = cv2.CascadeClassifier(path)
        except Exception as e:
            raise e

    def detect_faces(self, image, conf_threshold: float = 0.7) -> List[List[int]]:
        """Performs facial detection on an image. Uses OpenCV DNN based face detector.
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

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faceRects = self.face_detector.detectMultiScale(
		    gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30),
		    flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        # Bounding box coordinates of faces in image
        bboxes = []
        for (x1, y1, w, h) in faceRects:
            x2 = x1 + w
            y2 = y1 + h
            bboxes.append([x1, y1, x2, y2])

        return bboxes

    def __repr__(self):
        return "FaceDetectorHaar"


if __name__ == "__main__":
    # Sample Usage
    ob = FaceDetectorHaar()
    img = cv2.imread("faces/Akagi/Akagi_7.jpg")

    bboxes = ob.detect_faces(convert_to_rgb(img), conf_threshold=0.99)
    
    print(bboxes)
    print(ob)
    print(img.shape)
    for bbox in bboxes:
        cv2.imwrite('out/Akagi_7.jpg', draw_bounding_box(img, bbox))
        cv2.imshow("Test", draw_bounding_box(img, bbox))
        cv2.waitKey(0)
