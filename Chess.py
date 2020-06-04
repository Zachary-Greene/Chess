from Pieces import *

pygame.init()

w, h = 720, 720

win = pygame.display.set_mode((w, h))

icon = pygame.image.load('Assets/chess_icon.ico')

pygame.display.set_caption('Chess')
pygame.display.set_icon(icon)

chess_board = pygame.image.load('Assets/chess_board.png')

# b_caught = []  # to be implemented
# w_caught = []

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
    mousePos = pygame.mouse.get_pos()  # mousePos as the position of the mouse cursor
    click = pygame.mouse.get_pressed()  # define click as a method of detecting a mouse button down object

    if click[0] == 1 and piece.hitbox[0] <= mousePos[0] <= piece.hitbox[0] + piece.hitbox[2]:  # if the left mouse button is clicked and
        # then if its clicked in the hitbox (x plane)
        if piece.hitbox[1] <= mousePos[1] <= piece.hitbox[1] + piece.hitbox[3]:  # if its clicked in the hitbox (y plane)
            piece.x = mousePos[0] - (piece.hitbox[2] / 2)  # centers the piece under the mouse cursor
            piece.y = mousePos[1] - (piece.hitbox[3] / 2)  # ...


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
            
        # calling the moveTo function for each piece
        moveTo(BlackBishop1)
        moveTo(BlackBishop2)
        moveTo(BlackKing)
        moveTo(BlackKnight1)
        moveTo(BlackKnight2)
        moveTo(BlackPawn1)
        moveTo(BlackPawn2)
        moveTo(BlackPawn3)
        moveTo(BlackPawn4)
        moveTo(BlackPawn5)
        moveTo(BlackPawn6)
        moveTo(BlackPawn7)
        moveTo(BlackPawn8)
        moveTo(BlackQueen)
        moveTo(BlackRook1)
        moveTo(BlackRook2)

        moveTo(WhiteBishop1)
        moveTo(WhiteBishop2)
        moveTo(WhiteKing)
        moveTo(WhiteKnight1)
        moveTo(WhiteKnight2)
        moveTo(WhitePawn1)
        moveTo(WhitePawn2)
        moveTo(WhitePawn3)
        moveTo(WhitePawn4)
        moveTo(WhitePawn5)
        moveTo(WhitePawn6)
        moveTo(WhitePawn7)
        moveTo(WhitePawn8)
        moveTo(WhiteQueen)
        moveTo(WhiteRook1)
        moveTo(WhiteRook2)

    redrawWindow()
