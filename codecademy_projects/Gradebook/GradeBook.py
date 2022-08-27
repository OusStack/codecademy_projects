# Codeacademy
# Python_3-Lists-Gradebook

subjects = ["physics", "calculus", "poetry", "history"]
grade = [98, 97, 85, 88]

gradebook = []

for i in range(4):
    temp = [subjects[i], grade[i]]
    gradebook.append(temp)
print(gradebook)

gradebook.append(["computer Science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)

gradebook[-1][-1] = gradebook[-1][-1] + 5
print(gradebook)

for subjects in gradebook:
    if subjects[1] >= 90:
        subjects[1] = "Pass"
    else:
        subjects[1] = "Fail"
print(gradebook)

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

# empty line