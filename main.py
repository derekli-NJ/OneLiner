#All one liners here


javaString = '''public class HelloWorld {

    public static void main(String[] args) {
        // Prints "Hello, World" to the terminal window.
        System.out.println("Hello, World");
    }
}'''

def convertToOneLiner(javaString):
	javaString = javaString.strip()

	charactersToReplace = ["\n", "\t", "\r"]
	formattedString = ""
	for line in javaString.splitlines():
		line = line.strip()
		for character in charactersToReplace:
			line = line.replace(character, "")
		formattedString += line
			
	return formattedString

print(convertToOneLiner(javaString))
