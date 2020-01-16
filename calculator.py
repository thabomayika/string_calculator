import re

def add(string_val):
    num = []
    neg = []
    for letter in re.findall(r"-?\d+", string_val):
        try:
            if int(letter) > 1000:
                letter = 0
            if int(letter) < 0:
                neg_num.append(letter)
            num.append(int(letter))
        except:
            continue
    if len(string_val) == 0: 
        return 0
    
    try:
        int(string_val[-1])
    except:
        return "Not ok"
       
    return sum(num)

print(add("1"))
  