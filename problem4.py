sentence = "the cat and the hat and the bat"

words = sentence.split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)

most_common = max(count, key=count.get)
print("Most common word:", most_common)
print("Count:", count[most_common])
