#sub sequence extraction in ascending order
def heap(s,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < s and sqc[i] < sqc[l]: #make sure that each node is greater than its children  
        max = l   #makes said node the max
    if r < s and sqc[max] < sqc[r]: #make sure that each node is greater than its children 
        max = r   #makes said node the max
    if max != i:   
        switch(i, max)   
        heap(s, max)   

def sort():     
    s = len(sqc)  #s is length of sequence
    start = s // 2 - 1 # use // instead of / #start at mid point
    for i in range(start, -1, -1):   
        heap(s, i)   
    for i in range(s-1, 0, -1):   
        switch(i, 0)   
        heap(i, 0)

def switch(i, j):                    
    sqc[i], sqc[j] = sqc[j], sqc[i] 

sqc = [10, 20, 60, 30, 50, 40]
sort()
print(sqc)
