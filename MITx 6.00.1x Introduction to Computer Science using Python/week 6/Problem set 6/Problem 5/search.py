##def search(L, e):
##    for i in range(len(L)):
##        if L[i] == e:
##            return True
##        if L[i] > e:
##            return False
##    return False
##
##def newsearch(L, e):
##    size = len(L)
##    for i in range(size):
##        if L[size-i-1] == e:
##            return True
##        if L[i] < e:
##            return False
##    return False
##
##L1 = [9,10,11]
##L2 = [1,2,3,4,5,6,7,8]
##
##e = 15
##e_1 = 10
##
##e1 = 8
##e1_ = 4
##
##print(search(L1,e),newsearch(L1,e))
##print(search(L1,e_1),newsearch(L1,e_1))
##print(search(L2,e1),newsearch(L2,e1))
##print(search(L2,e1_),newsearch(L2,e1_))
##
##
def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)


L = [1,2,3,4,5,6,7,8]
L1 = [9,8,7,6,5,4,3,1]
swapSort(L1)
print()
modSwapSort(L)
