board = [
    [
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
    ],
    [
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
    ],
    [
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
    ],
    [
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
    ],
    [
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
    ],
    [
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
    ],
    [
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
    ],
    [
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
        "--",
    ],
]
board_original = board.copy()
for file in range(6):

    f = open(f"D:\STEVE\input\\file{file+1}.txt", "r")
    data_list = f.read().split()

    color = data_list[0]

    if color == chr(66) or color == chr(98):
        color = int(0)
    elif color == chr(67) or color == chr(99):
        color = int(1)
    else:
        print("Podano złe dane")
        continue

    space_row = int(data_list[1])

    if space_row <= 8:
        pass
    else:
        print("Podano złe dane")
        continue

    space_col = int(data_list[2])

    if space_col <= 8:
        pass
    else:
        print("Podano złe dane")
        continue

    piece = data_list[3]
    piece.lower()
    if (
        piece == "w"
        or piece == "g"
        or piece == "s"
        or piece == "k"
        or piece == "h"
        or piece == "p"
    ):
        pass
    else:
        print("Podano złe dane")
        continue

    if color == 0:
        piece = piece.upper()
    else:
        pass

    for row in range(8):
        for column in range(8):
            if board[space_row - 1][space_col - 1] == board[row][column]:
                board[space_row - 1][space_col - 1] = piece

    def get_pawn_moves(space_row, space_col, board):
        if color == 0:
            if board[space_row - 2][space_col - 1] == "--":
                board[space_row - 2][space_col - 1] = "x"
                # if sprawdzający czy 1 miejsce przed psotawionym szachem jest wolne
                if space_row >= 3 and board[space_row - 3][space_col - 1] == "--":
                    board[space_row - 3][space_col - 1] = "x"
                # if sprawdzający czy 2 miejscea przed postawionym szachem są wolne
        else:
            if board[space_row + 1][space_col - 1] == "--":
                board[space_row][space_col - 1] = "x"
                # if sprawdzający czy 1 miejsce przed psotawionym szachem jest wolne
                if space_row <= 6 and board[space_row + 1][space_col - 1] == "--":
                    board[space_row + 1][space_col - 1] = "x"
                # if sprawdzający czy 2 miejscea przed postawionym szachem są wolne

    def get_rook_moves(space_row, space_col, board):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        # 4 kierunki poruszania sie
        for d in directions:
            for i in range(1, 8):
                end_row = space_row + d[0] * i - 1
                end_col = space_col + d[1] * i - 1
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    if board[end_row][end_col] == "--":
                        board[end_row][end_col] = "x"
                else:
                    break

    def get_bishop_moves(space_row, space_col, board):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        # 4 kierunki poruszania sie tym razem na ukos XD
        for d in directions:
            for i in range(1, 8):
                end_row = space_row + d[0] * i - 1
                end_col = space_col + d[1] * i - 1
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    if board[end_row][end_col] == "--":
                        board[end_row][end_col] = "x"
                else:
                    break

    def get_knight_moves(space_row, space_col, board):
        possible_moves_knight = (
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        )
        # 8 kierunków poruszania sie tym razem ELECZKA
        for moves in possible_moves_knight:
            end_row = space_row + moves[0] - 1
            end_col = space_col + moves[1] - 1
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                if board[end_row][end_col] == "--":
                    board[end_row][end_col] = "x"
            else:
                break

    def get_king_moves(space_row, space_col, board):
        possibe_moves_king = (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        )
        for move in range(8):
            end_row = space_row + possibe_moves_king[move][0] - 1
            end_col = space_col + possibe_moves_king[move][1] - 1
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                if board[end_row][end_col] == "--":
                    board[end_row][end_col] = "x"
            else:
                break

    def get_queen_moves(space_row, space_col, board):
        get_bishop_moves(space_row, space_col, board)
        get_rook_moves(space_row, space_col, board)

    piece = piece.lower()

    # match piece:
    #     case "p": get_pawn_moves(space_row, space_col, board)
    #     case "h":get_queen_moves(space_row, space_col, board)
    #     case "w":get_rook_moves(space_row, space_col, board)
    #     case "s":get_knight_moves(space_row, space_col, board)
    #     case "g":get_bishop_moves(space_row, space_col, board)
    #     case "k":get_king_moves(space_row, space_col, board)

    if piece == "p":
        get_pawn_moves(space_row, space_col, board)
    elif piece == "h":
        get_queen_moves(space_row, space_col, board)
    elif piece == "w":
        get_rook_moves(space_row, space_col, board)
    elif piece == "s":
        get_knight_moves(space_row, space_col, board)
    elif piece == "g":
        get_bishop_moves(space_row, space_col, board)
    elif piece == "k":
        get_king_moves(space_row, space_col, board)

    # print(board)
    # print("\n")
    with open(f"D:\STEVE\output\output{file+1}.txt", "w") as f:
        for _list in board:
            for i in _list:
                f.write(str(i) + "\t")
            f.write("\n")

    board = [
        [
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
        ],
        [
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
        ],
        [
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
        ],
        [
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
        ],
        [
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
        ],
        [
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
        ],
        [
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
        ],
        [
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
            "--",
        ],
    ]
