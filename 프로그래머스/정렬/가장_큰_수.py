def solution(numbers):
    def sort_key(x: str) -> str:
        return (x * 4)[:4]

    numbers = sorted([str(n) for n in numbers],
                     reverse=True,
                     key=sort_key)
    return str(int(''.join(numbers)))