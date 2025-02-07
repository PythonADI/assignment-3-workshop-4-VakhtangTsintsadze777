phone_numbers = []

num = int(input("How many phone numbers do you want to add to the list? "))
country_code = input("Enter country code (e.g., +1): ")

for _ in range(num):
    phone_number = input("Enter phone number: ")
    full_number = f"{country_code}-{phone_number}"
    phone_numbers.append(full_number)

print("\nSending Messages!")
for number in phone_numbers:
    print(f"Sending message to: {number}")
