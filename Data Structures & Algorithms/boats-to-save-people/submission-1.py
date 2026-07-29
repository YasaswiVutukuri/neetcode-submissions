class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # 1. Sort from lightest to heaviest
        l, r = 0, len(people) - 1
        boats = 0
        
        while l <= r:
            # If the lightest and heaviest person fit together...
            if people[l] + people[r] <= limit:
                l += 1  # Lightest person gets on the boat!
            
            # The heaviest person ALWAYS gets on the boat
            r -= 1
            boats += 1  # We used 1 boat
            
        return boats