import json
import scipy.io as scio
import os
import matplotlib.pyplot as plt
import scipy.signal
import numpy as np,numpy
import scipy.ndimage
from sklearn.decomposition import PCA
import math
import pywt
from matplotlib.font_manager import FontProperties
import gzip
import csv
import glob
import pandas as pd
#차원축소를 할수있다.
#차원축소가능한 이유 - 정보를 몰아준다. 한쪽으로, 독립이라는 가정하에.
#상대적으로 pc1이 pc2보다 더 중요하다. (그려보면 알수있다.) 어떤 축이 중요한가?

def readCsiAmp(filename, antenna, subwave, length):
    try:
        mat = scio.loadmat(filename)
    except:
        print(filename + ' meets error when read')
        return {}

    # print(mat)
    csi = mat['csi'][0][0][1][0][antenna]
    label = mat['csi'][0][0][2][0][0]

    arr = []
    for data in csi:
        arr.append(np.absolute(data[subwave]))
    l = len(arr)

    if l < length:# error data
        print(filename + ' meets error in array length')
        return {}

    # arr = scipy.signal.savgol_filter(arr, 19, 11)

    z = length / l

    arr = scipy.ndimage.zoom(arr, z, )

    arr = arr.tolist()

    d = {}
    d['arr'] = arr
    d['label'] = str(label)

    # print(d)
    return d

def readCsiPhase_Diff(filename, antenna, subwave, length): # diff after calculate the angle
    try:
        mat = scio.loadmat(filename)
    except:
        print(filename + ' meets error when read')
        return {}

    # print(mat)

    csi = mat['csi'][0][0][1][0]
    label = mat['csi'][0][0][2][0][0]

    if antenna == 0:
        an1 = 0
        an2 = 1
    elif antenna == 1:
        an1 = 0
        an2 = 2
    elif antenna == 2:
        an1 = 1
        an2 = 2

    phase1 = []
    for data in csi[an1]:
        phase1.append(np.angle(data[subwave]))

    phase2 = []
    for data in csi[an2]:
        phase2.append(np.angle(data[subwave]))
    
    phase1 = np.array(phase1)
    phase2 = np.array(phase2)

    arr = phase1 - phase2

    l = len(arr)

    if l < length:# error data
        print(filename + ' meets error in array length')
        return {}

    # arr = scipy.signal.savgol_filter(arr, 19, 11)

    z = length / l

    arr = scipy.ndimage.zoom(arr, z, )

    arr = arr.tolist()
    if math.isnan(arr[0]):
        print(filename + ' meets nan error')
        return {}

    d = {}
    d['arr'] = arr
    d['label'] = str(label)

    # print(d)
    return d

def readCsiPhase_Diff2(filename, antenna, subwave, length): # diff before calculate the angle
    try:
        mat = scio.loadmat(filename)
    except:
        print(filename + ' meets error when read')
        return {}

    # print(mat)

    csi = mat['csi'][0][0][1][0]
    label = mat['csi'][0][0][2][0][0]

    csi0 = csi[0]
    csi1 = csi[1]
    csi2 = csi[2]
    csidiff0 = csi0 - csi1
    csidiff1 = csi0 - csi2
    csidiff2 = csi1 - csi2

    if antenna == 0:
        csidiff = csidiff0
    elif antenna == 1:
        csidiff = csidiff1
    elif antenna == 2:
        csidiff = csidiff2

    arr = []
    for data in csidiff:
        arr.append(np.angle(data[subwave]))


    l = len(arr)

    if l < length:# error data
        print(filename + ' meets error in array length')
        return {}

    # arr = scipy.signal.savgol_filter(arr, 19, 11)

    z = length / l

    arr = scipy.ndimage.zoom(arr, z, )

    arr = arr.tolist()
    if math.isnan(arr[0]):
        print(filename + ' meets nan error')
        return {}

    d = {}
    d['arr'] = arr
    d['label'] = str(label)

    # print(d)
    return d

