import random
from bubble_sort import bubble_sort
data = list(range(10))#Produces an ordered list
random.shuffle(data) # Call the shuffle function to disrupt the order
print(data)# sort before
bubble_sort(data)# Call the bubbling sorting algorithm
print(data)#sorted after