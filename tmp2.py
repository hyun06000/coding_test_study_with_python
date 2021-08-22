# 백준 5032번 탄산음료


# e : 가지고 있는 빈 병의 수
# f : 그날 발견한 빈 병의 수
# c : 새 병으로 바꾸는데 필요한 빈 병의 수
e, f, c = map(int,input().split(' '))

drink = [0]

def empty_bottles(bottles, exchange):
    new_bottles, remains = divmod(bottles, exchange)
    drink[0] += new_bottles

    total_remains = new_bottles + remains # 바꿔서 얻은 새 음료를 마시면 다시 빈 병이 생긴다.
    if total_remains < exchange:
        return 

    empty_bottles(total_remains, exchange)

empty_bottles(e + f, c)
print(drink[0])