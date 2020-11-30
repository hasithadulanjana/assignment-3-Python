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