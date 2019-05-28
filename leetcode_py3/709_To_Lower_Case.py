class Solution:
	def toLowerCase(self, str):
		# return str.lower()

		ans =""

		for ch in str:
			if 'A' <= ch <='Z':
				ans += chr(ord(ch) + ord('a') - ord('A'))
			else:
				ans += ch

		return ans



		

if __name__ == '__main__':

	string = "Hello"
	print(Solution().toLowerCase(string))



'''  
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
'''

