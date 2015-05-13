class Solution:
    # @param A a list of integers
    # @return an integer

    def removeDuplicates(self, A):
        if not A:
            return 0
        cnt = 0
        pos = 1
        flag = False
        n = len(A)
        for i in xrange(1, n):
            if A[i] == A[i-1]:
                if flag:
                    cnt += 1
                else:
                    flag = True
                    A[pos] = A[i]
                    pos += 1
            else:
                flag = False
                A[pos] = A[i]
                pos += 1
        return n-cnt
