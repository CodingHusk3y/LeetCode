class Solution:
    def convertDateToBinary(self, date: str) -> str:
        days = date.split("-")
        binary_days = []

        for day in days:
            binary_day = bin(int(day))[2:]
            binary_days.append(binary_day)

        return "-".join(binary_days)