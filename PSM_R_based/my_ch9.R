rm(list = ls())

# loading packages
library("Hmisc")              #가중평균, 가중분산
library("tidyverse")          #데이터관리 및 변수사전처리
summarize <- dplyr::summarize  #dplyr의 summarize 함수를 이용
library("optmatch")
library("Zelig")
library("MatchIt")
library("cobalt")
# Can't install: library("treatSens")
library("sensitivitymw")
library("sensitivityfull")

# loading data
setwd("/Users/sunghyouk/github/study_room/PSM_R_based/")
mydata <- read_csv("observational_study_survey.csv")

# preprocess
mydata <- mydata %>% mutate(
    gen20 = ifelse(gen == "20", 1, 0),
    gen30 = ifelse(gen == "30", 1, 0),
    gen40 = ifelse(gen == "40", 1, 0),
    gen50 = ifelse(gen == "50", 1, 0)
)

mydata <- mydata %>% filter(rally_con == 0) %>% select(-rally_con)

mydata$Rtreat <- ifelse(mydata$rally_pro == 1, 0, 1)

mydata <- mydata %>% rename(y = vote_will, treat = rally_pro)

# descriptive statistics
mean_SD_range <- function(myvariable) {
    myM <- format(round(mean(myvariable), 2), 2)
    mySD <- format(round(sd(myvariable), 2), 2)
    myMn <- format(round(min(myvariable), 2), 2)
    myMx <- format(round(max(myvariable), 2), 2)
    str_c(myM, "\n(", mySD, ")", "\n[", myMn, ", ", myMx, "]")
}

mean_SD <- function(myvariable) {
    myM <- format(round(mean(myvariable), 2), 2)
    mySD <- format(round(sd(myvariable), 2), 2)
    str_c(myM, "\n(", mySD, ")")
}

mydata %>%
group_by(treat) %>%
summarize_at(
    vars(y, female, edu:vote_past, gen20:gen50),
    mean_SD
) %>%
pivot_longer(cols = 2:14, names_to = "vars") %>%
mutate(treat = ifelse(treat == 0, "Control", "Treated")) %>%
pivot_wider(names_from = "treat", values_from = value) %>%
write.csv("DesStat_Table01.csv", row.names = FALSE)

# OLS regression
cvrt <- "female+gen20+gen30+gen40+gen50+edu+hhinc+libcon+int_eff+
      park_eva_a+good_eco+vote_past"
y_T_cov <- as.formula(str_c("y~treat+", cvrt))
OLS_estimands <- lm(y_T_cov, mydata) %>%
  confint("treat") %>%
  as_tibble()
names(OLS_estimands) <- c("LL95", "UL95")
OLS_estimands

# Propensity score analysis method application
att_formula <- as.formula(str_c("treat~", cvrt))
atc_formula <- as.formula(str_c("Rtreat~", cvrt))

# 1) IPTW
mydata$pscore <- glm(att_formula,
data = mydata,
family = binomial(link = "logit")) %>%
fitted()

mydata <- mydata %>%
mutate(
    Wate = ifelse(treat == 1, 1 / pscore, 1 / (1 - pscore)),
    Watt = ifelse(treat == 1, 1, 1 / (1 - pscore)),
    Watc = ifelse(treat == 1, 1 / pscore, 1)
)

# 2) Greedy matching using propensity score - matchIt package
# ATT
set.seed(1234)
greedy_att <- matchit(formula = att_formula,
data = mydata,
distance = "glm",
link = "linear.logit",
method = "nearest",
caliper = 0.15,
discard = "none",
ratio = 2,
replace = FALSE
)
summary(greedy_att)

# ATC
set.seed(4321)
greedy_atc <- matchit(atc_formula,
data = mydata,
distance = "glm",
link = "linear.logit",
method = "nearest",
caliper = 0.15,
discard = "none",
ratio = 2,
replace = TRUE
)

summary(greedy_atc)

# 3) Optimal matching using propensity score
# ATT
set.seed(1234)
optimal_att <- matchit(formula = att_formula,
data = mydata,
distance = "glm",
link = "linear.logit",
method = "optimal",
# caliper = 0.15,
discard = "none",
ratio = 2,
replace = FALSE)

summary(optimal_att)
# ATC - can't calculate

# 4) Full matching using propensity score
# ATT
set.seed(1234)
full_att <- matchit(formula = att_formula,
data = mydata,
distance = "glm",
link = "linear.logit",
method = "full",
discard = "none")

summary(full_att)

# ATC
set.seed(4321)
full_atc <- matchit(formula = atc_formula,
data = mydata,
distance = "glm",
link = "linear.logit",
method = "full",
discard = "none")

summary(full_atc)