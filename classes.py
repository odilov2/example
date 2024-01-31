from datetime import datetime
from BASE import Database


class City:
    def __init__(self, city_id, name):
        self.city_id = city_id
        self.name = name
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_city(data):
        query = f"""
        INSERT INTO city(name) VALUES('{data['name']}')
        """
        return Database.connect(query)


class Address:
    def __init__(self, address_id, city_id, name, district):
        self.address_id = address_id
        self.name = name
        self.city_id = city_id
        self.district = district
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_address(data):
        query = f"""
        INSERT INTO address(city_id, name, district) VALUES('{data['city_id']}', '{data['name']}', '{data['district']}')
        """
        return Database.connect(query)


class Customer:
    def __init__(self, customer_id, first_name, last_name, username, password, email, address_id, birth_year):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.address_id = address_id
        self.birth_year = birth_year
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_customer(data):
        query = f"""
        INSERT INTO customer(first_name, last_name, username, password, email, address_id, birth_year) VALUES('{data['first_name']}','{data['last_name']}', '{data['username']}', '{data['password']}', '{data['email']}', '{data['address_id']}', '{data['birth_year']}')
        """
        return Database.connect(query)


class Product:
    def __init__(self, product_id, name, count, price, description, weekly_report):
        self.product_id = product_id
        self.name = name
        self.count = count
        self.price = price
        self.description = description
        self.weekly_report = weekly_report
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_product(data):
        query = f"""
        INSERT INTO product(name, count, price, description, weekly_report) VALUES('{data['name']}', '{data['count']}', '{data['price']}', '{data['description']}', '{data['weekly_report']}')
        """
        return Database.connect(query)


class Payment:
    def __init__(self, payment_id, customer_id, product_id, amount):
        self.payment_id = payment_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.amount = amount
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_payment(data):
        query = f"""
        INSERT INTO payment(customer_id, product_id, amount) VALUES('{data['customer_id']}', '{data['product_id']}', '{data['amount']}')
        """
        return Database.connect(query)

