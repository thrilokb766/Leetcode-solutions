import bisect

class Solution(object):
    def minimumDifference(self, nums):
        n = len(nums)
        half = n // 2
        total = sum(nums)

        # Split nums into two halves
        left, right = nums[:half], nums[half:]

        # Helper function: generate all subset sums of a list
        def generate_sums(arr):
            sums = [[] for _ in range(len(arr) + 1)]
            sums[0].append(0)
            for num in arr:
                for i in range(len(arr) - 1, -1, -1):
                    for s in sums[i]:
                        sums[i + 1].append(s + num)
            return sums

        left_sums = generate_sums(left)
        right_sums = generate_sums(right)

        best = float('inf')
        target = total / 2.0

        # For each subset size in left half
        for i in range(len(left_sums)):
            right_part = right_sums[half - i]
            right_part.sort()
            for s in left_sums[i]:
                need = target - s
                # Binary search nearest value
                idx = bisect.bisect_left(right_part, need)
                for j in [idx, idx - 1]:
                    if 0 <= j < len(right_part):
                        curr = s + right_part[j]
                        diff = abs(total - 2 * curr)
                        best = min(best, diff)

        return int(best)
