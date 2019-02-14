def largest(arr,n): 
    max = arr[0] 
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i] 
    return max
alist=[]
n=int(input("enter the numbers"))
for i in range (0,n,1):
    arr=int(input("enter the arr num"))
    alist.append(arr) 
Ans=largest(alist,n) 
print ("Largest in given array is",Ans)
