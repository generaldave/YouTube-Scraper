# David Fuller
#
# 7-27-2016

#Define a File Handler class
class FileHandler(object):
    # Constructor
    def __init__(self, filename):
        self.filename = "/path/to/downloaded/git/files/"
        self.filename = self.filename + filename

    # Method overwrites given file with given token
    def write(self, tokens, delimiter, newline):
        # Declare outputString
        outputString = ""
        
        # Open file as write
        fileObj = open(self.filename, 'w')

        # Create string to write to file
        for token in tokens:
            # Make sure there is no newline character
            if (newline):
                outputString = outputString + token + "\n"
            else:
                outputString = outputString + delimiter + token
        outputString = outputString[1:]   # Strip comma at beginning
        
        # Write token to file
        fileObj.write(outputString)

        # Close file
        fileObj.close

    # Method appends given token to end of given file
    def append(self, token, delimiter, newline):
        # Open file as read/write
        fileObj = open(self.filename, 'r+')

        # Make sure there is no newline character
        fileObj.seek(-1, 2)
        if (fileObj.read(2) == "\n"):
            fileObj.seek(-1, 2)

        # Decide whether or not to add a new line at
        # the end of token
        if (newline):
            token = delimiter + token + '\n'
        else:
            token = delimiter + token

        # Write token to file
        fileObj.write(token)

        # Close file
        fileObj.close

    # Method reads file and returns it's contents
    def read(self):
        # Open file as read
        fileObj = open(self.filename, 'r')

        # Storre file contents
        inputString = fileObj.read()

        # Close file
        fileObj.close

        # Return file contents
        return inputString
