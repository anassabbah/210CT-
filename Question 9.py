#binary search
def bsearch(no_list, value):
    low = 0 
    high = len(no_list)-1
    result = False

    while low<=high and not result: #while the lower bound is less than the higher bound and isnt the value
        midpoint = (low + high)//2  #take pointer to midpoint
        if no_list[midpoint] == value: #if midpoint is the value return true
            result = True
        else:
            if value < no_list[midpoint]: #else to lower if value is less than midpoint
                high = midpoint-1 #or go higher if value > midpoint
            else: #continue until result is found
                low = midpoint+1
    return result

testlist = [2, 3, 5, 6, 7, 13]
print(bsearch(testlist, 2 and 9))
