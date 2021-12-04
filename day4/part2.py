input = open('input', 'r').read().split('\n')
BingoDraw = input[0].split(",")
BingoBoardsInput = input[2:]
CurrentBingoBoard = []
BingoBoardArr = []
WinningBoardDetermined = False
def finalize(board, draw):
    Score = sum(i for i in board if isinstance(i, int))
    FinalScore = int(Score) * int(draw)
    print("Sum: " + str(Score) + ", WinNum: " + str(draw) + ", Final Score:" + str(FinalScore))
    exit(0)
def checkIfWon(board):
    for i in range(0, 5):
        if board[i * 5:i * 5 + 5] == ['bingo'] * 5 or board[i::5] == ['bingo'] * 5:
            return True
    return False
for line in BingoBoardsInput:
    if line == "":
        BingoBoardArr.append(CurrentBingoBoard)
        CurrentBingoBoard = []
    elif not line:
        break
    else:
        line = line.split()
        line = map(int, line)
        line = list(line)
        CurrentBingoBoard.extend(line)
for draw in BingoDraw:
    for boardNum in reversed(range(len(BingoBoardArr))):
        board = BingoBoardArr[boardNum]
        boardlength = len(BingoBoardArr[boardNum])
        for i in range(boardlength):
            if board[i] == int(draw):
                board[i] = 'bingo'
        if checkIfWon(BingoBoardArr[boardNum]):
            if len(BingoBoardArr) == 1:
                finalize(BingoBoardArr[boardNum], draw)
            BingoBoardArr.remove(BingoBoardArr[boardNum])