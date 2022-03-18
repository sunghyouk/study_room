# loading packages
library("optmatch")
library("tidyverse")
library("Zelig")
library("MatchIt")
library("cobalt")
library("treatSens")
library("sensitivitymw")
library("sensitivityfull")

# loading data
setwd("/Users/sunghyouk/github/study_room/PSM_R_based/")
mydata <- read_csv("observational_study_survey.csv")

# preprocess
mydata <- mydata %>% mutate(
    gen20 <- ifelse(gen == "20s", 1, 0),
    gen30 <- ifelse(gen == "30s", 1, 0),
    gen40 <- ifelse(gen == "40s", 1, 0),
    gen50 <- ifelse(gen == "50s", 1, 0)
)

mydata <- mydata %>% filter(rally_con == 0) %>% select(-rally_con)

mydata$Rtreat <- ifelse(mydata$rally_pro == 1, 0, 1)

mydata <- mydata %>% rename(y = vote_will, treat = rally_pro)
