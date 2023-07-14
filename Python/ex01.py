s = input("1~9사이의 정수를 입력하세요:")
n = int("%s" % s)
nn = int("%s%s" % (s,s))
nnn = int("%s%s%s" % (s,s,s))
nnnn = int("%s%s%s%s" % (s,s,s,s))
sum = n + nn + nnn + nnnn
print(sum)
