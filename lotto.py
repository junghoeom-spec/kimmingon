import random

def draw_lotto():
    numbers = sorted(random.sample(range(1, 46), 6))
    bonus = random.choice([n for n in range(1, 46) if n not in numbers])
    return numbers, bonus

def check_rank(my_numbers, winning_numbers, bonus):
    my_set = set(my_numbers)
    win_set = set(winning_numbers)
    match = len(my_set & win_set)
    has_bonus = bonus in my_set

    if match == 6:
        return 1
    elif match == 5 and has_bonus:
        return 2
    elif match == 5:
        return 3
    elif match == 4:
        return 4
    elif match == 3:
        return 5
    else:
        return None

def print_result(rank):
    prizes = {
        1: ("1등", "약 20억원"),
        2: ("2등", "약 6천만원"),
        3: ("3등", "약 150만원"),
        4: ("4등", "5만원"),
        5: ("5등", "5천원"),
    }
    if rank:
        name, prize = prizes[rank]
        print(f"  축하합니다! {name} 당첨! (상금: {prize})")
    else:
        print("  아쉽게도 낙첨되었습니다.")

def main():
    print("=" * 40)
    print("        로또 6/45 추첨 프로그램")
    print("=" * 40)

    while True:
        print("\n[메뉴]")
        print("  1. 자동 번호 생성")
        print("  2. 수동 번호 입력")
        print("  3. 종료")
        choice = input("\n선택: ").strip()

        if choice == "1":
            my_numbers = sorted(random.sample(range(1, 46), 6))
            print(f"\n  내 번호: {my_numbers}")

        elif choice == "2":
            try:
                raw = input("  번호 6개 입력 (공백 구분, 1~45): ")
                my_numbers = list(map(int, raw.split()))
                if len(my_numbers) != 6 or not all(1 <= n <= 45 for n in my_numbers):
                    print("  올바른 번호를 입력해주세요.")
                    continue
                if len(set(my_numbers)) != 6:
                    print("  중복 번호가 있습니다.")
                    continue
                my_numbers = sorted(my_numbers)
                print(f"\n  내 번호: {my_numbers}")
            except ValueError:
                print("  숫자를 입력해주세요.")
                continue

        elif choice == "3":
            print("\n  프로그램을 종료합니다.")
            break
        else:
            print("  올바른 메뉴를 선택해주세요.")
            continue

        # 당첨 번호 추첨
        winning, bonus = draw_lotto()
        print(f"  당첨 번호: {winning}  보너스: [{bonus}]")

        # 결과 확인
        rank = check_rank(my_numbers, winning, bonus)
        print_result(rank)

if __name__ == "__main__":
    main()
