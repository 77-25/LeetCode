# https://leetcode.cn/problems/count-servers-that-communicate/
from collections import defaultdict
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # defaultdict区别dict，都是字典，但是前者访问不存在的key时会自动赋值0
        dgrid = defaultdict(int)
        # 0-行，1-列，第一遍遍历，为字典标记元素出现在i行j列
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                dgrid[f'0{i}'] += 1
                dgrid[f'1{j}'] += 1

        # 第二遍遍历，从字典中找出不是“孤家寡人”的行列，递增
        # 第一次遍历会出现某行或某列只有一台机器(==1)，这个时候不能说这个服务器可以通信，所以判断条件是>1
        ct = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (dgrid[f'0{i}'] > 1 or dgrid[f'1{j}'] > 1):
                    ct += 1
        return ct