#This program is a meme

def handleUserInput():
	print ("Hi! Are you ready to make your code better?")
	file_name = ""
	while file_name.find(".java") == -1:
		file_name = input ("Type your file name here (needs to be a .java file): ")
	user_remove_comment = input("Type 'y' to remove comments ")
	javaString = read_file(file_name)
	javaString = convertToOneLiner(javaString)
	if user_remove_comment == 'y':
		javaString = remove_comments(javaString)
	print(convertToOneLiner(javaString))
	write_file(file_name, javaString)

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
        if (line[-1] != ";"):
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

handleUserInput()
