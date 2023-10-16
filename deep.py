#define assign
def main():
    #answer
    answer = input("What's the answer to the Great Question of Life, the Universe, and Everything?")
    #case section
    answer = answer.lower()
    #replace str
    answer = answer.replace('-', ' ')
    #assing if function
    if answer == '42' or answer == 'forty two' or answer == 'forty-two':
        print("Yes")
    else:
        print("No")
main()
