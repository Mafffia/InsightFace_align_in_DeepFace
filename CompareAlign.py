from insightface.utils import face_align
import cv2
from insightface.app import FaceAnalysis
import face_align
import matplotlib.pyplot as plt
from deepface import DeepFace
from deepface.commons import functions


def compare(img):
    face_img = face_align.get_face_align(img)
    arcalign = DeepFace.analyze(img_path = face_img, actions = ['age', 'gender', 'race', 'emotion'],detector_backend='skip',align=False)
    deepalign = DeepFace.analyze(img_path = img, actions = ['age', 'gender', 'race', 'emotion'],detector_backend='opencv',align=True)
    return arcalign,deepalign