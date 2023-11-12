# Generated by Django 4.2.5 on 2023-11-09 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('ID_M', models.IntegerField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Cat_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=255)),
                ('Menu_ID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('Chef_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField()),
                ('Employee_Phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Cust_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('ContcNumber', models.IntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Age', models.IntegerField()),
                ('Sex', models.CharField(max_length=20)),
                ('Booking', models.DateField()),
                ('Phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Age', models.IntegerField()),
                ('Sex', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('Birth_Date', models.DateField()),
                ('TimeEntry', models.TimeField()),
                ('DepartureTime', models.TimeField()),
                ('Type', models.CharField(max_length=255)),
                ('Restaurant_ID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('Menu_ID', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('Recipe_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('Waiter_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField()),
                ('Employee_Phone', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=20)),
                ('Boss_ID', models.IntegerField()),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.boss')),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('Method', models.CharField(max_length=255)),
                ('Amount', models.FloatField()),
                ('Payment_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Order_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('SaucersN', models.IntegerField()),
                ('customer_phone', models.CharField(max_length=20)),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.chef')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
                ('waiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.waiter')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('Manager_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField()),
                ('Employee_Phone', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cost', models.FloatField()),
                ('Amount', models.IntegerField()),
                ('Expiration', models.DateField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.restaurant'),
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('Dish_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=255)),
                ('Cost', models.FloatField()),
                ('Category_ID', models.IntegerField()),
                ('Recipe_ID', models.IntegerField()),
                ('Order_ID', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='waiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.waiter'),
        ),
        migrations.AddField(
            model_name='chef',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee'),
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.menu'),
        ),
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('Cashier_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField()),
                ('Employee_Phone', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('Amount', models.FloatField()),
                ('Bill_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_phone', models.CharField(max_length=20)),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cashier')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Administrative',
            fields=[
                ('Admin_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Salary', models.FloatField()),
                ('Employee_Phone', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
            ],
        ),
    ]
