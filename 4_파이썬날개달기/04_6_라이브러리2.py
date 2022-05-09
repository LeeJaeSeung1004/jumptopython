#라이브러리


#glob
# 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다.
# 이럴 때 사용하는 모듈이 바로 glob이다.

# 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)

# glob 모듈은 디렉터리 안의 파일들을 읽어서 돌려준다. *, ? 등 메타 문자를 써서 원하는 파일만 읽어 들일 수도 있다.

# 다음은 C:/doit 디렉터리에 있는 파일 중 이름이 mark로 시작하는 파일을 모두 찾아서 읽어들이는 예이다.

import glob
from time import time
glob.glob("c:/doit/mark*")

#tempfile
# 파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다.
# tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.

import tempfile
filename = tempfile.mkdtemp()

#tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다.
#이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다. f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.

import tempfile
f = tempfile.TemporaryFile()
f.close()

# time
# 시간과 관련된 time 모듈에는 함수가 굉장히 많다.
# 그중 가장 유용한 몇 가지만 알아보자.

#time.time

#time.time()은 UTC(Universal Time Coordinated 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 돌려주는 함수이다.
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 돌려준다.

import time
time.time()

#time.localtime

#time.localtime은 time.time()이 돌려준 실수 값을 사용해서 연도, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수이다.

time.localtime(time.time())

#time.asctime
#위 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.

time.asctime(time.localtime(time.time()))

#time.ctime

#time.asctime(time.localtime(time.time()))은 time.ctime()을 사용해 간편하게 표시할 수 있다. asctime과 다른 점은 ctime은 항상 현재 시간만을 돌려준다는 점이다.

time.ctime()

#time.strftime

#time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))

#strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.

#시간에 관계된 것을 표현하는 포맷 코드

# 포맷코드	설명	                             예
# %a	       요일 줄임말	                         Mon
# %A	       요일	                                 Monday
# %b	       달 줄임말	                          Jan
# %B	       달	                                 January
# %c	       날짜와 시간을 출력함	                  06/01/01 17:22:21
# %d	       날(day)	                              [01,31]
# %H	       시간(hour)-24시간 출력 형태	           [00,23]
# %I	       시간(hour)-12시간 출력 형태	           [01,12]
# %j	       1년 중 누적 날짜	                      [001,366]
# %m	       달	                                  [01,12]
# %M	       분	                                  [01,59]
# %p	       AM or PM	                              AM
# %S	       초	                                  [00,59]
# %U	       1년 중 누적 주-일요일을 시작으로	       [00,53]
# %w	       숫자로 된 요일	                      [0(일요일),6]
# %W	       1년 중 누적 주-월요일을 시작으로	       [00,53]
# %x	       현재 설정된 로케일에 기반한 날짜 출력	06/01/01
# %X	       현재 설정된 로케일에 기반한 시간 출력	17:22:21
# %Y	       년도 출력	                          2001
# %Z	       시간대 출력	                          대한민국 표준시
"%%	       문자	                                  %"
# %y	       세기부분을 제외한 년도 출력	           01

#다음은 time.strftime을 사용하는 예이다

import time
time.strftime("%x",time.localtime(time.time()))
time.srtftime("%c",time.localtime(time.time()))

#time.sleep

#time.sleep 함수는 주로 루프 안에서 많이 사용한다.
# 이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다. 다음 예를 보자.

import time

for i in range(10):
    print(i)
    time.sleep(1)
    
#위 예는 1초 간격으로 0부터 9까지의 숫자를 출력한다. 위 예에서 볼 수 있듯이 time.sleep 함수의 인수는 실수 형태를 쓸 수 있다.
#즉 1이면 1초, 0.5면 0.5초가 되는 것이다.

# calendar

# calendar는 파이썬에서 달력을 볼 수 있게 해주는 모듈이다.

# calendar.calendar(연도)로 사용하면 그해의 전체 달력을 볼 수 있다. 결괏값은 달력이 너무 길어 생략하겠다.

import calendar
print(calendar.calendar(2015))

# calendar.prcal(연도)를 사용해도 위와 똑같은 결괏값을 얻을 수 있다.

calendar.prcal(2015)

# 다음 예는 2015년 12월의 달력만 보여 준다.
calendar.prmonth(2015, 12)

# December 2015
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
# 7  8  9  10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31

calendar.weekday

#calendar 모듈의 또 다른 유용한 함수를 보자.
#weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보를 돌려준다.
#월요일은 0, 화요일은 1, 수요일은 2, 목요일은 3, 금요일은 4, 토요일은 5, 일요일은 6이라는 값을 돌려준다.

calendar.weekday(2015,12,31)

#위의 예에서 2015년 12월 31일은 목요일임을 보여 준다.

#calendar.monthrange

#monthrange(연도, 월) 함수는 입력받은 달의 1일이 무슨 요일인지와
#그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.

calendar.monthrange(2015, 12)

#위 예는 2015년 12월 1일은 화요일이고, 이 달은 31일까지 있다는 것을 보여 준다.

#날짜와 관련된 프로그래밍을 할 때 위 2가지 함수는 매우 유용하게 사용된다.