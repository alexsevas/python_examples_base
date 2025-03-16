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

#face verification
result = DeepFace.verify(
  img1_path = "D:\\AI_DATA\\Faces\\Elon_Musk.png",
  img2_path = "D:\\AI_DATA\\Faces\\Elon_Musk_blue_bg.png",
  model_name = models[0],
)
print (result)