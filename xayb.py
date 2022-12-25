def binarysort(a,key):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(high+low)//2
        if a[mid]==key:
            print("search successful key found at location",(mid+1))
            return
        elif key <a[mid]:
            high=mid-1
        else:
            low=mid+1
            print("search unsuccessful")
a=[1,2,3,4,5,6,7,8,9,45]
print("the array elements are :",a)
k=int(input("enter the key:"))
binarysort(a,k)
