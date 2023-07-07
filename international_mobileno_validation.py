import re

def validate_phone_number(regex, phone_number):
    match = re.search(regex, phone_number)
    if match:
        return print("VALID")
    return print("INVALID")

pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

test_phone_numbers=input("Enter the mobile number with country code:")
print(f"{test_phone_numbers}: {validate_phone_number(pattern,test_phone_numbers)}")
