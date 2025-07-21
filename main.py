"""
Main application file for the calculator project.

This demonstrates how the calculator module can be used in a real application.
"""

from src.calculator import add, subtract, multiply, divide, power


def main():
    """Main function to demonstrate calculator operations."""
    print("Welcome to the Calculator Application!")
    print("=" * 40)

    # Demonstrate all operations
    print(f"Addition: 5 + 3 = {add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {subtract(10, 4)}")
    print(f"Multiplication: 6 * 7 = {multiply(6, 7)}")
    print(f"Division: 15 / 3 = {divide(15, 3)}")
    print(f"Power: 2^8 = {power(2, 8)}")

    print("\nCalculator operations completed successfully!")


if __name__ == "__main__":
    main()
