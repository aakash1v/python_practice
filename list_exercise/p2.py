# Python Program to Swap Two Elements in a List

'''Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 

Examples:  

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
'''

def swap(newlist,pos1,pos2):
    # actual positions..
    pos1 = pos1 -1
    pos2 = pos2 -1
    
    temp = newlist[pos1]
    newlist[pos1]= newlist[pos2]
    newlist[pos2] = temp
    return newlist

def swap(newlist,pos1,pos2):
    # actual positions..
    pos1 = pos1 -1
    pos2 = pos2 -1
    print('Second approach')
    newlist[pos1] , newlist[pos2]= newlist[pos2] ,newlist[pos1]
    return newlist

def swap(list,pos1,pos2):
    # actual positions..
    pos1 = pos1 -1
    pos2 = pos2 -1

    print('Third approach')
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2-1)

    list.insert(pos1,second_ele)
    list.insert(pos2,first_ele)
    return list

def swap(list,pos1,pos2):
    # actual positions..
    pos1 = pos1 -1
    pos2 = pos2 -1

    print('fourth approach')
    get  = list[pos1],list[pos2]

    list[pos2],list[pos1] = get
    return list

def swap(list,pos1,pos2):
    # actual positions..
    pos1 = pos1 -1
    pos2 = pos2 -1
    print("fifth approach")

    for i , x in enumerate(list):
        if i == pos1 :
            elem1 = x
        if i == pos2:
            elem2 = x
        
    list[pos1] = elem2
    list[pos2] = elem1
        

    return list



# driver code 
li = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

li2 = [1, 2, 3, 4, 5]
pos1 = 2
pos2 = 5
result = swap(li2,pos1,pos2)
print(result)