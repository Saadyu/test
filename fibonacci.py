x = int(input("Enter the number of terms : "))
a = 1
new = 0
lst = []
for i in range((x+1)//2):
    new += a
    a += new
    lst.append(new)
    lst.append(a)
for a in range(x):
    print(lst[a], end=" ")
