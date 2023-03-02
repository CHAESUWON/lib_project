from functions_for_lib import *

# 고민거리 : 책 이름 조회할 때, 저자명 조회할 때 비슷한것도 출력할 것인가? 특히 저자명

# _________________________________ 변수 _________________________________________


log_in_check = False
book_to_rent = []

# _________________________________ 실행 구문 ____________________________________

while True:
    # 인터페이스 (V) - 예외처리 완료
    print("\n\n")
    print("1. 로그인")  ---
    print("2. 회원가입")
    print("Q. 나가기")

    first_num = input("\n선택지를 선택해주세요 >> ")
    print()
  
    # 1. 로그인 (V)
    if first_num == '1':
        #로그인 함수 RETURN 값 형식
        # [True/False, 사용자 ID]

        log_in_data = log_in()
        log_in_check = log_in_data[0]
        log_in_ID = log_in_data[1]
        
    # 2. 회원가입 (V)
    elif first_num == '2':
        # 회원가입을 하는 함수
        # RETURN 값 없음
        sign_in() 

    # 3. 나가기 (V)
    elif first_num.upper() == 'Q':
        print("프로그램 종료")
        break

    # 4. 예외처리 (V)
    else:
        print("오류 : 잘못입력하셨습니다.")


    # 로그인 완료시 들어가는 인터페이스 - 예외처리 완료
    while log_in_check:
        
        print("\n\n")
        # && 문제 있는지 확인
        print(f"[*** 로그인된 계정: { log_in_ID } ***]\n")

        # 유저의 빌린책 목록 출력
        count = 1
        print("-"*10, f"[{log_in_ID}]의 빌린 책 목록", "-"*10)
        for row in return_result_from_Oracle():
            # 아이디 입력받아와야함
            if row[0] == log_in_ID:
                print((count), row[1:-1])
                count += 1
        user_rent_book_num = count
        count = 1
        
        print("-"*42)
        print("(최대로 빌릴 수 있는 책의 수 : 5권)")
        print("\n")

        print("1. 도서 조회 - ")
        print("2. 도서 대여 - ")
        print("3. 도서 반납 - ")
        print("Q. 로그아웃\n\n")

        second_num = input("선택지를 선택해주세요 >> ")
        print()

        # 1. 책 찾기
        if second_num == '1':
            search_book(book_to_rent)

        # 2. 도서 대여
        elif second_num == '2':
            rent_book(book_to_rent, log_in_ID)

        # 2. 도서 반납
        elif second_num == '3':
            return_book(log_in_ID)

        # 4. 로그아웃 (V)
        elif second_num.upper() == 'Q':
            print(f"계정: { log_in_ID } | 로그아웃 완료")
            # 장바구니 비우기
            book_to_rent = []
            log_in_check = False
            break

        else:
            print("오류 : 잘못입력하셨습니다.")