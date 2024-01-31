import classes


def main():
    print("Siz city jadvaliga ma`lumot qo`shyapsiz")
    name = input("name: ")

    data = {
        "name": name
    }

    print(classes.City.insert_city(data))
    print("City jadvaliga ma`lumot qo`shildi")
    print("-----------------------")


def main2():
    print("Siz address jadvaliga ma`lumot qo`shyapsiz")
    city_id = int(input("city_id: "))
    name = input("name: ")
    district = input("district: ")

    data = {
        "name": name,
        "district": district,
        "city_id": city_id
    }

    print(classes.Address.insert_address(data))
    print("Address jadvaliga ma`lumot qo`shildi")
    print("-----------------------")


def main3():
    print("Siz customer jadvaliga ma`lumot qo`shyapsiz")
    address_id = int(input("address_id: "))
    first_name = input("first_name: ")
    last_name = input("last_name: ")
    birth_year = input("birth_year: ")
    username = input("username: ")
    password = input("password: ")
    email = input("email: ")

    data = {
        "first_name": first_name,
        "last_name": last_name,
        "birth_year": birth_year,
        "address_id": address_id,
        "username": username,
        "password": password,
        "email": email
    }

    print(classes.Customer.insert_customer(data))
    print("Customer jadvaliga ma`lumot qo`shildi")
    print("-----------------------")


def main4():
    print("Siz product jadvaliga ma`lumot qo`shyapsiz")
    name = input("name: ")
    count = int(input("count: "))
    price = int(input("price: "))
    description = input("description: ")
    weekly_report = input("weekly_report: ")

    data = {
        "name": name,
        "count": count,
        "price": price,
        "description": description,
        "weekly_report": weekly_report
    }

    print(classes.Product.insert_product(data))
    print("Product jadvaliga ma`lumot qo`shildi")
    print("-----------------------")

    print("Jadvallarga ma`lumotlar kiritildi!!!")


if __name__ == "__main__":
    main()
    main2()
    main3()
    main4()