#NÚMERO MAIOR E MENOR
print("Type only numbers :)")
a = int(input("First Number: "))
b = int(input("Second Number: "))
c = int(input("Third Number: "))
if a > b and c:
    print(a, "is the biggest number!")
if a < b and a < c:
    print(a, "is the smallest number") 
elif b > a and c:
    print(b, "is the biggest number!")
if b < a and b < c:
    print (b, "is the smallest number.")
elif c > a and b:
    print (c, "is the biggest number!")
if c < a and c < b:
    print (c, "is the smallest number.")
input()
