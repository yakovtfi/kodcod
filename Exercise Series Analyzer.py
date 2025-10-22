def input_series():
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
    series = input_series()
    while True:
        show_menu()
        choice = input("Choose an option [0-9]: ")
        match choice:
            case "0":
                print("Exiting program. Goodbye!")
                break
            case "1":
                series = input_series()
            case "2":
                print("Series:", series)
            case "3":
                print("Reversed:", list(reversed(series)))
            case "4":
                print("Sorted:", sorted(series))
            case "5":
                print("Max value:", max(series))
            case "6":
                print("Min value:", min(series))
            case "7":
                print("Average:", sum(series) / len(series))
            case "8":
                print("Number of elements:", len(series))
            case "9":
                print("Sum:", sum(series))
            case _:
                print("Invalid option. Please choose between 0 and 9.")

if __name__ == "__main__":
    main()
