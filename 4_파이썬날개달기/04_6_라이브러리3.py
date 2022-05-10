#라이브러리

#random
#random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다. random과 randint에 대해 알아보자.

#다음은 0.0에서 1.0 사이의 실수 중에서 난수 값을 돌려주는 예를 보여 준다.

import random
random.random()

#다음 예는 1에서 10 사이의 정수 중에서 난수 값을 돌려준다.

random.randint(1,10)

#다음 예는 1에서 55 사이의 정수 중에서 난수 값을 돌려준다.

random.randint(1,55)

#random 모듈을 사용해서 재미있는 함수를 하나 만들어 보자.

#random_pop.py
# import random
# def random_pop(data):
#     number = random.randint(0,len(data)-1)
#     return data.pop(number)

# if __name__ == "__main__":
#     data = [1,2,3,4,5]
#     while data:
#         print(random_pop(data))
        
#위 random_pop 함수는 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 돌려준다.
# 물론 꺼낸 요소는 pop 메서드에 의해 사라진다.

#random_pop 함수는 random 모듈의 choice 함수를 사용하여 다음과 같이 좀 더 직관적으로 만들 수도 있다.

import random_pop
random_pop.random_pop()

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

# random.choice 함수는 입력으로 받은 리스트에서 무작위로 하나를 선택하여 돌려준다.

# 리스트의 항목을 무작위로 섞고 싶을 때는 random.shuffle 함수를 사용하면 된다.

import random
data = [1,2,3,4,5]
random.shuffle(data)

#[1, 2, 3, 4, 5] 리스트가 shuffle 함수에 의해 섞여서 [5, 1, 3, 4, 2]로 변한 것을 확인할 수 있다.

#webbrowser
#webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다.
# 다음 예제는 웹 브라우저를 자동으로 실행하고 해당 URL인 google.com으로 가게 해 준다.

import webbrowser
webbrowser.open("http://google.com")

#webbrowser의 open 함수는 웹 브라우저가 이미 실행된 상태라면 입력 주소로 이동한다.
#만약 웹 브라우저가 실행되지 않은 상태라면 새로 웹 브라우저를 실행한 후 해당 주소로 이동한다.

#open_new 함수는 이미 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열리게 한다.
webbrowser.open_new("http://google.com")