from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        initial_color = image[sr][sc]
        if initial_color != color:
            self.do_flood_fill(image, sr, sc, color, initial_color)
        return image

    def do_flood_fill(
        self, image: List[List[int]], r: int, c: int, color: int, initial_color: int
    ):
        if (
            r < 0
            or r >= len(image)
            or c < 0
            or c >= len(image[0])
            or image[r][c] != initial_color
        ):
            return
        image[r][c] = color
        self.do_flood_fill(image, r - 1, c, color, initial_color)
        self.do_flood_fill(image, r + 1, c, color, initial_color)
        self.do_flood_fill(image, r, c - 1, color, initial_color)
        self.do_flood_fill(image, r, c + 1, color, initial_color)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr1, sc1, color1 = 1, 1, 2
    expected1 = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert sol.floodFill(image1, sr1, sc1, color1) == expected1

    # Test case 2
    image2 = [[0, 0, 0], [0, 1, 1]]
    sr2, sc2, color2 = 1, 1, 1
    expected2 = [[0, 0, 0], [0, 1, 1]]
    assert sol.floodFill(image2, sr2, sc2, color2) == expected2

    # Test case 3
    image3 = [[0, 0, 0], [0, 0, 0]]
    sr3, sc3, color3 = 0, 0, 2
    expected3 = [[2, 2, 2], [2, 2, 2]]
    assert sol.floodFill(image3, sr3, sc3, color3) == expected3

    # Additional test case 1: No change when color is the same as initial_color
    image4 = [[1, 1], [1, 1]]
    sr4, sc4, color4 = 0, 0, 1
    expected4 = [[1, 1], [1, 1]]
    assert sol.floodFill(image4, sr4, sc4, color4) == expected4

    # Additional test case 2: Completely different colors
    image5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sr5, sc5, color5 = 1, 1, 0
    expected5 = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    assert sol.floodFill(image5, sr5, sc5, color5) == expected5

    print("All test cases passed.")
