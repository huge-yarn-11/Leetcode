class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph)
        words = paragraph.split()
        count_s = Counter(words)

        banned_set = set(banned)

        max_w = ""
        max_count = 0

        for i in count_s:
            if i not in banned_set and count_s[i] > max_count:
                max_w = i
                max_count = count_s[i]
        return max_w