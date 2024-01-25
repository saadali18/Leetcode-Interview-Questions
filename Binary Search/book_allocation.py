# Time complexity: O(n * log(total_pages))
# Problem link:https://www.codingninjas.com/studio/problems/allocate-books_1090540?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTabValue=PROBLEM
# Explanation: Binary search is performed over the range of possible maximum pages,

def is_possible(arr, n, m, mid):
    students = 1
    pages_read = 0
    
    for i in range(n):
        if arr[i] > mid:
            return False
        if pages_read + arr[i] > mid:
            students += 1
            pages_read = arr[i]
        else:
            pages_read += arr[i]
        
        if students > m:
            return False
    
    return True

def min_pages(arr, n, m):
    if n < m:
        return -1
    
    total_pages = sum(arr)
    start = max(arr)  # Lower bound for binary search
    end = total_pages  # Upper bound for binary search
    result = -1
    
    while start <= end:  # Binary search loop
        mid = (start + end) // 2
        
        if is_possible(arr, n, m, mid):
            result = mid
            end = mid - 1  # Move to the left half
        else:
            start = mid + 1  # Move to the right half
    
    return result

