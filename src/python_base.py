#n진법을 10진법으로 변환
b = str(11)
n = 2
print(int(b,n))

#10진법을 n 진법으로 변환시는?
#이건 짜야하나 근데 2진법 8진법 16진법은 있다.
a = 11
print(str(bin(a))[2:])
#oct 8
#hex 16

t = [1,5,4,3,2]

for i,v in enumerate(t,start=2):
    print(i,v) # 인덱스를 자기 맘대로 수정할수 있다. 왜 쓰는겨?
p = ["A","BC"]
print(list(zip(t,p)))
