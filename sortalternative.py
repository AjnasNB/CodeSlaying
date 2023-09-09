def alternateSort(arr):
    arr.sort()
    alternate_array=[]
    N=len(arr)
    for i in range(0, N, 2):
        alternate_array.append(arr[i])

    return alternate_array

def main():
    arr=[]
    arr_size=int(input())
    arr=list(map(int,input().split()))

    result=alternateSort(arr)
    print(" ".join([str(res) for res in result]))

if __name__=="__main__":
    main()