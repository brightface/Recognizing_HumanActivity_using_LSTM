import numpy as np
import tensorflow as tf
from crossvali_input import csv_import, DataSet

# ARR_FINAL = np.empty([1, 4], float) #np.empty 는 0을 의미한다. 또한 0에 가까울수도 있는 쓰레기 값이 들어간다.
# #앞자리는 차원수 뒷자리는 개수. 기본 1차원 배열이기 때문에 [1,4] 하면 2차원 배열로 4개가 들어간다.
# xx = np.empty([1, 500, 90], float) #이 뜻은 그러면 2차원 500행 90 칸 이네
# print(xx)
#
# xx1 = np.empty(0, float)
# yy1 = np.empty([0], float)
# zz1 = np.empty([0], float)
# print(xx1)
# print(np.empty([0, 90], float))
# print(ARR_FINAL)

#gpu 사용한다.
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
# log_device_placement을 True로 설정하여 세션을 만듭니다.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# op를 실행합니다.
print(sess.run(c))

if __name__ == "__main__":
    csv_import()