class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}

    def computeArea(self, A, B, C, D, E, F, G, H):
        def area(x, y):
            return 0 if x < 0 or y < 0 else x * y

        return area(C-A, D-B) + area(G-E, H-F) - \
            area(min(C, G) - max(A, E), min(D, H) - max(B, F))
