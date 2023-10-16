#str.endswith(suffix[, start[, end]])
#Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position.
def main():
    file = input("File name: ").strip()
    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".jpeg") or file.endswith(".jpg"):
        print("image/jpeg")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf") or file.endswith(".PDF"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
main()