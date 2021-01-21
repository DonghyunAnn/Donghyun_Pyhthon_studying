#print(num + bool+ 문자열 )-> str()처리를 해줘야함
#print(num, bool, 문자열 )-> str()처리 안해도 됨
'''
주석처리
아니면 드래그해서 ctrl+/ 하면 한번에 주석처리
'''

#연산자
'''
연산자 %->나머지 //->몫
bool은 not(bool)-> 역으로 나오게 됨
x=x연산자숫자 == x연산자=숫자 
abs(num) -> 절대값
pow(x,y) -> x^y
round(num) -> 반올림
'''

#from library import 기능(*=전체)

#난수생성
'''
from random import *
print(random()) # 0.0~1.0 미만의 임의의 값
print(random() * 10) # 0.0~ 10.0 미만의 임의의 값
print(int(random()*10)) # 0~10 미만의 임의의 값
print(int(random()*10)+1) # 1~10 미만의 임의의 값
print(randrange(1,46)) #1부터 46미만의 임의의 값
print(randint(1,45)) #1부터 45이하의 임의의 값
'''

# 퀴즈: print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4,28)) + "일로 선정되었습니다")

#문자열
'''
sentence="""
나는 소년이고,
파이썬은 쉬워요
""" -> """ """ 문자열 줄바꿈도 가능
#파이썬은 시작점이 0임 그리고 위치의 직전까지임 0에서 6까지면 [0:7]
sentence="Python is Amazing"
print(sentence.upper())
print(sentence.lower())
print(sentence[0].isupper())
print(len(sentence))
print(sentence.replace("Python","JAVA"))
index=sentence.index("n")
print(index)
index=sentence.index("n",index+1)
print(index)
#find와 index는 비슷하지만 find는 문자열에 없을 경우 -1처리 index는 error발생하고 뒤가 진행이 안됨
print(sentence.count("n"))
'''

#문자열 입력
'''
#방법1
print("나는 %d살입니다." % 20) #d는 정수값 의미
print("나는 %s을 좋아해요" %"파이썬") #s는 str
print("Apple은 %c로 시작해요" %"A") #c는 character
print("나는 %s색과 %s색을 좋아해요" % ("파란","빨간"))
#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))#순서바꾸기
#방법3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20,color="빨간"))
#방법4
age=20
color="파란"
print(f"나는 {age}살이며, {color}색을 좋아해요")
'''

#탈출문자
'''
\n: 줄바꿈
\" \':문장 내에서 따옴표
\\: 문장 내에서 \
\r: 커서를 맨 앞으로
\b: 백스페이스(한 글자 삭제)
\t: 탭
'''

#퀴즈
# url="http://google.com"
# myurl=url.replace("http://","")
# pw=myurl[:3]+str(len(myurl[:myurl.index('.')]))+str(myurl.count("e"))+"!"
# print("{}의 생성된 비밀번호는 {}입니다".format(url,pw))

#리스트: 다양한 자료형 함께 사용할 수 있음
'''
subway=["유재석","조세호","박명수"]
subway.append("하하") #append는 뒤쪽에 추가해주는것
subway.insert(1,"정형돈") #insert는 위치에 추가
subway.pop() #뒤쪽에서 하나씩 꺼내는것
subway.count("유재석") #내용물의 개수를 찾는것
'''
'''
numlist=[5,4,3,2,1]
numlist.sort() #정렬
numlist.reverse() #역으로 정렬
numlist.clear() #모두 지우기
numlist=[5,4,3,2,1]
mixlist=["조세호",20,True]
numlist.extend(mixlist) #extend는 list에 다른 list 붙여주는 것
print(numlist)
'''

#사전: 콜론(:)을 사용함
'''
cabinet={3:"유재석",100:"김태호"}
print(cabinet[3]) # 사전에 없을 경우 error발생으로 프로그램이 멈춤
print(cabinet.get(3)) # 사전에 없을 경우 none이라고 발생&프로그램 진행
print(3 in cabinet) # in을 통해서 사전안에 존재하는지 존재하지 않는지 확인할 수 있음
cabinet["c-20"]= "조세호" # 이런식으로 추가하는 것 검색값이 같다면 업데이트
del cabinet["c-20"] # 기존에 존재하던 사전내용을 삭제
print(cabinet.keys()) # key값만 출력
print(cabinet.values()) # value 값만 출력
cabinet.clear() # 사전 내 내용 모두 삭제
'''

