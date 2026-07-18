sub1 = int(input("Enter the marks of Os subject : "))
sub2 = int(input("Enter the marks of Python subject : "))
sub3 = int(input("Enter the marks of ML subject : "))
sub4 = int(input("Enter the marks of AI subject : "))
sub5 = int(input("Enter the marks of OOPS subject : "))
length = len([sub1, sub2, sub3, sub4, sub5])
sum = sub1+sub2+sub3+sub4+sub5
avg = sum/length
print(f"The count of all subjects is : {length}")
print(f"The sum of all subjects is : {sum}")
print(f"The average of all subjects is : {avg}")
