from data import *





#class Human(pygame.Rect):
#    def __init__(self, x, y, width, height, image):
#        super().__init__(x, y, width, height)
#        self.image_list = image
#        self.image = self.image_list[0]
#        self.cords = 0
#        self.step = 2
#        self.grav_power = 2
#        self.static_gravity = -2
#        self.jump = -1
#        self.jump_power = 12
#        self.can_jump = False
#        self.gravity_speed = 0




class Human(pygame.Rect):
    def __init__(self, x, y, width, height, image_list, step, hp=None): 
        super().__init__(x, y, width, height)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.cords = 0 
        self.step = step 
        self.grav_power = 2 
        self.static_gravity = -2 
        self.jump_power = 12
        self.can_jump = False
        self.gravity_speed = 0 
        self.hp = hp 




    def grav(self,wall_list):
        self.gravity_speed += 1
        self.y += self.gravity_speed

        for wall in wall_list:
            if self.colliderect(wall) and self.gravity_speed >= 0:
                self.y = wall.top - self.height 
                self.gravity_speed = 0
                self.can_jump = True
                break

        for wall in wall_list: 
            if self.colliderect(wall) and self.gravity_speed >= 0:
                self.y = wall.top - self.height
                self.gravity_speed = 0
                self.can_jump = True
                break
            elif self.colliderect(wall) and self.gravity_speed < 0: 
                self.y = wall.bottom
                self.gravity_speed = 0








    def move(self,window):
        self.grav()
        window.blit(self.image,(self.x,self.y))
        event = pygame.key.get_pressed()
        if event[pygame.K_d]:
            height = round(temp_map[0].height *0,2)
            if self.x > 200:
                for i in range(0, len(temp_map)):
                    if self.collidepoint(temp_map[i].x - self.step, temp_map[i].y + height) or self.collidepoint(temp_map[i].x - self.step, temp_map):
                        break
                else:
                    for brick in temp_map:
                        brick.x -= self.step
            else:
                for i in range(0, len(temp_map)):
                    if self.collidepoint(temp_map[i].x - self.step, temp_map[i].y + height) or self.collidepoint(temp_map[i].x - self.step, temp_map):
                        break
                else:
                    self.x += self.step



        if event[pygame.K_d]:
            height = round(temp_map[0].height *0,2)
            if self.x - temp_map[0].x > 200:
                for i in range(0, len(temp_map)):
                    if self.collidepoint(temp_map[i].x + self.step, temp_map[i].y + height) or self.collidepoint(temp_map[i].x - self.step, temp_map):
                        break
                else:
                    for brick in temp_map:
                        brick.x += self.step
            else:
                for i in range(0, len(temp_map)):
                    if self.collidepoint(temp_map[i].x + self.step, temp_map[i].y + height) or self.collidepoint(temp_map[i].x - self.step, temp_map):
                        break
                else:
                    self.x -= self.step






    def jump(self): 
        if self.can_jump:
            self.gravity_speed = -self.jump_power 
            self.can_jump = False

    def collide_enemy(self, list_obj):
        index = self.collidelist(list_obj)
        if index != -1:
            self.x = self.start_x 
            self.y = self.start_y
            if hasattr(self, 'hp'):
                self.hp -= 1


    def collide_heart(self, heart_list):
        index = self.collidelist(heart_list)
        if index != -1:
            heart_list.pop(index)
            if hasattr(self, 'hp'): 
                self.hp += 1


    def move_image(self):
        if len(self.image_list) > 1:
            self.cords = (self.cords + 1) % (len(self.image_list) * 10) 
            self.image = self.image_list[self.cords // 10]
        else:
            self.image = self.image_list[0] 




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







class Hero(Human):
    def __init__(self,x,y,width,height,image_list,step,hp):
        super().__init__(x,y,width,height,image_list,step,hp)
        self.walk = {"up": False, "down": False, "left":False,"right":False}
        self.side = False
        self.start_x = self.x
        self.start_y = self.y
        self.gravity_speed = 0

    def move(self, window):
        if self.walk["left"]:
            self.x -= self.step
            self.side = True
            if self.collidelist(wall_list) != -1:
                self.x += self.step

        if self.walk["right"]:
            self.x += self.step
            self.side = False
            if self.collidelist(wall_list) != -1:
                self.x -= self.step



        moved = any(self.walk.values())
        if moved:
            self.move_image()
        else:
            self.image = self.image_list[0]

        image_to_blit = self.image
        if self.side:
            image_to_blit = pygame.transform.flip(self.image, True, False)

        window.blit(image_to_blit, (self.x, self.y))



                




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
     


    def __init__(self, x, y, width, height, image_list, step, orientation, radius=0):
        super().__init__(x, y, width, height, image_list, step)
        self.orientation = orientation
        self.start_x = x
        self.start_y = y
        self.radius = radius
        # Flip images if orientation indicates facing left initially
        if "left" in self.orientation: # Changed from find("left") != 1
            for i in range(len(self.image_list)):
                self.image_list[i] = pygame.transform.flip(self.image_list[i], True, False)


    def guardian(self, window):
        self.move_image() 
        if self.orientation == "vertical":
            self.y += self.step
            if self.y < self.start_y - self.radius or self.y > self.start_y + self.radius:
                self.step *= -1
        elif self.orientation == "horizontal":
            self.x += self.step
            if self.x < self.start_x - self.radius or self.x > self.start_x + self.radius:
                self.step *= -1
        window.blit(self.image, (self.x, self.y))


    def striker(self, window, bullet):
        self.move_image()
        window.blit(self.image, (self.x, self.y))
        bullet.move(window)


    def collide_hero(self, hero):
        if self.colliderect(hero):
            if hasattr(hero, 'hp'):
                hero.hp -= 1
            hero.x = hero.start_x
            hero.y = hero.start_y

class Bullet(pygame.Rect):
    def __init__(self, x, y, width, height, color, orientation, step, image=None):
        super().__init__(x, y, width, height)
        self.color = color
        self.image = image
        self.orientation = orientation
        self.start_x = x
        self.start_y = y
        self.step = step
        self.active = True

    def move(self, window):
        if not self.active: return 

        if self.orientation.find('vertical') != -1:
            self.y += self.step
            if self.y < 0 or self.y > size_window[1] or self.collidelist(wall_list) != -1:
                self.active = False 
        elif self.orientation.find('horizontal') != -1:
            self.x += self.step
            if self.x < 0 or self.x > size_window[0] or self.collidelist(wall_list) != -1:
                self.active = False 

        if self.image:
            window.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(window, self.color, self)

    def collide_hero(self, hero):
        if self.active and self.colliderect(hero):
            if hasattr(hero, 'hp'): 
                hero.hp -= 1
            self.active = False




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
    buff_list = []

    def __init__(self, x, y, width, height, image, designed, step, working_time):
        super().__init__(x, y, width, height)
        self.image = image
        self.designed = designed
        self.step = step
        self.time_start = 0
        self.working_time = working_time
        self.active = False

    def move(self, window):
        if not self.active:
            self.y += self.step 
            window.blit(self.image, (self.x, self.y))

    def completing(self, hero, bot_list):
        if self.designed == "HP":
            if hasattr(hero, 'hp'):
                hero.hp += 1
        elif self.designed == "move_speed":
            hero.step += 2
            self.time_start = pygame.time.get_ticks()
        # Add other buff effects here (e.g., speed_bullet, speed_shoot, immortal)
        # You'll need to define these attributes in your Hero class first

    def work_time(self, current_time, hero):
        if self.active and current_time - self.time_start > self.working_time:
    
            if self.designed == "move_speed":
                hero.step -= 2
            # Add other buff reversals here
            return True # Indicate that the buff has expired
        return False # Buff is still active or not started

    def collide(self, hero): 
        if self.colliderect(hero) and not self.active:
            self.active = True
            self.completing(hero, [])



class Heart(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image

    def blit(self, window):
        window.blit(self.image, (self.x,self.y))

    def collide_hero(self, hero):
        if self.colliderect(hero):
            if hasattr(hero, 'hp'):
                hero.hp += 1
            return True # 
        return False






#ADD IMAGE!!!
class Wall(pygame.Rect):
    def __init__(self, x, y, width, height, image): 
        super().__init__(x, y, width, height)
        self.image = image 


        

make_map(temp_map["LVL1"]["map"])




        

make_map(temp_map["LVL1"]["map"])
