#클래스

# 클래스는 왜 필요한가?
# 프로그래머들이 가장 많이 사용하는 프로그래밍 언어 중 하나인 C 언어에는 클래스가 없다.
# 이 말은 굳이 클래스가 없어도 프로그램을 충분히 만들 수 있다는 뜻이다.
# 파이썬으로 잘 만든 프로그램을 살펴보아도 클래스를 사용하지 않고 작성한 것들이 상당히 많다.
# 클래스는 지금까지 공부한 함수나 자료형처럼 프로그램 작성을 위해 꼭 필요한 요소는 아니다.

# 하지만 프로그램을 작성할 때 클래스를 적재적소에 사용하면 프로그래머가 얻을 수 있는 이익은 상당하다. 예제를 통해 한번 생각해 보자.

# 여러분 모두 계산기를 사용해 보았을 것이다.
# 계산기에 숫자 3을 입력하고 + 기호를 입력한 후 4를 입력하면 결괏값으로 7을 보여 준다.
# 다시 한 번 + 기호를 입력한 후 3을 입력하면 기존 결괏값 7에 3을 더해 10을 보여 준다. 
# 즉 계산기는 이전에 계산한 결괏값을 항상 메모리 어딘가에 저장하고 있어야 한다.

#이런 내용을 우리가 앞에서 익힌 함수를 이용해 구현해 보자. 계산기의 "더하기" 기능을 구현한 파이썬 코드는 다음과 같다.

result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

#이전에 계산한 결괏값을 유지하기 위해서 result 전역 변수(global)를 사용했다. 프로그램을 실행하면 예상한 대로 다음과 같은 결괏값이 출력된다.
3
7

# 그런데 만일 한 프로그램에서 2대의 계산기가 필요한 상황이 발생하면 어떻게 해야 할까?
# 각 계산기는 각각의 결괏값을 유지해야 하기 때문에 위와 같이 add 함수 하나만으로는 결괏값을 따로 유지할 수 없다.

# 이런 상황을 해결하려면 다음과 같이 함수를 각각 따로 만들어야 한다.

result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(4))

# 똑같은 일을 하는 add1과 add2 함수를 만들었고 각 함수에서 계산한 결괏값을 유지하면서 저장하는 전역 변수 result1, result2가 필요하게 되었다.

# 결괏값은 다음과 같이 의도한 대로 출력된다.

3
7
3
10

# 계산기 1의 결괏값이 계산기 2에 아무 영향을 끼치지 않음을 확인할 수 있다.
# 하지만 계산기가 3개, 5개, 10개로 점점 더 많이 필요해진다면 어떻게 해야 할까?
# 그때마다 전역 변수와 함수를 추가할 것인가?
# 여기에 빼기나 곱하기 등의 기능을 추가해야 한다면 상황은 점점 더 어려워질 것이다.

# 아직 클래스에 대해 배우지 않았지만, 위와 같은 경우에 클래스를 사용하면 다음과 같이 간단하게 해결할 수 있다.

# 다음 예시 클래스를 아직은 이해하지 못해도 좋다. 곧 자세하게 배울 것이다. 여기에서는 클래스 개념만 이해하면 된다.

class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self,num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#프로그램을 실행하면 함수 2개를 사용했을 때와 동일한 결과가 출력된다.

3
7
3
10

#Calculator 클래스로 만든 별개의 계산기 cal1, cal2(파이썬에서는 이것을 객체라고 부른다)가 각각의 역할을 수행한다.
# 그리고 계산기(cal1, cal2)의 결괏값 역시 다른 계산기의 결괏값과 상관없이 독립적인 값을 유지한다.
# 클래스를 사용하면 계산기 대수가 늘어나더라도 객체를 생성만 하면 되기 때문에 함수를 사용하는 경우와 달리 매우 간단해진다.
# 만약 빼기 기능을 더하려면 Calculator 클래스에 다음과 같은 빼기 기능 함수를 추가해 주면 된다.

#클래스의 이점은 단순히 이것만이 아니다. 하지만 이것 하나만으로도 "도대체 왜 클래스가 필요한 것일까?"라는 근본적인 물음에 대한 해답이 되었을 것이다.

# 클래스와 객체

# 과자를 만드는 과자 틀과 그것을 사용해 만든 과자이다.

