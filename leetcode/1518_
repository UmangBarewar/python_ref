class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        Drunk = numBottles
        
        while numBottles >= numExchange:
            new_bottles = numBottles // numExchange
            rem = numBottles % numExchange
            Drunk += new_bottles
            numBottles = new_bottles + rem
        
        return Drunk
