#딕셔너리
# 딕셔너리는 "이름" = "홍길동" 같은 대응관계를 나타내는 자료이다
# 요즘 사용하는 대부분의 언어는 이러한 대응 관계를 나타내는 자료형을 가지고 있는데
# 이를 연관 배열 또는 해시라고 한다
# 파이썬에서는 이것을 딕셔너리라고한다
# key와 value를 한쌍으로가진다

# 딕셔너리는 리스트나 튜플처럼 순차적으로 해당요소값을 구하지않고 key를 통해 value를 얻는다

#딕셔너리는 어떻게 만들까
#딕셔너리의 기본형

#{key1:value1, key2:value2, key3:value3}

# key와 value의 쌍들이 {}로 둘러싸여 있다
# 요소들은 key:value 형태로 이루어져있고 쉼표로 구분된다
# key에는 상수를쓰고 value에는 변수와 상수 둘다 쓸수있다

dic = {"name":"pey","phone":"0119993323","birth":"1118"}
#여기서 key는 "name","phone","birth"이고 value는 "pey","0119993323","1118"이다
#key에 정수값을 넣을수도 있고 value에 리스트도 넣을수있다

#딕셔너리 추가삭제
#딕셔너리 추가
a = {1:"a"}
a[2] ="b"
#{1:"a"}딕셔너리에 a[2] = "b"와 같이 입력하면 딕셔너리 a에 key와 value가 각각2와 "b"인 딕셔너리가 추가된다
#딕셔너리 삭제
del a[1]
#del a[key]처럼 입력하면 지정한키에 해당하는 딕셔너리요소가 삭제된다