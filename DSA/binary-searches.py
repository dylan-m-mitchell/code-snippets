def binSearch(arr: list[int], target: int) -> int:
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        if arr[mid] > target:
            high = mid - 1
    return -1

def firstOccurence(arr: list[int], target: int) -> int:
    low = 0
    high = len(arr) - 1
    last_seen = -1
    
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] == target:
            last_seen = mid
            high = mid -1
        if arr[mid] < target:
            low = mid + 1
        if arr[mid] > target:
            high = mid-1
    
    return last_seen

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4, 5]
    print("Test 1: firstOccurence([1,2,2,2,3,4,5], 2) =>", firstOccurence(arr, 2))  # Should be 1

    arr2 = [1, 1, 1, 1, 1]
    print("Test 2: firstOccurence([1,1,1,1,1], 1) =>", firstOccurence(arr2, 1))  # Should be 0

    arr3 = [1, 2, 3, 4, 5]
    print("Test 3: firstOccurence([1,2,3,4,5], 3) =>", firstOccurence(arr3, 3))  # Should be 2

    arr4 = [1, 2, 3, 4, 5]
    print("Test 4: firstOccurence([1,2,3,4,5], 6) =>", firstOccurence(arr4, 6))  # Should be -1

    arr5 = []
    print("Test 5: firstOccurence([], 1) =>", firstOccurence(arr5, 1))  # Should be -1