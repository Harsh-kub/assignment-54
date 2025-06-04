# assignment-5
# task 1:

s={"alice":"85",
   "harsh":"56",
   "aheesh":"55",   }
s1=input("Enter student's name : ")

if s1 in s:
    m=s[s1]
    print(s1,"'s marks: ",m)
else:
    print("student not found")

   # task 2:

list1=[1,2,3,4,5,6,7,8,9,10] 
list2=list1[0:5]
print("Original  iist: ", list1)
print("Extracted first five elements: ", list2)
list2.reverse()
print("Reversed extracted elements: ", list2 )

   
