def gcd(m, n):
    if m == n:
        return n
    elif m < n:
        return gcd(m,n-m)
    elif m > n:
        return gcd(m-n, n) 
    
def find_max(u):
    if len(u) == 1:
        return u[0]
    return max(u[-1],find_max(u[:-1]))


def zip(u, v): 
    if len(u) == len(v) == 0:
        return[]
    return [u[0],v[0]] + zip(u[1:],v[1:])

def remove_number(x, nums): 
    if len(nums) == 0:
        return []
    elif x == nums[0]:
        return [] + remove_number(x,nums[1:])
    elif x != nums[0]:
        return [nums[0]] + remove_number(x,nums[1:])
    
    
def removeLetter(string, letter):
    if len(string) == 0:
        return ""
    elif letter == string[0]:
        return "" + removeLetter(string[1:],letter)
    elif letter != string[0]:
        return string[0] + removeLetter(string[1:],letter)
        
    return
def palindrec(str):
    if len(str) == 0:
        return True
    elif str[0] != str[-1]:
        return False
    return palindrec(str[1:-1])

def palindite(str):
    if len(str) == 0:
        return True
    loop = len(str) // 2
    print(loop)
    for i in range(loop):
        if str[i] != str[len(str)-(i+1)]:
            return False
    return True

        

    


    


print(palindite('abcdcba'))
# print(removeLetter("test string", "t"))
# print(remove_number(5, [1,5,2,4,3,55,5,6,3,2])) #returns [1, 2, 3, 4, 6, 2, 1]
# print(zip([1, 2, 3], [4, 5, 6])) #returns [1, 4, 2, 5, 3, 6]
# print(find_max([1, 7, 4,99, 5]))

# print(removeLetter("test string", "t"))
#print(remove_number(5, [1, 2, 3, 4, 5, 6, 5, 2, 1])) #returns [1, 2, 3, 4, 6, 2, 1]
# zip([1, 2, 3], [4, 5, 6]) #returns [1, 4, 2, 5, 3, 6]
# a = [1,2,3]
# n = len(a)
# print(find_max(a,n))