# 과자 틀 → 클래스 (class)
# 과자 틀에 의해서 만들어진 과자 → 객체 (object)
# 여기에서 설명할 클래스는 과자 틀과 비슷하다. 클래스(class)란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면이고(과자 틀), 객체(object)란 클래스로 만든 피조물(과자 틀을 사용해 만든 과자)을 뜻한다.

# 클래스로 만든 객체에는 중요한 특징이 있다. 바로 객체마다 고유한 성격을 가진다는 것이다. 과자 틀로 만든 과자에 구멍을 뚫거나 조금 베어 먹더라도 다른 과자에는 아무 영향이 없는 것과 마찬가지로 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.

# 다음은 파이썬 클래스의 가장 간단한 예이다.

class Cookie:
    pass

# 위의 클래스는 아무 기능도 갖고 있지 않은 껍질뿐인 클래스이다.
# 하지만 이렇게 껍질뿐인 클래스도 객체를 생성하는 기능이 있다.
# "과자 틀"로 "과자"를 만드는 것처럼 말이다.

# 객체는 클래스로 만들며 1개의 클래스는 무수히 많은 객체를 만들어 낼 수 있다.
# 위에서 만든 Cookie 클래스의 객체를 만드는 방법은 다음과 같다.

a = Cookie()
b = Cookie()

#Cookie()의 결괏값을 돌려받은 a와 b가 바로 객체이다. 마치 함수를 사용해서 그 결괏값을 돌려받는 모습과 비슷하다.

# 사칙연산 클래스 만들기
# "백견(見)이 불여 일타(打)"라고 했다. 클래스를 직접 만들며 배워 보자.

# 여기에서는 사칙연산을 쉽게 해주는 클래스를 만들어 볼 것이다. 사칙연산은 더하기, 빼기, 나누기, 곱하기를 말한다.

# 클래스를 어떻게 만들지 먼저 구상하기
# 클래스는 무작정 만드는 것보다 클래스로 만든 객체를 중심으로 어떤 식으로 동작하게 할것인지 미리 구상을 한 후에 생각한 것들을 하나씩 해결하면서 완성해 나가는 것이 좋다.

# 사칙연산을 가능하게 하는 FourCal 클래스가 다음처럼 동작한다고 가정해 보자.

# 먼저 a = FourCal()를 입력해서 a라는 객체를 만든다.

# a = FourCal()

# 그런 다음 a.setdata(4, 2)처럼 입력해서 숫자 4와 2를 a에 지정해 주고

# a.setdata(4,2)

# a.add()를 수행하면 두 수를 합한 결과(4 + 2)를 돌려주고

# print(a.add())

# a.mul()을 수행하면 두 수를 곱한 결과(4 * 2)를 돌려주고

# print(a.mul())

# a.sub()를 수행하면 두 수를 뺀 결과(4 - 2)를 돌려주고

# print(a.sub())

# a.div()를 수행하면 두 수를 나눈 결과(4 / 2)를 돌려준다.

# print(a.div())

# 이렇게 동작하는 FourCal 클래스를 만드는 것이 바로 우리의 목표이다.

# 클래스 구조 만들기
# 자, 그러면 지금부터 앞에서 구상한 것처럼 동작하는 클래스를 만들어 보자.
# 제일 먼저 할 일은 a = FourCal()처럼 객체를 만들 수 있게 하는 것이다.
# 일단은 아무 기능이 없어도 되기 때문에 매우 간단하게 만들 수 있다.
# 다음을 따라 해 보자.

class FourCal:
    pass

# 우선 대화형 인터프리터에서 pass란 문장만을 포함한 FourCal 클래스를 만든다.
# 현재 상태에서 FourCal 클래스는 아무 변수나 함수도 포함하지 않지만 우리가 원하는 객체 a를 만들 수 있는 기능은 가지고 있다.
# 확인해 보자.

# ※ pass는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 주로 사용한다.

a = FourCal()
type(a)

# 위와 같이 a = FourCal()로 a 객체를 먼저 만들고 그다음에 type(a)로 a 객체가 어떤 타입인지 알아보았다.
# 역시 객체 a가 FourCal 클래스의 객체임을 알 수 있다.

# ※ type 함수는 파이썬이 자체로 가지고 있는 내장 함수로 객체 타입을 출력한다.