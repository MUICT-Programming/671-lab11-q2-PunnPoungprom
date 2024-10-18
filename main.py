def find_min_max(lst):
    return [min(lst), max(lst)]

def summation(n, lst1, lst2):
    updated_list = []
    for i in range(n):
        updated_list.append(lst1[i] + lst2[i])
    return updated_list

n = int(input())

lst1 = []
lst2 = []
for i in range(n):
    lst1.append(int(input()))

for i in range(n):
    lst2.append(int(input()))

sum = summation(n, lst1, lst2)
print(sum)
print(find_min_max(sum))
