# Student Management System
# class Student:
#     course_name = "Python"

#     def __init__(self, name, roll_no):
#         self.student_name = name
#         self.roll_no = roll_no

#     def display(self):
#         print(f"Student name: {self.student_name}")
#         print(f"Roll No: {self.roll_no}")
#         print(f"Course Name: {Student.course_name}")


# s1 = Student("Ramesh", 1)
# s1.display()



# Employee Salary Details
# class Employee():
#     def __init__(self, Emp_name, Emp_id, Salary):
#         self.name = Emp_name
#         self.Emp_id = Emp_id
#         self.salary = Salary

#     def display(self):
#         print(f"Employee Name: {self.name}")
#         print(f"Employee Id: {self.Emp_id}")
#         print(f"Salary: {self.salary}")


# s1 = Employee("Sushant", 123, 75000)
# s1.display()



# Mobile Phone Details
# class Mobile():
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def display(self):
#         print("Brand: ",self.brand)
#         print("Model: ",self.model)
#         print("Price: ",self.price)

#     def discount(self, discount_percent):
#         discount_amount = self.price * (discount_percent / 100)
#         self.price -= discount_amount
#         print(f"Applied {discount_percent}% discount. New Price: {self.price}")

# phone1 = Mobile("Samsung", "Galaxy S24", 75000)
# phone1.display()

# phone1.discount(10)  # Applies a 10% discount
# phone1.display()



# Bank Account
# class ATM():
#     def __init__(self, balance = 0):
#         self.balance = balance

#     def Check_balance(self):
#         return self.balance

#     def deposit(self, amount):
#         if amount <= 0 :
#             print("Invalid Amount")
#         else: 
#             self.balance += amount
#             print(f'Deposited: {amount}')
#             print(f'Available Balance: {self.balance}')

#     def Withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid Amount")
#         elif amount > self.balance :
#             print("Insufficient Balance")
#         else:
#             self.balance -= amount
#             print(f'{amount} Withdraw Successfully')
#             print(f'Available Balance: {self.balance}')

#     def Updated_balance(self):
#         print(f'Updated balance is {self.balance}')

# w1 = ATM()
# w1.Check_balance()
# w1.deposit (7000)
# w1.Withdraw(2000)
# w1.Updated_balance()



# Car Rental System
# class Car:
#     def __init__(self, car_name, rent_per_day, rental_days):
#         self.car_name = car_name
#         self.rent_per_day = rent_per_day
#         self.rental_days = rental_days

#     def calculate_rent(self, days):
#         self.rental_days = days
#         return self.rent_per_day * days


# # Example usage
# car = Car("Honda City", 5000, 3)
# total = car.calculate_rent(5)
# print(f"Car: {car.car_name} | Total Rent for {car.rental_days} days: {total}")



# Book Information – Parameterized Constructor
# class Book():
#     def __init__(self, name, author, price):
#         self.name = name
#         self.author = author
#         self.price = price

#     def display(self):
#         print("Book Name: ",self.name)
#         print("Author Name: ",self.author)
#         print("Prize: ",self.price)

# b1 = Book("It Ends With Us","Colleen Hoover", 477)
# b1.display()

# b2 = Book("It Start With Us","Colleen Hoover", 577)
# b1.display()



#  Rectangle Area
# class Area_rectangle():

#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print(f'Area of Reactangle is: {self.length * self.width}')

# a1 = Area_rectangle(8, 5)
# a1.area()



# Electricity Bill
# class ElectricityBill:
#     def __init__(self, customer_name, units_consumed):
#         self.customer_name = customer_name
#         self.units_consumed = units_consumed

#     def calculate_bill(self):
#         if self.units_consumed < 0:
#             raise ValueError("Units consumed cannot be negative.")

#         if self.units_consumed <= 100:
#             bill = self.units_consumed * 5
#         elif self.units_consumed <= 200:
#             bill = (100 * 5) + ((self.units_consumed - 100) * 7)
#         else:
#             bill = (100 * 5) + (100 * 7) + ((self.units_consumed - 200) * 10)

#         return bill

#     def display_bill(self):
#         total = self.calculate_bill()
#         print(f"Customer Name : {self.customer_name}")
#         print(f"Units Consumed: {self.units_consumed}")
#         print(f"Total Bill    : ₹{total:.2f}")


# customer1 = ElectricityBill("Aarav Sharma", 250)
# customer1.display_bill()



#  Product Inventory
# class Product():
#     def __init__(self, productname, price, quantity):
#         self.name = productname
#         self.price = price
#         self.quantity = quantity

#     def display(self):
#         print("Product Name: ",self.name)
#         print("Price: ", self.price)
#         print("Quantity: ",self.quantity)

