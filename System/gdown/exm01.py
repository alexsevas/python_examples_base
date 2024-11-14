
# conda activate 3dpy39

import gdown

url = "https://drive.google.com/uc?id=1l_5RK28JRL19wpT22B-DY9We3TVXnnQQ"


output = "test.txt"
gdown.download(url, output)
