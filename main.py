#This program is a meme

def convertToOneLiner(javaString):
	javaString = javaString.strip()
	charactersToReplace = ["\n", "\t", "\r"]
	formattedString = ""
	for line in javaString.splitlines():
		line = line.strip()
		line = make_comments_nice(line)
		for character in charactersToReplace:
			line = line.replace(character, "")
		formattedString += line
		if len(line) > 0 and not(line[-1] == ";"):
			formattedString += " "
			
	return formattedString



def read_file(file_name):
    with open("./" + file_name) as f:
        return f.read()


def write_file(file_name, javaString):
	with open("./" + file_name, 'w') as f:
		f.write(javaString)	

def remove_comments(file):
    inString = False
    inComment = False
    lastC = ""
    chars = list(file)
    index = 0
    while index < len(chars):
        c = chars[index]
        if not(inComment):
            if not(inString):
                if (lastC == "/" and c == "*"):
                    inComment = True
                    index = index - 2
                    c = ""
            if not(lastC == "\\") and c == "\"":
                inString = not(inString)
            index += 1
        else:
            if (lastC == "*" and c == "/"):
                inComment = False
            del chars[index]
        lastC = c
    return "".join(chars)

def make_comments_nice(line):
    inString = False
    inComment = False
    lastC = ""
    commentIndex = -1;
    for i in range(len(line)):
        c = line[i]
        if not(inComment):
            if not(inString):
                if lastC == "/":
                    if c == "/":
                        commentIndex = i
                        break
                    elif c == "*":
                        inComment = True
            if not(lastC == "\\") and c == "\"":
                inString = not(inString)
        else:
            if (lastC == "*" and c == "/"):
                inComment = False
        lastC = c
    if commentIndex == -1:
        return line
    tmp = list(line)
    tmp[commentIndex] = "*"
    return "".join(tmp) + "*/"

file_in = "PlayerTest.java"
file_out = "out.java"
javaString = read_file(file_in)
#out_string = remove_comments(convertToOneLiner(javaString))
out_string = convertToOneLiner(javaString)
print(out_string)
write_file(file_out, out_string)
