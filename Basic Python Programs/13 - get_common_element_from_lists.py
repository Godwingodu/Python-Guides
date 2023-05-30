# Find common elements from 2 lists
l1 = [int(ele) for ele in input().split()]
l2 = [int(ele) for ele in input().split()]

def common(list1, list2):
    for x in list1:
        if x in list2:
            print(x,end=' ')
            
        # for y in list2:
        #     if x == y:
        #         print(x,end=' ')


common(l1,l2)