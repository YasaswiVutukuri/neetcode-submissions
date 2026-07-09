class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        
        M, N = len(matrix), len(matrix[0])
        # Create a prefix matrix padded with an extra row and column of 0s
        self.prefix = [[0] * (N + 1) for _ in range(M + 1)]
        
        # Fill the prefix matrix
        for r in range(1, M + 1):
            for c in range(1, N + 1):
                self.prefix[r][c] = (matrix[r - 1][c - 1] + 
                                     self.prefix[r - 1][c] + 
                                     self.prefix[r][c - 1] - 
                                     self.prefix[r - 1][c - 1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Evaluate the region in O(1) time using our pre-calculated matrix
        return (self.prefix[row2 + 1][col2 + 1] - 
                self.prefix[row1][col2 + 1] - 
                self.prefix[row2 + 1][col1] + 
                self.prefix[row1][col1])