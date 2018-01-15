class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_dict = {}
        anagram_list = []
        count = 0
        for s in strs:
            srtd = "".join(sorted(s))
            if srtd in anagram_dict:
                anagram_list[anagram_dict[srtd]].append(s)
            else:
                anagram_dict[srtd] = count
                anagram_list.append([s])
                count += 1
        return anagram_list


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))