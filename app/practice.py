def merge_sort(l1:list, l2:list):
    return sorted(l1+l2)


# yoyo=merge_sort(["g",43,"k",3,43],[6,7,6,8,23,3,23,23])
# print(yoyo)


#- Find intersection/union of two lists.

def inser_union(l1:list, l2:list):
    union_list = []
    for i in sorted(l1+l2):
        if i not in union_list:
            union_list.append(i)
        else:
            pass
    return union_list


# un = inser_union([1,3,2,4,5],[1,3,4,6,5,3,8,545])
# print(un)

#- Implement a dictionary sort by values.

#- Check if a list contains duplicates.
from collections import Counter
def dup_check_list(l:list):
    con = Counter(l)
    for k,v in con.items():
        if v > 1:
            return "list has a dubplicate values"
    else:
        return "list does not has duplicate values"

# yoy=dup_check_list([1,2,3])
# print(yoy)

a=0
def yooo():
    global a
    a+=1
    return "changed"

# m = yooo()
# print(m,a)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(6))
