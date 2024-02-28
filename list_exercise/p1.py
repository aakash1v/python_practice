# Python program to interchange first and last elements in a list

def SwapList(newlist):

    n= len(newlist)-1
    temp = newlist[0]
    newlist[0]=newlist[n]
    newlist[n]= temp
    return newlist

def SwapList(newlist):
    newlist[0],newlist[-1] = newlist[-1],newlist[0]
    print('Second approach')
    return newlist

def SwapList(newlist):
    #  Storing the first and last element 
    # as a pair in a tuple variable get
    get = newlist[-1],newlist[0]

    newlist[0],newlist[-1] = get
    print('Third approach')
    return newlist


def SwapList(newlist):
    a, *b, c = newlist
    list = [c, *b, a ]
    print('fourth approach')
    return list

def SwapList(newlist):
    first = newlist.pop(0)
    last = newlist.pop(-1)
    
    newlist.append(first)
    newlist.insert(0,last)
    print('fifth approach')
    return newlist

# sixth approach ...
def SwapList(newlist):
    if len(newlist)>2:
        newlist = newlist[-1:] + newlist[1:-1]+ newlist[:1]
    print('sixth approach')
    return newlist


#Driver code

li = [12, 35, 9, 56, 24]
result = SwapList(li)
print(result)
