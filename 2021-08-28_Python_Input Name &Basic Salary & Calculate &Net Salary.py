#python _Input Name and Basic Salary and Calculate and Net Salary

"Computer Programmin Tutor, June 10 ,2021"
name = input("Enter Name: ")
basic = float(input("Enter The Basic Salary,[£]: "))
if basic <= 8000:
    da = basic*0.75
    hra = basic*0.25

elif basic <= 15000:
    da = basic*0.86
    hra = basic*0.3

else:
    da = basic*0.96
    hra = basic*0.4

gross = basic +hra + da
pf = 0.16*basic
net = gross - pf

print("Name: ",name)
print("Basic Salary,[£]:",basic)
print("Gross Salary,[£]: ",gross)
print("Net Salary,[£]:",net)
