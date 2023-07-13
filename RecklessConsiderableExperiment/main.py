'''
print("Hello world!")

a = 2  # 0x0001
b = 3  # 0x0002
c = a + b  # 0x0003
print(c)

# variable은 메모리 주소에 해당 값을 집어 넣는 것
# python read code top to bottom
c = 1
print(c)
a = 10
b = 1
print(c)
# the value of "c" didn't change

# if you want to create a variable that variable has a space on each name, you shouldn't write the space
# you shouldn't start variable with numbers. Start just with text

# my_name = hojun
# 'hojun' is not defined / 여기서 의미하는 것은 hojun을 variable로 본다는 것. but hojun을 정의하지 않음
# text를 입력하고 싶을 경우
# boolean의 경우 True or False 로 쓰면 됨(반드시 첫글자는 대문자여야 함) "False"랑은 매우 다름 0과 1

my_name = "hojun"
age = 20
dead = False
print("Hello my name is", my_name)
print("and I'm", age, "years old")


# funciton은 def를 이용해서 정의 할 수 있고, 코드를 매번 다시 짤 필요 없이 재사용 가능하게 하는 것
# variable하고 다른 것은 정의할 때 variable은 앞에 아무것도 쓰지 않았지만, function의 경우 def를 사용
def say_hello():
  print("hello how r u?")


say_hello
# function은 play 버튼이 따로 있어서 그냥 쓴다고 해서 호출되지 않는다.
say_hello()


# 어떻게 function에 data를 넣는지
# python은 빈 공간을 활용해서 안에 어떤 것이 있는지 이해하기 때문에 절대로 def 아래에 print를 들여쓰기 없이 붙여 쓰면 않된다. 빈 공간을 주어야 안에 무언가 들어있다는 의미를 준다.
# 위의 function은 값을 받을 공간이 없다. 정의해 주지 않았으니까
def say_hello_name(
  user_name, user_age
):  # 여기서 user_name이라는 데이터를 받는 것이다. / multi parameter 그리고 이 상태로 아래 say_hello_name("hojun") 을 실행하면 error가 발생(필수 argument가 없다고 나옴)
  print("Hello", user_name,
        "how are you?")  # user_name is parameter(플레이스 홀더/그릇)
  print("you are", user_age, "years old")


# say_hello_name("hojun") # hojun is argument(실제 데이터)

say_hello_name("hojun", 20)

# 질문 : print는 몇 개의 argument가 가능할까?
# say_hello_name 데이터를 만들 때는 데이터를 위한 공간으로 2개를 만들었는데 그렇다면 print는 몇 개의 공간이 있을까? 무한대의 공간
'''


# 편의상 위의 전 과정 다 주석처리
def say_hello(user_name="anonymous"
              ):  # user_name -> user_name= 로 바꾸는 것 만으로도 argument가 주어지지 않은 경우에
  print("hello", user_name)


say_hello("hojun")
say_hello(
)  # 이렇게 user_name을 입력하지 않으면 기본적으로 에러를 일으키지만, default값을 지정해줌으로써 에러를 피할 수 있다.
# hojun의 경우 프로세스가 user_name="anonymous"라는 parameter전체가 argument로 바뀌지만, argument가 없을 경우 parameter가 치환되지 않고 내용 그대로 적용된다.
