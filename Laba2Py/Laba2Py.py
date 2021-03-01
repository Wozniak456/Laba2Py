import random
def bubble_sort(a):
    k = 0
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            k += 1
            #print(k)
            if a[j]>=a[j+1]:
               a[j], a[j+1] = a[j+1], a[j]
            #print(a)
    print(k) 
    return a

def improved_bubble_sort(a):
    k = 0
    isChanged = True 
    endOfList = len(a)-1
    while isChanged:
        isChanged = False
        for i in range(endOfList):
            k += 1
            #print(k)
            if a[i] >= a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                isChanged = True
            #print(a)
        endOfList-=1
    print(k)
    return a

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
    print(k)
    return a

def reverse_bubble_sort(a): #обернений порядок
    isChanged = True 
    endOfList = len(a)-1
    while isChanged:
        isChanged = False
        for i in range(endOfList):
            if a[i] <= a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                isChanged = True
        endOfList-=1
    return a

def random(count): # рандомний порядок
    import random
    array = list(range(count))
    random.shuffle(array)
    return array


#print("input a number")
#num = int(input())
print("10 елементiв")

list1 = list(range(10))

#найлегші випадки
print("bubble: ")
bubble_sort(list1)
print("improved bubble: ")
improved_bubble_sort(list1)
print("insertion: ")
insertion_sort(list1)

#найскладніші випадки
print("\nbubble: ")
bubble_sort(reverse_bubble_sort(list1))
print("improved bubble: ")
improved_bubble_sort(reverse_bubble_sort(list1))
print("insertion: ")
insertion_sort(reverse_bubble_sort(list1))

#рандом
print("\nbubble: ")
bubble_sort(random(10))
print("improved bubble: ")
improved_bubble_sort(random(10))
print("insertion: ")
insertion_sort(random(10))

print("\n100 елементiв")
list1 = list(range(100))

#найлегші випадки
print("bubble: ")
bubble_sort(list1)
print("improved bubble: ")
improved_bubble_sort(list1)
print("insertion: ")
insertion_sort(list1)

#найскладніші випадки
print("\nbubble: ")
bubble_sort(reverse_bubble_sort(list1))
print("improved bubble: ")
improved_bubble_sort(reverse_bubble_sort(list1))
print("insertion: ")
insertion_sort(reverse_bubble_sort(list1))

#рандом
print("\nbubble: ")
bubble_sort(random(100))
print("improved bubble: ")
improved_bubble_sort(random(100))
print("insertion: ")
insertion_sort(random(100))

print("\n1000 елементiв")
list1 = list(range(1000))

#найлегші випадки
print("bubble: ")
bubble_sort(list1)
print("improved bubble: ")
improved_bubble_sort(list1)
print("insertion: ")
insertion_sort(list1)

#найскладніші випадки
print("\nbubble: ")
bubble_sort(reverse_bubble_sort(list1))
print("improved bubble: ")
improved_bubble_sort(reverse_bubble_sort(list1))
print("insertion: ")
insertion_sort(reverse_bubble_sort(list1))

#рандом
print("\nbubble: ")
bubble_sort(random(1000))
print("improved bubble: ")
improved_bubble_sort(random(1000))
print("insertion: ")
insertion_sort(random(1000))

print("\n10000 елементiв")
list1 = list(range(10000))

#найлегші випадки
print("bubble: ")
bubble_sort(list1)
print("improved bubble: ")
improved_bubble_sort(list1)
print("insertion: ")
insertion_sort(list1)

#найскладніші випадки
print("\nbubble: ")
bubble_sort(reverse_bubble_sort(list1))
print("improved bubble: ")
improved_bubble_sort(reverse_bubble_sort(list1))
print("insertion: ")
insertion_sort(reverse_bubble_sort(list1))

#рандом
print("\nbubble: ")
bubble_sort(random(10000))
print("improved bubble: ")
improved_bubble_sort(random(10000))
print("insertion: ")
insertion_sort(random(10000))