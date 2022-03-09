"""
목표:
사용자에게 이름, 성 순서로 성명을 두 개 입력하라고 요청 - input()
사용자에게 새로운 이름 조합을 이름, 성 순서로 보여준다.
새로운 이름은 사용자가 입력한 이름을 조합하고, 새로운 성은 사용자가 입력한 성을 조합.
"""

"""
pseudocode:
사용자 입력을 받아서 변수에 저장
전체 이름을 이름과 성으로 분리
이름을 어떻게 잘라서 조합할지 결정
한 이름의 앞부분과 다른 이름의 뒷부분을 합친다.
"""

# 사용자 이름 2개 받기
print("Welcome to the Mashup Game!")
name1 = input("Enter one full name (First Last): ")
name2 = input("Enter another full name (First Last): ")

# 성과 이름으로 분리
space = name1.find(" ")
name1_first = name1[0:space]
name1_last = name1[space+1:len(name1)]

space = name2.find(" ")
name2_first = name2[0:space]
name2_last = name2[space+1:len(name2)]

# 분리한 것을 2로 나눠 홀짝의 경우로 나눠서 처리
len_name1_first = len(name1_first)
len_name2_first = len(name2_first)
len_name1_last = len(name1_last)
len_name2_last = len(name2_last)

index_name1_first = int(len_name1_first/2)
index_name2_first = int(len_name2_first/2)
index_name1_last = int(len_name1_last/2)
index_name2_last = int(len_name2_last/2)

lefthalf_name1_first = name1_first[0:index_name1_first]
righthalf_name1_first = name1_first[index_name1_first:len_name1_first]
lefthalf_name2_first = name2_first[0:index_name2_first]
righthalf_name2_first = name2_first[index_name2_first:len_name2_first]
lefthalf_name1_last = name1_last[0:index_name1_last]
righthalf_name1_last = name1_last[index_name1_last:len_name1_last]
lefthalf_name2_last = name2_last[0:index_name2_last]
righthalf_name2_last = name2_last[index_name2_last:len_name2_last]

# 이름 조합하기
newname1_first = lefthalf_name1_first.capitalize() + \
        righthalf_name2_first.lower()
newname1_last = lefthalf_name1_last.capitalize() + \
        righthalf_name2_last.lower()

newname2_first = lefthalf_name2_first.capitalize() + \
        righthalf_name1_first.lower()
newname2_last = lefthalf_name2_last.capitalize() + \
        righthalf_name1_last.lower()

print("All done! Here are two possibilities, pick the one you like best!")
print(newname1_first, newname1_last)
print(newname2_first, newname2_last)
