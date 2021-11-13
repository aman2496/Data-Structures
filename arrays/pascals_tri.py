def combination(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result = []

        for count in range(numRows):
            rows = []

            for elem in range(count + 1):
                rows.append(combination(count, elem))
            result.append(rows)

        return result

        
