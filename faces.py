def convert(text):
    return text.replace("Hello :)", "Hello 🙂").replace("Goodbye :(", "Goodbye 🙁")
def main():
    user_input = input("Write emotions: ")
    converted_text = convert(user_input)
    print(converted_text)
main()