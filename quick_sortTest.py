from quick_sort import quick_sort
if __name__ == '__main__':
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    quick_sort(array, 0, len(array)-1)
    print(array)