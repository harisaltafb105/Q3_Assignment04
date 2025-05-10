def sentence_gen(word, part_of_speech):
    temp1= f"i am excited to add this {word} to my vast collection"
    temp2= f"its so nice outside tday it makes me want to {word}"
    temp3= f"looking out my window the sky is big and {word}"
    if part_of_speech == 1:
        return(temp1)
    elif part_of_speech == 2:
        return(temp2)
    elif part_of_speech == 3:
        return(temp3)
    
def main():
    word = input("Enter a word: ")
    part_of_speech = int(input("Enter a part of speech (1 which means noun, 2 means verb, or 3 means adjective): "))
    sentence = sentence_gen(word, part_of_speech)
    print(sentence)

if __name__ == '__main__':
    main()
    