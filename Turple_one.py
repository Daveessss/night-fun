

students =[
    ("Alice",78),
    ("Bob",45),
    ("Charlie",90),
    ("Diana",62),
    ("Kent",30)
]
for name, score in students:
    print(name)
    print(score)


print("\n")
print("The names and grades of students who scored 60 and above ")
for name, score in students:
    if score >= 60:
        print(name , score, "\n")
#        print(score)


print(" ")
count = 0
for name, grade in students:
    if grade >= 50
    count = count + 1
print(f'The amount of students that passed is {count}')
