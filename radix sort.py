def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def main():
    # Input a list of numbers
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        unsorted_list = [int(num) for num in input_str.split()]
    except ValueError:
        print("Invalid input. Please enter a list of numbers.")
        return

    # Call the radix_sort function to sort the list
    radix_sort(unsorted_list)

    # Display the sorted list
    print("Sorted List:", unsorted_list)

if __name__ == "__main__":
    main()
