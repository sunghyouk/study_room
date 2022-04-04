def zero_mat(n, p):
    """
    영행렬 생성
    입력값: 생성하고자 할 영행렬의 크기 n행, p열
    출력값: (n x p) 영행렬 Z
    """
    Z = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            row.append(0)
        Z.append(row)
    return Z


def deepcopy(A):
    """
    깊은 복사 (deepcopy) 구현
    입력값: 깊은 복사를 하고자 하는 행렬 리스트 A
    출력값: 깊은 복사된 결과 행렬 리스트 res
    """
    if type(A[0]) == list:
        n = len(A)
        p = len(A[0])
        res = zero_mat(n, p)  # 입력값 A와 동일한 크기인 영행렬을 생성
        for i in range(0, n):
            for j in range(0, p):
                res[i][j] = A[i][j]
        return res
    else:
        n = len(A)
        res = []
        for i in range(0, n):
            res.append(A[i])
        return res


def u_tri(A):
    """
    상 삼각 행렬 변환
    입력값: 상 삼각 행렬로 변환하고자 하는 행렬 A
    출력값: 행렬 A를 상 삼각 행렬로 변환시킨 행렬 utri
    """

    n = len(A)
    p = len(A[0])
    utri = []

    for i in range(0, n):
        row = []
        for j in range(0, p):
            if i > j:
                row.append(0)
            else:
                row.append(A[i][j])
        utri.append(row)
    return utri


def l_tri(A):
    """
    하 삼각 행렬 변환
    입력값: 하 삼각 행렬로 변환하고자 하는 행렬 A
    출력값: 행렬 A를 하 삼각 행렬로 변환시킨 행렬 ltri
    """

    n = len(A)
    p = len(A[0])
    ltri = []

    for i in range(0, n):
        row = []
        for j in range(0, p):
            if i < j:
                row.append(0)
            else:
                row.append(A[i][j])
        ltri.append(row)
    return ltri


def det_rec(A):

    """
    행렬 A의 행렬식 구하기 (재귀 방식을 이용)
    입력값: 행렬식을 구하고자 하는 행렬 A
    출력값: 행렬 A의 행렬식 res
    """

    n = len(A)
    res = 0

    # 2*2 행렬의 행렬식 구하기
    if n == 2:
        res = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return res

    # n*n 행렬의 행렬식 구하기
    for i in range(0, n):
        X = deepcopy(A)
        X = X[1:]
        nx = len(X)

        for j in range(0, nx):
            X[j] = X[j][0:i] + X[j][i+1:]

        sign = (-1) ** (i % 2)
        sub_det = det_rec(X)
        res += sign * A[0][i] * sub_det

    return res


def transpose(A):
    """
    행렬의 전치 행렬
    입력값: 전치 행렬을 구하고자 하는 행렬 A
    출력값: 행렬 A의 전치 행렬 At
    """

    n = len(A)
    p = len(A[0])

    At = []
    for i in range(0, p):
        row = []
        for j in range(0, n):
            val = A[j][i]
            row.append(val)
        At.append(row)
    return At


def scalar_mul(b, A):
    """
    행렬의 스칼라 곱
    입력값: 스칼라 곱을 수행할 스칼라 b, 행렬 A
    출력값: 스칼라 b와 행렬 A의 스칼라 곱 결과인 행렬 C
    """

    n = len(A)
    p = len(A[0])

    res = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            val = b * A[i][j]
            row.append(val)
        res.append(row)
    return res


def inv(A):
    """
    행렬 A의 역행렬 구하기
    입력값: 행렬 A
    출력값: 행렬 A의 역행렬 res
    """

    n = len(A)
    X = deepcopy(A)

    C = []
    for i in range(0, n):
        row_C = []
        idx_r = list(range(0, n))
        idx_r.remove(i)
        for j in range(0, n):
            idx_c = list(range(0, n))
            idx_c.remove(j)
            M = []
            for k in idx_r:
                row_M = []
                for lc in idx_c:
                    val = X[k][lc]
                    row_M.append(val)
                M.append(row_M)
            Mij = det_rec(M)
            Cij = ((-1)**(i+j))*Mij
            row_C.append(Cij)
        C.append(row_C)

    adj = transpose(C)
    res = scalar_mul(1/det_rec(X), adj)

    return res


