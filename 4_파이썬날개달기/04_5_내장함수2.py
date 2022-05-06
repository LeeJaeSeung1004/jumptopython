#내장함수

#id
#id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.
a = 3
print(id(3))
print(id(a))
b =a
print(id(b))

# 위 예의 3, a, b는 고유 주소 값이 모두 같다. 즉 3, a, b가 모두 같은 객체를 가리키고 있다.

# 만약 id(4)라고 입력하면 4는 3, a, b와 다른 객체이므로 당연히 다른 고유 주소 값이 출력된다.

# input
# input([prompt])은 사용자 입력을 받는 함수이다.
# 매개변수로 문자열을 주면 다음 세 번째 예에서 볼 수 있듯이 그 문자열은 프롬프트가 된다.
#[ ] 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법임을 기억하자.
a = input()
print(a)
b = input("Enter: ")

#위에서 입력받은 문자열을 확인해 보면 다음과 같다.
print(b)

# int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로,
# 정수를 입력으로 받으면 그대로 돌려준다.

int("3")
int(3.4)

# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.

# 2진수로 표현된 11의 10진수 값은 다음과 같이 구한다.
int("11",2)
3

#16진수로 표현된 1A의 10진수 값은 다음과 같이 구한다.
int("1A",16)
26

# isinstance
# isinstance(object, class )는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.

class Person: pass

a = Person()
isinstance(a,Person)

#위 예는 a가 Person 클래스가 만든 인스턴스임을 확인시켜 준다

b =3
isinstance(b,Person)

# b는 Person 클래스가 만든 인스턴스가 아니므로 False를 돌려준다

# len
# len(s)는 입력값의 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.

len("python")
len([1,2,3])
len((1,"a"))

#list
#list(S)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다
list("python")
list((1,2,3))

#list 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다

a = [1,2,3]
b = list(a)
print(b)

# map

# map(f,iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다
# map은 입력받은 자료형의 각 요소를 함수f가 수행한 결과를 묶어서 돌려주는 함수이다

#다음 예를 보자

def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

# two_times 함수는 리스트 요소를 입력받아 각 요소에 2를 곱한 결과값을 돌려준다.
# 실행 결과는 다음과 같다

# 결과값: [2,4,6,8]

#위 예제는 map 함수를 사용하면 다음처럼 바꿀 수 있다
def two_times(x):
    return x*2

list(map(two_times,[1,2,3,4]))
#이제 앞 예제를 해석해 보자. 먼저 리스트의 첫 번째 요소인 1이 two_times 함수의 입력값으로 들어가고 1 * 2의 과정을 거쳐서 2가 된다.
# 다음으로 리스트의 두 번째 요소인 2가 2 * 2 의 과정을 거쳐 4가 된다. 따라서 결괏값 리스트는 이제 [2, 4]가 된다.
# 총 4개의 요솟값이 모두 수행되면 마지막으로 [2, 4, 6, 8]을 돌려준다.
# 이것이 map 함수가 하는 일이다.
# 위 예에서 map의 결과를 리스트로 보여 주기위해 list 함수를 사용하여 출력하였다.

#앞의 예는 lambda를 사용하면 다음처럼 간략하게 만들 수 있다.

list(map(lambda a: a*2, [1, 2, 3, 4]))
[2, 4, 6, 8]

# max
# max(iterable)은 인수로 반복 가능한 자료형을 입력받아 그 최대값을 돌려주는 함수이다

max([1,2,3])
3
max("python")
"y"

# min
# min(iterable)은 max함수와 반대로 인수로 반복가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수이다

min([1,2,3])
1
min("python")
"h"

# oct
# oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다

oct(34)
0o42
oct(12345)
0o30071

# open
# open(filename,[mode])는 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수이다
# 읽기 방법(mode)를 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다

# mode 설명
# w    쓰기 모드로 파일 열기
# r    읽기 모드로 파일 열기
# a    추가 모드로 파일 열기
# b    바이너리 모드로 파일 열기

# b는 w,r,a와 함께 사용한다

f = open("binary_file","rb")

#위 예의 rb는 "바이너리 읽기 모드"를 의미한다.

#다음 예의 fread와 fread2는 동일한 방법이다.

fread = open("read_mode.txt","r")
fread2 = open("read_mode.txt")

# 즉 모드 부분을 생략하면 기본값으로 읽기 모드 r를 갖게 된다.

# 다음은 추가 모드(a)로 파일을 여는 예이다.

fappend = open("append_mode.txt","a")

# ord
# ord(c)는 문자의 유니코드 값을 돌려주는 함수이다

#※ ord 함수는 chr 함수와 반대이다.

ord("a")
97
ord("가")
44032

# pow
# pow(x,y)는 x의 y 제곱한 결과값을 돌려주는 함수이다

pow(2,4)
16
pow(3,3)
27


# range
# range([start,]stop[,step])은 for문과 함께 자주 사용하는 함수이다
# 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다

# 인수가 하나일경우

# 시작숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다

list(range(5))
[0,1,2,3,4]

# 인수가 2개일 경우

# 입력으로 주어지는 2개의 인수는 시작 숫자와 끝숫자늘 나타낸다ㅏ
# 단 끝숫자는 해당범위에 포함되지 않는다

list(range(5,10))
[5,6,7,8,9]

# 인수가 3개일 경우

# 세번째 인수는 숫자 사이의 거리를 말한다

list(range(1,10,2))
[1,3,5,7,9]
list(range(0,-10,-1))
[0,-1,-2,-3,-4,-5,-6,-7,-8,-9]

# round
# round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.

# ※ [, ndigits]는 ndigits가 있을 수도 있고 없을 수도 있다는 의미이다.

round(4.6)
5
round(4.2)

#다음과 같이 실수 5.678을 소수점 2자리까지만 반올림하여 표시할 수 있다.

round(5.678,2)
5.68

#round 함수의 두 번째 매개변수는 반올림하여 표시하고 싶은 소수점의 자릿수(ndigits)이다.

#sorted
#sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
sorted([3,1,2])
[1,2,3]
sorted(["a","c","b"])
sorted("zero")
['e', 'o', 'r', 'z']
sorted((3,2,1))
[1,2,3]

#리스트 자료형에도 sort 함수가 있다.
# 하지만 리스트 자료형의 sort 함수는 리스트 객체 그 자체를 정렬만 할 뿐 정렬된 결과를 돌려주지는 않는다.

str
#str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수이다.

str(3)
"3"
str('hi')
"hi"
str("hi".upper())
"HI"

# sum
# sum(iterable) 은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.

sum([1,2,3])
6
sum((4,5,6))
15

# tuple
# tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다. 만약 튜플이 입력으로 들어오면 그대로 돌려준다.

tuple("abc")
('a', 'b', 'c')
tuple([1, 2, 3])
(1, 2, 3)
tuple((1, 2, 3))
(1, 2, 3)

# type
# type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수이다.

type("abc")
#<class 'str'>
type([ ])
#<class 'list'>
type(open("test", 'w'))
#<class '_io.TextIOWrapper'>

# zip
# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.

# ※ 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미이다.

# 잘 이해되지 않는다면 다음 예제를 살펴보자.

list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]