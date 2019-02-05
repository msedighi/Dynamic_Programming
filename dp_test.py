import dynamic_programing as dp

#n = input("Enter a natural number: ")
n = 8
print("Fibonacci: ", dp.fibonacci(n))
f = dp.Fibonacci(n)
print("DP Fibonacci: ", f.compute())

Seq0 = [1,4,6,13,5,7,2,3,8]
Seq1 = [5,4,3,1,2]
Seq2 = [1,4,8,13,5,7,2,3,6]
Seq3 = [2,1,4,9,8,7]
Seq4 = [10,22,9,33,21,50,41,60,80]
LIS = dp.Longest_Increasing_Subsequence(Seq1)
print("LIS for ", Seq1, " is: ", LIS)


