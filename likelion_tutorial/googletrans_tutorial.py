# Gooletrans: 언어감지 기능 번역 기능
from googletrans import Translator
print(Translator)

# 번역기 만들기
translator=Translator()
#언어 감지
sentence = "안녕하세요 코드라이언입니다."
detected = translator.detect(sentence)
print(detected.lang)

#번역
#transtlate(text,dest,src) : src는 언어감지를 위해 사용되는 언어 선택임, dest는 바꾸는 언어
result=translator.translate(sentence,'en')
detected = translator.detect(sentence)

print()
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
