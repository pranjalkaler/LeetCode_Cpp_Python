class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        img = [ [ -1 for i in range(n)] for j in range(n) ]
        for i in range(n):
            for j in range(n):
                img[i][j] = 0 if image[i][n - j - 1] == 1 else 1
        
        # print(img)
        return img
