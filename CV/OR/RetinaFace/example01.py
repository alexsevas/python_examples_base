# conda activate 3dpy39

# первый запуск:
# 24-11-12 21:41:57 - retinaface.h5 will be downloaded from the url
# https://github.com/serengil/deepface_models/releases/download/v1.0/retinaface.h5
# Downloading...
# From: https://github.com/serengil/deepface_models/releases/download/v1.0/retinaface.h5
# To: C:\Users\A43X\.deepface\weights\retinaface.h5

from retinaface import RetinaFace
resp = RetinaFace.detect_faces("fe.jpg")
print (resp)