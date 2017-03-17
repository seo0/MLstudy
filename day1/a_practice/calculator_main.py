#클래스 메인 2번째줄이 클래스를 import하는법
from a_practice.calculator import calculator

if __name__ == '__main__':
    a = calculator()
    a.setNum(10,3)
    print(a.mul())

print("hello world")

