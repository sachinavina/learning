from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    index_map = {}
    for i, item in enumerate(nums):
        required_num = target - item
        if required_num not in index_map:
            index_map[item] = i
        else:
            return [index_map[required_num], i]


if __name__ == '__main__':
    print(two_sum([-3, 4, 3, 90], 0))
    print(two_sum([3, 3], 6))
