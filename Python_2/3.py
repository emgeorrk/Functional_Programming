orders = [
    {"order_id": 1, "customer_id": 101, "amount": 150.0},
    {"order_id": 2, "customer_id": 102, "amount": 200.0},
    {"order_id": 3, "customer_id": 101, "amount": 75.0},
    {"order_id": 4, "customer_id": 103, "amount": 100.0},
    {"order_id": 5, "customer_id": 101, "amount": 50.0},
    {"order_id": 6, "customer_id": 104, "amount": 125.0},
    {"order_id": 7, "customer_id": 102, "amount": 90.0},
    {"order_id": 8, "customer_id": 105, "amount": 180.0},
    {"order_id": 9, "customer_id": 103, "amount": 70.0},
    {"order_id": 10, "customer_id": 101, "amount": 110.0},
    {"order_id": 11, "customer_id": 104, "amount": 160.0},
    {"order_id": 12, "customer_id": 102, "amount": 220.0},
    {"order_id": 13, "customer_id": 105, "amount": 95.0},
    {"order_id": 14, "customer_id": 103, "amount": 120.0},
    {"order_id": 15, "customer_id": 101, "amount": 55.0},
    {"order_id": 16, "customer_id": 104, "amount": 130.0},
    {"order_id": 17, "customer_id": 102, "amount": 240.0},
    {"order_id": 18, "customer_id": 105, "amount": 110.0},
    {"order_id": 19, "customer_id": 103, "amount": 85.0},
    {"order_id": 20, "customer_id": 101, "amount": 70.0}
]

print("customer id: ", end='')
fid = int(input())

def filter_elements(user):
    if user["customer_id"] == fid: return True
    else: return False

orders = list(filter(filter_elements, orders))
for x in orders: print(x)
amounts = list(zip([x["customer_id"] for x in orders], [y["amount"] for y in orders]))
summa = sum([x[1] for x in amounts])
print("Sum = ", summa)
print("Avg sum = ", round(summa*1.0/len(amounts), 3))