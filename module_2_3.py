#Цикл While

my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

num = len(my_list)
i = 0
while i < num:
    if my_list[i] > 0:
        print(my_list[i])
        i += 1
    elif my_list[i] < 0:

        break






