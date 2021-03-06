from typing import List


class Matrix:
    def __init__(self, matrix_string: str):
        lines = matrix_string.splitlines()
        self._nums = [list(map(int, line.split())) for line in lines]
        self._colsz = len(self._nums[0])
        self._rowsz = len(self._nums)

    def row(self, index: int) -> List[int]:
        return self._nums[index - 1]

    def column(self, index: int) -> List[int]:
        return [row[index - 1] for row in self._nums]
