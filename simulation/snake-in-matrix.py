class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x, y = 0, 0
        direction_map = {
            "UP": (-1, 0),
            "RIGHT": (0, 1),
            "DOWN": (1, 0),
            "LEFT": (0, -1)
        }

        for command in commands:
            dx, dy = direction_map[command]
            x += dx
            y += dy

        final = x * n + y

        return final
            
                
