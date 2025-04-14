def three_sum(nums):
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    
    Solution must not contain duplicate triplets.
    
    LeetCode Problem 15: https://leetcode.com/problems/3sum/
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        List[List[int]] - List of all unique triplets that sum to zero
    """
    result = []
    nums.sort()  # Sort the array to handle duplicates and for two-pointer approach
    
    for i in range(len(nums) - 2):
        # Skip duplicate values for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # If the smallest possible sum is > 0, no solution with this i
        if nums[i] > 0:
            break
            
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
    return result


# Example usage
if __name__ == "__main__":
    example = [-1, 0, 1, 2, -1, -4]
    result = three_sum(example)
    print(f"Input: {example}")
    print(f"Output: {result}")  # Expected output: [[-1, -1, 2], [-1, 0, 1]]
