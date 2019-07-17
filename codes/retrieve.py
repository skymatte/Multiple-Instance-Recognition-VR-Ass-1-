import cv2
import numpy as np 
import os
import pickle
###TO Save SIFT DEscriptors as packages
def save_obj(obj, name ):
    with open(name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name, 'rb') as f:
        return pickle.load(f)
def Read_Vectorize(path):
    """
    - returns  a dictionary of all files with key as the data name and value as sift desciptors
    - also return the total no. of files
    """
    imlist = {}
    desc_lis = [[]]
    count = 0
    for each in os.listdir(path):
        print (" #### Reading image category ", each, " ##### ")
        imlist[each] = {}
        dir=os.path.join(path,each)
        for imfi in os.listdir(dir):
            imfile=os.path.join(dir,imfi)
            print ("Reading file ", imfi)
            im = cv2.imread(imfile, 0)
            keypoints,descriptors = cv2.xfeatures2d.SIFT_create().detectAndCompute(im,None)
            imlist[each][imfi]=(descriptors)
            desc_lis.append(descriptors)
            count +=1 
    return [imlist, count,desc_lis]
imlist={}
imlist,count,desc_lis = Read_Vectorize("../Train/")
#save_obj(imlist, "Train")
s2=[]
s3=[]
names=[]
for k in list(imlist):
    for j in list(imlist[k]):
        names.append([k,j])
        s3.append(j);
        for i in j:
            print(len(i))
            s2.append(i)
save_obj(imlist, "image.sift")
print(len(s2))
j= np.vstack(s2)
print(len(j))
np.save("Tfkmn", j)
i=np.vstack(s3)
np.save("tfrbof",i)
