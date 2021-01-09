class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")
#__name__을 사용해서 외부와 내부에서 실행하는건지 구분 가능
if __name__=="__main__":
    print("Thaland 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 떄만 실행돼요")
    trip_to=ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호줄")
