# Distinct characters in string | using array and loop only

def char(input):
    string = ""
    for i in input:
        if i not in string:
            string += i
    print(string)


char('cricket')
char('developer')