input = open('input', 'r').read().split('\n')
BingoDraw = input[0].split(",")
BingoBoardsInput = input[2:]
CurrentBingoBoard = []
BingoBoardArr = []
WinningBoardDetermined = False
def finalize(WinningBoard, LastNumber):
    Score = sum(i for i in WinningBoard if isinstance(i, int))
    FinalScore = int(Score) * int(LastNumber)
    print("Sum: " + str(Score) + ", WinNum: " + str(LastNumber) + ", Final Score:" + str(FinalScore))
    exit(0)
def checkIfWon(board):
    for i in range(0, 5):
        if board[i * 5:i * 5 + 5] == ['bingo'] * 5:
            return True
        elif board[i::5] == ['bingo'] * 5:
            return True
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
    for board in BingoBoardArr:
        boardlength = len(board)
        for i in range(boardlength):
            if board[i] == int(draw):
                board[i] = 'bingo'
        if checkIfWon(board):
            finalize(board, draw)