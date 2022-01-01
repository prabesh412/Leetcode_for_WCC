# Merge Sorted Array

def func(num1,m , num2, n):
    first_num = num1[0:m]
    second_num = num2[0:n]
    list3 = first_num + second_num
    print(sorted(list3))


func([1,2,3,0,0,0], 3, [2,5,6], 3)
func([1],1, [], 0)