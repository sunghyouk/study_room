from scipy.spatial.distance import pdist, squareform
from numpy import exp
from scipy.linalg import eigh
import numpy as np

def rbf_kernel_pca(X, gamma, n_components):
    """
    RBF 커널 PCA 구현
    
    매개변수
    ----------
    X: {넘파이 ndarray}, shape = [n_samples, n_features]
    
    gamma: float
        RBF 커널 튜닝 매개변수
        
    n_components: int
        반환할 주성분 개수
        
    반환값
    ----------
    alphas: {넘파이 ndarray}, shape = [n_samples, k_features]
        투영된 데이터셋
        
    lambdas: list
        
    """
    # M * N 차원의 데이터셋에서 샘플 간의 유클리디안 거리의 제곱을 계산
    sq_dists = pdist(X, 'sqeuclidean')
    
    # 샘플 간의 거리를 정방 대칭 행렬로 변환
    mat_sq_dists = squareform(sq_dists)
    
    # 커널 행렬을 계산
    K = exp(-gamma * mat_sq_dists)
    
    # 커널 행렬을 중앙에 맞춤
    N = K.shape[0]
    one_n = np.ones((N, N)) / N
    K = K - one_n.dot(K) - K.dot(one_n) + one_n.dot(K).dot(one_n)
    
    # 중앙에 맞춰진 커널 행렬의 고유값과 고유 벡터를 구함
    # scipy.linalg.eigh 함수는 오름차순으로 반환됨
    eigvals, eigvecs = eigh(K)
    eigvals, eigvecs = eigvals[::-1], eigvecs[:, ::-1]
    
    # 최상위 k개의 고유 벡터를 선택 (투영 결과)
    alphas = np.column_stack([eigvecs[:, i]
                              for i in range(n_components)])
    
    # 고유 벡터에 상응하는 고유값을 선택
    lambdas = [eigvals[i] for i in range(n_components)]
    
    return alphas, lambdas
