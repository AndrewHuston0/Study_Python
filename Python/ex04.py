scores = [80, 35, 66, 75, 90]
number = 0
score = 0


for score in scores :
    number += 1
    if score >= 60 :
        print("%d번 학생은 %d점으로 %s입니다." %(number, score, "합격"))
    else :
        print("%d번 학생은 %d점으로 %s입니다." %(number, score, "불합격"))


#number를 사용하지 않고 코딩하면 : (scores는 리스트 객체에 enumerate라는 함수를 사용)
# enmerate라는 함수는 튜플을 넘겨주게 됨 따라서 아래와 같이 씀
for (i, score) in enumerate(scores): # i 있는 부분의 소괄호는 생략해도 됨
    if score>=60:
        print("{0}번 학생은 {1}점으로 합격입니다.".format(i+1,score))
    else:
        print("{0}번 학생은 {1}점으로 불합격입니다.".format(i+1,score))
