from typing import List

#skeleton ccode for even_list
def even_list(int_list:List[int]) ->List[int]:
    res =[]
    for a in int_list:
        if a%2 ==0:
            res.append(a)
    return res

def sum_of_squares_of_even(even_int_list:List[int])->int:
    pass


def main():
    int_list = [1,2,3,4,5,6,7,8,9,10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main()