def readCsiPhase_Div(filename, antenna, subwave, length):
    try:
        mat = scio.loadmat(filename)
    except:
        print(filename + ' meets error when read')
        return {}

    # print(mat)

    csi = mat['csi'][0][0][1][0]
    label = mat['csi'][0][0][2][0][0]
    
    csi0 = csi[0]
    csi1 = csi[1]
    csi2 = csi[2]
    csidiv0 = csi0 / csi1
    csidiv1 = csi0 / csi2
    csidiv2 = csi1 / csi2
    
    if antenna == 0:
        csidiv = csidiv0
    elif antenna == 1:
        csidiv = csidiv1
    elif antenna == 2:
        csidiv = csidiv2

    arr = []
    for data in csidiv:
        arr.append(np.angle(data[subwave]))
    l = len(arr)

    if l < length:# error data
        print(filename + ' meets error in array length')
        return {}

    # arr = scipy.signal.savgol_filter(arr, 19, 11)

    z = length / l

    arr = scipy.ndimage.zoom(arr, z, )

    arr = arr.tolist()
    if math.isnan(arr[0]):
        print(filename + ' meets nan error')
        return {}

    d = {}
    d['arr'] = arr
    d['label'] = str(label)

    # print(d)
    return d

def readCsiAmp_Div(filename, antenna, subwave, length):
    try:
        mat = scio.loadmat(filename)
    except:
        print(filename + ' meets error when read')
        return {}

    # print(mat)

    csi = mat['csi'][0][0][1][0]
    label = mat['csi'][0][0][2][0][0]
    
    csi0 = csi[0]
    csi1 = csi[1]
    csi2 = csi[2]
    csidiv0 = csi0 / csi1
    csidiv1 = csi0 / csi2
    csidiv2 = csi1 / csi2
    
    if antenna == 0:
        csidiv = csidiv0
    elif antenna == 1:
        csidiv = csidiv1
    elif antenna == 2:
        csidiv = csidiv2

    arr = []
    for data in csidiv:
        arr.append(np.absolute(data[subwave]))
    l = len(arr)

    if l < length:# error data
        print(filename + ' meets error in array length')
        return {}

    # arr = scipy.signal.savgol_filter(arr, 19, 11)

    z = length / l

    arr = scipy.ndimage.zoom(arr, z, )

    arr = arr.tolist()
    if math.isnan(arr[0]):
        print(filename + ' meets nan error')
        return {}

    d = {}
    d['arr'] = arr
    d['label'] = str(label)

    # print(d)
    return d

def readAmp30(filename, antenna):
    try:
        mat = scio.loadmat(filename)
    except:
        print(filename + ' meets error when read')
        return {}

    # print(mat)
    csi = mat['csi'][0][0][1][0][antenna]
    label = mat['csi'][0][0][2][0][0]

    amp30 = []
    for data in csi:
        amp30.append(np.absolute(data))
    
    d = {}
    d['amp30'] = amp30
    d['label'] = str(label)
    return d

def read2AnPCAFive(filename, antenna, length):
    if antenna == 0:
        d0 = readAmp30(filename, 0)
        d1 = readAmp30(filename, 1)
    elif antenna == 1:
        d0 = readAmp30(filename, 0)
        d1 = readAmp30(filename, 2)
    elif antenna == 2:
        d0 = readAmp30(filename, 1)
        d1 = readAmp30(filename, 2)

    label = int(d0['label'])

    amp30_0 = np.array(d0['amp30'])
    if len(amp30_0) == 0:
        print(filename + ' meets error in array length')
        return {}
    amp30_1 = np.array(d1['amp30'])
    amp60 = np.concatenate((amp30_0, amp30_1), axis=1)

    
    #print(amp60.shape)
    
    l = len(amp60)

    #print(amp60.shape)

    pca = PCA(n_components=5)   
    pca.fit(amp60)                  
    arr5 = pca.fit_transform(amp60).T
    #print(arr5.shape)
    #print(pca.explained_variance_ratio_) 
    
    d = {}

    for i in range(5):
        arr = arr5[i]

        z = length / l

        arr = scipy.ndimage.zoom(arr, z, )

        arr = arr.tolist()

        arrname = 'arr' + str(i)
        d[arrname] = arr
    d['label'] = str(label)

    return d
    

