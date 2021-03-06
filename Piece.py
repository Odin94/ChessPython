import pygame
import Utils

from Graphics import screen, offset

class Piece():
    def __init__(self, team_color, board_x, board_y, w, h, surface):
        self.team_color = team_color

        self.board_x = board_x
        self.board_y = board_y
        self.w = w
        self.h = h

        self.captured = False

        self.surface = surface

        self.possible_moves = []

        self.move_history = []

    def draw(self, xoffset = 0): # xoffset is used for captured pieces only
        if not self.captured:
            screen.blit(self.surface, (offset[0] + self.board_x*self.w, offset[1] + self.board_y*self.h))
        else: # draw on the side of the board because the piece was captured
            screen.blit(self.surface, (offset[0] + xoffset + 8*self.w, offset[1] + self.board_y*self.h))


    def mouse_on_piece(self, mouse_pos):
        rx = self.board_x * self.w + offset[0]
        ry = self.board_y * self.h + offset[1]

        return Utils.point_in_rect(mouse_pos, (rx, ry, self.w, self.h))

    def update_possible_moves(self, board): # this method is used to generate possible moves. Actual moves are generated in the player/ai/etc class and include captured pieces
        pass


class Pawn(Piece):
    def __init__(self, team_color, board_x, board_y, w, h, surface): #x & y are Chessboard coordinates here!
        super().__init__(team_color, board_x, board_y, w, h, surface)

    def update_possible_moves(self, board):
        print(str(self.board_x) + " / " + str(self.board_y))
        moves = []

        #two steps forward
        if self.team_color == "black" and self.board_y == 6 and not board[self.board_x][self.board_y-2].occupying_piece and not board[self.board_x][self.board_y-1].occupying_piece: #board[self.board_x][self.board_y-2] should only get checked if board_y == 6 so this shouldnt ever go off board
            moves.append((self.board_x, self.board_y-2))

        elif self.team_color == "white" and self.board_y == 1 and not board[self.board_x][self.board_y+2].occupying_piece and not board[self.board_x][self.board_y+1].occupying_piece: 
            moves.append((self.board_x, self.board_y+2))

        #one step forward
        try:
            if self.team_color == "black" and board[self.board_x][self.board_y-1].occupying_piece == None: #try: because "self.board_y-1" could be off-board
                moves.append((self.board_x, self.board_y-1))

            elif self.team_color == "white" and board[self.board_x][self.board_y+1].occupying_piece == None:
                moves.append((self.board_x, self.board_y+1))
        except (IndexError, AttributeError) as e: # IndexError if the piece is at the border of the board and e.g. board_x+1 doesnt exist, Attribute if occupying_piece is None
            #print(e)
            pass

        #one step diagonally right
        try:
            if self.team_color == "black" and board[self.board_x+1][self.board_y-1].occupying_piece.team_color != self.team_color:
                moves.append((self.board_x+1, self.board_y-1))

            elif self.team_color == "white" and board[self.board_x+1][self.board_y+1].occupying_piece.team_color != self.team_color:
                moves.append((self.board_x+1, self.board_y+1))
        except (IndexError, AttributeError) as e:
            #print(e)
            pass

        #one step diagonally left
        try:
            if self.team_color == "black" and board[self.board_x-1][self.board_y-1].occupying_piece.team_color != self.team_color:
                moves.append((self.board_x-1, self.board_y-1))

            elif self.team_color == "white" and board[self.board_x-1][self.board_y+1].occupying_piece.team_color != self.team_color:
                moves.append((self.board_x-1, self.board_y+1))
        except (IndexError, AttributeError) as e:
            #print(e)
            pass

        self.possible_moves = moves


