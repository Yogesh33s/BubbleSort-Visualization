import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                display_array(arr)

    # Display final sorted array
    display_array(arr, final=True)


def display_array(arr, delay=0.15, final=False):

    plt.bar(range(len(arr)), arr, color='blue' if not final else 'green')
    plt.pause(delay)

    if not final:
        plt.clf()


def main():

    # Create random array
    arr = np.random.randint(1, 100, 20)

    print("Initial array:", arr)

    bubble_sort(arr)

    # Keep final plot open
    plt.show()


if __name__ == "__main__":
    main()
