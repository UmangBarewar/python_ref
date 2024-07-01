def binary_to_decimal(binary_str):
    try:
        return int(binary_str, 2)
    except ValueError:
        return "Invalid binary number."

def decimal_to_binary(decimal_number):
    try:
        return bin(int(decimal_number)).replace("0b", "")
    except ValueError:
        return "Invalid decimal number."

def main():
    while True:
        print("\nMenu:")
        print("1. Convert Binary to Decimal")
        print("2. Convert Decimal to Binary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            binary_str = input("Enter a binary number: ")
            result = binary_to_decimal(binary_str)
            print(f"Decimal representation: {result}")
        elif choice == '2':
            decimal_number = input("Enter a decimal number: ")
            result = decimal_to_binary(decimal_number)
            print(f"Binary representation: {result}")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