class Rook(Piece):
    def __init__(self, team_color, board_x, board_y, w, h, surface): #x & y are Chessboard coordinates here!
        super().__init__(team_color, board_x, board_y, w, h, surface)

    def update_possible_moves(self, board):
        print(str(self.board_x) + " / " + str(self.board_y))
        moves = []

        # move down
        if not self.board_y == 7:
            for i in range(self.board_y+1, len(board[0])):
                if board[self.board_x][i].occupying_piece and board[self.board_x][i].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding
                    break
                moves.append((self.board_x, i))

                if board[self.board_x][i].occupying_piece and board[self.board_x][i].occupying_piece.team_color != self.team_color: # if enemy piece is in the way, stop adding after this piece
                    break

        # move up
        if not self.board_y == 0:
            for i in reversed(range(self.board_y)): # add tiles above the rook
                print("this is",i)
                if board[self.board_x][i].occupying_piece and board[self.board_x][i].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding
                    break
                moves.append((self.board_x, i))

                if board[self.board_x][i].occupying_piece and board[self.board_x][i].occupying_piece.team_color != self.team_color: # if enemy piece is in the way, stop adding after this piece
                    break

        # move right
        for i in range(self.board_x+1, len(board[0])):
            if board[i][self.board_y].occupying_piece and board[i][self.board_y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding
                break
            moves.append((i, self.board_y))

            if board[i][self.board_y].occupying_piece and board[i][self.board_y].occupying_piece.team_color != self.team_color: # if enemy piece is in the way, stop adding after this piece
                break

        # move left
        if not self.board_x == 0:
            for i in reversed(range(self.board_x)): # add tiles left of the rook
                print(i)
                if board[i][self.board_y].occupying_piece and board[i][self.board_y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding
                    break
                moves.append((i, self.board_y))

                if board[i][self.board_y].occupying_piece and board[i][self.board_y].occupying_piece.team_color != self.team_color: # if enemy piece is in the way, stop adding after this piece
                    break

        self.possible_moves = moves



class Knight(Piece):
    def __init__(self, team_color, board_x, board_y, w, h, surface): #x & y are Chessboard coordinates here!
        super().__init__(team_color, board_x, board_y, w, h, surface)

    def update_possible_moves(self, board):
        print(str(self.board_x) + " / " + str(self.board_y))
        moves = []

        # every combination of +-2 and +-1 
        for x, y in ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
            try:
                if self.board_x + x  < 0 or self.board_y + y < 0: # python accepts negative indices which is not intended behaviour in this case.
                    raise IndexError("negative list indices are considered out of range")


                if (not board[self.board_x + x][self.board_y + y].occupying_piece) or (not board[self.board_x + x][self.board_y + y].occupying_piece.team_color == self.team_color): # if empty or not occupied by own unit, add move
                    print(self.board_x + x, self.board_y + y)
                    moves.append((self.board_x + x, self.board_y + y))
            except (IndexError, AttributeError) as e:
                pass

        self.possible_moves = moves


class Bishop(Piece):
    def __init__(self, team_color, board_x, board_y, w, h, surface): #x & y are Chessboard coordinates here!
        super().__init__(team_color, board_x, board_y, w, h, surface)

    def update_possible_moves(self, board):
        print(str(self.board_x) + " / " + str(self.board_y))
        moves = []

        # bottom left
        for x, y in zip(reversed(range(self.board_x)), range(self.board_y+1, len(board[0]))):
            try:
                if board[x][y].occupying_piece:
                    if not board[x][y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding. If enemy piece is in the way, add it and then stop adding
                        moves.append((x, y))
                    break
                moves.append((x, y))
            except IndexError as e:
                print(e)
                pass

        # bottom right
        for x, y in zip(range(self.board_x+1, len(board)), range(self.board_y+1, len(board[0]))):
            try:
                if board[x][y].occupying_piece:
                    if not board[x][y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding. If enemy piece is in the way, add it and then stop adding
                        moves.append((x, y))
                    break
                moves.append((x, y))
            except IndexError as e:
                print(e)
                pass

        # top left
        for x, y in zip(reversed(range(self.board_x)), reversed(range(self.board_y))):
            try:
                if board[x][y].occupying_piece:
                    if not board[x][y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding. If enemy piece is in the way, add it and then stop adding
                        moves.append((x, y))
                    break
                moves.append((x, y))
            except IndexError as e:
                print(e)
                pass

        # top right
        for x, y in zip(range(self.board_x+1, len(board)), reversed(range(self.board_y))):
            try:
                if board[x][y].occupying_piece:
                    if not board[x][y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding. If enemy piece is in the way, add it and then stop adding
                        moves.append((x, y))
                    break
                moves.append((x, y))
            except IndexError as e:
                print(e)
                pass

        self.possible_moves = moves


class Queen(Piece):
    def __init__(self, team_color, board_x, board_y, w, h, surface): #x & y are Chessboard coordinates here!
        super().__init__(team_color, board_x, board_y, w, h, surface)

    def update_possible_moves(self, board):
        print(str(self.board_x) + " / " + str(self.board_y))
        moves = []

        # move down
        if not self.board_y == 7:
            for i in range(self.board_y+1, len(board[0])):
                if board[self.board_x][i].occupying_piece and board[self.board_x][i].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding
                    break
                moves.append((self.board_x, i))

                if board[self.board_x][i].occupying_piece and board[self.board_x][i].occupying_piece.team_color != self.team_color: # if enemy piece is in the way, stop adding after this piece
                    break

        # move up
        if not self.board_y == 0:
            for i in reversed(range(self.board_y)): # add tiles above the rook
                print("this is",i)
                if board[self.board_x][i].occupying_piece and board[self.board_x][i].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding
                    break
                moves.append((self.board_x, i))

                if board[self.board_x][i].occupying_piece and board[self.board_x][i].occupying_piece.team_color != self.team_color: # if enemy piece is in the way, stop adding after this piece
                    break

        # move right
        for i in range(self.board_x+1, len(board)):
            if board[i][self.board_y].occupying_piece and board[i][self.board_y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding
                break
            moves.append((i, self.board_y))

            if board[i][self.board_y].occupying_piece and board[i][self.board_y].occupying_piece.team_color != self.team_color: # if enemy piece is in the way, stop adding after this piece
                break

        # move left
        if not self.board_x == 0:
            for i in reversed(range(self.board_x)): # add tiles left of the rook
                print(i)
                if board[i][self.board_y].occupying_piece and board[i][self.board_y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding
                    break
                moves.append((i, self.board_y))

                if board[i][self.board_y].occupying_piece and board[i][self.board_y].occupying_piece.team_color != self.team_color: # if enemy piece is in the way, stop adding after this piece
                    break


        # diagonal movement

        # bottom left
        for x, y in zip(reversed(range(self.board_x)), range(self.board_y+1, len(board[0]))):
            try:
                if board[x][y].occupying_piece:
                    if not board[x][y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding. If enemy piece is in the way, add it and then stop adding
                        moves.append((x, y))
                    break
                moves.append((x, y))
            except IndexError as e:
                print(e)
                pass

        # bottom right
        for x, y in zip(range(self.board_x+1, len(board)), range(self.board_y+1, len(board[0]))):
            try:
                if board[x][y].occupying_piece:
                    if not board[x][y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding. If enemy piece is in the way, add it and then stop adding
                        moves.append((x, y))
                    break
                moves.append((x, y))
            except IndexError as e:
                print(e)
                pass

        # top left
        for x, y in zip(reversed(range(self.board_x)), reversed(range(self.board_y))):
            try:
                if board[x][y].occupying_piece:
                    if not board[x][y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding. If enemy piece is in the way, add it and then stop adding
                        moves.append((x, y))
                    break
                moves.append((x, y))
            except IndexError as e:
                print(e)
                pass

        # top right
        for x, y in zip(range(self.board_x+1, len(board)), reversed(range(self.board_y))):
            try:
                if board[x][y].occupying_piece:
                    if not board[x][y].occupying_piece.team_color == self.team_color: # if own piece is in the way, stop adding. If enemy piece is in the way, add it and then stop adding
                        moves.append((x, y))
                    break
                moves.append((x, y))
            except IndexError as e:
                print(e)
                pass

        self.possible_moves = moves


class King(Piece):
    def __init__(self, team_color, board_x, board_y, w, h, surface): #x & y are Chessboard coordinates here!
        super().__init__(team_color, board_x, board_y, w, h, surface)

    def update_possible_moves(self, board):
        print(str(self.board_x) + " / " + str(self.board_y))
        moves = []

        for x, y in ((1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)):
            try:
                if self.board_x + x  < 0 or self.board_y + y < 0: # python accepts negative indices which is not intended behaviour in this case.
                    raise IndexError("negative list indices are considered out of range")

                print(self.board_x + x, self.board_y + y)
                if (not board[self.board_x + x][self.board_y + y].occupying_piece) or (not board[self.board_x + x][self.board_y + y].occupying_piece.team_color == self.team_color): # if empty or not occupied by own unit, add move
                    moves.append((self.board_x + x, self.board_y + y))
            except (IndexError, AttributeError) as e:
                pass

        # castling
        
        if not self.move_history: # King must not have moved yet
            try:
                if not board[0][self.board_y].occupying_piece.move_history: # rook must not have moved yet
                    blocked = False
                    for x in range(1, self.board_x):
                        if board[x][self.board_y].occupying_piece:
                            blocked = True
                            break
                        #TODO: check if king is in check or if any of the positions between rook and king are under attack
                    if not blocked:
                        moves.append((2, self.board_y, "castling"))
            except AttributeError as e:
                print(e)

            try:
                if not board[7][self.board_y].occupying_piece.move_history: # rook must not have moved yet
                    blocked = False
                    for x in range(self.board_x+1, 7):
                        if board[x][self.board_y].occupying_piece:
                            blocked = True
                            break
                        #TODO: check if king is in check or if any of the positions between rook and king are under attack
                    if not blocked:
                        moves.append((6, self.board_y, "castling"))
            except AttributeError as e:
                print(e)

        



        self.possible_moves = moves