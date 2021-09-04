import cv2 
import numpy as np
import mtcnn

import os
import sys
import uuid
from typing import Dict, List, Tuple
from architecture import InceptionResNetV2
from sklearn.preprocessing import Normalizer
import pickle
from scipy.spatial.distance import cosine

from exception import (
    InvalidImage,
    NoNameProvided,
    NoFaceDetected,
    FaceMissing,
    InvalidFaceDetector
)
from validator import (
    is_valid_img,
    path_exists
)
from utility import (
    draw_bounding_box
)
from face_detection_haar import FaceDetectorHaar
from face_detection_mtcnn import FaceDetectorMTCNN

class FaceRecognizer:
    """Class for Face Recognizer related methods.

    Raises:
        InvalidImage: [description]
        NoNameProvided: [description]
        NoFaceDetected: [description]
        FaceMissing: [description]
    """

    def __init__(
        self,
        face_detector: str = "mtcnn",
        conf_threshold: float = 0.7,
        db_loc="faces",
        encoding_path: str = "encodings",  
    ) -> None:
        """Constructor

        Args:
            face_detector (str, optional): Type of face detector to use. Options:
                mtcnn, haar. Defaults to 'mtcnn'.
            conf_threshold (float, optional): Threshold confidence to consider
            db_loc (str, optional): Path to save the user images file.
                Defaults to 'faces'.
            encoding_path (str, optional): Path to save the encoding file.
                Defaults to 'encodings'.
        """
        if face_detector == "haar":
            self.face_detector = FaceDetectorHaar()
        elif face_detector == "mtcnn":
            self.face_detector = FaceDetectorMTCNN()
        else:
            # self.face_detector = FaceDetectorDlib()
            raise InvalidFaceDetector

        self.conf_threshold = conf_threshold
        self.db_loc = db_loc
        
        if not path_exists(encoding_path):
            os.mkdir(encoding_path)
        self.encoding_path = encoding_path

        self.face_encoder = InceptionResNetV2()
        self.face_encoder.load_weights("facenet_keras_weights.h5")
        self.required_shape = (160,160)

        
    def register_face(self, user_name: str, detection_interval: int = 5, num_pictures: int = 100):
        """Register Face

        Args:
            user_name (str): The user name captured images.
            detection_interval (int, optional): the interval which trigger the action of capturing image from  video.
                For ex., every 5 frames, one image will be captured.
                Defaults to 5.
            num_pictures (int, optional): number of pictures which will be captured.
                Defaults to 100
        """

        path = os.path.join(self.db_loc, user_name)
        if not path_exists(path):
            os.mkdir(path)

        cap = None
        num = 0
        try:
            cap = cv2.VideoCapture(0)
            frame_num = 0

            while True:
                status, frame = cap.read()
                if not status:
                    print("CAM NOT OPEN")
                    break

                if frame_num % detection_interval == 0:
                    # detect faces
                    bboxes = self.face_detector.detect_faces(image=frame)
                    try:
                        if len(bboxes) == 1:
                            bbox = bboxes[0]
                            x1, y1, x2, y2 = bbox
                            img = draw_bounding_box(frame, bbox)
                            cv2.imshow(user_name, img)
                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                break

                            file_name = os.path.join(path, str(uuid.uuid4()) + ".jpg")
                            cv2.imwrite(file_name, frame)
                            num += 1
                            if num >= num_pictures:
                                break
                    except Exception as e:
                        raise e
                frame_num += 1
        except Exception as e:
            raise e
        finally:
            cv2.destroyAllWindows()
            cap.release()

    def normalize(self, img):
        """Normalize an image
        """
        mean, std = img.mean(), img.std()
        return (img - mean) / std

    def _encode(self, img, bbox):
        x1, y1, x2, y2  = bbox
        face = img[y1:y2 , x1:x2]
        face = self.normalize(face)
        face = cv2.resize(face, self.required_shape)
        face_d = np.expand_dims(face, axis=0)
        encode = self.face_encoder.predict(face_d)[0]
        print("shape:", encode.shape)
        
        return encode

    def encode(self, encode_name: str = "encodings.pkl"):
        """Encode Image
        Args:
            encode_name (str): The encode file name.
                Defaults to encodings.pkl.
        """
        encodes = []
        encoding_dict = dict()
        l2_normalizer = Normalizer('l2')

        for face_names in os.listdir(self.db_loc):
            person_dir = os.path.join(self.db_loc, face_names)
            for image_name in os.listdir(person_dir):
                image_path = os.path.join(person_dir,image_name)

                img_BGR = cv2.imread(image_path)
                img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

                bboxes = self.face_detector.detect_faces(img_RGB)
                if len(bboxes) == 0:
                    continue

                encode = self._encode(img_RGB, bboxes[0])
                encodes.append(encode)

            if encodes:
                encode = np.sum(encodes, axis=0)
                encode = l2_normalizer.transform(np.expand_dims(encode, axis=0))[0]
                encoding_dict[face_names] = encode
        
        file_path = os.path.join(self.encoding_path, encode_name)
        with open(file_path, 'wb') as file:
            pickle.dump(encoding_dict, file)

    def detect(self, img, encoding_dict):
        recognition_t = 0.5
        l2_normalizer = Normalizer('l2')
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        bboxes = self.face_detector.detect_faces(img_rgb, self.conf_threshold)
        for bbox in bboxes:
            encode = self._encode(img, bbox)
            encode = l2_normalizer.transform(encode.reshape(1, -1))[0]

            name = 'unknown'
            distance = float("inf")
            for db_name, db_encode in encoding_dict.items():
                dist = cosine(db_encode, encode)
                if dist < recognition_t and dist < distance:
                    name = db_name
                    distance = dist
            img = draw_bounding_box(img, bbox, (0, 0, 255), name, (0, 0, 255))
 
        return img

    def load_pickle(self, encode_name):
        file_path = os.path.join(self.encoding_path, encode_name)
        with open(file_path, 'rb') as f:
            encoding_dict = pickle.load(f)
        return encoding_dict

    

if __name__ == "__main__":
    fr = FaceRecognizer()
    # fr = FaceRecognizer(face_detector='haar')

    # Automatic create 100 images for user Akagi
    # fr.register_face(user_name='Akagi')

    # encode model
    encode_name = "encodings.pkl"
    # fr.encode()

    encoding_dict = fr.load_pickle(encode_name)
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret,frame = cap.read()

        if not ret:
            print("CAM NOT OPEN") 
            break
        
        frame = fr.detect(frame, encoding_dict)

        cv2.imshow('camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

