# We are trying the iterative approach here

def run(items, target):
    left  = 0
    right = len(items)-1

    while left <= right:
        mid = (left+right)//2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return -1 



if __name__ == '__main__':
    items = [1, 3, 4, 2, 8]
    print(run( items, 18 ))
