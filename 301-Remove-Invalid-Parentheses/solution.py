class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(cur):
            left, right = 0, 0
            for i in range(len(cur)):
                if cur[i] == '(':
                    left += 1
                elif cur[i] == ')':
                    right += 1
                if left < right:
                    return False
            return left == right
        result, queue, visited = [], [s], set()
        visited.add(s)
        found = False
        while queue:
            cur = queue.pop(0)
            if is_valid(cur):
                found = True
                result.append(cur)
            if found:
                continue
            for i in range(len(cur)):
                if cur[i] == '(' or cur[i] == ')':
                    cand = cur[0:i] + cur[i + 1:]
                    if cand not in visited:
                        visited.add(cand)
                        queue.append(cand)
        return result

            