import cv2 
import numpy as np
import mtcnn

import os
import sys
import uuid
from typing import Dict, List, Tuple

from exception import (
    InvalidImage,
    NoNameProvided,
    NoFaceDetected,
    FaceMissing,
    InvalidFaceDetector
)
from validator import (
    is_valid_img
)
from utility import (
    draw_bounding_box
)
from face_data_store import FaceDataStore
from face_detection_haar import FaceDetectorHaar
from face_detection_mtcnn import FaceDetectorMTCNN

class FaceRegister:
    """Class for Face Register related methods.

    Raises:
        InvalidImage: [description]
        NoNameProvided: [description]
        NoFaceDetected: [description]
        FaceMissing: [description]
    """

    def __init__(
        self,
        persistent_data_loc="data/facial_data.json",
        face_detection_threshold: int = 0.99,
        face_detector: str = "dlib",
    ) -> None:
        """Constructor

        Args:
            persistent_data_loc (str, optional): Path to save the persistence storage file.
                Defaults to 'data/facial_data.json'.
            face_detection_threshold (int, optional): Threshold facial model confidence to consider a detection.
                Defaults to 0.99.
            face_detector (str, optional): Type of face detector to use. Options:
                dlib, mtcnn, haar. Defaults to 'dlib'.
        """
        if face_detector == "haar":
            self.face_detector = FaceDetectorHaar()
        elif face_detector == "mtcnn":
            self.face_detector = FaceDetectorMTCNN()
        else:
            # self.face_detector = FaceDetectorDlib()
            raise InvalidFaceDetector

        self.face_detection_threshold = face_detection_threshold
        self.datastore = FaceDataStore(persistent_data_loc=persistent_data_loc)

def register_face(self, image=None, name: str = None, bbox: List[int] = None):
    """Method to register a face via the facial encoding.
    Siamese neural network is used to generate 128 numbers
    for a given facial region. These encodings can be used to identify a
    facial ROI for identification later.

    Args:
        image (numpy array, optional): Defaults to None.
        name (str, optional): Name to associate with the face. Defaults to None.
        bbox (List[int], optional): Facial ROI bounding box. Defaults to None.

    Raises:
        NoNameProvided:
        NoFaceDetected:

    Returns:
        Dict: Facial encodings along with an unique identifier and name
    """

    if not is_valid_img(image) or name is None:
        raise NoNameProvided if name is None else InvalidImage

    image = image.copy()
    face_encoding = None

    try:
        if bbox is None:
            bboxes = self.face_detector.detect_faces(image=image)
            if len(bboxes) == 0:
                raise NoFaceDetected
            bbox = bboxes[0]
        face_encoding = self.get_facial_fingerprint(image, bbox)

        # Convert the numpy array to normal python float list
        # to make json serialization simpler
        facial_data = {
            "id": str(uuid.uuid4()),
            "encoding": tuple(face_encoding.tolist()),
            "name": name,
        }
        # save the encoding with the name
        self.save_facial_data(facial_data)
    except Exception as exc:
        raise exc
    return facial_data


detection_interval = 5

if __name__ == "__main__":
    required_shape = (160,160)
    path_m = "facenet_keras_weights.h5"
    face_detector = mtcnn.MTCNN()
    
    cap = None
    try:
        cap = cv2.VideoCapture(0)
        frame_num = 0

        while True:
            status, frame = cap.read()
            if not status:
                print("CAM NOT OPEND")
                break

            if frame_num % detection_interval == 0:
                # detect faces
                bboxes = face_detector.detect_faces(image=frame)
                print('bboxes:',bboxes)
                try:
                    if len(bboxes) == 1:
                        facial_data = self.face_recognizer.register_face(
                            image=frame, name=name, bbox=bboxes[0]
                        )
                        if facial_data:
                            draw_bounding_box(frame, bboxes[0])
                            cv2.imshow("Registered Face", frame)
                            cv2.waitKey(0)
                            logger.info("Press any key to continue......")
                            break
                except Exception as exc:
                    traceback.print_exc(file=sys.stdout)
            frame_num += 1
    except Exception as exc:
        raise exc
    finally:
        cv2.destroyAllWindows()
        cap.release()


    while cap.isOpened():
        ret,frame = cap.read()

        if not ret:
            print("CAM NOT OPEND") 
            break
        

        cv2.imshow('camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break