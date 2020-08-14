def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    """
    method 1
    遍历 strs， sort 每个 str， 将 sorted str 作为 key 存入hash， 将 str 当作 value 存入
    O(n^2 logN), O(n)
    """
    from collections import defaultdict
    d = defaultdict(list)
    # d = {}
    for str in strs:
        d[tuple(sorted(str))].append(str)
        # d[tuple(sorted(str))] = d.get(tuple(sorted(str)), [])+[str]
    return list(d.values)
    
    """
    method 2
    遍历 strs， 使用数组统计 str 中字母的个数，将数组作为 key 存入hash，将 str 作为 value 存入
    O(n^2), O(n)
    """
    from collections import defaultdict
    dic = defaultdict(list)
    # dic = {}
    for str in strs:
        count = [0] * 26
        for ch in str:
            count[ord(ch) - ord('a')] += 1
        dic[tuple(count)].append(str)
        # dic[tuple(count)] = dic.get(tuple(count), []) + [str]
    return list(dic.values())