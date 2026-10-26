word = "Programming"
# Print the word reversed using slicing
reverse=word[ : :-1]
print(f"The reverse of Programming is {reverse}")

# Print the first 3 and last 3 characters on one line
start_3=word[0:3]
end_3=word[-3:]
print(f"the first and last three words of Programming {start_3 }  {end_3}") 

# Count how many times "m" appears
c=word.count("m")
print(f"The m appears {c} times in programming")

# Write is_palindrome(s); test it on "level" and "python"
S = input("Enter the word to check palindrome: ")

def is_palindrome(S):
    rev = S[::-1]
    return S == rev

print(is_palindrome(S))
