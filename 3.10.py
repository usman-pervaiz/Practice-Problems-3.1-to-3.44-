print("\t\t\t  PRACTICE PROBLEM: 3.10")
def noVowel(s):
    for c in s:
        if c in "aeiouuAEIOU":
            return False
    return True    