#튜플: 내용변경 추가 불가 but 속도가 리스트보다 빠름 ()소괄호를 씀

#집합(set): 중복을 허용하지 않음, 순서가 없음 {}중괄호를 씀
'''
java={"유재석",'김태호','양세형'}
python=set(["유재석","박명수"])
print(java&python) #교집합
print(java.intersection(python)) #교집합
print(java|python) #합집합
print(java.union(python)) #합집합
print(java - python) #차집합
print(java.difference(python)) # 차집합
python.add("김태호") #추가
java.remove("김태호") #제거
'''

#자료구조의 변경
'''
menu={"커피","우유","주스"}
print(menu,type(menu))
menu=list(menu)
print(menu,type(menu))
menu=tuple(menu)
print(menu,type(menu))
menu=set(menu)
print(menu,type(menu))
'''

#퀴즈
# from random import *
# users=range(1,21) #형식이 range로 잡힘
# users=list(users)
# shuffle(users)
# winners = sample(users,4)
# print(users)
# print(winners)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")


#조건문
'''
weather=input("오늘 날씨는 어때요? ")
if weather == "비" or weather=="눈":
    print("우산을 챙겨요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")
'''

#for문: 한줄쓰기에는 \\\수식 혹은 함수 for i in 범위
'''
for waiting_no in range(1,5): # 1,2,3,4
    print("대기번호 : {}".format(waiting_no))
'''


#while문
'''
customer = "토르"
person = "unknown"
while person != customer:
    print("{}님,커피가 준비되었습니다".format(customer))
    person= input("이름이 어떻게 되세요?")
    if person=="토르":
        print("여기 주문하신 커피 나왔습니다")
    else:
        print("아직준비가 안됐습니다")
'''
#continue와 break
'''
absent=[2,5]
no_book=[7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지, {}은 교무실로 따라와".format(student))
        break
    print("{}번은 책 읽어봐".format(student))
'''

#퀴즈
# from random import *
# n=0
# for i in range(1,51):
#     time=randrange(5,50)
#     if time>=5 and time<=15:
#         print('[o] {0}번째 손님 (소요시간 : {1}분)'.format(i,time))
#         n+=1
#     else:
#         print('[ ] {0}번째 손님 (소요시간 : {1}분'.format(i,time))
#         n=n
# print("총 탑승 승객 : {} 분".format(n))


#사용자 정의 함수
'''
def open_account():
    print("새로운 계좌가 생성되었습니다")
def deposit(balance,money):
    print("입금이 완료되었습니다. 잔액은 {}원입니다".format(balance+money))
    return(balance+money)
deposit(1000,1000)
def withdraw_night(balance,money):
    commission=100
    return commission,balance-money-commission # 반환값 두개도 가능 ,로 연결
commission,balance=withdraw_night(1000,500)
print("수수료 {0}원이며, 잔액은 {1}원입니다".format(commission,balance))
'''
#기본값: 함수에 디폴트 값을 정해주는 것
'''
def profile(name, age=17, mainlang="파이썬"):
    print("이름: {0} \t 나이: {1} \t 주 사용 언어: {2}" \
        .format(name,age,mainlang))
profile('유재석')
profile('daniel')
'''

#키워드 값 : 입력값에서 순서를 바꿔도 상관이 없음
'''
def profile(name, age=17, mainlang="파이썬"):
    print("이름: {0} \t 나이: {1} \t 주 사용 언어: {2}" \
        .format(name,age,mainlang))
profile(name="유재석",mainlang="파이썬",age=17)
'''
#가변인자: 함수값에 다른 개수의 인자가 들어갈 때 *을 사용해주면 됨
'''
def profile(name,age,*language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    #end는 다음 print에서 줄바꿈이 일어나지 않게 해주는 것
    for lang in language:
        print(lang,end=" ")
    print()
profile("danny",25, "python", "java","C","C++","C#")
profile("jane",23,"java","R")
'''

