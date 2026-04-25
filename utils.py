def get_city():
    while True:
        city=input("Enter city: ").strip()
        if city:
            return city
        print("City cannot be empty")