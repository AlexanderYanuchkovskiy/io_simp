def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    total_left = (m + n + 1) // 2
    
    low, high = 0, m
    
    while low <= high:
        i = (low + high) // 2
        j = total_left - i
        

        nums1_left_max = float('-inf') if i == 0 else nums1[i-1]
        nums1_right_min = float('inf') if i == m else nums1[i]
        
        nums2_left_max = float('-inf') if j == 0 else nums2[j-1]
        nums2_right_min = float('inf') if j == n else nums2[j]

        if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
            if (m + n) % 2 == 1:
                return max(nums1_left_max, nums2_left_max)
            else:
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
        elif nums1_left_max > nums2_right_min:
            high = i - 1
        else:
            low = i + 1
    
    raise ValueError("Input arrays are not sorted or something went wrong.")

nums1 = input('array 1 >> ')
nums1 = list(map(int, nums1.split()))
nums2 = input('array 2 >> ')
nums2 = list(map(int, nums2.split()))
print(findMedianSortedArrays(nums1, nums2))
