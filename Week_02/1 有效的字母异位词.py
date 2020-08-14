def isAnagram(self, s, t):
    """
    method 1 
    比较 sort 后的 string 是否 ==
    O(NlogN), O(1)
    """
    return sorted(s) == sorted(t)
 
    """
    method 2
    两个 hash， 分别统计 s 和 t 中字母的个数
    比较两个 hash 是否 ==
    O(N), O(N)
    """
    # if not s and not t:
    #     return True
    # if not s or not t or len(s) != len(t):
    #     return False

    s_dict = {}
    t_dict = {}
    for ch in s:
        s_dict[ch] = s_dict.get(ch, 0) + 1
    for ch in t:
        t_dict[ch] = t_dict.get(ch, 0) + 1

    return s_dict == t_dict
    
    """
    method 3
    使用数组模拟hash， 分别统计 s 和 t 中字母的个数
    比较两个数组是否 ==
    """