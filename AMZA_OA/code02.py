class Code02:
    def getMinimumString(self, s_id: str) -> str:
        n = len(s_id)
        result = list(s_id)

        # Try each position
        for i in range(n - 1):
            # If current digit is greater than next digit
            if result[i] > result[i + 1]:
                # Decrease current digit by 1
                result[i] = str(int(result[i]) - 1)
                # Fill rest with 9s
                for j in range(i + 1, n):
                    result[j] = '9'
                break

        return ''.join(result)

