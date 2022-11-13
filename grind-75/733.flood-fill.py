from collections import deque


class SolutionBFS:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin_color = image[sr][sc]
        queue = deque()
        visited = set()
        queue.append((sr, sc))
        while len(queue):
            row, col = queue.popleft()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            image[row][col] = color
            if self.isValidIndex(image, row-1, col) and image[row-1][col] == origin_color:
                queue.append((row-1, col))
            if self.isValidIndex(image, row+1, col) and image[row+1][col] == origin_color:
                queue.append((row+1, col))
            if self.isValidIndex(image, row, col+1) and image[row][col+1] == origin_color:
                queue.append((row, col+1))
            if self.isValidIndex(image, row, col-1) and image[row][col-1] == origin_color:
                queue.append((row, col-1))
        return image

    def isValidIndex(self, image: List[List[int]], row: int, col: int) -> bool:
        if not len(image):
            return False
        return row >= 0 and row < len(image) and col >= 0 and col < len(image[0])


class SolutionDFS:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        self.fill(image, sr, sc, color, image[sr][sc])
        return image

    def fill(self, image: List[List[int]], sr: int, sc: int, color: int, srcColor: int) -> None:
        if not self.isValidIdx(image, sr, sc) or image[sr][sc] != srcColor:
            return
        image[sr][sc] = color
        self.fill(image, sr - 1, sc, color, srcColor)
        self.fill(image, sr + 1, sc, color, srcColor)
        self.fill(image, sr, sc - 1, color, srcColor)
        self.fill(image, sr, sc + 1, color, srcColor)

    def isValidIdx(self, image: List[List[int]], row: int, col: int) -> bool:
        return row >= 0 and row < len(image) and col >= 0 and col < len(image[0])
