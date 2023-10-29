# Code : Input String - 021%#$43) Output : 01234%#$)
# Number and symbol separated such that numbers are sorted and symbols appear in the
# same order

s = "021%#$43)"
output = "01234%#$)"

def sort_string(s):
    p1 = 0
    p2 = len(s) - 1

    while not (s[p2] in "0123456789"):
        p2 -= 1
    
    while not (s[p1] in "0123456789"):
        p1 += 1
    
    while p1 < p2:
        if s[p1] in "0123456789" and s[p2] not in "0123456789":
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
        
        elif s[p1] in "0123456789":
            p1 += 1
        
        elif s[p2] not in "0123456789":
            p2 -= 1

    return s

print(sort_string(list(s)))
    


