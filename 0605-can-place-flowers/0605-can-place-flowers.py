class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        str_flowerbed = ''.join(list(map(str, flowerbed)))
        str_flowerbed = '0' + str_flowerbed + '0'

        idx = 0
        for i in range(n):
            if '000' in str_flowerbed[idx:]:
               idx = idx + str_flowerbed[idx:].index('000') + 2
            else:
                return False
        return True