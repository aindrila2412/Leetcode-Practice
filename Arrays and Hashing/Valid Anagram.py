Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
  
  
  
Solution:
 
 
class Solution:
  def isAnagram(self, s: str, t: str):
   
   if len(s) != len(t):
     return False
    
   countS, countT = {}, {}
    
   for i in range(len(s)):
     countS[s[i]] = 1 + countS.get(s[i])
     countT[t[i]] = 1 + countT.get(t[i])
     
   for c in countS:
     if countS[c] != countT.get(c, 0):
       return False
      
   return True
     
  
  
