import random
count = int(input("구매 수량을 입력해주세요 : "))
cnt = 1
lotto = []
while cnt <= count:
    i = 1
    while i <= 45:
        lotto.append(i)
        i += 1 # i = i + 1
    size = len(lotto)
    y = 1
    while y <= 6:
        size -= 1 # 44, 43,42
        idx = random.randint(0, size)
        result = lotto.pop(idx)    
        print(result, end=",")
        y += 1
    lotto.clear()
    print() 
    cnt += 1