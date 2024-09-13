#  higher-order functions using lambda functions
# input: [1, 2, 3, 4, 5] Doubled: [2, 4, 6, 8, 10] Squared: [1, 4, 9, 16, 25] Filtered (odd numbers): [1, 3, 5]
def apply_operation(numbers, operation):
    """
    Apply the given operation to each element in the list of numbers.

    :param numbers: List of numbers to be processed.
    :param operation: A function that defines the operation to apply to each element.
    :return: A new list with the operation applied to each element.
    """
    return [operation(number) for number in numbers]

# input:
numbers = [1, 2, 3, 4, 5 ]

# Doubled: [2, 4, 6, 8, 10]
doubled = apply_operation(numbers, lambda x: x * 2)
print(f"Doubled: {doubled}")

# Squared: [1, 4, 9, 16, 25]
squared = apply_operation(numbers,lambda x: x * x)
print(f"Squared: {squared}")

# Filtered (odd numbers): [1, 3, 5]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f"odd-numbers: {odd_numbers}")


