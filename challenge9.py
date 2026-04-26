import copy
def build_inventory():
    items_list = [
        {
            "item": "Laptop",
            "info": {
                "price": 50000,
                "stock": 10,
                "supplier": {"name": "Dell", "rating": 4.5}
            }
        },
        {
            "item": "Phone",
            "info": {
                "price": 20000,
                "stock": 25,
                "supplier": {"name": "Samsung", "rating": 4.2}
            }
        }
    ]
    return items_list
def update_data(dataset, roll_no):
    pos = roll_no % len(dataset)
    for j in range(len(dataset)):
        dataset[j]["info"]["price"] = int(dataset[j]["info"]["price"] * 0.9)
        if j == pos:
            dataset[j]["info"]["stock"] -= 5
            dataset[j]["info"]["supplier"]["rating"] += 0.1
def check_difference(data1, data2):
    diff = 0
    same = 0
    for k in range(len(data1)):
        if data1[k] != data2[k]:
            diff += 1
        else:
            same += 1
    return (diff, same)
roll_no = int(input("Enter roll number: "))
main_data = build_inventory()
original_copy = copy.deepcopy(main_data)
copy_shallow = main_data.copy()
copy_deep = copy.deepcopy(main_data)
update_data(copy_shallow, roll_no)
update_data(copy_deep, roll_no)
print("\n---- ORIGINAL DATA ----")
for idx, val in enumerate(main_data):
    print(idx, "->", val)
print("\n---- SHALLOW COPY ----")
for idx, val in enumerate(copy_shallow):
    print(idx, "->", val)
print("\n---- DEEP COPY ----")
for idx, val in enumerate(copy_deep):
    print(idx, "->", val)
result_shallow = check_difference(original_copy, copy_shallow)
result_deep = check_difference(original_copy, copy_deep)
print("\n---- RESULT ----")
print("Shallow Copy :", result_shallow)
print("Deep Copy :", result_deep)

