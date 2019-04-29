#problem for in class activity on 4.29.19


def redact(words, banned_words):
    """Runtime: O(n^2) becuase it runs each word in the list through another
    list, which gives it time complexity"""
    censored = []
    for word in words:
        if word not in banned_words:
            censored.append(word)
    return censored

words = ['a', 'b', 'c', 'c', 'd']
banned = ['d']

censor = redact(words, banned)
print(censor)
