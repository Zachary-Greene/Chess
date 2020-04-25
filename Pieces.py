import pygame

b_bishop = pygame.transform.scale(pygame.image.load('Assets/black_bishop.png'), (72, 76))
b_king = pygame.transform.scale(pygame.image.load('Assets/black_king.png'), (72, 76))
b_knight = pygame.transform.scale(pygame.image.load('Assets/black_knight.png'), (72, 76))
b_pawn = pygame.transform.scale(pygame.image.load('Assets/black_pawn.png'), (72, 76))
b_queen = pygame.transform.scale(pygame.image.load('Assets/black_queen.png'), (72, 76))
b_rook = pygame.transform.scale(pygame.image.load('Assets/black_rook.png'), (72, 76))

w_bishop = pygame.transform.scale(pygame.image.load('Assets/white_bishop.png'), (72, 76))
w_king = pygame.transform.scale(pygame.image.load('Assets/white_king.png'), (72, 76))
w_knight = pygame.transform.scale(pygame.image.load('Assets/white_knight.png'), (72, 76))
w_pawn = pygame.transform.scale(pygame.image.load('Assets/white_pawn.png'), (72, 76))
w_queen = pygame.transform.scale(pygame.image.load('Assets/white_queen.png'), (72, 76))
w_rook = pygame.transform.scale(pygame.image.load('Assets/white_rook.png'), (72, 76))


class Bishop(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.b_img = b_bishop
        self.w_img = w_bishop

    def draw(self, win):
        if self.color == 0:
            win.blit(b_bishop, (self.x, self.y))
        if self.color == 1:
            win.blit(w_bishop, (self.x, self.y))

        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # draw the hitbox
        self.hitbox = (self.x, self.y, self.width, self.height)  # create the hitbox


class King(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.b_img = b_king
        self.w_img = w_king

    def draw(self, win):
        if self.color == 0:
            win.blit(b_king, (self.x, self.y))
        if self.color == 1:
            win.blit(w_king, (self.x, self.y))

        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # draw the hitbox
        self.hitbox = (self.x, self.y, self.width, self.height)  # create the hitbox


class Knight(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.b_img = b_knight
        self.w_img = w_knight

    def draw(self, win):
        if self.color == 0:
            win.blit(b_knight, (self.x, self.y))
        if self.color == 1:
            win.blit(w_knight, (self.x, self.y))

        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # draw the hitbox
        self.hitbox = (self.x, self.y, self.width, self.height)  # create the hitbox


class Pawn(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.b_img = b_pawn
        self.w_img = w_pawn

    def draw(self, win):
        if self.color == 0:
            win.blit(b_pawn, (self.x, self.y))
        if self.color == 1:
            win.blit(w_pawn, (self.x, self.y))

        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # draw the hitbox
        self.hitbox = (self.x, self.y, self.width, self.height)  # create the hitbox


class Queen(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.b_img = b_queen
        self.w_img = w_queen

    def draw(self, win):
        if self.color == 0:
            win.blit(b_queen, (self.x, self.y))
        if self.color == 1:
            win.blit(w_queen, (self.x, self.y))

        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # draw the hitbox
        self.hitbox = (self.x, self.y, self.width, self.height)  # create the hitbox


class Rook(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.b_img = b_rook
        self.w_img = w_rook

    def draw(self, win):
        if self.color == 0:
            win.blit(b_rook, (self.x, self.y))
        if self.color == 1:
            win.blit(w_rook, (self.x, self.y))

        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # draw the hitbox
        self.hitbox = (self.x, self.y, self.width, self.height)  # create the hitbox
