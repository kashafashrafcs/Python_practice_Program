marks = [88,45,92,67,30,75]
#Count how many marks are 50 or more
count=0
for m in marks:
    if m >= 50:
        count+=1
#Print the average with 1 decimal place      

average=0 
length=len(marks)
s=sum(marks)
length=len(marks)
average=s/length

# Print the highest and lowest mark

hihgest_marks=max(marks)
lowest_marks=min(marks)
#print
print(f"The number of  marks 50 or more= {count}")
print(f"The average of marks with 1 decimal {average:.1f}")
print(f"The highest marks = {hihgest_marks}")
print(f"The lowest marks ={lowest_marks}")