#지역변수와 전역변수
'''
gun=10
def checkpoint(soldiers):
    global gun #전역 공간에 있는 gun을 가져와 주는 것
    #이렇게 안가져와 주면 지역 공간의 gun을 새롭게 선언해줘야 함
    gun=gun-soldiers
    print("[함수 내] 남은 총 :{} ".format(gun))
print("전체 총: {}".format(gun))
checkpoint(2)
print("남은 총: {}".format(gun))
def checkpoint_ret(gun,soldiers):
    gun=gun-soldiers
    return gun
gun=checkpoint_ret(gun,2)
print("남은 총: {}".format(gun))
'''

#퀴즈
# def std_weight(height,gender):
#     if gender=="남자":
#         return height*height*22
#     elif gender=="여자":
#         return height*height*21      
# height=170
# gender="남자"
# weight=round(std_weight(height/100,gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다".format(height,gender,weight))

#표준입출력: input을 사용해 입력하면 str으로 처리됨
'''
print("Python", "Java", sep="vs",end="?")
print("무엇이 더 재밌을까요?")
import sys
print("python","java", file=sys.stdout) #표준입력
print("python","java", file=sys.stderr) #표준에러

scores={"math":0, "english":50,"coding":100}
for subject, score in scores.items():#items 로 부르면 key 와 value 가 나옴
    print(subject,score)
    print(subject.ljust(8),str(score).rjust(4),sep=":")
    #8개의 공간을 확보하고 좌로정렬, 4개의 공간을 호가보하고 우로정렬

for num in range(1,21):
    print("대기번호 : "+ str(num).zfill(3))#zfill만큼의 크기 그 외에는 0으로 채우기

'''

#출력포맷: {0:채울것정렬부호형식}
'''
#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리  공간을 확보
print("{0: >10}".format(500))
#양수일 떈 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#빈 자리는 _, 왼쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0:_<10}".format(500))
#3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000))
#3자리마다 콤마를 찍어주기 +
print("{0:+,}".format(100000000))
#3자리마다 콤마를 찍어주기, 자리수 확보하기, 빈공간 ^
print("{0:^<+30,}".format(100000000))
#소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))
'''

#파일입출력 
'''
#w는 write
#score.txt파일을 쓰기 목적으로 써서 쓰고 파일을 닫는것
score_file=open("score.txt","w",encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()
#a는 append .write를 써야하며 기존 파일에 추가하는것
score_file=open("score.txt","a",encoding="utf8")
score_file.write("과학 : 80") 
score_file.write("\n코딩 : 100") # 줄바꿈이 없음
'''
'''
#r은 read
score_file=open("score.txt","r",encoding="utf8")
print(score_file.read())#전체를 읽어내리는거
print(score_file.readline())#한줄씩 읽어내리는것
print(score_file.readline(),end=" ")#한줄씩 읽어내리는것
score_file.close()
#전체가 몇 줄인지 모를 때 오픈하는법1
score_file=open("score.txt","r",encoding="utf8")
while True:
    line=score_file.readline()
    if not line:#라인이 없으면
        break
    print(line,end="")
score_file.close()
#전체가 몇 줄인지 모를 때 오픈하는법1 #list로 저장해서 가져오는것
score_file=open("score.txt","r",encoding="utf8")
lines=score_file.readlines() # list형태로 저장
for line in lines:
    print(line,end="")
score_file.close
'''

#Pickle
'''
import pickle
profile_file= open("profile.pickle","wb")#쓰기목적, binary
profile={"이름":"박명수",'나이': 30,"취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile,profile_file)#profile에 있는 정보를 file에 저장
profile_file.close()

profile_file= open("profile.pickle","rb")#쓰기목적, binary
proflie=pickle.load(profile_file)#file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
'''

#with: with문을 사용해서 close를 안해도 됨
'''
import pickle
with open("profile.pickle",'rb') as profile_file:
    print(pickle.load(profile_file))
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())
'''

#퀴즈
# for i in range(1,51):
#     bogofile=open("{0}주차.txt".format(i),"w",encoding="utf8")
#     print(" - {0}주차 주간보고 - ".format(i),file=bogofile)
#     print("부서 : ",file=bogofile)
#     print("이름 : ",file=bogofile)
#     print("업무 요약 : ",file=bogofile)
#     bogofile.close()

