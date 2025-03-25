def find_element_index(arr, target):
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if arr[start] <= arr[mid]:
            if arr[start] <= target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # Check if the right half is sorted
        else:
            if arr[mid] < target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    
    return None

# Example usage
arr = [13, 18, 25, 2, 8, 10]
target = 2
print(find_element_index(arr, target))