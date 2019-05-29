class Solution:

	def uniqueMorseRepresentations(self, words):
		Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
					"--","-.","---",".--.","--.-",".-.","...",
					"-","..-","...-",".--","-..-","-.--","--.."]          
		Morse_dict = {}
		# output = []
		output = set()
		for word in words:
			Morse_code = ""
			for ch in word:
				if ch not in Morse_dict:
					idx = ord(ch) - ord('a')
					Morse_dict[ch] = Morse[idx]
					Morse_code += Morse[idx]
				else:
					Morse_code += Morse_dict[ch]
			# output.append(Morse_code)
			output.add(Morse_code)
			# print(Morse_code,'\'')
		return len(set(output))


	def method_by_set_directly(self, words):
		# because set can overwrite the repeative elements
		Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
					"--","-.","---",".--.","--.-",".-.","...",
					"-","..-","...-",".--","-..-","-.--","--.."] 
		Morse_words = set()
		for word in words:
			Morse_ch = ""
			for ch in word:
				Morse_ch += Morse[ord(ch) - ord('a')]
			Morse_words.add(Morse_ch)
		return len(Morse_words)

if __name__ == '__main__':
	words = ["gin", "zen", "gig", "msg"]
	print(Solution().uniqueMorseRepresentations(words))
	print(Solution().method_by_set_directly(words))

'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
'''
