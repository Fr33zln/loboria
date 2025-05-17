from data import *





class Human(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image_list = image
        self.image = self.image_list[0]
        self.cords = 0
        self.step = 2
        self.grav_power = 2
        self.static_gravity = -2
        self.jump = -1
        self.jump_power = 12
        self.can_jump = False



    def grav(self):
        if self.collidepoint(temp_map) == -1:
            self.y =+ self.grav_power
            self.grav_power -= 0.01
        else:
            self.grav_power = self.static_gravity
            self.can_jump = True






    def move(self,window):
        self.grav()
        window.blit(self.image,(self.x,self.y))
        event = pygame.key.get_pressed()
        if event[pygame.K_d]:
            height = round(temp_map[0].height *0,2)
            if self.x > 200:
                for i in range(0, len(temp_map)):
                    if self.collidepoint(temp_map[i].x - self.step, temp_map[i].y + height) or self.collidepoint(temp_map[i].x - self.step, temp_map)
                        break
                else:
                    for brick in temp_map:
                        brick.x -= self.step
            else:
                for i in range(0, len(temp_map)):
                    if self.collidepoint(temp_map[i].x - self.step, temp_map[i].y + height) or self.collidepoint(temp_map[i].x - self.step, temp_map)
                        break
                else:
                    self.x += self.step



        if event[pygame.K_d]:
            height = round(temp_map[0].height *0,2)
            if self.x - temp_map[0].x > 200:
                for i in range(0, len(temp_map)):
                    if self.collidepoint(temp_map[i].x + self.step, temp_map[i].y + height) or self.collidepoint(temp_map[i].x - self.step, temp_map)
                        break
                else:
                    for brick in temp_map:
                        brick.x += self.step
            else:
                for i in range(0, len(temp_map)):
                    if self.collidepoint(temp_map[i].x + self.step, temp_map[i].y + height) or self.collidepoint(temp_map[i].x - self.step, temp_map)
                        break
                else:
                    self.x -= self.step










    def move(self,window):
        self.grav()
        window.blit(self.image,(self.x,self.y))
        event = pygame.key.get_pressed()
        if event[pygame.K_d]:
            if self.x - temp_map[0].x > 200:
                for brick in temp_map:
                    brick.x -= self.step
            else:
                self.x += self.step
        if event[pygame.K_a]:
            if self.x - temp_map[0].x > 200:
                for brick in temp_map:
                    brick.x += self.step
            else:
                self.x -= self.step

    def jump(self):
        if self.jump != 1:
            self.y -= self.jump
            self.jump -= 1

    def collide_enemy(self, list_obj):
        if self.collidelist(list_obj) != -1:
            self.x = self.start_x
            self.y = self.start_y
            self.hp -= 1


    def collide_heart(self, heart_list):
        index = self.collidelist(heart_list)
        if index != -1:
            heart_list.pop(index)
            self.hp += 1
            

class Maps(pygame.Rect):
    def __init__(self,x,y,width,height,image):
        super().__init__(x,y,width,height)
        self.image = image

def make_map(new_map):
    x,y = 0,0
    width, height = brick_size
    for line in new_map:
        for elem in line:
            if elem == "1":
                wall_list.append(Wall(x,y,width,height,brick_img))
            x += width
        x = 0
        y += height





    def move_image(self):
        if self.image_count == len(self.image_list * 10) - 1:
            self.image_count =0
        if self.image_count %10 == 0:
            self.image = self.image_list[self.image_count // 50]
        self.image_count += 1

class Hero(Human):
    def __init__(self,x,y,width,height,image_list,step,hp):
        super().__init__(x,y,width,height,image_list,step)
        self.walk = {"up": False, "down": False, "left":False,"right":False}
        self.side = False
        self.hp = hp
        self.start_x = self.x
        self.start_y = self.y

    def move(self, window):
        if self.walk["down"] and self.y < size_window[0]:
            self.y += self.step
            if self.collidelist(wall_list) != -1:
                self.y -= self.step
            self.side = False


        if self.walk["up"] and self.y < size_window[0]:
            self.y -= self.step
            if self.collidelist(wall_list) != -1:
                self.y += self.step
            self.side = False


        if self.walk["left"] and self.x > 0:
            self.x -= self.step
            if self.collidelist(wall_list) != -1:
                self.x += self.step
            self.side = True


        if self.walk["right"] and self.x < size_window[0]:
            self.x += self.step
            if self.collidelist(wall_list) != -1:
                self.x -= self.step
            self.side = False

        for value in list(self.walk.values()):
            if value:
                self.move_image()
                break
        else:
            self.image = self.image_list[0]
        if self.side:
            self.image_now = pygame.transform.flip(self.image, True , False)
        else:
            self.image_now = self.image
   
        self.move_image()
        window.blit(self.image_now, (self.x,self.y))
    



    #JUMP









    



    #def change_race(self,hp,image_list):
    #    if self.hp =<3:
    #            self.image = 




class Bot(Human):
    def __init__(self,x,y,width,height,image_list,step,orientation, radius = 0):
        super().__init__(x,y,width,height,image_list,step)
        self.orientation = orientation
        self.start_x = x
        self.start_y = y
        self.radius = radius
        if self.orientation.find("left") != 1:
            index = 0
            while index <len(self.image_list):
                self.image_list[index] = pygame.transform.flip(self.image_list[index],True, False)
                index +=1         
     

    def guardian(self,window):
        if self.orientation == "vertical":
            self.y += self.step
            if self.y  <self.start_y - self.radius or self.y > self.start_y + self.radius:
                self.step *= -1

        elif self.orientation == "horizontal":
            self.x += self.step
            if self.x  <self.start_x - self.radius or self.x > self.start_x + self.radius:
                self.step *= -1
        self.move_image()
        window.blit(self.image,(self.x,self.y))

    



    def striker(self,window,bullet):
        self.move_image()
        window.blit(self.image, (self.x, self.y))
        bullet.move(window)



    def collide_hero(self,hero):
        if self.colliderect(hero):
            hero.hp =- 1
            hero.x = hero.start_x
            hero.y = hero.start_y

class Bullet(pygame.Rect):
    def __init__(self,x,y,width,height,color,orientation,step,image = None):
        super().__init__(x,y,width,height)
        self.color = color
        self.image = image
        self.orientation = orientation
        self.start_x = x
        self.start_y = y
        self.step = step


    def move(self, window):
        if self.orientation.find('vertical') != -1:
            self.y += self.step
            if self.y < 0 or self.y > size_window[1] or self.collidelist(wall_list) != -1:
                self.y = self.start_y
        elif self.orientation.find('horizontal') != -1:
            self.x += self.step
            if self.x < 0 or self.x > size_window[0] or self.collidelist(wall_list) != -1:
                self.x = self.start_x
        pygame.draw.rect(window,self.color,self)


    def collide_hero(self,hero):
        if self.colliderect(hero):
            hero.hp =- 1
            bullet_image_list.remove(self)



class Buff(pygame.Rect):

    buff_list = list()

    def __init__(self,x,y,width,height,image,designed,step,working_time):
        super().__init__(x,y,width,height)
        self.image = image
        self.designed = designed
        self.step = step
        self.time_start = 0
        self.working_time = working_time
        self.active = False

    def move(self,window):
        if not self.active:
            self.y += self.step
            window.blit(self.image, (self.x, self.y))


    def completing(self,hero,bot_list):
        if self.designed == "HP":
            hero.hp += 1
        elif self.designed == "move_speed":
            hero.step += 2
            self.time_start = pygame.time.get_ticks()


    def work_time(self,end_time,hero):
        if end_time - self.time._start > self.working_time:
            if self.designed == "speed_bullet":
                hero.speed_bullet /=2
            elif self.designed == "speed_shoot":
                hero.shoot_limit *=2
            elif self.designed == "immortal":
                hero.immortal = False
            print(self)
            Buff.buff_list.remove(self)




    def collide(self,hero, bot_list):
        if self.colliderect(hero) and not self.active:
            self.active = True
            self.completing(hero, bot_list)















class Heart(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image
        
    def blit(self,window):
        window.blit(self.image, (self.x,self.y))

    def collide_hero(self,hero):
        if self.colliderect(hero):
            hero.hp =+ 1
            heart_list.remove(self)



class Well(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image
        
    def blit(self,window):
        window.blit(self.image, (self.x,self.y))




class Wall(pygame.Rect):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color





        

make_map(temp_map["LVL1"]["map"])
