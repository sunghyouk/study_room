
def make_sentence(who, what):
    doing = who + " is " + what
    return doing


def show_story(person, action, number, thing):
    what = make_sentence(person, action)
    num_times = str(number) + " " + thing
    my_story = what + " " + num_times
    print(my_story)


who = "Hector"
what = "eating"
thing = "bananas"
number = 8

sentence = make_sentence(who, thing)
print(make_sentence(who, what))

your_story = show_story(who, what, number, thing)
my_story = show_story(sentence, what, number, thing)

print(your_story)  # None 출력
