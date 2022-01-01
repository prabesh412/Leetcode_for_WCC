# Missing Duplicates

def func(nums):
    list = [i for i in nums if nums.count(i) == 1]
    print(list)
func([4,1,2,1,2])
