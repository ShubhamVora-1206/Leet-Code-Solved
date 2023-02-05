class Solution:
    def numTilings(self, N: int) -> int:
        def numTilingsD(N):
            if N in cacheD: return cacheD[N]
            if N <= 2: return N if N > 0 else 1 
            cacheD[N] = (numTilingsD(N - 2) + numTilingsD(N - 1) + (2 * numTilingsT(N - 1))) % ((10**9) + 7)
            return cacheD[N]

        def numTilingsT(N):
            if N in cacheT: return cacheT[N]
            if N <= 2: return 0 if N == 1 else 1
            cacheT[N] = (numTilingsD(N - 2) + numTilingsT(N - 1)) % ((10**9) + 7)
            return cacheT[N]
        cacheD, cacheT = {}, {}
        return numTilingsD(N)
