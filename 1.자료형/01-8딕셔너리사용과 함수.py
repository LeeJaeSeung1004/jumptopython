#딕셔너리 key를 사용해 value얻기
grade = {"pey":10,"julliet":99}
grade["pey"]
grade["julliet"]
# 리스트나 튜플 문자열과 달리 
# 딕셔너리는 key를 이용해서 value를 구하는 방법이다
# key의 value를 얻기 위해서는 변수[key]를사용한다

# 주의 사항
# 딕셔너리에서 key는 고유한 값이므로 중복되는key를 설정하면 하나
# 빼고 나머지는 모두 무시된다
a= {1:"a",1:"b"}
# Key가 중복되었을때 1개를 제외한 값이 무시되는 이유는
# key를 통해 value를 얻는 딕셔너리의 특징 때문이다 
# 동일한 키가 있으면 어떤 key를 불러야 할지 알수없기 때문이다
# key에는 리스트를 쓸수없다 하지만 튜플은 쓸수있다
#왜냐하면 리스트는 값이 변할수도 있지만 튜플은 안변하기 때문이다

#함수들
#key리스트만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()
#x.keys()는 딕셔너리 x의 key만을 모아서 dict_keys 객체를 돌려준다
#dict_keys객체는 리스트를 쓰는것과 차이가 없지만 리스트고유의 append,insert,pop,remove,sort함수는 사용불가하다
for i in a.keys():
    print(i)
#dict_keys객체를 리스트로 바꾸려면 list(a.keys())형식으로쓴다

#value 리스트 만들기(values)
a.values()
#dict_values(["pey","0119993323","1118"])
#key를 얻는걷과 마찬가지 방법으로 values함수를 사용한다

#key,values쌍 얻기(items)
a.items()
#dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

#key:values쌍 모두 지우기(clear)
a.clear()
#clear함수는 딕셔너리 안의 모든요소를 삭제한다

#key로 value얻기(get)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.get("name")
a.get("phone")
#get(x)함수라는 key에 대응되는 value를 돌려준다 a["name"]과 같다
# 단 a["nokey"]처럼 존재하지않는키로 값을 가져오려할경우 a["nokey"]는 오류를 발생시키고
# a.get("nokey")는 none을 돌려준다
# 딕셔너리안에 찾으려는 key값이 없을 경우 정해둔 디폴트값을 불러오려면 
# get(X,"디폴트 값")을 사용하면 편하다

#해당key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
"name" in a
"email" in a
# name문자열은 a딕셔너리의 key중 하나이다 따라서 name in a르 호출하면 참을 돌려준다
# 반대로 email은 존재하지 않으므로 거짓을 돌려준다