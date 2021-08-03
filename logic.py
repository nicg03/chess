import pygame 


class Core:
    def __init__(self, screen):
        self.screen = screen

        #  white
        self.wrook = pygame.image.load('images\\wrook.png')
        self.rect_wrook1 = self.wrook.get_rect()
        self.rect_wrook2 = self.wrook.get_rect()

        self.wknight = pygame.image.load('images\\wknight.png')
        self.rect_wknight1 = self.wknight.get_rect()
        self.rect_wknight2 = self.wknight.get_rect()

        self.wqueen = pygame.image.load('images\\wqueen.png')
        self.rect_wqueen = self.wqueen.get_rect()

        self.wking = pygame.image.load('images\\wking.png')
        self.rect_wking = self.wking.get_rect()

        self.wbishop = pygame.image.load('images\\wbishop.png')
        self.rect_wbishop1 = self.wbishop.get_rect()
        self.rect_wbishop2 = self.wbishop.get_rect()

        self.wpawn = pygame.image.load('images\\wpawn.png')
        self.rect_wpawn1 = self.wpawn.get_rect()
        self.rect_wpawn2 = self.wpawn.get_rect()
        self.rect_wpawn3 = self.wpawn.get_rect()
        self.rect_wpawn4 = self.wpawn.get_rect()
        self.rect_wpawn5 = self.wpawn.get_rect()
        self.rect_wpawn6 = self.wpawn.get_rect()
        self.rect_wpawn7 = self.wpawn.get_rect()
        self.rect_wpawn8 = self.wpawn.get_rect()

        #  black
        self.brook = pygame.image.load('images\\brook.png')
        self.rect_brook1 = self.brook.get_rect()
        self.rect_brook2 = self.brook.get_rect()

        self.bknight = pygame.image.load('images\\bknight.png')
        self.rect_bknight1 = self.bknight.get_rect()
        self.rect_bknight2 = self.bknight.get_rect()

        self.bqueen = pygame.image.load('images\\bqueen.png')
        self.rect_bqueen = self.bqueen.get_rect()

        self.bking = pygame.image.load('images\\bking.png')
        self.rect_bking = self.bking.get_rect()

        self.bbishop = pygame.image.load('images\\bbishop.png')
        self.rect_bbishop1 = self.bbishop.get_rect()
        self.rect_bbishop2 = self.bbishop.get_rect()

        self.bpawn = pygame.image.load('images\\bpawn.png')
        self.rect_bpawn1 = self.bpawn.get_rect()
        self.rect_bpawn2 = self.bpawn.get_rect()
        self.rect_bpawn3 = self.bpawn.get_rect()
        self.rect_bpawn4 = self.bpawn.get_rect()
        self.rect_bpawn5 = self.bpawn.get_rect()
        self.rect_bpawn6 = self.bpawn.get_rect()
        self.rect_bpawn7 = self.bpawn.get_rect()
        self.rect_bpawn8 = self.bpawn.get_rect()

        self.go_move = []

        self.rect_black_pawn = [self.rect_bpawn1, self.rect_bpawn2, self.rect_bpawn3, self.rect_bpawn4, self.rect_bpawn5, self.rect_bpawn6, self.rect_bpawn7, self.rect_bpawn8]
        self.rect_white_pawn = [self.rect_wpawn1, self.rect_wpawn2, self.rect_wpawn3, self.rect_wpawn4, self.rect_wpawn5, self.rect_wpawn6, self.rect_wpawn7, self.rect_wpawn8]

        self.black_in_order = [self.brook, self.bknight, self.bbishop, self.bqueen, self.bking, self.bbishop, self.bknight, self.brook]
        self.white_in_order = [self.wrook, self.wknight, self.wbishop, self.wqueen, self.wking, self.wbishop, self.wknight, self.wrook]

        self.rect_black_in_order = [self.rect_brook1, self.rect_bknight1, self.rect_bbishop1, self.rect_bqueen, self.rect_bking, self.rect_bbishop2, self.rect_bknight2, self.rect_brook2]
        self.rect_white_in_order = [self.rect_wrook1, self.rect_wknight1, self.rect_wbishop1, self.rect_wqueen, self.rect_wking, self.rect_wbishop2, self.rect_wknight2, self.rect_wrook2]

        self.order_of_pos = self.rect_white_in_order + self.rect_white_pawn + self.rect_black_pawn + self.rect_black_in_order
        self.order_of_pos_image = self.white_in_order + [self.wpawn]*8 + [self.bpawn]*8 + self.black_in_order

        self.pos = []
        self.counter = None

    def return_counter(self, counter):
        self.counter = counter

    def draw_board(self, pos):
        for i in range(0, 4):
            if i < 2:
                if i == 0:
                    for a in range(0, 8):
                        rect = self.rect_white_in_order[a]
                        rect.centerx, rect.centery = pos[a]
                        self.screen.blit(self.white_in_order[a], rect)
                else:
                    for a in range(0, 8):
                        rect = self.rect_white_pawn[a]
                        rect.centerx, rect.centery = pos[8+a]
                        self.screen.blit(self.wpawn, rect)
            else:
                if i == 3:
                    for a in range(0, 8):
                        rect = self.rect_black_in_order[a]
                        rect.centerx, rect.centery = pos[24+a]
                        self.screen.blit(self.black_in_order[a], rect)
                else:
                    for a in range(0, 8):
                        rect = self.rect_black_pawn[a]
                        rect.centerx, rect.centery = pos[16+a]
                        self.screen.blit(self.bpawn, rect)

    def move(self, click_pos, pos, internal_command, go_move):
        self.go_move = go_move
        if not internal_command and not self.go_move:
            for i in pos:
                if click_pos[0] in range(i[0] - 30, i[0] + 30) and click_pos[1] in range(i[1] - 30, i[1] + 30):
                    self.go_move = [self.order_of_pos[pos.index(i)], self.order_of_pos_image[pos.index(i)],
                                    pos.index(i)]
                else:
                    continue
            return True, self.go_move
        elif internal_command and self.go_move:
            brain = Brain(pos, self.go_move[2], click_pos, self.counter)
            next_element_position = brain.return_next_pos()[0]
            self.go_move[0].center = next_element_position
            self.screen.blit(self.go_move[1], self.go_move[0])
            #  pos[self.go_move[2]] = self.go_move[0].center
            pos = brain.return_next_pos()[1]
            self.go_move = []

            return False, self.go_move, pos


