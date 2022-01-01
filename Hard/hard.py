def func(list):
    list1 = sorted(list)
    len_list1 = len(list1)
    correct_array = [i for i in range(1, len_list1+1)]
    index = 0
    output = []
    for i in correct_array:
        index += 1
        if i not in list1:
            list1.insert(index-1, i)
            output.append(i)
    print(f'output = {len(output)}')
    print(f'the list {list} should be changed {len(output)} time to get {list1[0:len_list1]}')

func([1,2,3,5,6])
func([1,2,4,5,6])
func([1,10,100,1000])