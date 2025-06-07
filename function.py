#FUNCTION
from data import *


class Human(pygame.Rect):
    def __init__(self, x, y, width, height, image_list, step, hp=None): 
        super().__init__(x, y, width, height)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.cords = 0 
        self.step = step 
        self.grav_power = 2 
        self.static_gravity = -2 
        self.jump_power = 30
        self.can_jump = False
        self.gravity_speed = 0 
        self.hp = hp 




    def grav(self, wall_list, bot_list): 
        self.gravity_speed += 1
        self.y += self.gravity_speed

        for wall in wall_list:
            if self.colliderect(wall):
                if self.gravity_speed >= 0:
                    self.y = wall.top - self.height
                    self.gravity_speed = 0
                    self.can_jump = True
                elif self.gravity_speed < 0: 
                    self.y = wall.bottom
                    self.gravity_speed = 0
                break 

    
        for bot in bot_list: 
            if self.colliderect(bot):

                if self.gravity_speed >= 0 and self.bottom <= bot.centery + self.height/4: 
                    self.y = bot.top - self.height 
                    self.gravity_speed = -self.jump_power // 2
                    self.can_jump = True 
                    return bot 
                else:

                    pass 

        return None 

    def move(self,window):
        self.grav()
        window.blit(self.image,(self.x,self.y))
        event = pygame.key.get_pressed()
        if event[pygame.K_d]:
            height = round(temp_map[0].height *0,1)
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


    #def immortality(self):
        



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
            elif elem == "2":
                wall_list.append(Wall(x,y,width,height,grass_img))
            elif elem == "3":
                wall_list.append(Wall(x,y,width,height,dirt_img))               
            x += width
        x = 0
        y += height








class Hero(Human):
    def __init__(self,x,y,width,height,image_list,step,hp):
        super().__init__(x,y,width,height,image_list,step,hp)
        self.walk = {"left":False,"right":False}
        self.side = False
        self.start_x = self.x
        self.start_y = self.y
        self.gravity_speed = 0
        self.start_time = 0

    def move(self, window, wall_list, camera_offset_x, camera_offset_y, bot_list):
        # Pass both wall_list and bot_list to the grav method
        stomped_bot = self.grav(wall_list, bot_list)

        moving_horizontally = False
        if self.walk["left"]:
            self.x -= self.step
            self.side = False
            moving_horizontally = True
            if self.collidelist(wall_list) != -1:
                self.x += self.step

        if self.walk["right"]:
            self.x += self.step
            self.side = True
            moving_horizontally = True

            if self.collidelist(wall_list) != -1:
                self.x -= self.step


        screen_center_x = size_window[0] // 2


        if self.x - camera_offset_x > screen_center_x + 100: # Move camera right
            camera_offset_x += (self.x - camera_offset_x) - (screen_center_x + 100)
        elif self.x - camera_offset_x < screen_center_x - 100: # Move camera left
            camera_offset_x += (self.x - camera_offset_x) - (screen_center_x - 100)


        screen_center_y = size_window[1] // 2
        if self.y - camera_offset_y > screen_center_y + 50:
            camera_offset_y += (self.y - camera_offset_y) - (screen_center_y + 50)
        elif self.y - camera_offset_y < screen_center_y - 50:
            camera_offset_y += (self.y - camera_offset_y) - (screen_center_y - 50)


        if moving_horizontally:
            self.move_image()
        else:
            self.image = self.image_list[0]

        image_to_blit = self.image
        if self.side:
            image_to_blit = pygame.transform.flip(self.image, True, False)

        window.blit(image_to_blit, (self.x - camera_offset_x, self.y - camera_offset_y))

        return camera_offset_x, camera_offset_y, stomped_bot 

                

    def collide_enemy(self, bot_list): 
        stomped_bot = None
        for bot in bot_list:
            if self.colliderect(bot):
                if self.gravity_speed >= 0 and self.bottom <= bot.centery + self.height/4:
                    stomped_bot = bot
                    break 
                else:
                    if pygame.time.get_ticks()-self.start_time > 0:
                        self.start_time = pygame.time.get_ticks() + 2000
               
                        self.x = self.start_x
                        self.y = self.start_y
                        if hasattr(self, 'hp'):
                            self.hp -= 1
                        return None 

        return stomped_bot 


