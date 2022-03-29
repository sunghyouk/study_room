def read_file(file):
    """
    file, 파일 객체
    첫 번째 줄부터 시작해서 매 두 번째 줄을 튜플에 넣는다
    두 번째 줄부터 시작해서 매 두 번째 줄을 다른 튜플에 넣는다
    Returns 두 튜플로 이뤄진 튜플
    """

    first_every_2 = ()
    second_every_2 = ()
    line_count = 0

    for line in file:
        stripped_line = line.replace("\n", "")
        if line_count % 2 == 0:
            first_every_2 += (stripped_line, )
        elif line_count % 2 == 1:
            second_every_2 += (stripped_line, )
        line_count += 1
    return (first_every_2, second_every_2)


def sanitize(some_tuple):
    """
    phones, 문자열이 들어 있는 튜플
    튜플에 들어 있는 문자열에서 모든 대시, 공백, 괄호를 없앤다
    Returns 대시, 공백, 괄호를 없앤 문자열로 이뤄진 새 튜플
    """

    clean_string = ()

    for st in some_tuple:
        st = st.replace(" ", "")
        st = st.replace("-", "")
        st = st.replace("(", "")
        st = st.replace(")", "")
        clean_string += (st, )
    return clean_string


def analyze_friends(names, phones, all_areacodes, all_places):
    """
    names, 친구 이름이 들어 있는 튜플
    phones, 친구 전화번호 (특수문자는 없앤)가 들어 있는 튜플
    all_areacodes, 지역 코드가 들어 있는 튜플
    all_places, 지역 코드에 대한 주 이름이 들어 있는 튜플
    친구가 몇 명인지와 친구들의 전화번호가 속한 주 목록을 표시한다
    (이때 같은 주는 한 번만 표시)
    """

    def get_unique_area_codes():
        """
        Returns phones에 있는 지역 코드 목록 (중복된 경우 1개만 포함)
        """

        area_codes = ()
        for ph in phones:
            if ph[0:3] not in area_codes:
                area_codes += (ph[0:3], )
        return area_codes

    def get_states(some_areacodes):
        """
        some_areacodes, 지역 코드가 들어 있는 튜플
        Returns 지역 코드에 해당하는 주 이름이 들어 있는 튜플
        """

        states = ()
        for ac in some_areacodes:
            if ac not in all_areacodes:
                states += ("BAD AREACODE", )
            else:
                index = all_areacodes.index(ac)
                states += (all_places[index], )
        return states

    num_friends = len(names)
    unique_area_codes = get_unique_area_codes()
    unique_states = get_states(unique_area_codes)
    print("You have ", num_friends, "friends!")
    print("They live in ", unique_states)
