from functools import reduce

users = [
    {"name": "Eva", "expenses": [75, 90, 60, 110]},
    {"name": "Frank", "expenses": [50, 80, 70, 95]},
    {"name": "Grace", "expenses": [200, 250, 180, 300]},
    {"name": "Henry", "expenses": [120, 80, 110, 150]},
    {"name": "Ivy", "expenses": [60, 70, 55, 75]},
    {"name": "Jack", "expenses": [180, 220, 160, 240]},
    {"name": "Katie", "expenses": [95, 110, 85, 120]},
    {"name": "Liam", "expenses": [70, 100, 90, 115]},
    {"name": "Mia", "expenses": [250, 280, 240, 290]},
    {"name": "Noah", "expenses": [110, 130, 105, 140]},
    {"name": "Olivia", "expenses": [300, 350, 290, 400]},
    {"name": "Peter", "expenses": [130, 160, 120, 170]},
    {"name": "Quinn", "expenses": [220, 260, 210, 280]},
    {"name": "Ryan", "expenses": [85, 95, 75, 105]},
    {"name": "Sophia", "expenses": [180, 210, 170, 220]},
    {"name": "Thomas", "expenses": [105, 120, 100, 130]},
    {"name": "Uma", "expenses": [240, 270, 230, 280]},
    {"name": "Victor", "expenses": [160, 190, 150, 200]},
    {"name": "Wendy", "expenses": [90, 105, 80, 115]},
    {"name": "Xander", "expenses": [350, 400, 330, 450]}
]

def filter_elemrnts(user):
    return True

def get_expenses_sum(user):
    user["expenses_sum"] = sum(user["expenses"])
    return user


users = list(filter(filter_elemrnts, users))
users = list(map(get_expenses_sum, users))

print(reduce(lambda x, y: x+y["expenses_sum"], users, users[0]["expenses_sum"]))