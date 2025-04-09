class getTransactionTripletCount:

    def getTransactionTripletCount(self, transactionHistory, divisor) -> int:
        n = len(transactionHistory)
        count = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                pair_sum = transactionHistory[i] + transactionHistory[j]
                for k in range(j + 1, n):
                    if (pair_sum + transactionHistory[k]) % divisor == 0:
                        count += 1

        return count