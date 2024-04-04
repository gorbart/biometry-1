import cv2
from mtcnn import MTCNN

detector = MTCNN()

def preprocess_image(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = detector.detect_faces(img_rgb)

    if len(results) == 0:
        return img

    bounding_box = results[0]['box']
    x, y, w, h = bounding_box
    face = img_rgb[y:y+h, x:x+w]
    aligned_face = cv2.resize(face, (152, 152))

    return aligned_face