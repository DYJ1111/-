class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 贪心
        # time: O(n * len(commmand)), space: O(obstacles)
        x, y = 0, 0
        obstacles = set(map(tuple, obstacles))
        max_distance = 0
        dx, dy = 0, 1  # x have left and right, y have up and down
        for command in commands:
            if command == -1:
                dx, dy = dy, -dx  # 方向！！！
            elif command == -2:
                dx, dy = -dy, dx  # 方向！！！
            else:
                for i in range(command):
                    if (x+dx, y+dy) in obstacles:
                        break
                    else:
                        x += dx
                        y += dy
                max_distance = max(max_distance, x*x + y*y)
        return max_distance