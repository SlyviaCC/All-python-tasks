from linear_research import linearsearch
arr = [1, 5, 6, 4, 2, 5, 7, 9, 4]
x = 5
l = len(arr)
n = linearsearch(arr, x, l)
if n:
    print("The index of the element is:", n)
else:
    print("Element not found!")