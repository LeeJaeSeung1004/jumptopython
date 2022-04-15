# 문자열


# 문자열이란 문자 단어등으로 구성된 문자들의 집합을 말한다
# 예를 들면 다음과 같은 것들이 문자열이다.
"Life is too short, You need Python"
"a"
"123"
# 위 문자열 예문을 보면 모두 큰따옴표(" ")로 둘러싸여 있다.


# 문자열은 어떻게 만들고 사용할까?

# 파이썬에서 문자열을 만드는 방법은 총 4가지이다.

"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''


#문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때

#문자열 안에도 작은따옴표와 큰따옴표가 들어 있어야 할 경우가 있다.

# 1. 문자열에 작은따옴표 (') 포함시키기
     #Python's favorite food is perl
 
# 큰따옴표 안에 들어 있는 작은따옴표는 문자열을 나타내기 위한 기호로 인식되지 않는다.
food = "Python's favorite food is perl"

# 시험 삼아 다음과 같이 큰따옴표(")가 아닌 작은따옴표(')로 문자열을 둘러싼 후 다시 실행해 보자. 
# 'Python'이 문자열로 인식되어 구문 오류(SyntaxError)가 발생할 것이다.
# food = 'Python's favorite food is perl'
#   File "<stdin>", line 1
#     food = 'Python's favorite food is perl'
#                    ^
# SyntaxError: invalid syntax

# 2. 문자열에 큰따옴표 (") 포함시키기

# "Python is very easy." he says.

# 다음과 같이 문자열을 작은따옴표(')로 둘러싸면 된다.
say = '"Python is very easy." he says.'

# 이렇게 작은따옴표(') 안에 사용된 큰따옴표(")는 문자열을 만드는 기호로 인식되지 않는다.
                    
# 3. 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

# 백슬래시(\)를 작은따옴표(')나 큰따옴표(") 앞에 삽입하면 문자 ('), (") 그 자체를 뜻하게 된다.


# 여러 줄인 문자열을 변수에 대입하고 싶을 때

# 1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"

# 위 예처럼 줄바꿈 문자 \n을 삽입하는 방법이 있지만 읽기에 불편하고 줄이 길어지는 단점이 있다.

# 2. 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 사용하기

#파이썬에서는 다음과 같이 작은따옴표 3개(''') 또는 큰따옴표 3개(""")를 사용한다.

# 작은따옴표 3개를 사용한 경우
multiline='''
Life is too short
You need python
'''

# 큰따옴표 3개를 사용한 경우
multiline="""
Life is too short
You need python
"""



# 문자열 연산


# 문자열 더해서 연결하기
head = "python"
tail = " is fun!"
head + tail
'Python is fun!'
# 문자열변수와 문자열변수사이에 +를 넣으면 순서대로 연결되어 출력한다

# 문자열 곱하기
a = "python"
a * 2
'pythonpython'
# 문자열 변수 * 숫자는 문자열변수를 숫자만큼 반복하라는 의미이다


# 문자열 길이 구하기

# 문자열 길이를 알려면 len(문자열변수)를 사용하면 된다