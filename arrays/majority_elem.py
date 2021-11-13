'''
    Boyer's Moore Algorithm --> O(1) Space

            We first assume that our first num is the majority element
            So the count here is 1 as we have seen it 1 times, if the
            count in the end is greater than 0 we are sure that this is majority element
            as if you take count of majority element and subtract sum of all counts of non
            Majority element, if that count is still positive that it proves that is
            majority element. We do not need to check count in end over here as we are
            sure that there exists a majority element.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        candidate = nums[0]

        for n in nums[1:]:
            if candidate == n:
                count += 1
            else:
                count -= 1

                if count == 0:
                    candidate = n
                    count = 1
        return candidate
