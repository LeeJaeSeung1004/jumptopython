#04장 연습문제
#Q1)주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
a = 1
def is_odd(a):
    if a % 2 == 1:
        return True
    else:
        return False
    
#Q2)입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

def number_average(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

#Q3)
#다음은 두개의 숫자를 입력받아 더해서 값을 돌려주는 프로그램이다

# input1 = input("첫번째 숫자를 입력하세요:")
# input2 = input("두번째 숫자를 입력하세요:")

# total = input1 + input2
# print("두 수의 합은 %s 입니다" % total)

#이 프로그램을 수행해 보자.

# 3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.

# ※ int 함수를 사용해 보자.
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print(f"두 수의 합은 {total} 입니다")

# Q4)
# 다음 중 출력 결과가 다른 것 한 개를 골라 보자.

# 1. print("you" "need" "python")
# 2. print("you"+"need"+"python")
# 3. print("you", "need", "python")
# 4. print("".join(["you", "need", "python"]))

#3번

# Q5)
# 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.

# f1 = open("test.txt", 'w')
# f1.write("Life is too short")

# f2 = open("test.txt", 'r')
# print(f2.read())
#이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

#Q6)
#사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

user_input = input("저장할 내용을 입력하세요")
file = open("text.txt","a")
file.write(user_input)
file.write("\n")
file.close()


# Q7)
# 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

# Life is too short
# you need java
# ※ replace 함수를 사용해 보자.


f = open("test.txt", "r")
change =f.read()
f.close()

change = change.replace("java", "python")

f = open("test.txt", "w")
f.write(change)
f.close()