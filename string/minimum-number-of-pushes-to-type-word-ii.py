class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_counts = Counter(word)
        sorted_letters = sorted(letter_counts.items(), key=lambda x: -x[1])
        
        if len(sorted_letters) <= 8:
            return len(word)

        total_presses = 0

        for index, (letter, count) in enumerate(sorted_letters):
        # Calculate the number of presses: 1 (1 press for first letter on key),
        # 2 (2 presses for second letter on key), etc.
            key_presses = index // 8 + 1
            total_presses += key_presses * count
    
        return total_presses 

