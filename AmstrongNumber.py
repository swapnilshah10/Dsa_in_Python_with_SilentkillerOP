def isArmstrong(num):
    #
    temp = num
    num = str(num)
    ans = 0
    for i in num:
        ans+= int(i)**len(num)
    return ans == temp

def main():
    #
    num = int(input())
    print(isArmstrong(num))