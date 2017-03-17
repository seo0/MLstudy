#자주쓰는 빈출 내장함수
#내가 만들고자 하는 프로그램이 이미 만들어져 있는지 보는게 중요하다.
#연습이 아닌이상 또 만드는건 불필요한 일이다.
#이미 만들어진 프로그램들은 테스트 과정을 수도 없이 많은 테스트과정을 거쳐서 검증되어있다.(특히, 파이썬 배포본)
#함수를 외우지는 못해도 그런함수가 있는지를 알면 나중에 찾아서 보면 된다. 혹은 이런 모듈에다가 다 모아두면 찾아보기 쉽다.

num = -3

print(abs(num))

print(all([1,2,3,4])) #true
print(all([1,2,3,4,0])) #false

print(any([1,2,3,0])) #하나라도 true 면 true

print(divmod(10,3))

print(chr(97)) #아스키 코드

#enumerate 주로 for문과 함께 쓰인다. 현재 index를 쉽게 알 수 있다.
for i,name in enumerate(["body","foo","bar"]):
    print(i,name)
#필터 코드 수를 줄이고 속도가 빠르다. 리턴값이 참인것들만 묶어 준다.
def positive(x):
    return x>0
print(list(filter(positive,[1,3,-2,0,-5,6])))
"""
#위에 코드랑 같은걸 함수로 짜면
def positive(numberList):
    result =[]
    for num in numberList:
        if(num>0):
            result.append(num)
    return result
"""

#id 는 reference (주소 값을 반환한다) 파이썬은 모든게 다 '객체'이다 리터럴이 아니다.
a=3
b=3
print(id(a))
print(id(b))
print(id(3))
"""
a=input("숫자를 넣으시오. ")
print(a)
"""

print(int('3'))#int로 변환하기.

class Person:
    pass
a= Person()
print(isinstance(a,Person)) #이쪽 클래스의 instant인지 판별, 코드가 매우 길어지고 복잡할때 사용.

#lamda 는 def으로 만들만큼 복잡하지 않을때 사용한다.(간결하게 사용 가능) 코드의 가독성을 높인다.
#def를 사용할수 없는 곳에서도 쓰인다.
sum = lambda a,b:a+b
print(sum(10,7))

myList = [lambda a,b:a+b,lambda a,b:a*b] #리스트 안에다가 함수를 넣을 수 있다. for 같은거 돌리때도 편할듯.
print(myList) #주소값을 반환한다.
print(myList[0])
print(myList[0](3,4))
#길이 반환
num = list(range(1,10))
print(len(num))

print(list("python"))

#map 함수와 반복 가능한 자료형을 입력 받는다.
def two_times(x):return x*2
print(map(two_times,[1,2,3,4])) #리스트로 안자르면 통채로 인식한다(주소값으로)
print(list(map(two_times,[1,2,3,4])))
#lambda랑 합쳐서 이렇게도 쓴다. 이게 프로그램 속도 때문에 이렇게 한다.
print(list(map(lambda a:a*2,[1,2,3,4])))

print(max([1,2,3,4,5,6]))
print(min([1,2,3,4,5,6]))

print(pow(3,4))

print(list(range(4,10)))
print(list(range(4,10,2)))#간격이 2씩
num = list(range(1,10))
print(num)

print(sorted([3,1,2,10,20003,5,7]))
#sorted 는 반환값이 있는데
a = [1,10,3,4,500,3]
result = a.sort()
print(result)
print(a) #반환하지 않고 a 자체가 바뀜

#데이터 input을 할때 자료형이 안맞으면 안돌아가는 경우가 많다. 이럴때 type으로 테스트를 해서 맞는 데이터를 넣거나, 맞는 데이터로 자료형을 바꾼다.
print(type(a))

#데이터 전처리할때 좋다.
print(list(zip([1,2,3],[4,5,6]))) #동일한 개수로 묶어준다. 각 list의 첫자리들끼리 묶는다.
print(list(zip([1,2],[3,4],[5,6])))


