class Solution:
	def numUniqueEmails(self, emails):
		address = set()
		if not emails:
			return 0
		else:
			for email in emails:
				local = email.split('@')[0]
				domain = email.split('@')[1]

				local = local.split('+')[0]
				local = local.replace('.', '')
				address.add(local + '@' + domain)

		return len(address)


	def forget_replace(self, emails):
		address = set()

		for email in emails:
			local = email.split('@')[0]
			domain = email.split('@')[1]

			same_local = ""
			local = local.split('.')
			for component in local:
				same_local += component
			ignore_local = same_local.split('+', 1)[0]
			address.add(ignore_local + '@' + domain)

		return len(address)

if __name__ == '__main__':
	emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
	print(Solution().numUniqueEmails(emails))
	print(Solution().forget_replace(emails))


''' Every email consists of a local name and a domain name, separated by the @
sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com
is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an
email address, mail sent there will be forwarded to the same address without
dots in the local name.  For example, "alice.z@leetcode.com" and
"alicez@leetcode.com" forward to the same email address.  (Note that this rule
does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus
sign will be ignored. This allows certain emails to be filtered, for example
m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does
not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How
many different addresses actually receive mails?

 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","t
estemail+david@lee.tcode.com"] Output: 2 Explanation: "testemail@leetcode.com"
and "testemail@lee.tcode.com" actually receive mails
’‘’
