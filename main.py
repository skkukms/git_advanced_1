from typing import List

#skeleton ccode for even_list
def even_list(int_list:List[int]) ->List[int]:
    pass

def sum_of_squares_of_even(even_int_list:List[int])->int:
    sum =0
    for a in even_int_list:
        sum+=a*a
    return sum


def main():
    int_list = [1,2,3,4,5,6,7,8,9,10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main()