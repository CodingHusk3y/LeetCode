class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        ans = ""
        index = 0

        while num > 0:
            if num % 1000 != 0:
                group = ""
                part = num % 1000

                if part >= 100:
                    group += ones[part // 100] + " Hundred "
                    part %= 100

                if part >= 20:
                    group += tens[part // 10] + " "
                    part %= 10

                if part > 0:
                    group += ones[part] + " "

                group += thousands[index] + " "
                ans = group + ans 

            num //= 1000
            index += 1

        return ans.strip()   

        
