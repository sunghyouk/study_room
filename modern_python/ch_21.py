# 함수의 예제

def take_attendance(classroom_roaster, who_is_here):
    '''
    docstring에 들어갈 내용:
    1) 입력:
    classroom_roaster, tuple # 자료형 명시
    who_is_here, tuple

    2) 계산 과정
    classroom_roaster에 있는 모든 사람이
    who_is_here에 들어 있는지 검사
    학생이 who_is_here에 있는 경우에 그 이름을 출력

    3) 출력
    returns "출석 부르기 끝"
    '''

    for kid in classroom_roaster:
        if kid in who_is_here:
            print(kid)
    return "출석 부르기 끝"
