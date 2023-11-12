from django.db import models

class Boss(models.Model):
    ID_M = models.IntegerField(primary_key=True)
    Salary = models.FloatField()

class Menu(models.Model):
    Menu_ID = models.IntegerField(primary_key=True)

class Category(models.Model):
    Cat_ID = models.IntegerField(primary_key=True)
    Type = models.CharField(max_length=255)
    Menu_ID = models.IntegerField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class Recipe(models.Model):
    Recipe_ID = models.IntegerField(primary_key=True)
    Type = models.CharField(max_length=255)

class Restaurant(models.Model):
    ID = models.IntegerField(primary_key=True)
    Address = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20)
    Boss_ID = models.IntegerField()
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE)

class Employee(models.Model):
    Name = models.CharField(max_length=255)
    Age = models.IntegerField()
    Sex = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Birth_Date = models.DateField()
    TimeEntry = models.TimeField()
    DepartureTime = models.TimeField()
    Type = models.CharField(max_length=255)
    Restaurant_ID = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Administrative(models.Model):
    Admin_ID = models.IntegerField(primary_key=True)
    Salary = models.FloatField()
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Manager(models.Model):
    Manager_ID = models.IntegerField(primary_key=True)
    Salary = models.FloatField()
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Chef(models.Model):
    Chef_ID = models.IntegerField(primary_key=True)
    Salary = models.FloatField()
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Cashier(models.Model):
    Cashier_ID = models.IntegerField(primary_key=True)
    Salary = models.FloatField()
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Waiter(models.Model):
    Waiter_ID = models.IntegerField(primary_key=True)
    Salary = models.FloatField()
    Employee_Phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Customer(models.Model):
    Cust_ID = models.IntegerField(primary_key=True)
    ContcNumber = models.IntegerField()
    Name = models.CharField(max_length=255)
    Age = models.IntegerField()
    Sex = models.CharField(max_length=20)
    Booking = models.DateField()
    Phone = models.CharField(max_length=20)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)

class Pay(models.Model):
    Method = models.CharField(max_length=255)
    Amount = models.FloatField()
    Payment_ID = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order(models.Model):
    Order_ID = models.IntegerField(primary_key=True)
    SaucersN = models.IntegerField()
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    customer_phone = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Dish(models.Model):
    Dish_ID = models.IntegerField(primary_key=True)
    Type = models.CharField(max_length=255)
    Cost = models.FloatField()
    Category_ID = models.IntegerField()
    Recipe_ID = models.IntegerField()
    Order_ID = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Ingredients(models.Model):
    Cost = models.FloatField()
    Amount = models.IntegerField()
    Expiration = models.DateField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Bill(models.Model):
    Amount = models.FloatField()
    Bill_ID = models.IntegerField(primary_key=True)
    cashier = models.ForeignKey(Cashier, on_delete=models.CASCADE)
    customer_phone = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
