def wordInMatrix(arr: list[list[str]], fWord: str) -> bool:
    fWord = fWord.upper()
    words = []
    word = ''
    for index, subArr in enumerate(arr):
        word = ''
        for index2, let in enumerate(subArr):
            word += let
            words.append(word)

    for i in range(len((arr[0]))):
        word = ''
        for j in range(len(arr)):
            word += arr[j][i]
            words.append(word)
    
    return fWord in words


def main() -> None:
    word = 'foam'
    exists = wordInMatrix([['F', 'A', 'C', 'I'],
                            ['O', 'B', 'Q', 'P'],
                            ['A', 'N', 'O', 'B'],
                            ['M', 'A', 'S', 'S']], word)
    
    if exists:
        print(f'The word, {word}, is in the matrix')
    else:
        print(f'The word, {word}, is not in the matrix')

if __name__ == "__main__":
    main()