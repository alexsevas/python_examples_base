# первый запуск:
# 24-11-13 14:04:49 - vgg_face_weights.h5 will be downloaded...
# Downloading...
# From: https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5
# To: C:\Users\A43X\.deepface\weights\vgg_face_weights.h5

# conda activate 3dpy39

from deepface import DeepFace
from open3d.examples.visualization.draw import actions

#import dlib

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

#print ("dlib.DLIB_USE_CUDA = ", dlib.DLIB_USE_CUDA)

#face verification
result = DeepFace.verify(
  img1_path = "Elon_Musk.png",
  img2_path = "Elon_Musk_blue_bg.png",
  model_name = models[0],
)
print (result)

'''
#face recognition
dfs = DeepFace.find(
  img_path = "Elon_Musk.png",
  db_path = "C:/workspace/my_db",
  model_name = models[1],
)
print (dfs)


#embeddings
embedding_objs = DeepFace.represent(
  img_path = "Elon_Musk.png",
  model_name = models[2],
)
print (embedding_objs)
'''
# Facial Attribute Analysis
objs = DeepFace.analyze(
  img_path = "Putin.png",
  actions = ['age', 'gender', 'race', 'emotion'],
)
print(objs)