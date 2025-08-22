class Solution:
    def maximum69Number (self, num: int) -> int:
        numStr = str(num)
        newStr = ""
        changed = False
        for i in range(0,len(numStr)):
            if numStr[i] == '6':
                if changed:
                    newStr += '6'
                else:
                    newStr += '9'
                    changed = True
            else:
                newStr += '9'

        return int(newStr)
        