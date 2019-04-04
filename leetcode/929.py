# https://leetcode.com/problems/unique-email-addresses/solution/
# easy
class Solution:
    def stripEmail(self, email):
        stripped, ignoring, checkingDomain = "", False, False
        for c in email:
            if c is "@":
                ignoring = False
                checkingDomain = True
            elif not checkingDomain:
                if c is ".":
                    continue
                elif c is "+":
                    ignoring = True
                    continue

            if not ignoring:
                stripped += c

        return stripped

    def numUniqueEmails(self, emails: List[str]) -> int:
        emSet = set()
	
        for em in emails:
            strippedEm = self.stripEmail(em)

            if not strippedEm in emSet:
                emSet.add(strippedEm)
		
        return len(emSet)
