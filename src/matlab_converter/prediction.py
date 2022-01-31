
import tensorflow as tf
import numpy as np
import matlab.engine
import matplotlib.pyplot as plt

eng = matlab.engine.start_matlab()
#/home/kimyonghwan/2019_Final/src/LR0.0001_BATCHSIZE200_NHIDDEN200/model.ckpt.meta
saver = tf.train.import_meta_graph('../LR0.0001_BATCHSIZE200_NHIDDEN200/model.ckpt.meta') #modified
graph = tf.get_default_graph()
x = graph.get_tensor_by_name("Placeholder:0")
pred = graph.get_tensor_by_name("add:0")
plt.ion()

b = np.arange(0, 15000)
act = ["walk", "empty", "sitdown"]
# tmp = 0

#매틀랩으로 실시간 Prediction
while 1: #modified

    # tmp+=1
    k = 1
    t = 0
    #real time data input but now one data
    #/home/kimyonghwan/linux-80211n-csitool-supplementary/netlink/190528_data_2/190528_2_walking2.dat
    csi_trace = eng.read_bf_file('../190528_Dataset2/sitdown49.dat') #modified
    kkk = len(csi_trace)
    if len(csi_trace) < 500: #modified
        continue #modified
    #여기서부터 시작 그 위는 있을리 없어도 컨티뉴 한다. 혹시 모르니.
    ARR_FINAL = np.empty([0, 90], float)
    xx = np.empty([1, 500, 90], float)
    xx1 = np.empty([0], float)
    yy1 = np.empty([0], float)
    zz1 = np.empty([0], float)
    try:
        while (k <= 500): #실시간 데이터는 500줄만 읽어온다. 그게 아니고 그냥 시간임. #modified
            csi_entry = csi_trace[t] #여기 t를 이해해야겠네. matlab을 이해해야 한다.
            try:
                csi = eng.get_scaled_csi(csi_entry)
                A = eng.abs(csi)
                ARR_OUT = np.empty([0], float)

                ARR_OUT = np.concatenate((ARR_OUT, A[0][0]), axis=0)
                ARR_OUT = np.concatenate((ARR_OUT, A[0][1]), axis=0)
                ARR_OUT = np.concatenate((ARR_OUT, A[0][2]), axis=0)

                xx1 = np.concatenate((xx1, A[0][0]), axis = 0)
                yy1 = np.concatenate((yy1, A[0][1]), axis = 0)
                zz1 = np.concatenate((zz1, A[0][2]), axis = 0)
                ARR_FINAL = np.vstack((ARR_FINAL, ARR_OUT))
                k = k + 1
                t = t + 1

            except matlab.engine.MatlabExecutionError:
                print('MatlabExecutionError occured!!!')
                # break #modified
            xx[0] = ARR_FINAL
            break

    except ValueError:
        print('ValueError occured!!!')
        # continue #modified


    with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
        saver.restore(sess, '../LR0.0001_BATCHSIZE200_NHIDDEN200/model.ckpt.meta')
        n = pred.eval(feed_dict={x: xx})
        n2 = tf.argmax(n, 1)
        result = n2.eval()
        print(act[int(result)])
        sess.close()

