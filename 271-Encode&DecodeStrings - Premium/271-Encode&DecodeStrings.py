class Solution:

    def encode(self, strs: [str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    # 4#neet
    def decode(self, s: str) -> [str]:

        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res


solution = Solution()
res1 = solution.encode(["we", "say", ":", "yes"])
print(res1)
res = solution.decode(res1)
print(res)