#     def total_price(self):
#         Total = self.price * self.quantity
#         print(f'TOTAL : {Total}')

# p1 = Product("Headphones", 15000, 8)
# p1.display()
# p1.total_price()

        

# Company Employee Counter
# class Employeee():
#     comp_name = "Wipro"
#     Emp_count = 50000

#     def __init__(self, emp_id, emp_name):
#         self.name = emp_name
#         self.id = emp_id

#     def display(self):
#         print("Employee Name: ",self.name)
#         print("Employee Id: ", self.id)
#         print("Company Name: ",Employeee.comp_name)
#         print("Employee Count: ",Employeee.Emp_count)

# e1 = Employeee("Rahul", 123)
# e1.display()



#  School Student Information
# class School():
#     School_name = "KUK Vidyalay"

#     def __init__(self, std_name, roll_no):
#         self.name = std_name
#         self.no = roll_no
#         self.percentage = 83

#     def display(self):
#         print("School Name: ",School.School_name)
#         print("Student Name: ", self.name)
#         print("Roll No: ",self.no)
#         print("Peracentage: ",self.percentage)

# s1 = School("Dipak", 27)
# s1.display()



# Shopping Cart
# class Shoppingcart:
#     discount_percentage = 0.10  

#     def __init__(self, customer_name, total_amount):
#         self.name = customer_name
#         self.amount = total_amount

#     def display(self):
#         discount_amount = self.amount * self.discount_percentage
#         final_amount = self.amount - discount_amount

#         print("Customer Name:", self.name)
#         print("Total Amount:", self.amount)
#         print("Discount Applied:", discount_amount)
#         print("Final Amount:", final_amount)


# cart1 = Shoppingcart("Rahul", 1000)
# cart1.display()



# Hospital Patient Management
# class Patient():
#     Hopsital_name = "Orchid Hospital"

#     def __init__(self, p_name, p_age, disease):
#         self.name = p_name
#         self.age = p_age
#         self.disease = disease

#     def display(self):
#         print("Patient Name: ",self.name)
#         print("Patient Age: ",self.age)
#         print("Patient Disease: ",self.disease)
#         print("Hospital_Name: ",Patient.Hopsital_name)

# p1 = Patient("Suresh", 57, "Cancer")
# p1.display()



#  Online Course Management
# class Course:
#     Institute_Name = "TKA"

#     def __init__(self, c_name, c_fee):
#         self.name = c_name
#         self.fee = c_fee
#         self.final_fee = c_fee 

#     def calculate_fee(self, discount_percentage):
#         discount = (self.fee * discount_percentage) / 100
#         self.final_fee = self.fee - discount
#         return self.final_fee
        
#     def display(self):
#         print(f'Institute Name: {Course.Institute_Name}') 
#         print(f'Course Name: {self.name}') 
#         print(f'Course Fee: {self.fee}') 
#         print(f'Final Fee: {self.final_fee}') 

# c1 = Course("Python", 25000)
# c1.calculate_fee(10)
# c1.display()



# Student Result Management
# class StudentResult:
#     def __init__(self, name, mark1, mark2, mark3):
#         self.name = name
#         self.marks = [mark1, mark2, mark3]
#         self.total = 0
#         self.percentage = 0.0

#     def calculate_total(self):
#         self.total = sum(self.marks)

#     def calculate_percentage(self):
#         self.calculate_total()
#         self.percentage = (self.total / 300) * 100

#     def display_result(self):
#         self.calculate_percentage()
        
#         print(f"Student Name: {self.name}")
#         print(f"Marks: {self.marks}")
#         print(f"Total Marks: {self.total}/300")
#         print(f"Percentage: {self.percentage:.2f}%")


# student1 = StudentResult("Aarav", 85, 90, 78)
# student1.display_result()
  


# Food Ordering System
# class FoodOrder:
#     def __init__(self, customer_name, food_item, food_price, quantity):
#         self.customer_name = customer_name
#         self.food_item = food_item
#         self.food_price = food_price
#         self.quantity = quantity
#         self.discount = 0

#     def calculate_bill(self):
#         total = self.food_price * self.quantity
#         final_bill = total - (total * self.discount / 100)
#         return final_bill

#     def apply_coupon(self, discount):
#         self.discount = discount

#     def display_order(self):
#         print("Customer:", self.customer_name)
#         print("Food Item:", self.food_item)
#         print("Price:", self.food_price)
#         print("Quantity:", self.quantity)
#         print("Discount:", self.discount, "%")
#         print("Final Bill:", self.calculate_bill())


# # Example usage
# order = FoodOrder("Rahul", "Burger", 150, 2)
# order.apply_coupon(10)
# order.display_order()

