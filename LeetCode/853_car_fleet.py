# LeetCode 853. Car Fleet
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    n = len(position)
    times = {}
    fleets_number = n

    for i in range(0, n):
        distance = target - position[i]
        times[position[i]] = distance / speed[i]
    sorted_positions = position.copy()
    sorted_positions.sort(reverse=True)

    current_time = times[sorted_positions[0]]

    for i in range(1, n):
        if times[sorted_positions[i]] <= current_time:
            fleets_number -= 1
        else:
            current_time = times[sorted_positions[i]]
    return fleets_number


if __name__ == "__main__":
    assert carFleet(target=10, position=[3], speed=[3]) == 1
    assert carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]) == 3
    assert carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1])
    assert carFleet(target=10, position=[6, 8], speed=[3, 2])
