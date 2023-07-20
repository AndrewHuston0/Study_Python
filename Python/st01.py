# 리스트, 튜플 생성:

my_list = [1, "가", 2.4, True] # 기본적으로 이질적인 데이터를 다룰 수 있도록 만들어진 구조
my_tuple = (1, "가", 2.4, True) # 튜플은 소괄호를 사용해서 만듦

# 차이점은 list는 읽기 쓰기가 가능하고, tuple은 읽기 전용(한 번 만들어지면 수정 불가)

num_1_10 = range(1,11,2) # range객체(start, stop(포함 안됨), step)

my_obj = list(num_1_10) # 일반적으로 list객체를 만들 때 range객체를 이용해서 연속적인 숫자들을 만듦

# my_obj = tuple(num_1_10) tuple함수를 이용해서도 읽기 전용객체 생성 가능


#range 객체의 특징

# range(start, stop, step) 특징이 있고, 주로 for문과 같은 반복문에서 쓰이는데,
# 실제로 데이터를 미리 만들지 않고 루프에서 호출 될 때마다 만듦

# 확인

for n in num_1_10:
    print(n)

# 갖고 있는 게 아니라 루프 안에서 하나씩 생성하는 구조

my_str = "happy day!" # 이런 문자열 객체를 이용해서 list를 만들 수도 있음

my_obj_str = list(my_str) # 이렇게 되면 happy day!의 개별적인 문자들이 원소가 됨

# 마찬가지로 튜플로도 가

#------------------------------------
# 리스트, 튜플: 연산

nums_1 = [1,2,3]
nums_2 = [4,5]

print(nums_1 + nums_2) # +연산자를 사용할 경우 [1,2,3,4,5]로 연결됨
print(nums_1 * 2) # 이렇게 되면 [1,2,3,1,2,3]으로 nums_1을 두번 반복하는 구조의 결과를 만듦
# print(nums_1 - nums_1) 이렇게 마이너스 연산은 할 수 없음 => list와 list는 -연산이 안된다고 함
# print(nums_1 - 1) 이렇게 리스트에서 int를 빼는 것도 안된다고 함

# -----------------------------------
# 리스트, 튜플 : 항목 접근
nums = [1,2,3,4,5] # 여기서 index는 [0~4] 또는 [-5~-1]로 접근 가능 마지막 값은 [-1]번 인덱스여야 되고
# 맨 처음 값은 [0]번 index여야 됨
# 여러 항목 접근은
print(nums[2:4:1]) # range와 동일하게 접근 [start:stop(역시 포함 안됨):step]
print(nums[2:4]) # step의 경우에는 기본이 1이기 때문에 생략하면 1씩 증가라는 의미를 갖음
print(nums[-3:-1]) # 위와 동일한 의미

#--------------------------------------
# 리스트 : 조작

nums_3 = [1,3,5,7,9]
print(nums_3)
nums_3.append(11) # append를 통해 list에 값을 추가해줄 수 있음(마지막 index로 들어감)
print(nums_3)
nums_3.pop() # 가장 큰 index에 해당하는 data를 제거할 수 있음
print(nums_3)
nums_3.insert(2,4) # index 2에 4라는 값을 삽입, 이 경우 뒤의 index는 한 칸씩 증가해 이동(대체되는 게 아님)
print(nums_3)
del nums_3[5] # nums_3의 5번 index를 del이라는 명령어를 이용해서 제거 할 수 있음
print(nums_3)
# ps. function과 명령어(정확히 말하자면 keyword)는 다름
# 여기서 append와 insert는 function과 다른 method라고 불리는데 둘의 차이는
# function의 경우 독립적인 code 조각으로 code내 어느 곳에서나 호출 가능하지만
# method의 경우 object나 class와 연결되어 있어 무조건 class나 object의 호출이 필요하다
# 즉, 요약하면 독립적으로 실행 가능한가, 종속되어있나 차이가 있다.

# Python에서는 keyword를 제외한 모든 것들이 object(객체) 따라서 built-in-function을
# 재정의 할 수도 있음(변수 이름으로 쓸 수도 있음)

int = 1
print(int)
# print를 1로 대입해서 출력하려고 하면 'int' object is not callable이라고 나옴
# 이 경우 예약어를 변수로 사용하고 예약어를 이용할 경우 오류가 발생하는 것이다.
# int도 print와 같은 예약어 함수이지만 변수로 재지정이 가능하다.

nums_3.remove(7) # remove method로 7이라는 값을 찾아 제거한다.
print(nums_3)

#---------------------------------------
# 리스트 : 항목 확인
nums0 = [1,3,2,3,5]
print(2 in nums0) # in 연산자를 이용해서 list내에 2가 있는 지 확인 -> 있으면 True를 반환
print(4 not in nums0) # not in 연산자를 이용해서 4가 없는 지 확인 -> 없으면 True를 반환
print(nums0.count(3)) # nums0안에 3이란 게 몇개 존재하는 지 값의 빈도수를 확인해주는 count메소드

#----------------------------------------
# 내포(comprehension)

rng_1_10 = range(1,11)
# 짝수에 해당하는 값을 찾아서 거기에 2를 곱해서 새로운 list를 만들 거라면
# 그러면 내포는 기본적으로 새로운 객체를 만들 때 사용
list_2_even = [ 2 * v for v in rng_1_10 if v % 2 == 0] # 2로 나눈 나머지 값이 0이면 = 짝수이
print(list_2_even)
# for문이 list객체를 생성하는 리터럴 안에서 사용하는 것

