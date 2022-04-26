#매개변수 지정하여 호출하기
#함수를 호출할때 매개변수를 지정할수있다

from cgi import print_arguments


def add(a,b):
    return a+b

#앞에서 알아본 add 함수이다. 이 함수를 다음과 같이 매개변수를 지정하여 사용할 수 있다.

result = add(a=3,b=7) #a에 3 ,b에 7을 전달
print(result)

#매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다는 장점이 있다.
result = add(b=5 ,a=3)
print(result)

#입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
#입력값이 여러 개일 때 그 입력값을 모두 더해 주는 함수를 생각해 보자. 하지만 몇 개가 입력될지 모를 때는 어떻게 해야 할까?

#def 함수이름(*매개변수):
    # 수행할문장
    # 
    
# 괄호 안의 매개변수 부분이 *매개변수로 바뀌었다.
# 여러 개의 입력값을 모두 더하는 함수를 직접 만들어 보자. 예를 들어 add_many(1, 2)이면 3을, add_many(1,2,3)이면 6을, add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)이면 55를 돌려주는 함수를 만들어 보자.

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

# 위에서 만든 add_many 함수는 입력값이 몇 개이든 상관이 없다.
# *args처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 튜플로 만들어준다.
# 만약 add_many(1, 2, 3)처럼 이 함수를 쓰면 args는 (1, 2, 3)이 되고,
# add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)처럼 쓰면 args는 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)이 된다.
# 여기에서 *args는 임의로 정한 변수 이름이다. *pey, *python처럼 아무 이름이나 써도 된다.

# args는 인수를 뜻하는 영어 단어 arguments의 약자이며 관례적으로 자주 사용한다.

# 이함수를 실행해 보자

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

# add_many(1,2,3)으로 함수를 호출하면 6을 돌려주고, add_many(1, 2, 3, 4, 5, 6, 7, 8, 9,10)을 대입하면 55를 돌려준다.

# 여러 개의 입력을 처리할 때 def add_many(*args)처럼 함수의 매개변수로 *args만 사용할 수 있는 것은 아니다.
#다음 예를 보자.

