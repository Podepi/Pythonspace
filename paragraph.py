def writePara(text, w, h):
    words = text.split(" ")
    output = [""]
    line = 0
    for word in words:
        if len(word) > w:
            word = word[0:w]
        if len(word) + len(output[line]) > w:
            print len(word) + len(output[line])
            line += 1
            if line >= h:
                break
            output.append("\n")

        word += " "
        output[line] += word
    text = ""
    for word in output:
        text += word
    print text
