#problem for in class activity on 4.29.19
from sets import Set

def redact(words, banned_words):
    """Runtime: O(1) becuase it runs each word through a hashed set which makes it instant
       Space complexity: O(n) becuase it needs to have three lists open to run so it depends on """
    banned = Set(banned_words)
    censored = [word for word in words if not banned.contains(word)] #google filter
    # censored = []
    # for word in words:
    #     if not banned.contains(word):
    #         censored.append(word)
    return censored


words = ['a', 'b', 'c', 'c', 'd']
banned = ['d']

censor = redact(words, banned)
print(censor)
