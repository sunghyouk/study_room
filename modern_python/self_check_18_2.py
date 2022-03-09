password = "robot fort flower graph"
space_count = 0
ch = 0

# while i < len(password):
#     if password[i] == " ":
#         space_count += 1
#     i += 1
# print(space_count)

for ch in password:
    if ch == " ":
        space_count += 1
print(space_count)
