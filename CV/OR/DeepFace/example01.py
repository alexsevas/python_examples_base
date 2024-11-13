# первый запуск:
# 24-11-13 14:04:49 - vgg_face_weights.h5 will be downloaded...
# Downloading...
# From: https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5
# To: C:\Users\A43X\.deepface\weights\vgg_face_weights.h5

# conda activate 3dpy39

from deepface import DeepFace

models = [
  "VGG-Face",
  "Facenet",
  "Facenet512",
  "OpenFace",
  "DeepFace",
  "DeepID",
  "ArcFace",
  "Dlib",
  "SFace",
  "GhostFaceNet",
]

result = DeepFace.verify(
  img1_path = "Elon_Musk.png",
  img2_path = "Elon_Musk_blue_bg.png",
  model_name = models[0],
)

print (result)
