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