# class: 틀-> 연관있는 변수와 함수의 집합
#__init__:생성자->마린은 객체 여기에는 self를 제외한 값 모두 입력해야함
'''
class Unit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력{0}, 공격력 {1}\n".format(self.hp,self.damage))
marine1=Unit("마린",40,5)
marine2=Unit("마린",40,5)
tank1=Unit("탱크",150,35)
wraith1=Unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))
wraith2=Unit("빼앗은 레이스",80,5)
wraith2.clocking=True
if wraith2.clocking==True:#클래스에서 객체를 확장시킬 수 있음
    print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))
'''
#method
'''
class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
    def attack(self,location):
        print("{0}: {1} 방향으로 적군을 공격합니다 [공격력{2}]".format(self.name,location,self.damage))
    def damaged(self,damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}이 파괴되었습니다".format(self.name))
firebat1=AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
'''

#상속
'''
#일반유닛 : 부모클래스
class Unit:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
#일반유닛을 상속받아서 attackunit을 만드는것 : 자녀클래스
class AttackUnit(Unit):
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name,hp)
        self.damage=damage
    def attack(self,location):
        print("{0}: {1} 방향으로 적군을 공격합니다 [공격력{2}]".format(self.name,location,self.damage))
    def damaged(self,damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}이 파괴되었습니다".format(self.name))
#다중 상속
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed
    def fly(self,name,location):
        print("{0}:{1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))
class FlyableAttackunit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)
'''

#연산자 오버로딩: 부모클래스에서 정의한 method말고 자식클래스에서 정의한 method를 사용하고자 할때
'''
#일반유닛
class Unit:
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{}유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("{0}:{1} 방향으로 이동합니다. [속도 {2}]".format(self.name,location,self.speed))

    def damaged(self,damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}이 파괴되었습니다".format(self.name))

#공격유닛
class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage=damage

    def attack(self,location):
        print("{0}: {1} 방향으로 적군을 공격합니다 [공격력{2}]".format(self.name,location,self.damage))
    
    def damaged(self,damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}이 파괴되었습니다".format(self.name))
#연산자 오버로딩으로 하위 class에 move를 추가
#공중유닛 및 공중공격가능유닛
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed
    def fly(self,name,location):
        print("{0}:{1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))
class FlyableAttackunit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage) #지상스피드는 0
        Flyable.__init__(self,flying_speed)
    def move(self, location):
        self.fly(self.name,location)
'''
#Pass: 완성하지 않아도 완성된것처럼 만들 수 있음
#Super: 다중 상속을 할 때는 두번 다 초기화 해야함
'''
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
    def stimpack(self):
        if self.hp >10:
            self.hp-=10
            print("{}: 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{}: 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

class Tank(AttackUnit):
    seize_developed =False #시즈모드 개발 여부
    
    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode=False

    def set_seizemode(self):
        if Tank.seize_developed == False:
            return
        if Tank.seize_developed == True:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{} : 싲 모드를 해제합니다".format(self.name))
            self.damage /= 2
            self.seize_mode = False

class Wraith(FlyableAttackunit):
    def __init__(self):
        FlyableAttackunit.__init__(self,"레이스",80,20,5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print("{} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked=False
        else:
            print("{} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked=True


def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    print("Player : gg") 
    print("[player] 님이 게임에서 퇴장하셨습니다.")

#실제게임시작
game_start()
#유닛생성
m1=Marine()
m2=Marine()
m3=Marine()
t1=Tank()
t2=Tank()
w1=Wraith()
#유닛일괄관리
attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
#전군이동
for unit in attack_units:
    unit.move("1시")
#탱크시즈모드
Tank.seize_developed=True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다")
#공격모드준비
for unit in attack_units:
    if isinstance(unit, Marine):
    #지금 만들어진 객체가 어느 클래스인스턴스인지 확인
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seizemode()
    elif isinstance(unit, Wraith):
        unit.clocking()
#전군공격
for unit in attack_units:
    unit.attack("1시")
#전군피해
from random import *
for unit in attack_units:
    unit.damaged(randint(5,20))
#게임종료
game_over()
'''

