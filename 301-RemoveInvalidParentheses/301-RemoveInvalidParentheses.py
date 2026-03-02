# Last updated: 3/1/2026, 11:44:31 PM
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # BFS approach to find the minimum number of removals
        result = []
        visited = set([s])
        queue = [s]
        found = False

        while queue and not found:
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.pop(0)

                # If current string is valid, add to result
                if is_valid(current):
                    result.append(current)
                    found = True

                # If we found valid strings at this level, don't go deeper
                if found:
                    continue

                # Try removing each parenthesis
                for i in range(len(current)):
                    if current[i] not in '()':
                        continue

                    new_str = current[:i] + current[i+1:]
                    if new_str not in visited:
                        visited.add(new_str)
                        queue.append(new_str)

        return result