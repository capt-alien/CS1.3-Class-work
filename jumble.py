from sets import Set

def dict():
    """Opens the dictionary-words file at the path. Assigns the file to 'f'.
    Reads 'f' and splits each word into a 'words' array element.
    Closes 'f'. Returns the array of dictionary words."""

    f = open("/usr/share/dict/words", "r")
    words = f.read().split().lower()
    f.close()
    return words

def c_split(word):
    return [char for char in word]


def jumble(jumble):
    jumble = jumble.lower()
    j_list = c_split(jumble)
    j_set = Set(j_list)
    j_len = j_set.length
    possable_words = []
    #Get dictionary list:
    dict= dict()
    #itterate thorough the dictionary looking for matches
    for word in dict:
        if len(word)==j_len:
            w_set = Set(c_split(word))
            if j_set.difference(w_set) == 0:
                possable_words.append(word)
        #return words after itteration complete
    return possable_words

    if __name__ == '__main__':
        word = "tefon"
        answer = jumble(word)
        print(answer)
