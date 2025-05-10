from function import *


window = pygame.display.set_mode(size_window)
pygame.display.set_caption("Loboria")

clock = pygame.time.Clock()


hero = Hero(
    10,
    10,
    size_hero[0],
    size_hero[1],
    hero_image_list,
    1,
    2
)

bot1 = Bot(
    100,
    335,
    size_hero[0],
    size_hero[1],
    bot1_image_list,
    1,
    "vertical",
    radius = 105,
)



bot4 = Bot(
    100,
    10,
    size_hero[0],
    size_hero[1],
    bot3_image_list,
    2,
    "vertical",
    radius = 120,
)
bullet4= Bullet(bot4.x+17,
                 bot4.y,
                 20, 20,
                 WHITE,
                 bot4.orientation,
                 1)







heart_list.append(Heart(290,255,50, 50, heart_image_list))
heart_list.append(Heart(390,80,50, 50, heart_image_list))
well_list.append(Well(700,10,50, 50, well_image_list))

font = pygame.font.Font(None, 40)
what_window = "menu"
rect_start = pygame.Rect(size_window[0]//2-125,200,250,80)
rect_end = pygame.Rect(size_window[0]//2-125,350,250,80)
rect_levels = pygame.Rect(size_window[0]//2-125,50,250,80)
text_start = font.render("START", True, BLACK)
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
        pygame.draw.rect(window,WHITE, rect_start)
        pygame.draw.rect(window,WHITE,rect_end)
        pygame.draw.rect(window,WHITE,rect_levels)
        window.blit(text_start, (rect_start.centerx - font.size("START")[0] // 2,rect_start.centery - font.size("START")[1]//2))
        window.blit(text_end, (rect_end.centerx - font.size("END")[0] // 2,rect_end.centery - font.size("END")[1]//2))
        window.blit(text_levels, (rect_levels.centerx - font.size("LEVELS")[0] // 2,rect_levels.centery - font.size("LEVELS")[1]//2))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                if rect_start.collidepoint(x,y):
                    what_window = "game"
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
        window.fill(BLACK)
        window.blit(heart_image_list, (3,3))
        render_hp = font.render(f"x{hero.hp}", True, BLACK)
        window.blit(render_hp, (22,3))
#    x,y = 0,0
#    for i in range(100):
#        pygame.draw.line(window, WHITE, (0, y), (size_window[0],y))
#        pygame.draw.line(window, WHITE, (x, 0), (x, size_window[1]))
#        x += 10
#        y += 10

        hero.move(window)
        bot1.guardian(window)
        bot4.striker(window, bullet4)



        hero.collide_enemy([bot1,bot4,bullet4,])
        hero.collide_heart(heart_list)


        for heart in heart_list:
            heart.blit(window)

        for well in well_list:
            well.blit(window)

        for wall in wall_list:
            pygame.draw.rect(window, wall.color, wall)
            #print(wall.x,wall.y)





        for event in events:
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.walk["up"] = True
                if event.key == pygame.K_a:
                    hero.walk["left"] = True
                if event.key == pygame.K_s:
                    hero.walk["down"] = True
                if event.key == pygame.K_d:
                    hero.walk["right"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.walk["up"] = False
                if event.key == pygame.K_a:
                    hero.walk["left"] = False
                if event.key == pygame.K_s:
                    hero.walk["down"] = False
                if event.key== pygame.K_d:
                    hero.walk["right"] = False


    for event in events:
            if event.type == pygame.QUIT:
                game = False
    clock.tick(FPS)
    pygame.display.flip()
