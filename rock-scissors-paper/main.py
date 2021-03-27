import random
import os

usr_input = str(input("가위를 내려면 A, 바위를 내려면 B, 보자기를 내려면 C를 입력하십시오> "))


def a_set():
    if usr_input == "A":
        print("사용자: 가위")
        print("-------------------------------->", " 비겼습니다.")

    if usr_input == "B":
        print("사용자: 바위")
        print("-------------------------------->", " 당신이 이겼습니다.")

    if usr_input == "C":
        print("사용자: 보자기")
        print("-------------------------------->", " 당신이 패배했습니다.")


def b_set():
    if usr_input == "A":
        print("사용자: 가위")
        print("-------------------------------->", " 당신이 졌습니다.")

    if usr_input == "B":
        print("사용자: 바위")
        print("-------------------------------->", " 비겼습니다.")

    if usr_input == "C":
        print("사용자: 보자기")
        print("-------------------------------->", "당신이 이겼습니다.")


def c_set():
    if usr_input == "A":
        print("사용자: 가위")
        print("-------------------------------->", " 당신이 이겼습니다.")

    if usr_input == "B":
        print("사용자: 바위")
        print("-------------------------------->", " 당신이 졌습니다.")

    if usr_input == "C":
        print("사용자: 보자기")
        print("-------------------------------->", " 비겼습니다.")


def chk_usr_validate():
    if usr_input == "A":
        pass

    elif usr_input == "B":
        pass

    elif usr_input == "C":
        pass

    else:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")
        os.system("pause")


def main():
    a_list = ("A", "B", "C")
    a = random.choice(a_list)

    if a == "A":
        print("컴퓨터: 가위")
        a_set()
    if a == "B":
        print("컴퓨터: 바위")
        b_set()
    if a == "C":
        print("컴퓨터: 보자기")
        c_set()


def input_re():
    usr_input_re = str(input("가위를 내려면 A, 바위를 내려면 B, 보자기를 내려면 C를 입력하십시오> "))
    chk_usr_validate()
    main()
    whether_retry()


def whether_retry():  # 다시 하는 기능
    retry_usr = str(input("다시 하시겠습니까? (Y/N) > "))
    if retry_usr == "Y":
        input_re()

    if retry_usr == "N":
        os.system("pause")


chk_usr_validate()
main()
whether_retry()
