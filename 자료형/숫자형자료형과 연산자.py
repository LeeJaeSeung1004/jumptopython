# 숫자형이란 숫자형태로 이루어진 자료형으로 정수,실수,8진수,16진수같은것들이 있다
# 정수의 사용예 123,-345,0
# 실수의 사용예 123.45,-1234.5,3.4e10
# 8진수의 사용예 0o34,0o25
# 16진수의 사용예 0x2A,0xFF

# 정수형
# 정수형(Integer)이란 정수를 뜻하는 자료형을 말한다.
# 다음 예는 양의 정수와 음의 정수, 숫자 0을 변수 a에 대입하는 예이다.
a = 123
a = -178
a = 0

# 실수형
# 정수형(Integer)이란 정수를 뜻하는 자료형을 말한다.
# 다음 예는 양의 정수와 음의 정수, 숫자 0을 변수 a에 대입하는 예이다.
a = 1.2
a = -3.45
# 위 방식은 우리가 일반적으로 볼 수 있는 실수형의 소수점 표현 방식이다.

a = 4.24E10
a = 4.24e-10

# 위 방식은 "컴퓨터식 지수 표현 방식"으로 
# 파이썬에서는 4.24e10 또는 4.24E10처럼 표현한다(e와 E 둘 중 어느 것을 사용해도 무방하다).
# 여기서 4.24E10은 4.24 * 10^10, 4.24e-10은 4.24 * 10 ^-10을 의미한다.

# 8진수와 16진수
# 8진수(Octal)를 만드려면 숫자가 0o 또는 0O(숫자 0 + 알파벳 소문자 o 또는 대문자 O)로 
# 시작하면 된다.
a = 0o177

# 16진수(Hexadecimal)를 만들기 위해서는 0x로 시작하면 된다.
a = 0x8ff
b = 0xABC
# 8진수나 16진수는 파이썬에서 잘 사용하지 않는 형태의 숫자 자료형이다


# 연산자

# 사칙연산
# 계산기와 마찬가지로 연산자를 사용해 사칙연산을 수행한다.
a = 3
b = 4
a + b
#7
a - b
#-1
a * b
#12
a / b
#0.75

#x의 y제곱을 나타내는 ** 연산자
#이 연산자는 x ** y처럼 사용했을 때 x의 y제곱(x^y) 값을 돌려준다
a = 3
b = 4
a ** b
#81

#나눗셈 후 나머지를 반환하는 % 연산자
#%는 나눗셈의 나머지 값을 돌려주는 연산자이다. 
#7을 3으로 나누면 나머지는 1이 될 것이고 3을 7로 나누면 나머지는 3이 될 것이다.
7 % 3
1
3 % 7
3

#나눗셈 후 몫을 반환하는 // 연산자
#/ 연산자를 사용하여 7 나누기 4를 하면 그 결과는 1.75가 된다.
7 / 4
1.75
#나눗셈 후 몫을 반환하는 // 연산자를 사용한 경우
7 // 4
1
#1.75에서 몫에 해당되는 정수값 1만 돌려주는 것을 확인할 수 있다.