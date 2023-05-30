# Find largest word in a list
l1 = [ele for ele in input().split()]
largest = ''


def largest_word(list1):
    global largest
    for i in list1:
        if len(i) > len(largest):
            largest = i
    print(largest)
        

largest_word(l1)
