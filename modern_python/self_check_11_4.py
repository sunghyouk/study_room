celeb = input("Who is your favorite singer? (last name first name) ")
space = celeb.find(" ")

print(celeb[0:space])
print(celeb[space+1:])
