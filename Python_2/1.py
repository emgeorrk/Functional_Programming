students = [
    {"name": "David", "age": 23, "grades": [87, 91, 89, 93]},
    {"name": "Eva", "age": 20, "grades": [80, 88, 86, 91]},
    {"name": "Frank", "age": 22, "grades": [75, 83, 79, 87]},
    {"name": "Grace", "age": 21, "grades": [90, 92, 87, 93]},
    {"name": "Henry", "age": 23, "grades": [84, 89, 85, 91]},
    {"name": "Ivy", "age": 20, "grades": [78, 84, 82, 88]},
    {"name": "Jack", "age": 22, "grades": [91, 93, 90, 94]},
    {"name": "Katie", "age": 21, "grades": [87, 90, 86, 92]},
    {"name": "Liam", "age": 23, "grades": [82, 87, 84, 90]},
    {"name": "Mia", "age": 20, "grades": [89, 91, 88, 93]},
    {"name": "Noah", "age": 22, "grades": [76, 82, 79, 85]},
    {"name": "Olivia", "age": 21, "grades": [94, 96, 92, 97]},
    {"name": "Peter", "age": 23, "grades": [85, 88, 83, 89]},
    {"name": "Quinn", "age": 20, "grades": [91, 94, 90, 95]},
    {"name": "Ryan", "age": 22, "grades": [79, 85, 78, 86]},
    {"name": "Sophia", "age": 21, "grades": [92, 94, 91, 95]},
    {"name": "Thomas", "age": 23, "grades": [87, 90, 86, 92]},
    {"name": "Uma", "age": 20, "grades": [83, 88, 85, 91]},
    {"name": "Victor", "age": 22, "grades": [90, 93, 89, 94]},
    {"name": "Wendy", "age": 21, "grades": [88, 91, 87, 93]}
]

def avg(student):
    student["avg_grade"] = sum(student["grades"])*1.0/len(student["grades"])
    return student

def filter_elemrnts(student):
    return True


students = list(filter(filter_elemrnts, students))
students = list(map(avg, students))
students.sort(key = lambda x: x["avg_grade"], reverse=True)

for i in range(len(students)):
    if students[0]["avg_grade"] == students[i]["avg_grade"]: print(students[i])
    else: break