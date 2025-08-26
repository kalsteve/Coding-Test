from collections import Counter

def solution(nums):
    counter = Counter(nums)
    max = len(list(counter.elements())) // 2
    return len(counter.most_common(max))


def test_solution(self):
    self.assertEqual(solution([3, 3, 3, 2, 2, 4]), 3)
    self.assertEqual(solution([3, 3, 3, 2, 2, 2]), 2)
    self.assertEqual(solution([3, 3, 3, 3, 3, 3]), 1)
    self.assertEqual(solution([1, 1, 2, 2, 3, 3]), 3)
    self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 3)
