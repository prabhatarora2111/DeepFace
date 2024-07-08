from deepface import DeepFace
import cv2


img2 = cv2.imread("girlphoto.jpeg")
analysis = DeepFace.analyze(img2)
analysis
