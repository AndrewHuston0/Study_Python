'''리스트 내포 기능을 이용해 sentence 변수에 저장된 문자열로부터 filters에 저장된 문자들을
제거한 결과를 출력하는 코드를 작성하십시오.(단, 결과는 문자열 객체의 join()
메서드를 사용해 하나의 문자열로 출력하십시오)
'Python is powerful... and fast; plays well with others; runs everywhere; is freindly
& easy to learn; is Open'
'''
filters = 'aeiou\n;&. '
sentence = '''Python is powerful... and fast;
play well with other;
runs everywhere;
is friendly & easy to learn;
is Open.'''

syllabales = [syllabale for syllabale in sentence if syllabale not in filters]
# for in 먼저 쓰고, if 쓰고 마지막에 어디에 삽입하는 지 변수 지
print(''.join(syllabales))
# 이해 잘 안감