def inner_product(a, b):
    """
    벡터의 내적
    입력값: 내적할 벡터 리스트 a, b
    출력값: 벡터 a, b의 내적 결과 res
    """
    n = len(a)
    res = 0
    for i in range(0, n):
        res += a[i] * b[i]
    return res


def norm(a):
    """
    벡터의 norm
    입력값: norm을 구하고자 하는 벡터 a
    출력값: 벡터 a의 norm 결과 res
    """

    n = len(a)
    res = 0
    for i in range(0, n):
        res += a[i]**2
    res = res**0.5
    return res


# 벡터의 외적
def outer_product(a, b):
    """
    벡터의 외적
    입력값: 외적할 벡터 리스트 a, b
    출력값: 벡터 a, b의 외적 결과 res
    """
    res = []
    n1 = len(a)
    n2 = len(b)
    for i in range(0, n1):
        row = []
        for j in range(0, n2):
            val = a[i] * b[j]
            row.append(val)
        res.append(row)
    return res


# 행렬의 뺄셈
def subtract(A, B):
    """
    행렬의 뺄셈
    입력값: 행렬의 뺄셈을 수행할 행렬 A, B
    출력값: 행렬 A와 행렬 B의 뺄셈 결과인 행렬 C
    """

    n = len(A)
    p = len(A[0])

    res = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            val = A[i][j] - B[i][j]
            row.append(val)
        res.append(row)
    return res


def identity(n):
    """
    단위 행렬 생성
    입력값: 단위 행렬의 크기 n
    출력값: n*n 단위 행렬 I
    """

    Iden = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        Iden.append(row)
    return Iden


def v_add(u, v):
    """
    벡터의 덧셈
    입력값: 더하고자 하는 벡터 u, v
    출력값: 벡터 u, v의 덧셈 결과 w
    """
    n = len(u)
    w = []

    for i in range(0, n):
        val = u[i] + v[i]
        w.append(val)

    return w


def sign(a):
    """
    스칼라 a의 부호
    입력값: 스칼라 a
    출력값: 스칼라 a가 a>=0이면 1, a<0이면 -1 출력
    """

    res = 1
    if a < 0:
        res = -1
    return res


def householder(v):
    """
    하우스홀더 행렬
    입력값: 하우스홀더 행렬을 생성할 리스트 v
    출력값: 리스트 v를 이용해 생성한 하우스홀더 행렬 H
    """
    n = len(v)
    outer_mat = outer_product(v, v)
    inner_val = inner_product(v, v)
    V = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            val = (2/inner_val)*outer_mat[i][j]
            row.append(val)
        V.append(row)
    H = subtract(identity(n), V)
    return H


def normalize(a):
    """
    벡터 a의 normalization
    벡터 a의 norm을 1로 만들어 줌
    입력값: normalize할 벡터 리스트 a
    출력값: 벡터 a를 normalization한 결과 벡터 리스트 v
    """
    n = len(a)
    v = []

    for i in range(0, n):
        tmp = a[i]/norm(a)
        v.append(tmp)
    return v


