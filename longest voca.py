for word in voc:
    for ch in word:
        if ch in string:
            res.append(word)
            if len(word) >= 2:
                return max(res)
            else:
                return res[0]