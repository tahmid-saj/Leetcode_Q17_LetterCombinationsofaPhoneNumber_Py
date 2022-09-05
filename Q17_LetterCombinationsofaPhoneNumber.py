from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters_by_digits = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if len(digits) == 1:
            return list(letters_by_digits[digits])
        
        return list(
			"".join(p) 
			for p in product(*(letters_by_digits[digit] for digit in digits))
		)