class Bot(Human):
    def __init__(self, x, y, width, height, image_list, step, orientation, radius=0):
        super().__init__(x, y, width, height, image_list, step)
        self.orientation = orientation
        self.start_x = x
        self.start_y = y
        self.radius = radius
       
        if "left" in self.orientation: 
            for i in range(len(self.image_list)):
                self.image_list[i] = pygame.transform.flip(self.image_list[i], True, False)





    def guardian(self, window, camera_offset_x, camera_offset_y): 
        self.move_image()
        if self.orientation == "vertical":
            self.y += self.step
            if self.y < self.start_y - self.radius or self.y > self.start_y + self.radius:
                self.step *= -1
        elif self.orientation == "horizontal":
            self.x += self.step
            if self.x < self.start_x - self.radius or self.x > self.start_x + self.radius:
                self.step *= -1
        window.blit(self.image, (self.x - camera_offset_x, self.y - camera_offset_y)) 

    def striker(self, window, bullet, camera_offset_x, camera_offset_y): 
        self.move_image()
        window.blit(self.image, (self.x - camera_offset_x, self.y - camera_offset_y)) 
        bullet.move(window, camera_offset_x, camera_offset_y) 



    def move(self, window, camera_offset_x, camera_offset_y):
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
            window.blit(self.image, (self.x - camera_offset_x, self.y - camera_offset_y)) 
        else:
            pygame.draw.rect(window, self.color, (self.x - camera_offset_x, self.y - camera_offset_y, self.width, self.height)) # Apply offset


    def collide_hero(self, hero):
        pass 

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
    
    def move(self, window, camera_offset_x, camera_offset_y): 
        if self.orientation.find('vertical') != -1:
            self.y += self.step
            if self.y < 0 or self.y > size_window[1] or self.collidelist(wall_list) != -1:

                self.y = self.start_y 
 
        elif self.orientation.find('horizontal') != -1:
            self.x += self.step
            if self.x < 0 or self.x > size_window[0] or self.collidelist(wall_list) != -1:
 
                self.x = self.start_x
        pygame.draw.rect(window, (0, 255, 255), (self.x - camera_offset_x, self.y - camera_offset_y, self.width, self.height), 2) 
        pygame.draw.rect(window,self.color,(self.x - camera_offset_x,self.y - camera_offset_y, self.width, self.height)) 



    def collide_hero(self, hero): 
        if self.active and self.colliderect(hero) and pygame.time.get_ticks() - hero.start_time > 0:
            hero.start_time = pygame.time.get_ticks() + 2000
            if hasattr(hero, 'hp'): 
                hero.hp -= 1
            self.active = False
      

#class Buff(pygame.Rect):
#    buff_list = []
#
#    def __init__(self, x, y, width, height, image, designed, step, working_time):
#        super().__init__(x, y, width, height)
#        self.image = image
#        self.designed = designed
#        self.step = step
#        self.time_start = 0
#        self.working_time = working_time
#        self.active = False
#
#    def move(self, window):
#        if not self.active:
#            self.y += self.step 
#            window.blit(self.image, (self.x, self.y))
#
#    def completing(self, hero, bot_list):
#        if self.designed == "HP":
#            if hasattr(hero, 'hp'):
#                hero.hp += 1
#        elif self.designed == "move_speed":
#            hero.step += 2
#            self.time_start = pygame.time.get_ticks()
#
#
#    def work_time(self, current_time, hero):
#        if self.active and current_time - self.time_start > self.working_time:
#    
#            if self.designed == "move_speed":
#                hero.step -= 2
#          
#            return True 
#        return False 
#
#    def collide(self, hero): 
#        if self.colliderect(hero) and not self.active:
#            self.active = True
#            self.completing(hero, [])



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
            return True
        return False

class Wall(pygame.Rect):
    def __init__(self, x, y, width, height, image): 
        super().__init__(x, y, width, height)
        self.image = image 


        

make_map(temp_map["LVL1"]["map"])


#IDEAS

#Class LuckyBlock
    #Invicibility
    #+ 1 Hp
    #Increased_movespeed
    #Decreased_movespeed
    #Enemy
    #Reverse_walk




#Зробить так щоб коли hero доторкався до  bullet то він не починав з початку, а отримував щит на 2 секунди при отриманні урону

