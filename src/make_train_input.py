import numpy as np
import csv
import glob
import os

window_size = 1000
threshold = 60
slide_size = 200 #less than window_size!!!

def dataimport(path1, path2):
	xx = np.empty([0,window_size,90],float)
	yy = np.empty([0, 4], float) #### given matrix is a number of class

	###Input data###
	#data import from csv
	input_csv_files = sorted(glob.glob(path1))
	for f in input_csv_files:
		print("input_file_name=",f)
		data = [[ float(elm) for elm in v] for v in csv.reader(open(f, "r"))]
		tmp1 = np.array(data)
		x2 = np.empty([0,window_size,90],float)

		#data import by slide window
		k = 0
		while k <= (len(tmp1) + 1 - 2 * window_size):
			x = np.dstack(np.array(tmp1[k:k+window_size, 0:90]).T)
			x2 = np.concatenate((x2, x),axis=0)
			k += slide_size

		xx = np.concatenate((xx,x2),axis=0)
	xx = xx.reshape(len(xx),-1)

	###Annotation data###
	#data import from csv
	annotation_csv_files = sorted(glob.glob(path2))
	for ff in annotation_csv_files:
		print("annotation_file_name=",ff)
		ano_data = [[ str(elm) for elm in v] for v in csv.reader(open(ff,"r"))]
		tmp2 = np.array(ano_data)

		#data import by slide window
		y = np.zeros(((len(tmp2) + 1 - 2 * window_size)//slide_size+1, 4)) #### the last parameter should be the number of class
		k = 0
		while k <= (len(tmp2) + 1 - 2 * window_size):
			y_pre = np.stack(np.array(tmp2[k:k+window_size]))
			walking =0 #modified
			laydown = 0
			sit = 0
			for j in range(window_size):
				if y_pre[j] == "walk": #modified
					walk += 1
				elif y_pre[j] == "laydown": #modified
					laydown += 1
				elif y_pre[j] == "sit": #modified
					sit += 1

			if walking > window_size * threshold / 100: #modified
				y[k // slide_size, :] = np.array([0, 1, 0, 0])
			elif laydown > window_size * threshold / 100: #modified
				y[k // slide_size, :] = np.array([0, 0, 1, 0])
			elif empty > window_size * threshold / 100: #modified
				y[k // slide_size, :] = np.array([0, 0, 0, 1])
			else:
				y[k//slide_size,:] = np.array([2,0,0,0]) # should not be deleted
			k += slide_size
		yy = np.concatenate((yy, y),axis=0)
	print(xx.shape,yy.shape)
	return (xx, yy)


#### Main ####
if not os.path.exists("input_files/"):
	os.makedirs("input_files/")

for i, label in enumerate (["walk", "laydown", "sit"]):
	
	filepath1 = "./190528_Dataset2/190528_" + str(label) + "*.csv"
	filepath2 = "./190528_Dataset2/annotation_" + str(label) + "*.csv"
	
	outputfilename1 = "./input_files/xx_" + str(window_size) + "_" + str(threshold) + "_" + label + ".csv"
	outputfilename2 = "./input_files/yy_" + str(window_size) + "_" + str(threshold) + "_" + label + ".csv"
	
	x, y = dataimport(filepath1, filepath2)
	with open(outputfilename1, "w") as f:
		writer = csv.writer(f, lineterminator="\n")
		writer.writerows(x)
	with open(outputfilename2, "w") as f:
		writer = csv.writer(f, lineterminator="\n")
		writer.writerows(y)
	print(label + "finish!")