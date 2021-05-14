class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        last = 1
        while candies > 0:
            for i in range(num_people):
                if last < candies:
                    result[i] += last
                else:
                    result[i] += candies
                    candies = 0
                    break
                candies -= last
                last += 1
        return result