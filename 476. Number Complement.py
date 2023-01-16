class Solution:
    def findComplement(self, num: int) -> int:
        binary = ""
        while num >=1:
            binary += ''.join(str(num % 2))
            num = num // 2
        binary=binary[::-1]
        answer = ""
        for digit in binary:
            if digit == "0":
                answer += "1"
            else:
                answer += "0"
        addition = 0
        count = len(answer) - 1
        for i in range(count+1):
            addition += int(answer[i]) * (2 ** (count-i))
        return addition