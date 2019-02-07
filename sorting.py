
def Quick_Sort_Partition(a,i_first,i_last):
    pivot = a[i_last-1]
    i_s=i_first-1
    for i in range(i_first, i_last):
        if a[i] <= pivot:
            i_s += 1
            a[i],a[i_s] = a[i_s],a[i]
    
    if i_s > i_first:
        Quick_Sort_Partition(a,i_first, i_s)
    if i_last > (i_s + 1):
        Quick_Sort_Partition(a,i_s + 1, i_last)

def Quick_Sort(a):
    Quick_Sort_Partition(a,0,len(a))