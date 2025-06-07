from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("Loboria")


camera_offset_x = 0
camera_offset_y = 0


clock = pygame.time.Clock()


hero = Hero(
    x=10,
    y=10,
    width=size_hero[0],
    height=size_hero[1],
    image_list=hero_image_list,
    step=15,
    hp=3
)



bot1 = Bot(
    1300,
    365,
    size_bot[0], 
    size_bot[1],
    bot1_image_list,
    5,
    "horizontal",
    radius=165,
)

bot2 = Bot(
    735,
    365,
    size_bot[0], 
    size_bot[1],
    bot1_image_list,
    5,
    "horizontal",
    radius=215,
)

bot3 = Bot(
    1700,
    365,
    size_bot[0], 
    size_bot[1],
    bot1_image_list,
    -5,
    "horizontal",
    radius=165,
)


bot4 = Bot(
    30, 
    650,
    size_bot[0], 
    size_bot[1],
    bot3_image_list,
    2,
    "horizontal",
    radius=300,
)
bullet4= Bullet(bot4.x+17,
                 bot4.y+17,
                 20, 20,
                 WHITE,
                 bot4.orientation,
                 15)
bot5 = Bot(
    2365, 
    365,
    size_bot[0], 
    size_bot[1],
    bot3_image_list,
    2,
    "vertical",
    radius=150,
)
bullet5= Bullet(bot5.x+17,
                 bot5.y,
                 20, 20,
                 WHITE,
                 bot5.orientation,
                 -15)
bot6 = Bot(
    300, 
    0,
    size_bot[0], 
    size_bot[1],
    bot3_image_list,
    2,
    "horizontal",
    radius=150,
)
bullet6= Bullet(bot6.x+17,
                 bot6.y,
                 20, 20,
                 WHITE,
                 bot6.orientation,
                 15)


active_bots = [bot1,bot2,bot3,bot4,bot5,bot6]


heart_list.append(Heart(390,80,50, 50, heart_image_list))

font = pygame.font.Font(None, 40)
what_window = "menu"
rect_end = pygame.Rect(size_window[0]//2-125,300,250,80)
rect_levels = pygame.Rect(size_window[0]//2-125,200,250,80)
text_end = font.render("END", True, BLACK)
text_levels = font.render("LEVELS", True, BLACK)


#... = pygame.Rect(size_window[0]//2-x,y,width,height)
lvl1 = pygame.Rect(size_window[0]//2-125,35,250,80)
lvl2 = pygame.Rect(size_window[0]//2-125,145,250,80)
lvl3 = pygame.Rect(size_window[0]//2-125,255,250,80)
back = pygame.Rect(size_window[0]//2-125,365,250,80)

text_LVL1 = font.render("LVL1", True, BLACK)
text_LVL2 = font.render("LVL2", True, BLACK)
text_LVL3 = font.render("LVL3", True, BLACK)
text_back = font.render("BACK", True, BLACK)











game = True
while game:
    events = pygame.event.get()
    if what_window == "menu":
        window.fill(BLACK)
        window.blit(logo_img, (250,-50))
        pygame.draw.rect(window,WHITE,rect_end)
        pygame.draw.rect(window,WHITE,rect_levels)
        window.blit(text_end, (rect_end.centerx - font.size("END")[0] // 2,rect_end.centery - font.size("END")[1]//2))
        window.blit(text_levels, (rect_levels.centerx - font.size("LEVELS")[0] // 2,rect_levels.centery - font.size("LEVELS")[1]//2))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos

                if rect_levels.collidepoint(x,y):
                    what_window = "levels"
                elif rect_end.collidepoint(x,y):
                    game = False


    
    elif what_window =="levels":
        window.fill(BLACK)
        pygame.draw.rect(window,WHITE, lvl1)
        pygame.draw.rect(window,WHITE,lvl2)
        pygame.draw.rect(window,WHITE,lvl3)
        pygame.draw.rect(window,WHITE,back)
        window.blit(text_LVL1, (lvl1.centerx - font.size("LVL1")[0] // 2,lvl1.centery - font.size("LVL1")[1]//2))
        window.blit(text_LVL2, (lvl2.centerx - font.size("LVL2")[0] // 2,lvl2.centery - font.size("LVL2")[1]//2))
        window.blit(text_LVL3, (lvl3.centerx - font.size("LVL3")[0] // 2,lvl3.centery - font.size("LVL3")[1]//2))
        window.blit(text_back, (back.centerx - font.size("BACK")[0] // 2,back.centery - font.size("BACK")[1]//2))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                if lvl1.collidepoint(x,y):
                    what_window = "lvl1"
                elif back.collidepoint(x,y):
                    what_window = "menu"


    elif what_window == "lvl1":
        window.fill(CYAN)
        window.blit(heart_image_list, (3,3)) 
        render_hp = font.render(f"x{hero.hp}", True, BLACK)
        window.blit(render_hp, (22,3)) 

        camera_offset_x, camera_offset_y, stomped_bot = hero.move(window, wall_list, camera_offset_x, camera_offset_y, active_bots) 

        if stomped_bot:
            if stomped_bot in active_bots:
                active_bots.remove(stomped_bot) 
                if stomped_bot == bot4: 
                    bullet4.active = False
                if stomped_bot == bot5: 
                    bullet5.active = False 
                if stomped_bot == bot6: 
                    bullet6.active = False 
  
        hero.collide_enemy(active_bots) 
        if camera_offset_y > 600:
            hero.hp -= 1
            hero.x = hero.start_x 
            hero.y = hero.start_y

   
        for bot in active_bots: 
            if bot == bot1: 
                bot.guardian(window, camera_offset_x, camera_offset_y)
            elif bot == bot2: 
                bot.guardian(window, camera_offset_x, camera_offset_y)
            elif bot == bot3: 
                bot.guardian(window, camera_offset_x, camera_offset_y)
            elif bot == bot4:
                bot.striker(window, bullet4, camera_offset_x, camera_offset_y)
            elif bot == bot5:
                bot.striker(window, bullet5, camera_offset_x, camera_offset_y)
            elif bot == bot6:
                bot.striker(window, bullet6, camera_offset_x, camera_offset_y)

        if hero.hp == 0:
            game = False


        if bullet4.active:
            bullet4.collide_hero(hero)
        if bullet5.active:
            bullet5.collide_hero(hero)
        if bullet6.active:
            bullet6.collide_hero(hero)


        for heart in heart_list:
            window.blit(heart.image, (heart.x - camera_offset_x, heart.y - camera_offset_y))
            if heart.collide_hero(hero): 
                heart_list.remove(heart) 
                break 


        for wall_obj in wall_list:
            window.blit(wall_obj.image, (wall_obj.x - camera_offset_x, wall_obj.y - camera_offset_y))

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and hero.can_jump:
                    hero.jump()
                if event.key == pygame.K_d:
                    hero.walk["right"] = True
                if event.key == pygame.K_a:
                    hero.walk["left"] = True
                if event.key == pygame.K_y:
                    hero.hp -= 1
                    hero.x = hero.start_x
                    hero.y= hero.start_y


            if event.type == pygame.KEYUP:

                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_d:
                    hero.walk["right"] = False
                if event.key == pygame.K_a:
                    hero.walk["left"] = False
                

    for event in events:
        if event.type == pygame.QUIT:
            game = False
    clock.tick(FPS)
    pygame.display.flip()

