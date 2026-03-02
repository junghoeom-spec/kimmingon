def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

def main():
    print("=== 간단한 계산기 ===")
    while True:
        print("\n연산 선택: +, -, *, /  (종료: q)")
        op = input("연산자 입력: ").strip()
        if op == "q":
            break
        if op not in ("+", "-", "*", "/"):
            print("올바른 연산자를 입력하세요.")
            continue
        try:
            a = float(input("첫 번째 숫자: "))
            b = float(input("두 번째 숫자: "))
        except ValueError:
            print("숫자를 입력하세요.")
            continue

        if op == "+":
            print(f"결과: {add(a, b)}")
        elif op == "-":
            print(f"결과: {subtract(a, b)}")
        elif op == "*":
            print(f"결과: {multiply(a, b)}")
        elif op == "/":
            try:
                print(f"결과: {divide(a, b)}")
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()
