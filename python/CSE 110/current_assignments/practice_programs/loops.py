# colors = ["red", "blue", "green", "yellow"]

# for color in colors:
#     print(color)
# print()
# for i in range(1, 9):
#     print(i)
# print()
# for i in range(2, 21, 2):
#     print(i)
# print()

user_input = int(input("What number do you want? "))
user_range = user_input + 1


for row_num in range(1, user_range):
    for col_num in range(1, user_range):
        num = row_num * col_num
        print(f"{num:4}", end="")
    print()




