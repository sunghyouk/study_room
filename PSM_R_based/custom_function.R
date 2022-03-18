library(Zelig)

# 균형성 점검을 위한 이용자함수 설정
balance_check_PSW <- function(var_treat, var_cov, var_wgt) {
  std_var_cov <- (var_cov - mean(var_cov)) / sd(var_cov)
  simple_M1 <- mean(std_var_cov[var_treat == 1])
  simple_M0 <- mean(std_var_cov[var_treat == 0])
  simple_V1 <- var(std_var_cov[var_treat == 1])
  simple_V0 <- var(std_var_cov[var_treat == 0])
  wgted_M1 <- Hmisc::wtd.mean(x = std_var_cov[var_treat == 1], weights = var_wgt[var_treat == 1])
  wgted_M0 <- Hmisc::wtd.mean(x = std_var_cov[var_treat == 0], weights = var_wgt[var_treat == 0])
  wgted_V1 <- Hmisc::wtd.var(x = std_var_cov[var_treat == 1], weights = var_wgt[var_treat == 1])
  wgted_V0 <- Hmisc::wtd.var(x = std_var_cov[var_treat == 0], weights = var_wgt[var_treat == 0])
  B_wgt_Mdiff <- simple_M1 - simple_M0
  B_wgt_Vratio <- simple_V1 / simple_V0
  A_wgt_Mdiff <- wgted_M1 - wgted_M0
  A_wgt_Vratio <- wgted_V1 / wgted_V0
  balance_index <- tibble(B_wgt_Mdiff, A_wgt_Mdiff,
                         B_wgt_Vratio, A_wgt_Vratio)
  balance_index
}

# ATT추정을 위한 이용자정의 함수
SUMMARY_EST_ATT <- function(myformula, matched_data, n_sim, model_name) {
  # 2단계: 모형추정
  z_model <- zelig(as.formula(myformula),
                data = matched_data,
                model = "ls",
                weights = "weights", cite = FALSE)
  # 3단계: 추정된 모형을 적용할 X변수의 조건상정
  x_0 <- setx(z_model, treat = 0, data = matched_data) #통제집단가정 상황
  x_1 <- setx(z_model, treat = 1, data = matched_data) #처치집단가정 상황
  # 4단계: 1단계와 2단계를 근거로 기댓값(expected value, ev) 시뮬레이션
  s_0 <- sim(z_model, x_0, num = n_sim)
  s_1 <- sim(z_model, x_1, num = n_sim)
  # 5단계: ATT의 값을 추정한 후 95%신뢰구간 계산
  EST1 <- get_qi(s_1, "ev") - get_qi(s_0, "ev")
  summary_est1 <- tibble(
    LL95 = quantile(EST1, p = c(0.025)),
    PEst = quantile(EST1, p = c(0.500)),
    UL95 = quantile(EST1, p = c(0.975)),
    estimand = "ATT", model = model_name
  )
  rm(z_model, x_0, x_1, s_0, s_1)
  list(EST1, summary_est1)
}

# ATC추정을 위한 이용자정의 함수
SUMMARY_EST_ATC <- function(myformula, matched_data, n_sim, model_name) {
  # 2단계: 모형추정
  z_model <- zelig(as.formula(myformula),
                data = matched_data,
                model = "ls",
                weights = "weights", cite = FALSE)
  # 3단계: 추정된 모형을 적용할 X변수의 조건상정
  x_0 <- setx(z_model, Rtreat = 1, data = matched_data) #통제집단가정 상황(이 부분 주의)
  x_1 <- setx(z_model, Rtreat = 0, data = matched_data) #처치집단가정 상황(이 부분 주의)
  # 4단계: 1단계와 2단계를 근거로 기댓값(expected value, ev) 시뮬레이션
  s_0 <- sim(z_model, x_0, num = n_sim)
  s_1 <- sim(z_model, x_1, num = n_sim)
  # 5단계: ATT의 값을 추정한 후 95%신뢰구간 계산
  EST1 <- get_qi(s_1, "ev") - get_qi(s_0, "ev")
  summary_est1 <- tibble(
    LL95 = quantile(EST1, p = c(0.025)),
    PEst = quantile(EST1, p = c(0.500)),
    UL95 = quantile(EST1, p = c(0.975)),
    estimand = "ATC", model = model_name
  )
  rm(z_model, x_0, x_1, s_0, s_1)
  list(EST1, summary_est1)
}