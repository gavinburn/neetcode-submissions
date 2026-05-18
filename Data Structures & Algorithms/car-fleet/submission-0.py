class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        velocity = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        fleets = len(position)
        stack = deque()

        for pos, speed in velocity:
            time = (target-pos)/speed
            if stack and time <= stack[-1]:
                fleets-=1
                continue
            else:
                stack.append(time)

        return fleets