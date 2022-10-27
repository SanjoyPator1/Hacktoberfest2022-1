# Given a string S, print it after changing the middle element to * (if the length of the string is even, change the 2 middle elements to *).
# Sample Testcase : INPUT : hello
# OUTPUT: he*lo

# creating an empty list
lst = []
# # number of elements as input
n = int(input("Enter number of elements : "))
  
# # iterating till the range
for i in range(0, n):
    ele = (input())
    lst.append(ele)
l=len(lst)

if l%2!=0 :         #if length of the string is not even
    lst[l//2]="*"      
else:
    lst[l//2]="*"         #if length of the string is even
    lst[(l//2)-1]="*"
print(lst)
