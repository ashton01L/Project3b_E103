# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/7/2024

# Description: Write a program that asks the user to enter a positive integer,
# then prints a list of all positive integers that divide that number
# evenly, including itself and 1, in ascending order.

def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def main():
    try:
        # Prompt user for a positive integer
        num = int(input("Please enter a positive integer: "))

        if num <= 0:
            raise ValueError("Number must be a positive integer.")

        # Get list of factors
        factors = get_factors(num)

        # Print factors
        print(f"The factors of {num} are:")
        for factor in factors:
            print(factor)

    except ValueError as ve:
        print(f"Error: {ve}. Please enter a valid positive integer.")
    except Exception as e:
        print(f"Error: {e}. An unexpected error occurred.")

if __name__ == "__main__":
    main()