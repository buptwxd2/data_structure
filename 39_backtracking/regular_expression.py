pattern = 'a*c'
text = 'abc'

matched = False

def rmatch(i, j):      # current check the i-th char in the text; j means j-th char in the pattern
    global matched

    if matched:
        return      # already matched, just return

    if pattern[j] == '*':
        for k in range(len(text)-i+1):
            rmatch(i+k, j+1)
    elif pattern[j] == "?":
        rmatch(i, j+1)
        rmatch(i+1, j+1)
    else:               # ordinary char
        if text[i] != pattern[j]:
            matched = False
            return
        else:
            rmatch(i+1, j+1)


#   To be verify