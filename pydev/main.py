# from pydantic import BaseModel, PositiveInt, ValidationError


# class FibonacciInput(BaseModel):
#     n: PositiveInt


# def fibonacci(n):
#     """
#     Calculate the nth Fibonacci number.

#     Parameters:
#     n (int): The position of the Fibonacci number to calculate.

#     Returns:
#     int: The nth Fibonacci number.

#     """
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# # Example usage with validation:
# try:
#     input_data = FibonacciInput(n=10)  # Replace 10 with any positive integer
#     for i in range(1, input_data.n + 1):
#         print(fibonacci(i))
# except ValidationError as e:
#     print(e)
