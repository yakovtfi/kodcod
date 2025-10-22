def input_series():
    """Prompts the user to enter at least 3 positive numbers separated by spaces."""
    while True:
        data = input("Enter at least 3 positive numbers (space-separated): ")
        parts = data.split()
        try:
            numbers = [float(x) for x in parts]
            if len(numbers) < 3:
                print("Error: You must enter at least 3 numbers.")
                continue
            if any(n <= 0 for n in numbers):
                print("Error: All numbers must be positive.")
                continue
            return numbers
        except ValueError:
            print("Error: Please enter only numbers (no words).")

def show_menu():
    """Displays the main menu of the program."""
    print("-" * 60)
    print("Series Analyzer - Menu")
    print("1. Input a new series")
    print("2. Display the series (original order)")
    print("3. Display the series (reversed order)")
    print("4. Display the series (sorted low→high)")
    print("5. Display the Max value")
    print("6. Display the Min value")
    print("7. Display the Average value")
    print("8. Display the Number of elements")
    print("9. Display the Sum of the series")
    print("0. Exit")
    print("-" * 60)

def main():
    """Main control function for the Series Analyzer."""
    series = input_series()
    while True:
        show_menu()
        choice = input("Choose an option [0-9]: ")
        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice == "1":
            series = input_series()
        elif choice == "2":
            print("Series:", series)
        elif choice == "3":
            print("Reversed:", list(reversed(series)))
        elif choice == "4":
            print("Sorted:", sorted(series))
        elif choice == "5":
            print("Max value:", max(series))
        elif choice == "6":
            print("Min value:", min(series))
        elif choice == "7":
            print("Average:", sum(series) / len(series))
        elif choice == "8":
            print("Number of elements:", len(series))
        elif choice == "9":
            print("Sum:", sum(series))
        else:
            print("Invalid option. Please choose between 0 and 9.")

if __name__ == "__main__":
    main()
