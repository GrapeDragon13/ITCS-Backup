def puzzleMatrix(height):
    puzzle = []
    reversedPuzzle = []

    for i in range(height):
        puzzle.append(list(input()))

    for row in puzzle:
        reversedPuzzle.append(row[::-1])

    return puzzle, reversedPuzzle


def verticalDissection(height, width, puzzle):
    saved = []

    for i in range(width):
        temporarySave = []

        for j in range(height):
            temporarySave.append(puzzle[j][i])

        saved.append(temporarySave)

    return saved


def diagonalOrder(height, width, puzzle):
    save = []

    for line in range(1, (height + width)):
        start = max(0, line - height)
        count = min(line, (width - start), height)
        temporarySave = []

        for j in range(0, count):
            temporarySave.append(puzzle[min(height, line) - j - 1][start + j])

        save.append(temporarySave)

    return save


def singlePotential(puzzle):
    singles = []
    for row in puzzle:
        for item in row:
            singles.append(item)

    return singles


def potential(width, dissect):
    dissected = []

    for i in range(width):
        startCount = 0
        endCount = i + 2

        for part in dissect:
            for j in range(len(part) - endCount - startCount + 1):
                save = part[startCount:endCount]
                dissected.append(''.join(save))
                dissected.append(''.join(save[::-1]))
                startCount += 1
                endCount += 1

            startCount = 0
            endCount = i + 2

    return dissected


def printFind(findCount, setList):
    found = []

    for i in range(findCount):
        find = input()

        if find in setList:
            found.append(find + ' FOUND')
        else:
            found.append(find + ' NOT FOUND')

    return found


def main():
    # when done implement active search per word and update to avoid storing every possibility
    height, width = input().split()
    height, width = int(height), int(width)
    puzzle, reversedPuzzle = puzzleMatrix(height)
    findCount = int(input())
    # make everything horizontal for dissection
    dissect = []

    # putting rows straight to dissect
    vertical = verticalDissection(height, width, puzzle)

    diagonal = diagonalOrder(height, width, puzzle)
    reversedDiagonal = diagonalOrder(height, width, reversedPuzzle)

    dissect.extend(puzzle)
    dissect.extend(vertical)
    dissect.extend(diagonal)
    dissect.extend(reversedDiagonal)

    possibilities = []
    singles = singlePotential(puzzle)
    dissected = potential(width, dissect)

    possibilities.extend(singles)
    possibilities.extend(dissected)

    setList = set(possibilities)

    printout = printFind(findCount, setList)

    print(*printout, sep = '\n')

main()