def get_num():
    num = int(input("Please input a value: "))
    while (num < 1):
        num = int(input("Please input a positive value : "))
    return num


def create_table(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            print(i*j, end="\t")
        print("")


create_table(get_num())

repeat = input("Do you want to repeat? ")
while(repeat.lower() == 'y'):
    create_table(get_num())
    repeat = input("Do you want to repeat? ")