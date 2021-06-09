def selection_sort(list):
    min = list[0]
    minIndex = 0
    for outer in range(len(list) - 1):
        for index in range(outer+1, len(list) - 1):
            if list[index - 1] < min:
                min = list[index - 1]
                minIndex = index - 1
        list[outer], list[minIndex] = list[minIndex], list[outer]
    return list

# print(selection_sort([100,342,123123,1,56,24,0,345,123]))