"""   try:
    SKIPROW = 2 #Skip every 2 rows -> overlap 800ms to 600ms  (To avoid memory error)
    num_lines = sum(1 for l in open(filename))
    skip_idx = [x for x in range(1, num_lines) if x % SKIPROW !=0]
    mat = np.array(pd.read_csv(filename, header=None, skiprows = skip_idx))
    #mat = scio.loadmat(filename)
    except:
    print(filename + ' meets error when read')
    return {}
    """
def readCsiAmp_PCA(filename, antenna, length):
    
 
    SKIPROW = 2
    
    num_lines = sum(1 for l in open(filename))
    skip_idx = [x for x in range(1, num_lines) if x % SKIPROW !=0]
    mat = np.array(pd.read_csv(filename, header=None))
    #, skiprows = skip_idx
    #print(mat)
    #csi = mat['csi'][0][0][1][0][antenna]
    #label = mat['csi'][0][0][2][0][0]
    csi = mat
#label = mat['test_label']

    amp30_1 = []
    amp30_2 = []
    amp30_3 = []
    amp30 = []
    for data in csi:
        #amp30_1.append(np.absolute(data[0:29]))
        #amp30_2.append(np.absolute(data[30:59]))
        #amp30_3.append(np.absolute(data[60:89]))
        amp30.append(np.absolute(data))
    #amp30_1 = np.array(amp30_1)
    #amp30_2 = np.array(amp30_2)
    #amp30_3 = np.array(amp30_3)
    amp30 = np.array(amp30)
#print(len(amp30_1))  마지막 한줄을 자꾸 빼먹네... 아마 2줄에 한개씩 빼도록 설정..
#print(amp30_1)
#   print(amp30_2)
#   print(amp30_3)
    l = len(amp30)

    if l < length:# error data
        print('length is:'+ len(amp30))
        print(filename + ' meets error in array length')
        return {}

    #print(amp30.shape)

    pca = PCA(n_components=1)
    pca.fit(amp30)
    arr = pca.fit_transform(amp30)
    arr = pca.inverse_transform(arr)
    #pca.fit(amp30_1)
    #arr1 = pca.fit_transform(amp30_1)
    #arr1 = pca.inverse_transform(arr1)
#print(arr1)
    #pca.fit(amp30_2)
    #arr2 = pca.fit_transform(amp30_2)
    #arr2 = pca.inverse_transform(arr2)
#print(arr2)
    #pca.fit(amp30_3)
    #arr3 = pca.fit_transform(amp30_3)
    #arr3 = pca.inverse_transform(arr3)
#print(arr3)
    #print(arr.shape)
    #print(pca.explained_variance_ratio_)
    #arr = np.hstack((arr1,arr2,arr3)) # 3개의 행렬을 가로로 붙인다
# arr = np.squeeze(arr)
#print(arr.shape(0))

    

#z = length / l

#   arr = scipy.ndimage.zoom(arr, z, )

#   arr = arr.tolist()

#d = {}
#   d['arr'] = arr
#   d['label'] = str(label)
    d = np.round(arr,2)

    return d

def readCsiAmp_PCAFive(filename, antenna, length):
    try:
        mat = scio.loadmat(filename)
    except:
        print(filename + ' meets error when read')
        return {}

    # print(mat)
    csi = mat['csi'][0][0][1][0][antenna]
    label = mat['csi'][0][0][2][0][0]

    amp30 = []
    for data in csi:
        amp30.append(np.absolute(data))
    amp30 = np.array(amp30)
    
    l = len(amp30)

    if l < length:# error data
        print(filename + ' meets error in array length')
        return {}

    #print(amp30.shape)

    pca = PCA(n_components=5)   
    pca.fit(amp30)                  
    arr5 = pca.fit_transform(amp30).T
    #print(arr.shape)
    #print(pca.explained_variance_ratio_) 
    
    d = {}

    for i in range(5):
        arr = arr5[i]

        z = length / l

        arr = scipy.ndimage.zoom(arr, z, )

        arr = arr.tolist()

        arrname = 'arr' + str(i)
        d[arrname] = arr
    d['label'] = str(label)

    return d
    
    
