#변수
#변수만들기
a = 1
b = "python"
c = [1,2,3]

#변수이름 = 저장할값

# 변수란
# 파이썬에서 사용하는 변수는 객체를 가리키는 것이라고도 말할 수 있다. 객체란 우리가 지금껏 보아 온 자료형과 같은 것을 의미하는 말이다
a = [1,2,3]
#만약 위 코드처럼 a = [1, 2, 3]이라고 하면 [1, 2, 3] 값을 가지는 리스트 자료형(객체)이 자동으로 메모리에 생성되고
#변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소를 가리키게 된다.

#a변수가 가르키는 메모리의 주소는 id(a)로 확인할수있다
a = [1,2,3]
print(id(a))
#id 함수는 변수가 가리키고 있는 객체의 주소 값을 돌려주는 파이썬 내장 함수이다.
#내가 만든 리스트의 메모리 주소값은 2181353644224이다

#리스트복사
a = [1,2,3]
b = a
# b변수에 a변수를 대입하면 b는 a와 완전히 동일하다
# [1,2,3]리스트를 참조하는 변수가 a변수 1개에서 b변수가 추가되어
# 2개로 늘어난 차이만있다

id(a)
1387481280256
id(b)
1387481280256
#id(a)의 값이 id(b)의 값과 동일함을 알수있다
a is b # True
#동일한 객체인지 판단하는 파이썬 명령어 is를 실행해도 참을 돌려준다
a[1] = 4
print(a)
print(b)
#a 리스트의 두 번째 요소를 값 4로 바꾸었더니 a만 바뀌는 것이 아니라 b도 똑같이 바뀌었다.
# 그 이유는 앞에서 살펴본 것처럼 a, b 모두 동일한 리스트를 가리키고 있기 때문이다.
#b 변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 만들려면
#2가지 방법이 있다

#[:] 이용
#리스트 전체를 가리키는 [:]을 사용해서 복사하는 것이다.
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

# 2. copy 모듈 이용
# 두 번째는 copy 모듈을 사용하는 방법이다. 다음 예를 보면 from copy import copy라는 처음 보는 형태의 문장이 나오는데,
# 이것은 뒤에 설명할 파이썬 모듈 부분에서 자세히 다룬다.
# 여기에서는 단순히 copy 함수를 쓰기 위해서 사용하는 것이라고만 알아두자.
from copy import copy
a = [1,2,3]
b = copy(a)
#위 예에서 b = copy(a)는 b = a[:]과 동일하다.

#두 변수가 같은 값을 가지면서 다른 객체를 제대로 생성했는지 다음과 같이 확인해 보자.

print(b is a)
#위 예에서 b is a가 False를 돌려주므로 b와 a가 가리키는 객체는 서로 다르다는 것을 알 수 있다.

a = [1,2,3]
b = a.copy()
#다음처럼 리스트 자료형의 자체 함수인 copy 함수를 사용해도 copy 모듈을 사용하는 것과 동일하다.

a,b = ("python","life")
#위 예문처럼 튜플로 a, b에 값을 대입할 수 있다. 이 방법은 다음 예문과 완전히 동일하다.
(a, b) = 'python', 'life'
#튜플 부분에서도 언급했지만 튜플은 괄호를 생략해도 된다.

#리스트로 변수를 만들 수도 있다.
[a,b] = ['python', 'life']
#여러 개의 변수에 같은 값을 대입할 수도 있다.
a = b = "python"
a = 3
b = 5
a,b = b,a