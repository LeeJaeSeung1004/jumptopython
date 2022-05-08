#라이브러리


# sys
# sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.

# 명령 행에서 인수 전달하기 - sys.argv

# C:/User/home>python test.py abc pey guido

# 명령 프롬프트 창에서 위 예처럼 test.py 뒤에 또 다른 값을 함께 넣어 주면 sys.argv 리스트에 그값이 추가된다

# 예제를 따라하며 확인해 보자. 우선 다음과 같은 파이썬 프로그램을 작성하자
# argv_test.py 파일은 C:/doit/Mymod 디렉터리에 저장했다고 가정한다

# argv_test.py
# import sys
# print(sys.argv)

#명령 프롬프트 창에서 Mymod 디렉터리로 들어간 뒤 다음과 같이 실행해 보자.

# C:/doit/Mymod>python argv_test.py you need python
# ['argv_test.py', 'you', 'need', 'python']

#python 명령어 뒤의 모든 것들이 공백을 기준으로 나뉘어서 sys.argv 리스트의 요소가 된다

#강제로 스크립트 종료하기 - sys.exit

#sys.exit()

#sys.exit는 Ctrl+Z나 Ctrl+D를 눌러서 대화형 인터프리터를 종료하는 것과 같은 기능을 한다. 프로그램 파일 안에서 사용하면 프로그램을 중단시킨다.

#자신이 만든 모듈 불러와 사용하기 - sys.path

#sys.path는 파이썬 모듈들이 저장되어 있는 위치를 나타낸다.
#즉 이 위치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올수 있다

#다음은 그 실행 결과이다.

import os
import shutil
import sys
print(sys.path)
['c:\\Users\\ljseu\\source\\repos\\jumptopython\\4_파이썬날개달기',
'C:\\Python\\python310.zip', 'C:\\Python\\DLLs', 'C:\\Python\\lib',
'C:\\Python', 'c:\\Users\\ljseu\\source\\repos\\djangovenv',
'c:\\Users\\ljseu\\source\\repos\\djangovenv\\lib\\site-packages']

#위 예에서 ''는 현재 디렉터리를 말한다.

# path_append.py
import sys
sys.path.append("C:/doit/mymod")

#위와 같이 파이썬 프로그램 파일에서 sys.path.append를 사용해 경로 이름을 추가할 수 있다.
#이렇게 하고 난 후에는 C:/doit/Mymod 디렉터리에 있는 파이썬 모듈을 불러와서 사용할 수 있다.

#※ 파일 경로를 표시할 때 명령 프롬프트 창에서는 /, \든 상관없지만, 소스코드 안에서는 반드시 / 또는 \\ 기호를 사용해야 한다.

# pickle
# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
# 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여 준다.

import pickle
f = open("test.txt","wb")
data = {1: "python",2: "you need"}
pickle.dump(data,f)
f.close()

#다음은 pickle.dump로 저장한 파일을 pickle.load를 사용해서 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오는 예이다.

import pickle
f = open("test.txt","rb")
data = pickle.load(f)
print(data)

#위 예에서는 딕셔너리 객체를 사용했지만 어떤 자료형이든저장하고 불러올 수 있다.

#os
#OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈이다.

#내 시스템의 환경 변수값을 알고 싶을때 - os.environ

#시스템은 제각기 다른 환경 변수 값을 가지고 있는데, os.environ은 현재 시스템의 환경 변수 값을 보여 준다.
# 다음을 따라 해 보자.

import os
os.environ

#environ
# ({'ALLUSERSPROFILE': 'C:\\ProgramData',
# 'APPDATA': 'C:\\Users\\ljseu\\AppData\\Roaming',

# 위 결괏값은 자신의 시스템 정보이다.
# os.environ은 환경 변수에 대한 정보를 딕셔너리 객체로 돌려준다
# 자세히 보면 여러가지 유용한 정보를 찾을 수있다

# 돌려받은 객체가 딕셔너리이기 때문에 다음과 같이 호출할수있다.
# 다음은 자신시스템의 PATH 환경 변수 내용이다

os.environ["PATH"]

#디렉터리 위치 변경하기 - os.chdir

#os.chdir을 사용하면 다음과 같이 현재 디렉터리 위치를 변경할 수 있다
os.chdir("C:\windows")

#디렉터리 위치 돌려받기 - os.getcwd()
print(os.getcwd())

#시스템 명령어 호출하기 - os.system

#시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다.
#os.system("명령어")처럼 사용한다.
#다음은 현재 디렉터리에서 시스템 명령어 dir을 실행하는 예이다.

os.system("dir")

#실행한 시스템 명령어의 결괏값 돌려받기 - os.popen

#os.popen은 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 돌려준다.

f = os.popen("dir")

#읽어 들인 파일 객체의 내용을 보기 위해서는 다음과 같이 하면 된다.

print(f.read())

# 기타 유용한 os 관련 함수

# 함수	            설명
# os.mkdir(디렉터리)	디렉터리를 생성한다.
# os.rmdir(디렉터리)	디렉터리를 삭제한다.단, 디렉터리가 비어있어야 삭제가 가능하다.
# os.unlink(파일)	    파일을 지운다.
# os.rename(src, dst) src라는 이름의 파일을 dst라는 이름으로 바꾼다.

# shutil
# shutil은 파일을 복사해 주는 파이썬 모듈이다

# 다음 예시는 src라는 이름의 파일을 dst로 복사한다.
# 만약 dst가 디렉터리 이름이라면 src라는 파일 이름으로 dst 디렉터리에 복사하고 동일한 파일 이름이 있을 경우에는 덮어쓴다.

import shutil
shutil.copy("src.txt","dst.txt")

#위 예를 실행해 보면 src.txt 파일과 동일한 내용의 파일이 dst.txt로 복사되는 것을 확인할 수 있다