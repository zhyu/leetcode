class Solution:
    # @param num, a list of integer
    # @return an integer

    def maximumGap(self, num):
        l = len(num)
        if l < 2:
            return 0
        p_inf, n_inf = float('inf'), float('-inf')
        max_num = min_num = num[0]
        for n in num[1:]:
            max_num = max(max_num, n)
            min_num = min(min_num, n)
        bucket_size = (max_num-min_num-1) / (l-1) + 1
        buckets = [(p_inf, n_inf) for _ in xrange(l-1)]
        for n in num:
            if n == max_num or n == min_num:
                continue
            idx = (n-min_num) / bucket_size
            buckets[idx] = (min(n, buckets[idx][0]), max(n, buckets[idx][1]))
        gap, prev = 0, min_num
        for bucket_min, bucket_max in buckets:
            if bucket_min == p_inf or bucket_max == n_inf:
                continue
            gap = max(gap, bucket_min-prev)
            prev = bucket_max
        return max(gap, max_num - prev)
