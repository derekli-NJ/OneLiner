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
			
	return formattedString



def read_file(file_name):
    with open("./" + file_name) as f:
        return f.read()


def write_file(file_name, javaString):
	with open("./" + file_name, 'w') as f:
		f.write(javaString)	

def make_comments_nice(line):
    inString = False
    inComment = False
    lastC = "";
    commentIndex = -1;
    for i in range(len(line)):
        c = line[i]
        if not(inComment):
            if not(inString):
                if lastC == "/":
                    if c == "/":
                        commentIndex = i;
                        break;
                    elif c == "*":
                        inComment = True
            if not(lastC == "\\") and c == "\"":
                inString = not(inString)
        else:
            if (lastC == "*" and c == "/"):
                inComment = False;
        lastC = c;
    if commentIndex == -1:
        return line
    tmp = list(line)
    tmp[commentIndex] = "*"
    return "".join(tmp) + "*/"

file_name = "helloworld.java"
javaString = read_file(file_name)
javaString = convertToOneLiner(javaString)
print(convertToOneLiner(javaString))
write_file(file_name, javaString)
