import glob, os
from math import *
from tqdm import tqdm
import shutil

# input dirs
input_folders = [
    'flower_photos/daisy',
    'flower_photos/dandelion',
    'flower_photos/roses',
    'flower_photos/sunflowers',
    'flower_photos/tulips'
]

# base out dir
BASE_DIR_ABSOLUTE = "C:\\PROJECTS\\alexsevas_projects\\python_examples_base\\CV_Yolo8\\"
OUT_DIR = './datasets/flowers_prepared/'

# out dirs
OUT_TRAIN = OUT_DIR + 'train/'
OUT_VAL = OUT_DIR + 'test/'

# config
coeff = [80, 20] # train/val
exceptions = ['classes'] # .txt files that will be excluded

# prepare
if int(coeff[0]) + int(coeff[1]) > 100:
    print("Coeff can't exceed 100%/")
    exit(1)

def chunker (seq, size):
    return (seq[pos:pos +size] for pos in range(0, len(seq), size))

# print some info
print(f"Preparing images data by {coeff[0]}/{coeff[1]} rule")
print(f"Source folders: {len(input_folders)}")
print("Gathering data ...")

# collect in
source = {}
for sf in input_folders:
    source.setdefault(sf, [])

    os.chdir(BASE_DIR_ABSOLUTE)
    os.chdir(sf)

    for filename in glob.glob("*.jpg"):
        source[sf].append(filename)

# separate by train/val rule
train = {}
val = {}
for sk, sv in source.items():
    chunks = 10
    train_chunk = floor(chunks * (coeff[0] / 100))
    val_chunk = chunks - train_chunk

    train.setdefault(sk, [])
    val.setdefault(sk, [])
    for item in chunker(sv, chunks):
        train[sk].extend(item[0:train_chunk])
        val[sk].extend(item[train_chunk:])

# copy source to prepared
train_sum = 0
val_sum = 0

for sk, sv in train.items():
    train_sum += len(sv)

for sk, sv in val.items():
    val_sum += len(sv)

# print some info
print(f"\nOverall TRAIN images count: {train_sum}")
print(f"Overall TEST images count: {val_sum}")

os.chdir(BASE_DIR_ABSOLUTE)
print("\nCopying TRAIN source items to prepared folder ...")
for sk, sv in tqdm(train.items()):
    for item in tqdm(sv):
        imgfile_source = sk +item
        imgfile_dest = OUT_TRAIN + sk.split('/')[-2] + '/'

        os.makedirs(imgfile_dest, exist_ok=True)
        shutil.copyfile(imgfile_source, imgfile_dest + item)

os.chdir(BASE_DIR_ABSOLUTE)
print("\nCopying VAL source items to prepared folder ...")
for sk, sv in tqdm(val.items()):
    for item in tqdm(sv):
        imgfile_source = sk + item
        imgfile_dest = OUT_VAL + sk.split('/')[-2] + '/'

        os.makedirs(imgfile_dest, exist_ok=True)
        shutil.copyfile(imgfile_source, imgfile_dest + item)

# print some info
print("\nDONE!")
