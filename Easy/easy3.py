# Higher Re-occurance

def func(list):
    list_len = len(list)
    ans = []
    for i in list:
        if i > list_len/3:
           ans.append(i)
    print(ans)

func([1,2,3,4,5])