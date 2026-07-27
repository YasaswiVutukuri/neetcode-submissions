class Solution:

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k > n

        # Helper function to reverse elements in-place between left and right indices
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 1. Reverse entire array
        reverse(0, n - 1)
        # 2. Reverse first k elements
        reverse(0, k - 1)
        # 3. Reverse remaining n - k elements
        reverse(k, n - 1)