class Brain:
    def __init__(self, pos, touched_element, to_move, counter):
        self.counter = counter
        self.pos = pos
        self.in_order = ['wrook1', 'wknight1', 'wbishop1', 'wqueen', 'wking', 'wbishop2', 'wknight2', 'wrook2', 'wpawn1',
                         'wpawn2', 'wpawn3', 'wpawn4', 'wpawn5', 'wpawn6', 'wpawn7', 'wpawn8',
                         'bpawn1', 'bpawn2', 'bpawn3', 'bpawn4', 'bpawn5', 'bpawn6', 'bpawn7', 'bpawn8',
                         'brook1', 'bknight1', 'bbishop1', 'bqueen', 'bking', 'bbishop2', 'bknight2', 'brook2']
        self.grid_pos = []
        self.dict_element_and_pos = {}
        self.element = self.in_order[touched_element]
        self.to_move = to_move
        self.x_y = [31, 94, 157, 220, 283, 346, 409, 472]
        self.x = self.x_y
        self.y = self.x_y

    def create_requirements(self):
        for i in range(0, len(self.pos)):
            self.dict_element_and_pos[self.in_order[i]] = self.pos[i]
        for i in self.x_y:
            for a in self.x_y:
                self.grid_pos.append((i, a))

    def check_if_valid(self):
        go = False
        is_opponent = False
        is_opponent_name = None
        possible_opponent_pos = []
        possible_move = []
        #  PAWN
        if self.element[1:].startswith('pawn'):
            if self.element.startswith('w'):
                possible_opponent_pos.append((self.dict_element_and_pos[self.element][0]-63, self.dict_element_and_pos[self.element][1]-63))
                possible_opponent_pos.append((self.dict_element_and_pos[self.element][0]+63, self.dict_element_and_pos[self.element][1]-63))
            else:
                possible_opponent_pos.append((self.dict_element_and_pos[self.element][0]-63, self.dict_element_and_pos[self.element][1]+63))
                possible_opponent_pos.append((self.dict_element_and_pos[self.element][0]+63, self.dict_element_and_pos[self.element][1]+63))

            if self.dict_element_and_pos[self.element][1] in [94, 409]:
                if self.dict_element_and_pos[self.element][1] == 409:
                    possible_move.append((self.dict_element_and_pos[self.element][0], self.dict_element_and_pos[self.element][1]-63*2))
                    possible_move.append((self.dict_element_and_pos[self.element][0], self.dict_element_and_pos[self.element][1]-63))
                else:
                    possible_move.append((self.dict_element_and_pos[self.element][0], self.dict_element_and_pos[self.element][1]+63*2))
                    possible_move.append((self.dict_element_and_pos[self.element][0], self.dict_element_and_pos[self.element][1]+63))
            else:
                if self.element.startswith('w'):
                    possible_move.append((self.dict_element_and_pos[self.element][0], self.dict_element_and_pos[self.element][1]-63))
                else:
                    possible_move.append((self.dict_element_and_pos[self.element][0], self.dict_element_and_pos[self.element][1]+63))

            for i in self.pos:
                for a in possible_opponent_pos:
                    if a[0] in range(i[0]-30, i[0]+30) and a[1] in range(i[1]-30, i[1]+30):
                        possible_move.append(a)
                    else:
                        continue

            for i in possible_move:
                if self.found_grid_pos()[0] in range(i[0]-30, i[0]+30) and self.found_grid_pos()[1] in range(i[1]-30, i[1]+30):
                    go = True
                    for a in possible_opponent_pos:
                        if a[0] == i[0] and a[1] == i[1]:
                            is_opponent = True
                            for b in self.pos:
                                if b[0] in range(a[0]-30, a[0]+30) and b[1] in range(a[1]-30, a[1]+30):
                                    is_opponent_name = self.in_order[self.pos.index(b)]
                        else:
                           pass
                else:
                    continue

            for i in self.pos:
                if self.found_grid_pos()[0] in range(i[0]-30, i[0]+30) and self.found_grid_pos()[1] in range(i[1]-30, i[1]+30) and not is_opponent:
                    go = False
                else:
                    continue

            if self.element[0] == 'b' and self.counter % 2 == 0:
                pass
            elif self.element[0] == 'w' and self.counter % 2 != 0:
                pass
            else:
                go = False

            #  script finale
            if go and is_opponent:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
                self.pos[self.in_order.index(is_opponent_name)] = (1000, 2000)
            elif go:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
            else:
                pass

            return go

        #  ROOK
        elif self.element[1:].startswith('rook'):
            possible_move = []
            possible_opponent_pos = []
            is_opponent = False
            is_opponent_name = None
            go = False

            x = self.pos[self.in_order.index(self.element)][0]
            y = self.pos[self.in_order.index(self.element)][1]

            list_pos = []
            if self.found_grid_pos()[0] == x:
                if self.found_grid_pos()[1] < y:
                    self.y = sorted(self.y, reverse=True)
                    self.y = self.y[self.y.index(y)+1:]
                else:
                    self.y = self.y[self.y.index(y)+1:]
                for y1 in self.y:
                    list_pos.append((x, y1))
            else:
                if self.found_grid_pos()[0] < x:
                    self.x = sorted(self.x, reverse=True)
                    self.x = self.x[self.x.index(x)+1:]
                else:
                    self.x = self.x[self.x.index(x)+1:]
                for x1 in self.x:
                    list_pos.append((x1, y))

            self.x, self.y = self.x_y, self.x_y

            for p in list_pos:
                is_empty = True
                for a in self.pos:
                    if a == p:
                        is_empty = False
                        possible_opponent_pos.append(a)
                        break
                    else:
                        pass
                if is_empty:
                    possible_move.append((p))
                else:
                    break

            #  script finale
            for a in possible_opponent_pos:
                if self.found_grid_pos()[0] in range(a[0]-30, a[0]+30) and self.found_grid_pos()[1] in range(a[1]-30, a[1]+30):
                    for b in self.dict_element_and_pos.keys():
                        if self.dict_element_and_pos[b] == a:
                            is_opponent_name = b
                    is_opponent = True
                    go = True
                else:
                    continue

            if not is_opponent:
                for a in possible_move:
                    if self.found_grid_pos() == a:
                        go = True
                        is_opponent = False
                    else:
                        continue

            if self.element[0] == 'b' and self.counter % 2 == 0:
                pass
            elif self.element[0] == 'w' and self.counter % 2 != 0:
                pass
            else:
                go = False

            if go and is_opponent:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
                self.pos[self.in_order.index(is_opponent_name)] = (1000, 2000)
            elif go:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
            else:
                pass

            return go

        elif self.element[1:].startswith('bishop'):
            possible_move = []
            possible_opponent_pos = []
            is_opponent = False
            is_opponent_name = None
            go = False

            x = self.pos[self.in_order.index(self.element)][0]
            y = self.pos[self.in_order.index(self.element)][1]

            list_pos = []

            x_is_reverse = False
            y_is_reverse = False

            if self.found_grid_pos()[0] < x:
                x_is_reverse = True

            if self.found_grid_pos()[1] < y:
                y_is_reverse = True

            if x_is_reverse and y_is_reverse:
                self.x = sorted(self.x, reverse=True)
                self.y = sorted(self.y, reverse=True)
                self.x = self.x[self.x.index(x)+1:]
                self.y = self.y[self.y.index(y)+1:]
            elif x_is_reverse and not y_is_reverse:
                self.x = sorted(self.x, reverse=True)
                self.x = self.x[self.x.index(x)+1:]
                self.y = self.y[self.y.index(y)+1:]
            elif not x_is_reverse and y_is_reverse:
                self.y = sorted(self.y, reverse=True)
                self.x = self.x[self.x.index(x)+1:]
                self.y = self.y[self.y.index(y)+1:]
            else:
                self.x = self.x[self.x.index(x)+1:]
                self.y = self.y[self.y.index(y)+1:]

            list_pos = list(zip(self.x, self.y))
            self.x, self.y = self.x_y, self.x_y

            for p in list_pos:
                is_empty = True
                for a in self.pos:
                    if a == p:
                        is_empty = False
                        possible_opponent_pos.append(a)
                        break
                    else:
                        pass
                if is_empty:
                    possible_move.append((p))
                else:
                    break

            #  script finale
            for a in possible_opponent_pos:
                if self.found_grid_pos()[0] in range(a[0]-30, a[0]+30) and self.found_grid_pos()[1] in range(a[1]-30, a[1]+30):
                    for b in self.dict_element_and_pos.keys():
                        if self.dict_element_and_pos[b] == a:
                            is_opponent_name = b
                    is_opponent = True
                    go = True
                else:
                    continue

            if not is_opponent:
                for a in possible_move:
                    if self.found_grid_pos() == a:
                        go = True
                        is_opponent = False
                    else:
                        continue

            if self.element[0] == 'b' and self.counter % 2 == 0:
                pass
            elif self.element[0] == 'w' and self.counter % 2 != 0:
                pass
            else:
                go = False

            if go and is_opponent:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
                self.pos[self.in_order.index(is_opponent_name)] = (1000, 2000)
            elif go:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
            else:
                pass

            return go
        elif self.element[1:].startswith('knight'):
            possible_move = []
            possible_opponent_pos = []
            is_opponent = False
            is_opponent_name = None
            go = False

            list_pos = []

            x = self.pos[self.in_order.index(self.element)][0]
            y = self.pos[self.in_order.index(self.element)][1]

            if self.found_grid_pos()[0] < x and self.found_grid_pos()[1] < y:
                list_pos.append((x-63, y-126))
                list_pos.append((x-126, y-63))
            elif self.found_grid_pos()[0] > x and self.found_grid_pos()[1] < y:
                list_pos.append((x+63, y-126))
                list_pos.append((x+126, y-63))
            elif self.found_grid_pos()[0] < x and self.found_grid_pos()[1] > y:
                list_pos.append((x-126, y+63))
                list_pos.append((x-63, y+126))
            elif self.found_grid_pos()[0] > x and self.found_grid_pos()[1] > y:
                list_pos.append((x+63, y+126))
                list_pos.append((x+126, y+63))
            else:
                pass

            for p in list_pos:
                is_empty = True
                for a in self.pos:
                    if a == p:
                        is_empty = False
                        possible_opponent_pos.append(a)
                        break
                    else:
                        pass
                if is_empty:
                    possible_move.append((p))
                else:
                    break

            #  script finale
            for a in possible_opponent_pos:
                if self.found_grid_pos()[0] in range(a[0] - 30, a[0] + 30) and self.found_grid_pos()[1] in range(
                        a[1] - 30, a[1] + 30):
                    for b in self.dict_element_and_pos.keys():
                        if self.dict_element_and_pos[b] == a:
                            is_opponent_name = b
                    is_opponent = True
                    go = True
                else:
                    continue

            if not is_opponent:
                for a in possible_move:
                    if self.found_grid_pos() == a:
                        go = True
                        is_opponent = False
                    else:
                        continue

            if self.element[0] == 'b' and self.counter % 2 == 0:
                pass
            elif self.element[0] == 'w' and self.counter % 2 != 0:
                pass
            else:
                go = False

            if go and is_opponent:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
                self.pos[self.in_order.index(is_opponent_name)] = (1000, 2000)
            elif go:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
            else:
                pass

            return go
        elif self.element[1:].startswith('queen'):
            possible_move = []
            possible_opponent_pos = []
            is_opponent = False
            is_opponent_name = None
            go = False

            list_pos = []
            x = self.pos[self.in_order.index(self.element)][0]
            y = self.pos[self.in_order.index(self.element)][1]

            if self.found_grid_pos()[0] == x or self.found_grid_pos()[1] == y:
                # rook script

                if self.found_grid_pos()[0] == x:
                    if self.found_grid_pos()[1] < y:
                        self.y = sorted(self.y, reverse=True)
                        self.y = self.y[self.y.index(y) + 1:]
                    else:
                        self.y = self.y[self.y.index(y) + 1:]
                    for y1 in self.y:
                        list_pos.append((x, y1))
                else:
                    if self.found_grid_pos()[0] < x:
                        self.x = sorted(self.x, reverse=True)
                        self.x = self.x[self.x.index(x) + 1:]
                    else:
                        self.x = self.x[self.x.index(x) + 1:]
                    for x1 in self.x:
                        list_pos.append((x1, y))

                self.x, self.y = self.x_y, self.x_y

            else:
                #  bishop script
                x_is_reverse = False
                y_is_reverse = False

                if self.found_grid_pos()[0] < x:
                    x_is_reverse = True

                if self.found_grid_pos()[1] < y:
                    y_is_reverse = True

                if x_is_reverse and y_is_reverse:
                    self.x = sorted(self.x, reverse=True)
                    self.y = sorted(self.y, reverse=True)
                    self.x = self.x[self.x.index(x) + 1:]
                    self.y = self.y[self.y.index(y) + 1:]
                elif x_is_reverse and not y_is_reverse:
                    self.x = sorted(self.x, reverse=True)
                    self.x = self.x[self.x.index(x) + 1:]
                    self.y = self.y[self.y.index(y) + 1:]
                elif not x_is_reverse and y_is_reverse:
                    self.y = sorted(self.y, reverse=True)
                    self.x = self.x[self.x.index(x) + 1:]
                    self.y = self.y[self.y.index(y) + 1:]
                else:
                    self.x = self.x[self.x.index(x) + 1:]
                    self.y = self.y[self.y.index(y) + 1:]

                list_pos = list(zip(self.x, self.y))

                self.x, self.y = self.x_y, self.x_y

            for p in list_pos:
                is_empty = True
                for a in self.pos:
                    if a == p:
                        is_empty = False
                        possible_opponent_pos.append(a)
                        break
                    else:
                        pass
                if is_empty:
                    possible_move.append((p))
                else:
                    break

            #  script finale
            for a in possible_opponent_pos:
                if self.found_grid_pos()[0] in range(a[0] - 30, a[0] + 30) and self.found_grid_pos()[1] in range(
                        a[1] - 30, a[1] + 30):
                    for b in self.dict_element_and_pos.keys():
                        if self.dict_element_and_pos[b] == a:
                            is_opponent_name = b
                    is_opponent = True
                    go = True
                else:
                    continue

            if not is_opponent:
                for a in possible_move:
                    if self.found_grid_pos() == a:
                        go = True
                        is_opponent = False
                    else:
                        continue

            if self.element[0] == 'b' and self.counter % 2 == 0:
                pass
            elif self.element[0] == 'w' and self.counter % 2 != 0:
                pass
            else:
                go = False

            if go and is_opponent:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
                self.pos[self.in_order.index(is_opponent_name)] = (1000, 2000)
            elif go:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
            else:
                pass

            return go
        elif self.element[1:].startswith('king'):
            possible_move = []
            possible_opponent_pos = []
            is_opponent = False
            is_opponent_name = None
            go = False

            x = self.pos[self.in_order.index(self.element)][0]
            y = self.pos[self.in_order.index(self.element)][1]

            if self.found_grid_pos()[0] == x:
                if self.found_grid_pos()[1] < y:
                    possible_move.append((x, y-63))
                else:
                    possible_move.append((x, y+63))
            elif self.found_grid_pos()[1] == y:
                if self.found_grid_pos()[0] < x:
                    possible_move.append((x-63, y))
                else:
                    possible_move.append((x+63, y))
            elif self.found_grid_pos()[0] > x:
                if self.found_grid_pos()[1] > y:
                    possible_move.append((x+63, y+64))
                else:
                    possible_move.append((x+63, y-63))
            elif self.found_grid_pos()[0] < x:
                if self.found_grid_pos()[1] > y:
                    possible_move.append((x-63, y+64))
                else:
                    possible_move.append((x-63, y-63))
            else:
                pass

            for a in self.pos:
                if possible_move[0] == a:
                    possible_opponent_pos.append(a)

            #  script finale
            for a in possible_opponent_pos:
                if self.found_grid_pos()[0] in range(a[0] - 30, a[0] + 30) and self.found_grid_pos()[1] in range(
                        a[1] - 30, a[1] + 30):
                    for b in self.dict_element_and_pos.keys():
                        if self.dict_element_and_pos[b] == a:
                            is_opponent_name = b
                    is_opponent = True
                    go = True
                else:
                    continue

            if not is_opponent:
                for a in possible_move:
                    if self.found_grid_pos() == a:
                        go = True
                        is_opponent = False
                    else:
                        continue

            if self.element[0] == 'b' and self.counter % 2 == 0:
                pass
            elif self.element[0] == 'w' and self.counter % 2 != 0:
                pass
            else:
                go = False

            if go and is_opponent:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
                self.pos[self.in_order.index(is_opponent_name)] = (1000, 2000)
            elif go:
                self.pos[self.in_order.index(self.element)] = self.found_grid_pos()
            else:
                pass

            return go
        else:
            pass

    def found_grid_pos(self):
        next_pos = None
        for i in self.grid_pos:
            if self.to_move[0] in range(i[0]-30, i[0]+30) and self.to_move[1] in range(i[1]-30, i[1]+30):
                next_pos = i
            else:
                continue
        return next_pos

    def return_next_pos(self):
        self.create_requirements()
        next_pos = self.found_grid_pos()

        if self.check_if_valid():
            return next_pos, self.pos
        else:
            return self.dict_element_and_pos[self.element], self.pos

