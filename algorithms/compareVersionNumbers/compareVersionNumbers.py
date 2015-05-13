class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer

    def compareVersion(self, version1, version2):
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        l1, l2 = len(v1), len(v2)
        l = max(l1, l2)
        v1.extend([0] * max(0, l-l1))
        v2.extend([0] * max(0, l-l2))
        for idx in xrange(l):
            if v1[idx] > v2[idx]:
                return 1
            if v1[idx] < v2[idx]:
                return -1
        return 0
