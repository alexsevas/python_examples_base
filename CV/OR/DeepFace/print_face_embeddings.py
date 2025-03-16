# conda activate deepface39

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

#embeddings
embedding_objs = DeepFace.represent(
  img_path = "D:\\AI_DATA\\Faces\\Elon_Musk.png",
  model_name = models[7],
)
print (embedding_objs)