#퀴즈
# class house:
#     def __init__(self,location,house_type,deal_type,price,completion_year):
#         self.location=location
#         self.house_type=house_type
#         self.deal_type=deal_type
#         self.price=price
#         self.completion_year=completion_year
#     def show_detail(self):
#         print(self.location, self.house_type,self.deal_type,\
#             self.price,self.completion_year)
# house1=house("강남","아파트","매매","10억","2010년")
# house2=house("마포","오피스텔","전세","5억","2007년")
# house3=house("송파","빌라","월세","500/50","2000년")
# house=[]
# house.append(house1)
# house.append(house2)
# house.append(house3)
# print("총 {0}대의 매물이 있습니다".format(len(house)))
# for i in range(0,3):
#     house[i].show_detail()

#예외처리: try와 except 사용하기 
'''
try: 
    print("나누기 전용 계산기입니다")
    nums=[]
    nums.append(int(input("첫번쨰 숫자를 입력하세요 : ")))
    nums.append(int(input("두번쨰 숫자를 입력하세요 : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("에러! 잘못된 값 입력")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생했습니다")
    print(err)
'''

#에러 발생시키기: 조건문과 raise Error을 사용해서 발생시키는것
'''
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1= int(input("첫 번쨰 숫자를 입력하세요 : "))
    num2= int(input("두 번쨰 숫자를 입력하세요 : "))
    if num1>=10 or num2>=10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
'''

#사용자 정의 예외처리
#finally : 어떻게든 항상 뜨게 됨 강제종료되는 것을 막음
'''
class BignumberError(Exception):#Exception이라는 class를 상속
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1= int(input("첫 번쨰 숫자를 입력하세요 : "))
    num2= int(input("두 번쨰 숫자를 입력하세요 : "))
    if num1>=10 or num2>=10:
        raise BignumberError("입력값: {0} : {1}".format(num1,num2) )
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except BignumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
finally:
    print("계산기를 이용해 주셔서 감사합니다")
'''

#퀴즈
# class SoldoutError(Exception):
#     def _init(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
# chicken=10
# waiting=1
# while(True):
#     try:
#         print("남은 치킨 : {0}".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order> chicken:
#             print("재료가 부족합니다.")
#         elif order<=0:
#             raise ValueError 
#         else:
#             print("대기번호 {0}. {1}마리 주문이 완료되었습니다."\
#                 .format(waiting,order))
#             waiting +=1
#             chicken -=order
#         if chicken == 0:
#             raise SoldoutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다")
#     except SoldoutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break
        
#모듈: 함수를 모아둔 것
#호출 방법이 다양함
'''
import theater_module as mv #theater_module을 불러오는데 간단하게 mv로
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning
price(3)
price_morning(4)

from theater_module import price_soldier as price
price(5)
'''

#패키지:모듈을 모아둔 집합
'''
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()
'''

'''
import inspect
import random
print(inspect.getfile(random))#경로를 알 수 있음 모듈이 어디서부터 왔는지
'''

#pip install
#아래 콘솔창에 써야함
#pip install 패키지명 
#pip install --upgrade 패키지명
#pip uninstall 패키지명
#pip list
#pip show 패키지명

pip install plotly

#내장함수
#input : 사용자 입력을 받는 함수
#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
'''
import random
print(dir(random))
'''
#외장함수
#list of python moule 구글 검색하면 외장함수 목록들을 볼 수 있음 설명과 활용까지
#glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
'''
import glob
print(glob.glob("*.py"))
'''
# os : 운영체제에서 제공하는 기본 기능
'''
import os
print(os.getcwd())#현재 디렉토리
folder = "sample_dir"
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder,"폴더를 삭제하였습니다. ")
else:
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")
print(os.listdir())
'''
# #time : 시간관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# import datetime
# print("오늘 날짜는 ", datetime.date.today())
# #timedelta: 두 날짜 사이 간격
# today=datetime.date.today()
# love=datetime.datetime(2020,12,5)
# td=datetime.timedelta(days=100)
# print("우리가 만난지 100일은",love+td)
