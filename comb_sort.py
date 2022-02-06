"""Python implementation of comb sort.

Used algorithm from javatpoint.com"""


def next_gap(gap):
    """Used to calculate the gap between elements"""

    # Decrease gap using shrink factor
    gap = int((gap * 10) / 13)
    # Checks to see if the gap factor is less than zero
    if gap < 1:
        return 1
    return gap


def comb_sort(array):
    """Used to sort the array"""
    arr_len = len(array)

    # Intialize gap
    gap = arr_len

    # Allows while loop to start
    swapped = True

    # Checks if gap doesn't equal one or if anything was swapped
    while gap != 1 or swapped == 1:

        # Change gap size to updated gap size
        gap = next_gap(gap)

        # See if anything was swapped
        swapped = False

        # Loop to go through the entire list
        for arr_num in range(0, arr_len - gap):

            # Comparing the elements in the array
            if array[arr_num] > array[arr_num + gap]:

                # Switches greater value with smaller value
                array[arr_num], array[arr_num + gap] = array[arr_num + gap], array[arr_num]

                # Shows something was swapped
                swapped = True

    # Return sorted array
    return array


def main():
    """Driver program. Adaptable to be changed to a random array"""
    array = [36, 19, 39, 203, 292, 193, 1, 2, 3, 5, 1, 99]
    print(f"The sorted array is: {comb_sort(array)}")


if __name__ == "__main__":
    main()