def qr_gram(A):
    """
    그램 슈미트 과정을 이용한 QR분해
    입력값: 행렬 A
    출력값: 행렬 A를 그램 슈미트 과정을 이용해 QR분해한 결과행렬 Q, R
    """

    n = len(A)
    At = transpose(A)

    U = []
    norm_list = []

    V = []
    Q = []
    R = []

    for i in range(0, n):
        if i == 0:
            u = At[i]
            norm_u = norm(u)
            U.append(u)
            norm_list.append(norm_u)
        else:
            a = At[i]
            dp_list = []
            for j in range(0, i):
                dp = inner_product(a, U[j])
                dp_list.append(dp)

            u = []
            for j in range(0, n):
                val = a[j]
                for k in range(0, i):
                    val -= (dp_list[k]/norm_list[k]**2) * U[k][j]
                u.append(val)
            norm_u = norm(u)
            U.append(u)
            norm_list.append(norm_u)

        v = normalize(u)
        V.append(v)

    Q = transpose(V)

    for i in range(0, n):
        r = []
        for j in range(0, n):
            if i > j:
                r.append(0)
            else:
                r_ele = inner_product(At[j], V[i])
                r.append(r_ele)
        R.append(r)

    return Q, R


# 행렬 곱
def matmul(A, B):
    """
    행렬의 행렬 곱
    입력값: 행렬 곱을 수행할 행렬 A, B
    출력값: 행렬 A와 행렬 B의 행렬 곱 결과인 행렬 res
    """

    n = len(A)
    p1 = len(A[0])
    p2 = len(B[0])

    res = []
    for i in range(0, n):
        row = []
        for j in range(0, p2):
            val = 0
            for k in range(0, p1):
                val += A[i][k] * B[k][j]
            row.append(val)
        res.append(row)
    return res


def qr_householder(A):

    import copy

    # n = len(A)
    p = len(A[0])

    H_list = []

    for i in range(0, p):
        if i == 0:
            A1 = copy.deepcopy(A)
            exA = A1
        elif i < p-1:
            Ai = []
            for j in range(1, len(exA)):
                tmp_row = []
                for k in range(1, len(exA[0])):
                    tmp_row.append(tmp_res[j][k])
                Ai.append(tmp_row)
            exA = Ai
        elif i == p-1:
            Ap = []
            for j in range(1, len(tmp_res)):
                Ap.append(tmp_res[j][1])
            exA = Ap

        # 첫번째 열 추출
        if i < p-1:
            a = transpose(exA)[0]
        else:
            a = exA
        nm = norm(a)

        # e1 생성
        e = [1]
        for j in range(0, len(a)-1):
            e.append(0)

        # v 생성
        tmp_e = []
        for j in range(0, len(e)):
            val = sign(a[0])*nm*e[j]
            tmp_e.append(val)
        v = v_add(a, tmp_e)

        # H 생성
        H = householder(v)

        # H*A
        if i == p-1:
            tmp_res = []
            for j in range(0, len(H)):
                val = 0
                for k in range(0, len(H[0])):
                    val += H[j][k] * exA[k]
                tmp_res.append(val)
        else:
            tmp_res = matmul(H, exA)

        H_list.append(H)

        if i > 0:
            tmp_H = identity(len(A))
            for j in range(i, len(A)):
                for k in range(i, len(A)):
                    tmp_H[j][k] = H_list[-1][j-i][k-i]
            H_list[-1] = tmp_H

    Q = copy.deepcopy(H_list[0])
    for j in range(0, len(H_list)-1):
        Q = matmul(Q, H_list[j+1])

    R = copy.deepcopy(H_list[-1])
    for j in range(1, len(H_list)):
        R = matmul(R, H_list[-(j+1)])
    R = matmul(R, A)

    return Q, R


def eig_qr(A):
    """
    행렬 A가 대칭 행렬이어야만 사용할 수 있음
    QR분해를 이용한 고유값, 고유 벡터 구하기
    입력값: 고유값, 고유 벡터를 구하고자 하는 행렬 A
    출력값: E = 고유값, V = 고유 벡터
    """

    n = len(A)
    E = deepcopy(A)
    V = identity(n)
    for i in range(0, 30):
        Q, R = qr_gram(E)
        E = matmul(R, Q)
        V = matmul(V, Q)

    return E, V
