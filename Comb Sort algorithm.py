#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python implementation of Comb Sort

# Used to calculate the gap between elements
def next_gap(gap):
    
    # Decrease gap using shrink factor
    gap = int((gap*10)/13)
    # Checks to see if the gap factor is less than zero
    if gap < 1:
        return 1
    return gap

# Used to sort the array
def comb_sort(array):
    l = len(array)
    
    # Intialize gap
    gap = l
    
    # Allows while loop to start
    swapped = True
    
    # Checks if gap doesn't equal one or if anything was swapped
    while gap != 1 or swapped == 1:
        
        # Change gap size to updated gap size
        gap = next_gap(gap)
        
        # See if anything was swapped
        swapped = False

        # Loop to go through the entire list
        for a in range(0, l - gap):

            # Comparing the elements in the array
            if array[a] > array[a + gap]:
                
                # Switches greater value with smaller value
                array[a], array[a + gap] = array[a + gap], array[a]
                
                # Shows something was swapped
                swapped = True
    
    # Return sorted array
    return array

# Driver program
# Adaptable to be changed to a random array
array = [36,19,39,203,292,193,1,2,3,5,1,99]
print(f"The sorted array is: {comb_sort(array)}")


# Used algorithm from javatpoint.com

