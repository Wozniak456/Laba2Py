from pyFile import plot_data
import numpy as np
import random
def generate_data(n, gen_type):              
    if gen_type=="best":
        a = [i+1 for i in range(n)]
    elif gen_type=="worst":
        a = [i+1 for i in reversed(range(n))]
    else:
        a = [i+1 for i in range(n)]
        random.shuffle(a)
    return a
def bubble_sort(a):
    k = 0
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            k += 1
            if a[j]>=a[j+1]:
               a[j], a[j+1] = a[j+1], a[j]
    return k
def insertion_sort(a):
    k = 0
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
            k += 1
        a[j+1] = key
        k += 1
    return k
def bubble_impr_sort(a):
    k = 0
    isChanged = True 
    endOfList = len(a)-1
    while isChanged:
        isChanged = False
        for i in range(endOfList):
            k += 1
            if a[i] >= a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                isChanged = True
        endOfList-=1
    return k
sizes = [10, 100, 1000 ]
types = ["random", "best", "worst"]
data_plot = {'random': {'bubble':{}, 'insertion':{}, 'bubble_impr':{}}, 
             'best': {'bubble':{}, 'insertion':{}, 'bubble_impr':{}},
             'worst': {'bubble':{}, 'insertion':{}, 'bubble_impr':{}}}
for n in sizes:
    print("\nDATA SIZE: ", n)
    for gen_type in types:
        print ("\n\tDATA TYPE: ", gen_type)
        data = generate_data(n, gen_type)

        data_bubble = np.copy(data)
        bubble_op_count = bubble_sort(data_bubble)
        print("\tBubble sort operation count:", int(bubble_op_count))
        data_plot[gen_type]['bubble'][n] = bubble_op_count

        data_bubble_impr = np.copy(data)
        bubble_impr_op_count = bubble_impr_sort(data_bubble_impr)
        print("\tImproved bubble sort operation count:", int(bubble_impr_op_count))
        data_plot[gen_type]['bubble_impr'][n] = bubble_impr_op_count

        data_insertion = np.copy(data)
        insertion_op_count = insertion_sort(data_insertion)
        print("\tInsertion sort operation count:", int(insertion_op_count))
        data_plot[gen_type]['insertion'][n] = insertion_op_count

plot_data(data_plot, logarithmic=True, oneplot=True)     