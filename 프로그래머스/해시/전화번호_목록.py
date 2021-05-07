def solution(phone_book):
    phone_book.sort()

    for p, q in zip(phone_book[1:], phone_book[:-1]):
        if p.startswith(q):
            return False
    return True