lyrics = "Happy birthday to you Happy birthday to you Happy birthday to you dear Frank Happy birthday to you"

counts = {}
words = lyrics.split(" ")

for w in words:
    w = w.lower()
    if w not in counts:
        counts[w] = 1
    else:
        counts[w] += 1

print(counts)
