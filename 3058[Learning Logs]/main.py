"""3058: [LEARNING LOGS] BrickBridge"""

a = int(input())
b = int(input())
goal = int(input())

use_b = min(goal//5, b)
use_a = goal - (use_b * 5)

if use_a > a or use_b > b:
    print(-1)
else:
    print(use_a)
