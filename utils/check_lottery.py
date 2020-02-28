all_num = "03,06,08,14,19,26+12"
my_num_list = [
    "08,15,22,23,30,32+01",
    "11,13,15,20,24,27+04",
    "11,19,22,28,31,33+08",
    "07,08,10,11,14,24+08",
    "01,05,12,14,23,32+15",
]



def show_num(my_num, num_list=[]):
    for num in my_num:
        if num in num_list:
            print("\033[0;31m%s\033[0m" % num, end=" ")
        else:
            print(num, end=" ")

def make_list(num_str):
    red_num_str, blue_num_str = num_str.split("+")
    red_num_list = red_num_str.split(",")
    blue_num_list = blue_num_str.split(",")
    return red_num_list, blue_num_list



red_num_list, blue_num_list = make_list(all_num)

show_num(red_num_list)
print("+", end=" ")
show_num(blue_num_list)
print("\n" + "-" * 22)


for my_num in my_num_list:
    my_red_num_list, my_blue_num_list = make_list(my_num)
    show_num(my_red_num_list, red_num_list)
    print("+", end=" ")
    show_num(my_blue_num_list, blue_num_list)
    print()