def add_mul(choice,*args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
            
    return result

# add_mul 함수는 여러 개의 입력값을 의미하는 *args 매개변수 앞에 choice 매개변수가 추가되어 있다.

# 이 함수는 다음과 같이 사용할 수 있다.
result = add_mul("add",1,2,3,4,5)
print(result)

#매개변수 choice에 'add'가 입력된 경우 *args에 입력되는 모든 값을 더해서 15를 돌려주고, 'mul'이 입력된 경우 *args에 입력되는 모든 값을 곱해서 120을 돌려준다

#키워드 파라미터

#이번에는 키워드 파라미터에 대해 알아보자.
#키워드 파라미터를 사용할 때는 매개변수 앞에 별 두 개(**)를 붙인다. 역시 이것도 예제로 알아보자.
#먼저 다음과 같은 함수를 작성한다.

def print_kwargs(**A):
    print(A)
    
# print_kwargs 함수는 매개변수 A를 출력하는 함수이다.
# 이제 이 함수를 다음과 같이 사용해 보자.

print_kwargs(a= 1)
print_kwargs
print_kwargs(name="foo",age=3)

#입력값 a=1 또는 name='foo', age=3이 모두 딕셔너리로 만들어져서 출력된다는 것을 확인할 수 있다.
# 즉 **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.

#kwargs는 keyword arguments의 약자이며 args와 마찬가지로 관례적으로 사용한다.

#함수의 결괏값은 언제나 하나이다

def add_and_mul(a,b):
    return a+b,a*b
#add_and_mul 함수는 2개의 입력 인수를 받아 더한 값과 곱한 값을 돌려주는 함수이다.

result = add_and_mul(3,4)
# 결과값은 a+b와 a*b 2개인데 결괏값을 받아들이는 변수는 result 하나만 쓰였으니 오류가 발생하지 않을까? 당연한 의문이다. 하지만 오류는 발생하지 않는다. 그 이유는 함수의 결괏값은 2개가 아니라 언제나 1개라는 데 있다. add_and_mul 함수의 결괏값 a+b와 a*b는 튜플값 하나인 (a+b, a*b)로 돌려준다.

# 따라서 result 변수는 다음과 같은 값을 갖게 된다.

result = (7,12)
# 즉 결괏값으로 (7, 12)라는 튜플 값을 갖게 되는 것이다.

# 만약 이 하나의 튜플 값을 2개의 결괏값처럼 받고 싶다면 다음과 같이 함수를 호출하면 된다.
result1,result2= add_and_mul(3,4)

# 이렇게 호출하면 result1, result2 = (7, 12)가 되어 result1은 7이 되고 result2는 12가 된다.

# 또 다음과 같은 의문이 생길 수도 있다.

def add_and_mul(a,b):
    return a+b
    return a*b
# 위와 같이 return문을 2번 사용하면 2개의 결괏값을 돌려주지 않을까? 하지만 파이썬에서 위와 같은 함수는 참 어리석은 함수이다.
# 그 이유는 add_and_mul 함수를 호출해 보면 알 수 있다.
result = add_and_mul(2,3)
print(result)
# add_and_mul(2, 3)의 결괏값은 5 하나뿐이다. 두 번째 return문인 return a*b는 실행되지 않았다는 뜻이다.

#이 예에서 볼 수 있듯이 두 번째 return문인 return a*b는 실행되지 않았다. 따라서 이 함수는 다음과 완전히 동일하다.

def add_and_mul(a,b):
    return a+b
#즉 함수는 return문을 만나는 순간 결괏값을 돌려준 다음 함수를 빠져나가게 된다.

#[return의 또 다른 쓰임새]
#특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다. 다음 예를 보자.

def say_nick(nick): 
    if nick == "바보": 
         return 
    print("나의 별명은 %s 입니다." % nick)

#위 함수는 '별명'을 입력으로 전달받아 출력하는 함수이다. 이 함수 역시 반환 값(결괏값)은 없다(문자열을 출력한다는 것과 반환 값이 있다는 것은 전혀 다른 말이다. 혼동하지 말자.
#함수의 반환 값은 오로지 return문에 의해서만 생성된다).

# 매개변수에 초깃값 미리 설정하기
# 이번에는 조금 다른 형태로 함수의 인수를 전달하는 방법에 대해서 알아보자.
# 매개변수에 초깃값을 미리 설정해 주는 경우이다.

def say_myself(name,old,man=True):
    print(f"나의 이름은 {name}입니다")
    print(f"나이는 {old}입니다")
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
#say_myself 함수는 3개의 매개변수를 받아서 마지막 인수인 man이 True이면 "남자입니다.", False이면 "여자입니다."를 출력한다.

# 위 함수를 보면 매개변수가 name, old, man=True 이렇게 3개다.
# 그런데 낯선 것이 나왔다. man=True처럼 매개변수에 미리 값을 넣어 준 것이다. 이것이 바로 함수의 매개변수 초깃값을 설정하는 방법이다.
# 함수의 매개변수에 들어갈 값이 항상 변하는 것이 아닐 경우에는 이렇게 함수의 초깃값을 미리 설정해 두면 유용하다.

#초기화 시키고 싶은 매개변수는 항상 뒤에 놓지않으면 오류가 발생한다

# 함수 안에서 선언한 변수의 효력 범위

# 다음 예를 보자.
a =1
def vartest(a):
    a +=1
    
vartest(a)
print(a)

#먼저 a라는 변수를 생성하고 1을 대입한다.
# 다음 입력으로 들어온 값에 1을 더해 주고 결괏값은 돌려주지 않는 vartest 함수를 선언한다.
# 그리고 vartest 함수에 입력값으로 a를 주었다.
# 마지막으로 a의 값을 출력하는 print(a)를 입력한다.
# 과연 결괏값은 무엇이 나올까?

 #vartest 함수에서 매개변수 a의 값에 1을 더했으니까 2가 출력될 것 같지만 프로그램 소스를 작성해서 실행해 보면 결괏값은 1이 나온다.
 # 그 이유는 함수 안에서 새로 만든 매개변수는 함수 안에서만 사용하는 "함수만의 변수"이기 때문이다.
 # 즉 def vartest(a)에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수이지 함수 밖의 변수 a가 아니라는 뜻이다.
 
#따라서 vartest 함수는 다음처럼 변수 이름을 hello로 한 vartest 함수와 완전히 동일하다.

def vartest(hello):
    hello = hello + 1
    
# 즉 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과는 전혀 상관이 없다는 뜻이다.

# 다음 예를 보면 더욱 분명하게 이해할 수 있을 것이다.

def vartest(a):
    a = a + 1

vartest(3)
print(a)
# 위 프로그램 소스를 에디터로 작성해서 실행하면 어떻게 될까? 오류가 발생할 것이라고 생각한 독자는 모든 것을 이해한 독자이다.
# vartest(3)을 수행하면 vartest 함수 안에서 a는 4가 되지만 함수를 호출하고 난 뒤에 print(a) 문장은 오류가 발생하게 된다.
# 그 이유는 print(a)에서 입력받아야 하는 a 변수를 어디에서도 찾을 수가 없기 때문이다.
# 다시 말하지만 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 함수 밖에서는 사용되지 않는다.
# 이것을 이해하는 것은 매우 중요하다.

# 함수 안에서 함수 밖의 변수를 변경하는 방법

# 그렇다면 vartest라는 함수를 사용해서 함수 밖의 변수 a를 1만큼 증가시킬 수 있는 방법은 없을까? 이 질문에는 2가지 해결 방법이 있다.

# 1. return 사용하기

a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a) 
print(a)
#첫 번째 방법은 return을 사용하는 방법이다. vartest 함수는 입력으로 들어온 값에 1을 더한값을 돌려준다. 따라서 a = vartest(a)라고 대입하면 a가 vartest 함수의 결괏값으로 바뀐다. 여기에서도 물론 vartest 함수 안의 a 매개변수는 함수 밖의 a와는 다른 것이다.

#2. global 명령어 사용하기

# vartest_global.py
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)

# 두 번째 방법은 global 명령어를 사용하는 방법이다.
# 위 예에서 볼 수 있듯이 vartest 함수 안의 global a 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻이다.
# 하지만 프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다. 왜냐하면 함수는 독립적으로 존재하는 것이 좋기 때문이다.
# 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다.
# 그러므로 가급적 global 명령어를 사용하는 이 방법은 피하고 첫 번째 방법을 사용하기를 권한다.

#lambda

# lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
# 보통 함수를 한줄로 간결하게 만들 때 사용한다.
# 우리말로는 "람다"라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.

#사용법은 다음과 같다.

#lambda 매개변수1, 매개변수2, : 매개변수를 이용한 표현식

#한번 직접 만들어 보자.

add = lambda a, b: a+b
result = add(3, 4)
print(result)

#add는 두 개의 인수를 받아 서로 더한 값을 돌려주는 lambda 함수이다. 위 예제는 def를 사용한 다음 함수와 하는 일이 완전히 동일하다.

def add(a, b):
    return a+b
result = add(3, 4)
print(result)

#lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.

