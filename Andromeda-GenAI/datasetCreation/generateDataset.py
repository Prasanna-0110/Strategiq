import os

# def readFileFromNestedFolder():
#     files = []
#     for root, dirs, files in os.walk("C:\\Users\\JMalani\\Documents\\Andromeda\\dataset\\"):
#         print("jj", files)
#         for file in files:
#             if file.endswith(".csv"):
#                 with open(os.path.join(root, file), "r") as f:
#                     files.append(f.name)
#     return files

def readFileFromNestedFolder():
    al_files = []
    for root, dirs, files in os.walk("C:\\Users\\JMalani\\Documents\\Andromeda\\dataset\\"):
        for file in files:
            if file.endswith(".csv"):
                with open(os.path.join(root, file), "r") as f:
                    print(f.name)
                    al_files.append(f.name)
    return al_files

def getFileContent():
    files = readFileFromNestedFolder()
    print(files)
    all_messages = ""
    for file in files:
        message = f"fileName: {file}\n\n"
        with open(file, "rb") as f:
            message += f"content: {f.read()}\n\n"
            print(f.name, " is complete")
        all_messages += message
    writeToFile(all_messages)


def writeToFile(all_messages):
    with open("C:\\Users\\JMalani\\Documents\\Andromeda\\dataset\\output.txt", "w") as f:
        f.write(all_messages)
    print("File has been written")


getFileContent()