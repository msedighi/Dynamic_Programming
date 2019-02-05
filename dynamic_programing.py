def fibonacci(x):
    n = int(x)
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


class Fibonacci:
    def __init__(self, n):
        self.input = int(n)
        self.value = [None] * (self.input + 1)

    def compute_dp(self, x):
        if x <= 1:
            return x
        else:
            if self.value[x]:
                return self.value[x]
            else:
                if self.value[x-2] == None:
                    self.value[x-2] = self.compute_dp(x-2)
                if self.value[x-1] == None:
                    self.value[x-1] = self.compute_dp(x-1)

                return self.value[x-1] + self.value[x-2]

    def compute(self):
        return self.compute_dp(self.input)
    
def LIS(seq, subseq, i):
    if i < len(seq):
        l = len(subseq) - 1
        if subseq[l] < seq[i]:
            subseq.append(seq[i])
            return LIS(seq, subseq, i+1)
        else:
            L1 = LIS(seq, subseq, i+1)        
            while l >= 0:
                l -= 1
                if subseq[l] < seq[i]:
                    break
            
            subseq_new = subseq[0:(l+1)] + [seq[i]]
            L2 = LIS(seq, subseq_new, i+1)

            if len(L2) > len(L1):
                return L2
            else:
                return L1
    else:
        return subseq

def Longest_Increasing_Subsequence(Seq):
    return LIS(Seq, [Seq[0]], 1)