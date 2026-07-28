class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        nums = []

        for i in range(0, n - 1):
            for j in range(i + 1, n):  # Start j right after i, go all the way to end
                width = j - i
                height = min(heights[i], heights[j])
                area = width * height
                nums.append(area)      # append to list
        return max(nums)