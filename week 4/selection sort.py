import random
def selection_sort(InputArray):
    for i in range(len(InputArray)):
        for j in range(i+1, len(InputArray)):
                if InputArray[j] < InputArray[i]:
                    InputArray[i], InputArray[j] = InputArray[j], InputArray[i]
    return InputArray
InputArray = list((random.randint(1, 1000) for _ in range(140)))
print(selection_sort(InputArray))
