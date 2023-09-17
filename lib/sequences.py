
def print_fibonacci(length):
    # Handle the special cases when length is 0 or 1
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    # Initialize the first two elements of the Fibonacci sequence
    fibonacci_sequence = [0, 1]

    # Calculate and append the next elements until the desired length is reached
    while len(fibonacci_sequence) < length:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)

    # Print the generated Fibonacci sequence
    print(fibonacci_sequence)
