#jump to python 코드 기본코드
a= "life is too short"
a=a.split()
print(a)
b="a:b:c:d"
b=b.split(":")
print(b)
print("hello world {STR}".format(STR = a)) #헷갈리지 말라고
aaa = "hi"
#정렬
print("{0:<10}rkskek".format(aaa))
print("{0:>10}rkskek".format(aaa))
print("{0:^10}rkskek".format(aaa))
#소수점 표현 이런건 찾아가면서 하면 된다.
y=3.141592
print("{0:0.4f}".format(y))

#첫번째 시간 ㅣist의 인덱싱이랑 slice에대해 알려준다.
#리스트 삭제하기.
a=[1,2,3,4,5,6,7,8,9,10]
a[1:3]=[]
print(a)

del a[5]
print(a)
a.append(1000)
print(a)
a = a.sort()
print(a)

#tuple과 list의 차이가 뭘까? -> tuple은 상수이다. 즉, 프로그램내에서 절대 바뀌지 않는것은 프로그램 안전도를 높이기 위해 튜플로 사용한다.
t1 = (1,2,3,4)
print(t1)

#딕셔너리 자료형 hash mapping  (key와 value가 있는 관계)

a={"name":"길영재","phone":"010-8331-8284"}
print(a)
print(a.keys())
print(a.items())
print(a.values())
print(a.get("name1"))#a["key"]는 없는거면 에러가 뜨는데 get은 없어도 none이라고 반환한다
print('name'in a.keys()) #판별할때 사용한다.

#set 자료형 중복 허용x 순서가 없다.(indexing을 할수가 없다)
s1 = set([1,2,3,4,5,5])
print(s1)

a,b = ('python','life')
print(a)
print(b)

#가장 중


# 요한 복사!
a=[1,2,3]
b=a
print(a)
print(b)
a[1]= a[1]+10000
print(a)
print(b)
print(b is a)
#우리는 a만 더하고 싶은데 b도 더해졌다. 이렇면 안된다.
#'같은 객체'를 가르킨다.
#어떻게 해결해야 하나?

a=[1,2,3,4,5]
b=a[:]
print(a)
print(b)
a[1]= a[1]+10000
print(a)
print(b)
print(b is a) #test
#영향을 미치지 않는다.

print(1 in [1,2,3])
print(1 not in [1,2,3])

a = [1,2,3,4]
#이런 식으로도 간단하게 표현 가능하다.
result = [num*3 for num in a]
print(result)
result=[]
for num in a:
    result.append(num*3)
print(result)
#파이썬에서의 for의 특징은 indexing 접근도 가능하지만 그자체로 접근이 가능하다.(c++과 자바와 다른특징)

#file input and output
f=open("new.txt",'w')
for i in range(1,10):
    data = "{0} line \n".format(i)
    f.write(data)
f.close()
#gksgk한줄씩 읽는다.
f=open('new.txt','r')
while True:
    line = f.readline()
    if not line : break
    print(line,end='') #using end
f.close()

#lines가 되면 list로 읽는다.
f=open('new.txt','r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#read는 전체를 하나로 읽는다.
f=open('new.txt','r')
data = f.read()
print(data)
f.close()

#'w'로 열면 기존에 있던 파일들이 다사라진다. 추가만 하고싶으면 'a'를 써야한다.
#[파일 입출력] 입력을 한번에 하고 반환까지 해준다 편리함.
with open("foo.txt","w") as f:
    f.write("life is too sort, you need python")

class calculator:
    def __init__(self):
        self.first=0
        self.second =0
    def setNum(self,first,second):
        self.first = first
        self.second = second
    def mul(self):
        return self.first+self.second
    def minus(self):
        return self.first-self.second
    def multiple(self):
        return self.first*self.second
    def divide(self):
        if(self.second ==0):
            return "분모가 0"
        else:
            return self.first/self.second

equation1 = calculator()
equation1.setNum(10,5)
print(equation1.mul())
print(equation1.divide())
print(equation1.minus())
print(equation1.multiple())


a = ["apple","banana","pineapple","root"]
#해당 리스트의 index와 value를 한번에 알 수있다.
for i,fruit in enumerate(a):
    print(i," and ",fruit)

b=["사과","바나나","파인애플","루트"]
#zip을 쓸때는 두개의 리스트의 길이가 같아야한다. 길이가 다르면 나머지는 잘라낸다.
for i,j in zip(a,b):
    print(i,"and",j)