def cwt(data):
    sampling_rate = len(data)
    wavename = 'cgau8'
    totalscal = 65
    fc = pywt.central_frequency(wavename)
    cparam = 2 * fc * totalscal
    scales = cparam / np.arange(totalscal, 1, -1)
    [cwtmatr, frequencies] = pywt.cwt(data, scales, wavename, 1.0 / sampling_rate)

    # print(frequencies)
    t = np.arange(0, 1.0, 1.0 / sampling_rate)
    plt.figure(figsize=(8, 4))
    plt.subplot(211)
    plt.plot(t, data)
    plt.xlabel(u"time(s)")
    plt.subplot(212)
    plt.contourf(t, frequencies, abs(cwtmatr))
    plt.ylabel(u"Freq(Hz)")
    plt.xlabel(u"time(s)")
    plt.subplots_adjust(hspace=0.4)
    plt.show()

    
    return cwtmatr

def readCsiAmpCwt(filename, antenna, subwave, length):
    d = readCsiAmp(filename, antenna, subwave, length)
    if len(d) == 0:
        return {}
    arr = d['arr']
    label = d['label']
    cwtmatr = np.absolute(cwt(arr)).tolist()
    d1 = {}
    d1['arr'] = cwtmatr
    d1['label'] = label
    return d1

def readCsiAmp_DivCwt(filename, antenna, subwave, length):
    d = readCsiAmp_Div(filename, antenna, subwave, length)
    if len(d) == 0:
        return {}
    arr = d['arr']
    label = d['label']
    cwtmatr = np.absolute(cwt(arr)).tolist()
    d1 = {}
    d1['arr'] = cwtmatr
    d1['label'] = label
    return d1

def readCsiPhase_DiffCwt(filename, antenna, subwave, length):
    d = readCsiPhase_Diff(filename, antenna, subwave, length)
    if len(d) == 0:
        return {}
    arr = d['arr']
    label = d['label']
    cwtmatr = np.absolute(cwt(arr)).tolist()
    d1 = {}
    d1['arr'] = cwtmatr
    d1['label'] = label
    return d1

def readCsiPhase_DivCwt(filename, antenna, subwave, length):
    d = readCsiPhase_Div(filename, antenna, subwave, length)
    if len(d) == 0:
        return {}
    arr = d['arr']
    label = d['label']
    cwtmatr = np.absolute(cwt(arr)).tolist()
    d1 = {}
    d1['arr'] = cwtmatr
    d1['label'] = label
    return d1

if __name__ == '__main__':
    #read2AnPCAFive('./diffraction_nk_4_dengshan_1_4_4.mat', 1, 64)
    
    #/Users/taegi/Downloads/2018-cap1-8-master/Wifi_Activity_Recognition-master/input_files
    d = readCsiAmp_PCA('/Users/taegi/Downloads/2018-cap1-8-master/Wifi_Activity_Recognition-master/input_files/xx_1000_60_walk.csv', 3, 90) #
    with open('xx_1000_60_walk_PCAfiltered.csv', "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(d)
    #scipy.io.savemat('testAfterPca.mat', d) # pca로 처리후 저장

    # d = readCsiAmp_PCA('../bachelor/indata/diffraction_nk_4_dengshan_1_4_4.mat', 1, 64)
    #arr = d['arr']
    #cwtmatr, frequencies = cwt(arr) # continous wavelet transform
#print(cwtmatr.shape, frequencies.shape)
    
