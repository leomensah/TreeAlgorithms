def anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


str1 = "garden"
str2 = "denrag"

print(anagrams(str1, str2))