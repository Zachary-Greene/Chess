from Pieces import *  # imports pygame as well *somehow?*

pygame.init()

w, h = 720, 720

win = pygame.display.set_mode((w, h))

icon = pygame.image.load('Assets/chess_icon.ico')

pygame.display.set_caption('Chess')
pygame.display.set_icon(icon)

chess_board = pygame.image.load('Assets/chess_board.png')

# b_caught = []  # to be implemented
# w_caught = []

hold = False
run = True

# defining all the pieces x, y, width, height and color (respectively)
BlackBishop1 = Bishop(190, 10, 72, 76, 0)
BlackBishop2 = Bishop(455, 10, 72, 76, 0)
BlackKing = King(365, 10, 72, 76, 0)
BlackKnight1 = Knight(100, 10, 72, 76, 0)
BlackKnight2 = Knight(540, 10, 72, 76, 0)
BlackPawn1 = Pawn(15, 100, 72, 76, 0)
BlackPawn2 = Pawn(100, 100, 72, 76, 0)
BlackPawn3 = Pawn(190, 100, 72, 76, 0)
BlackPawn4 = Pawn(280, 100, 72, 76, 0)
BlackPawn5 = Pawn(365, 100, 72, 76, 0)
BlackPawn6 = Pawn(455, 100, 72, 76, 0)
BlackPawn7 = Pawn(540, 100, 72, 76, 0)
BlackPawn8 = Pawn(630, 100, 72, 76, 0)
BlackQueen = Queen(280, 10, 72, 76, 0)
BlackRook1 = Rook(15, 10, 72, 76, 0)
BlackRook2 = Rook(630, 10, 72, 76, 0)

WhiteBishop1 = Bishop(190, 630, 72, 76, 1)
WhiteBishop2 = Bishop(455, 630, 72, 76, 1)
WhiteKing = King(365, 630, 72, 76, 1)
WhiteKnight1 = Knight(100, 630, 72, 76, 1)
WhiteKnight2 = Knight(540, 630, 72, 76, 1)
WhitePawn1 = Pawn(15, 540, 72, 76, 1)
WhitePawn2 = Pawn(100, 540, 72, 76, 1)
WhitePawn3 = Pawn(190, 540, 72, 76, 1)
WhitePawn4 = Pawn(280, 540, 72, 76, 1)
WhitePawn5 = Pawn(365, 540, 72, 76, 1)
WhitePawn6 = Pawn(455, 540, 72, 76, 1)
WhitePawn7 = Pawn(540, 540, 72, 76, 1)
WhitePawn8 = Pawn(630, 540, 72, 76, 1)
WhiteQueen = Queen(280, 630, 72, 76, 1)
WhiteRook1 = Rook(15, 630, 72, 76, 1)
WhiteRook2 = Rook(630, 630, 72, 76, 1)


def moveTo(piece):
    global hold
    if event.type == pygame.MOUSEBUTTONDOWN:  # check if you push the mouse button down
        pos = pygame.mouse.get_pos()  # define pos as the position of the mouse cursor
        if piece.hitbox[0] <= pos[0] <= piece.hitbox[0] + piece.hitbox[2]:  # if you click inside the hitbox on the x plane
            if piece.hitbox[1] <= pos[1] <= piece.hitbox[1] + piece.hitbox[3]:  # if you click inside the hitbox on the y plane
                hold = True
    if hold:
        pos = pygame.mouse.get_pos()  # define pos as the position of the mouse cursor
        piece.x = pos[0] - (piece.hitbox[2] / 2)  # centers the piece under the cursor
        piece.y = pos[1] - (piece.hitbox[3] / 2)  # ...
        hold = True

    if event.type == pygame.MOUSEBUTTONUP:  # if you release the mouse button
        hold = False  # define hold as false


def redrawWindow():
    # drawing everything to the screen
    win.blit(chess_board, (0, 0))

    BlackBishop1.draw(win)
    BlackBishop2.draw(win)
    BlackKing.draw(win)
    BlackKnight1.draw(win)
    BlackKnight2.draw(win)
    BlackPawn1.draw(win)
    BlackPawn2.draw(win)
    BlackPawn3.draw(win)
    BlackPawn4.draw(win)
    BlackPawn5.draw(win)
    BlackPawn6.draw(win)
    BlackPawn7.draw(win)
    BlackPawn8.draw(win)
    BlackQueen.draw(win)
    BlackRook1.draw(win)
    BlackRook2.draw(win)

    WhiteBishop1.draw(win)
    WhiteBishop2.draw(win)
    WhiteKing.draw(win)
    WhiteKnight1.draw(win)
    WhiteKnight2.draw(win)
    WhitePawn1.draw(win)
    WhitePawn2.draw(win)
    WhitePawn3.draw(win)
    WhitePawn4.draw(win)
    WhitePawn5.draw(win)
    WhitePawn6.draw(win)
    WhitePawn7.draw(win)
    WhitePawn8.draw(win)
    WhiteQueen.draw(win)
    WhiteRook1.draw(win)
    WhiteRook2.draw(win)

    pygame.display.update()


while run:
    for event in pygame.event.get():  # for every event in pygame
        if event.type == pygame.QUIT:  # if an event is QUIT
            pygame.quit()  # quit pygame
            quit()  # quit the program

        moveTo(BlackBishop1)
        moveTo(BlackBishop2)

    redrawWindow()
