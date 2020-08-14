def combine(self, n: int, k: int) -> List[List[int]]:
    # if k > n or k <= 0:
    #     return []
    # result = []
    #
    # def combine_core(n, k, track, index):
    #     if k == len(track):
    #         result.append(track)
    #         return
    #
    #     for i in range(index, n+1):
    #         if len(track) < k:
    #             combine_core(n, k, track+[i], i+1)
    #
    # combine_core(n, k, [], 1)
    # return result
    import itertools
    return list(itertools.combinations(range(1, n+1), k))