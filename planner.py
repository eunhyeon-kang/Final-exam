# 스터디 플래너 기본 틀

# 스터디 일정을 저장할 리스트
study_plan = []

# 사용자 메뉴 코드입니당.
def show_menu():
    print("\n=== 스터디 플래너 ===")
    print("1. 과목 추가")
    print("2. 공부 해야하는 과목들 보기")
    print("3. 과목목 삭제")
    print("4. 종료")

# 공부 일정 추가 함수입니다.
def add_plan():
    date = input("날짜를 입력하세요 (ex) 2001.03.15 : ")
    subject = input("공부 할 과목을 입력하세요: ")
    study_plan.append({"날짜": date, "과목": subject})
    print("공부 할 과목이 추가되었습니당당")

# 공부 할 과목목 표시 함수 입니다.
def view_plans():
    if not study_plan:
        print("공부 할 과목이 없으니, 자유롭게 쉬세요~~ ")
    else:
        print("\n공부 할 과목 :")
        index = 1
        for plan in study_plan:
            print(f"{index}. {plan['날짜']} - {plan['과목']}")
            index += 1

# 과목 삭제 함수입니다다
def delete_plan():
    view_plans()
    if study_plan:
        index = input("삭제 할 과목 번호를 입력하세여여: ")
        if index.isdigit():
            index = int(index) - 1
            if 0 <= index < len(study_plan):
                deleted = study_plan[index]
                del study_plan[index]
                print(f"삭제된 과목목: {deleted['날짜']} - {deleted['과목']}")
            else:
                print("오류요")
        else:
            print("숫자를 선택해주세여여.")

# 메인 함수로써 프로그램 실행시 보여질 메뉴의 내용입니다.
def main():
    while True:
        show_menu()
        menu = input("1~4번 중 원하는 메뉴를 입력하세용용: ")
        if menu == "1":
            add_plan()
        elif menu == "2":
            view_plans()
        elif menu == "3":
            delete_plan()
        elif menu == "4":
            print("종료료")
            break
        else:
            print("오류, 다시 입력하쇼쇼")

if __name__ == "__main__":
    main()