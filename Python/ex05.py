def find(ordered_list, element_to_find):
    for element in ordered_list: #list 내 탐색할 때 for문으로
        if element == element_to_find: # 같은 거 있는지 확인
            return True
    return False # 루프 빠져나와서 (else 필요 없음)

a = [2,4,6,8,10]
print(a)
print("{} => {}".format(5,find(a,5)))
print("{} => {}".format(10,find(a,10)))
