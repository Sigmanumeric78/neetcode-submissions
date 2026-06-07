class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #this is to check the exact length of the string before we even start.
        if len(s) != len(t) :
            return False

        countS, countT ={},{}
#this is to keep a count of each of the strings and the get function is in case we dont have a count for 
#the count for the character yet so , the get function just puts the count to zero for a new character.

        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i],0)
            countT[t[i]] = 1+ countT.get(t[i],0)
#this compares the hashmap
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

