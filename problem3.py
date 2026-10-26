words = ["ai", "python", "data"]
square=[n*n for n in range(1,11) if n%2==0]
print (f"The square of even number from 1 to 10 {square}")

# A dict mapping each word to its length

result = {word: len(word) for word in words}
print(result)

word = "banana"

result = sorted(set(word))
print(result)




\

