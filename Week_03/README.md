## 泛型递归、树递归

### 思维要点

1. 不要人肉递归（递归的最大误区，要放弃借助递归树和人肉递归）

2. 找最近重复子问题

3. 数学归纳法思维

   ```python
   def recursion(level, p1):
       # terminator
       if level > MAX_LEVEL:
           print(result)
           return
       # process current level
       ...
       # drill down
       self.recursion(level+1, p1)
       # reverse current state if needed
       ...
   ```

### 实战题目

https://leetcode-cn.com/problems/generate-parentheses/
https://leetcode-cn.com/problems/invert-binary-tree/description/
https://leetcode-cn.com/problems/validate-binary-search-tree/
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
https://leetcode-cn.com/problems/climbing-stairs/

### 课后作业

https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
https://leetcode-cn.com/problems/combinations/
https://leetcode-cn.com/problems/permutations/
https://leetcode-cn.com/problems/permutations-ii/

## 分治、回溯

### 分治

找重复性、分解问题、组合子问题的结果

```python
def divide_conquer(problem, p1):
    # terminator
    if problem is None:
        return
    # prepare data, split data
    data = prepare_data(problem)
    subproblems = split_problem(data)
    # conquer subproblem
    subresult1 = divide_conquer(subproblem1, p1)
    subresult2 = divide_conquer(subproblem2, p1)
    # merge subresult
    result = merge_subresults(subresult1, subresult2)
    # reverse the state if needed
    ...
```

### 回溯

通常采用简单的递归方法

属于纯暴力穷举，复杂度很高，通过**剪枝**可以避免统计无效解，提高效率

### 实战题目

https://leetcode-cn.com/problems/powx-n/
https://leetcode-cn.com/problems/subsets/
https://leetcode-cn.com/problems/majority-element/description/
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
https://leetcode-cn.com/problems/n-queens/

## 本周作业

https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
https://leetcode-cn.com/problems/combinations/
https://leetcode-cn.com/problems/permutations/
https://leetcode-cn.com/problems/permutations-ii/

## 存在问题

- 组合、排列问题的时间，空间复杂度分析不清楚
- 全排列II问题中的剪枝问题不理解，（我选择的是在加入结果集的时候判断是否存在）

