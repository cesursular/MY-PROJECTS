def main():
    #.strip (remove spaces)
    question = input("Greeting: ").strip()
    if question == 'Hello' or question == 'Hello, Newman':
        print("$0")
    elif question == 'How you doing?':
        print("$20")
    elif question == "What's happening?" or question == "What's up?":
        print("$100")
main()