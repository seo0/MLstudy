#stor the variable
print("=====problem1====")
a =[100,200,300,400,500]
print(a)
num = 100
print(num)
date = "13일"
print("오늘 {0} 나는 {1}원이 있다.".format(date,num))

Grade = {"A+":4.3,"B+":3.3,"C+":2.3}
print(Grade)
print(Grade.keys())
print(Grade.values())

#for 구문
for i in range(5):
    print(i)

for i in range(len(a)):
    print(a[i])

for number in a:
    print(number)


#while 구문
i=5
while(i>0):
    print(i)
    i=i-1

num=100
if(num>0):
    print("양수")
elif(num==0):
    print("0")
else:
    print("음수")
print("====problem2=======")
class pocketmon:
    def __init__(self, name, attribute):
        self._name = name
        self._attribute = attribute
        # complete with initialisation of self._student_name and self._student_id
        pass

    def get_name(self):
        """ Return the name of the student """
        return self._name

    def get_attribute(self):
        """ Return the name of the student """
        return self._attribute

    def set_attribute(self,attri):
        self._attribute=attri

if __name__ == '__main__':
    dog = pocketmon("피카츄","fire")
    print(dog.get_name())
    print(dog.get_attribute())
    dog.set_attribute("wind")
    print(dog.get_attribute())
