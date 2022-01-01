# Maximum number of words you can type

def func(text, broken_letters=None):
    fault = ""
    for i in text:
        if i in broken_letters:
            fault += i

    answer = len(fault)
    if fault:
        print(f'you cannot type {text} because {answer} key is broken')
    else:
        print(f'you can type {text}')

func("hello world", "ad")
func("leet code", "lt")
func("hello", 'ks')