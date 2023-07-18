data = input("0~100점 사이의 점수를 입력하세요: ")
score = int(data)
grade = "NA" # NA값이 디폴트

if 90 <= score <=100 :
    grade = "A"
elif 80 <= score < 90 :
    grade = "B"
elif 70 <= score < 80 :
    grade = "C"
elif 60 <= score < 70 :
    grade = "D"
elif 0 <= score < 60 :
    grade = "F"

print("%d 점은 %s등급입니다." %(score, grade))
