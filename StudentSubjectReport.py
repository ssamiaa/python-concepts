# Nested Dictionary Q1a 
marks = {"Alice" : {'Math' : 90, 'English' : 40, 'Science' : 50}, 
         "Bob" : {'Math' : 50, 'English' : 60, 'Science' : 70},
         "Charlie" : {'Math' : 80, 'English' : 90, 'Science' : 100},
         "David" : {'Math' : 80, 'English' : 30, 'Science' : 70},}

subjects = ["Math", "English", "Science"]


# To find the subject wise topper Q1c 
for subject in subjects: 
    topper = ''
    highest = -1

    for student, subjects in marks.items():
        if subjects[subject] > highest:
            highest = subjects[subject]
            topper = student

    print (f"Topper in {subject} is {topper}")

# To find the average marks for each student Q1b, Q1d
for student, subjects in marks.items():
    for subject, score in subjects.items():
        average = sum(subjects.values()) / len(subjects)
        total = sum(subjects.values())

    print (f"Average marks for {student} in {subject} is {average}")
    print (f"Total marks for {student} in {subject} is {total}")


         