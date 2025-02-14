class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        n = len(chars)
        write = 0
        read = 0

        while read < n:
            key = chars[read]
            count = 0

            while read < n and chars[read] == key:
                count += 1
                read += 1

            chars[write] = key
            write += 1

            if count > 1:
                for digit in str(count):

                    chars[write] = digit
                    write += 1

        return write
            