def func(nums):
    sorted_num = sorted(nums)
    index = 0
    ans =[]
    if len(sorted_num) < 2:
        return 0
    for i in sorted_num:
        try:
            index += 1
            substraction = sorted_num[index] - i
            ans.append(substraction)

        except IndexError:
            data = None

    print(f'output: {max(ans)}')

func([3,6,9,1,10])
func([10])