Q1
QuestionTxt = "Please enter the value of "
x = input(QuestionTxt+ "Length ")
y = input(QuestionTxt+" Breadth ")
print('This is a Square' if x == y else 'This is not a square')

Q2
QuestionTxt = "Please enter the value of "
x = input(QuestionTxt+ "1 st ")
y = input(QuestionTxt+" 2 nd ")
print('Num '+ x + ' is greater than '+ y if x >=  y else 'Num '+ y +' is greater than '+ x)

Q3

untiValue= 100
discount = 0.10
quantity = int(input("Please enter the Quantity Value : "))
value=quantity*untiValue
if(value>=1000):
  disc=int(value*discount)
  newValue=int(value-value*discount)
  print("Original price: ",value, "\nDiscount Applied: ",disc  , "\nDue Amount to Be Paid :",newValue )
else:
  print("Discount Applied :","None" , "\nDue Amount to Be Paid :",value)
  
Q4
empSalary= int(input("Please enter the Current Salary : "))
workedYear= int(input("Please enter the No of years Worked : "))
bonus = 0.5
if(workedYear>=5):
  netBonus=int(empSalary*bonus)
  newSalary =int(empSalary+netBonus)
  print("Salary: ",empSalary, "\nNet Bonus: ",netBonus)
else:
  print("Salary: ",empSalary, "\nNet Bonus: ","No Bonus")
  
Q5
count = 0
ageList = list(range(3))
oldestPerson="Oldest Person Age is"
while count <3:
  age = int(input("Please Enter the Age : "))
  ageList.append(age)
  count=count+1
print(oldestPerson,max(ageList))

Q7
print("OUTPUT",abs(int(input("INPUT VALUE : "))))

Q8
noc =int(input("Number of Class Held :"))
noa =int(input("Number of Class Attend :"))
minAttends = 75
acutalAttend = int(noa/noc*100)
print('% of Class Attend :',acutalAttend)
print('Student is notllowed to Attend Exam' if acutalAttend >= minAttends else 'Student is not allowed to Attend Exam')

Q9

noc =int(input("Number of Class Held :"))
noa =int(input("Number of Class Attend :"))
minAttends = 75
acutalAttend = int(noa/noc*100)
print('% of Class Attend :',acutalAttend)
if (acutalAttend >= minAttends):
  print("Student is allowed to Attend Exam")
elif(True):
  mc=input("Any Medical issue, Type ('Y' or 'N') :")
  #to minimize the user error typing cabs or simple letter
  if(mc.capitalize()=="Y"):
   print("Student is allowed to Attend Exam")
  else:
   print("Student is NOT allowed to Attend Exam")
