import os

path = os.getcwd()

def read_file(file_name):
    with open(path + "\\" + file_name) as f:
        return f.read()

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


print(make_comments_nice("                    plan.validate(); // Update score").strip())
