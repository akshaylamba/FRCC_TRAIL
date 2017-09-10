import numpy
import os 
import pandas



path="data/WBC_ANNOTATION_FASTER_RCNN/VOC2012/JPEGImages/"


dirs = os.listdir( path )
ffile=[]
# This would print all the files and directories
for file in dirs:
	ffile.append(file[:-4])


file_name = r'trainval.txt'
with open(file_name, 'wb') as x_file:
	for i in ffile:	
		x_file.write(i+"\n")


