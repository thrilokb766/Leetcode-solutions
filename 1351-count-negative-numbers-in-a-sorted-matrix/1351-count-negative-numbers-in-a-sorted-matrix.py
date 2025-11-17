class Solution(object):
    def countNegatives(self, grid):
        negcount=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]<0:
                    negcount+=1
        return negcount
