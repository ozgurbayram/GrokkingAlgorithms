from random import randint
from BinarySearch import binarySearch

def random_list_creator(size)->list:
    list = []
    [list.append(randint(0,size)) for i in range(size)]
    return list

if __name__ == '__main__':
    list = random_list_creator(100)
    print(binarySearch(sorted(list),6))