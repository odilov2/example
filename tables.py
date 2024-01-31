from BASE import Database


def create_tables():
    city = f"""
    CREATE TABLE city(
        city_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        last_update TIMESTAMP DEFAULT NOW())
    """

    address = f"""
    CREATE TABLE address(
        address_id SERIAL PRIMARY KEY,
        city_id INT REFERENCES city(city_id),
        name VARCHAR(20),
        district VARCHAR(20),
        last_update TIMESTAMP DEFAULT NOW())
    """

    customer = f"""
    CREATE TABLE customer(
        customer_id SERIAL PRIMARY KEY,
        address_id INT REFERENCES address(address_id),
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        birth_year DATE,
        username VARCHAR(20),
        password VARCHAR(20),
        email VARCHAR(30),
        last_update TIMESTAMP DEFAULT NOW())
    """

    product = f"""
    CREATE TABLE product(
        product_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        count INT,
        price NUMERIC(8, 2),
        description VARCHAR(20),
        weekly_report VARCHAR(30),
        last_update TIMESTAMP DEFAULT NOW())
    """

    payment = f"""
    CREATE TABLE payment(
        customer_id INT REFERENCES customer(customer_id),
        product_id INT REFERENCES product(product_id),
        amount NUMERIC(10, 3),
        last_update TIMESTAMP DEFAULT NOW())
    """

    tables = [city, address, customer, product, payment]

    for table in tables:
        data = Database.connect(table)
        print(data)


if __name__ == "__main__":
    create_tables()


