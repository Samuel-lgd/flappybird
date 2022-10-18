# import pygame
import pygame
import random

from oiseau import *
from sol import *
from decor import *
from tuyau import *
from menu import *
from elements import *
from projectile import *


# Initialisation du game-engine
def start():
    pygame.init()

    pygame.font.init()
    ScoreFont = pygame.font.SysFont(None, 60)
    DelayFont = pygame.font.SysFont("Helvetica", 12)
    txtFont = pygame.font.SysFont(None, 30)

    imageShield = pygame.image.load("img/oiseauShield.png")
    # taille de l'écran
    size = (3 * 288, 512)  # 864
    screen = pygame.display.set_mode(size)

    # boucle tant qu'on a pas fini
    done = False
    pause = False

    # gestion des FPS
    clock = pygame.time.Clock()
    framecount = 0

    oiseau = Oiseau(screen)
    sol = Sol(screen)
    tuyaux = []
    for i in range(5):
        tuyaux.append(Tuyau(screen, 864 + 180 * i))
    decor = Decor(screen)
    star = Star(screen)
    menu = Menu(screen)
    shield = Shield(screen)

    # --- Fontions vitesse du jeu
    def gameSpeed(x):
        for tuyau in tuyaux:
            tuyau.speed = x
        sol.speed = x
        decor.speed = x*0.1
        star.speed = x
        menu.speed = x
        shield.speed = x
    gameSpeed(8)

    def getGameSpeed():
        return tuyaux[1].speed

    # --- Variables du jeu
    i = 1000
    score = 0
    limite = 0
    debut = True

    freneticMode = False
    shieldMode = False
    shieldModeTimer = -1
    invincible = -1

    menuOn = True
    acceleration = 0
    reaceleration = False
    reaceleration20 = 0
    cycle = 0
    multiplier = 1

    multiplierTxt = ""
    delayTxtBar = ""

    reset = False
    projectiles = []
    delay = 0
    coins = []
    coinSpawn = 30
    # -------- Boucle de jeu -----------
    while not done:
        framecount += 1
        # --- Evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    oiseau.jump()
                if event.key == pygame.K_SPACE and pause == True:
                    start()
                if event.key == pygame.K_SPACE and menuOn == True:
                    menuOn = False
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_p:
                    pause = not pause
            if event.type == pygame.MOUSEBUTTONDOWN and menuOn == False and not pause and debut == False:
                if delay <= 0:
                    projectiles.append(Projectile(
                        screen, oiseau, getGameSpeed()))
                    delay = 50
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and menu.xBtn < event.pos[0] < menu.xBtn + menu.largHb and menu.yBtn < event.pos[1] < menu.yBtn + menu.hautHb:
                menuOn = False

        # --- Mise à jour des objets
        hbTuyau = False
        hbSol = False
        hbFrenetic = False
        hbShield = False

        if menuOn:
            menu.update(True)
        else:
            menu.update(False)

        if not pause and not menuOn:
            limite += 1
            i += 1
            delay += -1
            coinSpawn += -1

            oiseau.update()
            sol.update()
            for tuyau in tuyaux:
                tuyau.update()
            decor.update()
            star.update()
            shield.update()
            for projectile in projectiles:
                projectile.update()
                if projectile.y > 400:
                    projectiles.remove(projectile)
            for coin in coins:
                coin.update()
                coin.speed = getGameSpeed()
                if coin.x <= -50:
                    coins.remove(coin)

        # --- Verification des collisions
            hbSol = sol.collision(oiseau)
            hbFrenetic = star.collision(oiseau)
            for projectile in projectiles:
                if projectile.collision(shield):
                    hbShield = True
            if freneticMode or shieldMode:
                for tuyau in tuyaux:
                    if tuyau.collision(oiseau):
                        if freneticMode and shieldMode:
                            shieldMode = "end"
                        elif freneticMode:
                            freneticMode = "end"
                        if shieldMode and shieldMode != "end":
                            shieldMode = "end"
                            invincible = 150
            else:
                for tuyau in tuyaux:
                    if tuyau.collision(oiseau):
                        print('T MORT')
                        hbTuyau = True

        # --- Menu pause
        if (hbSol) or (hbTuyau):
            pause = True

        # --- Score
        for tuyau in tuyaux:
            if tuyau.point(oiseau):
                if limite >= 30:
                    limite = 0
                if limite == 0:
                    cycle += 1
                    score += 1
                    if freneticMode:
                        score += 1*multiplier

                    if cycle == 5:
                        cycle = 0
                        if star.cooldown > 0:
                            star.cooldown += -1
                        if shield.cooldown > 0:
                            shield.cooldown += -1
                    limite += 1

        # --- Delay
        delayTxtBar = ""
        for i in range(delay//9):
            delayTxtBar += "■"
        if delay <= 0:
            bracket = ""
        else:
            bracket = "[            ]"

        scoreTxt = ScoreFont.render(
            ("Score: "+str(score)+multiplierTxt), True, (0, 0, 0))
        delayTxtBarRender = DelayFont.render(delayTxtBar, True, (0, 0, 0))
        delayBracket = DelayFont.render(bracket, True, (0, 0, 0))

        # --- Gestion vitesse de départ
        if debut == True:
            if i > 1015:
                gameSpeed(getGameSpeed() - 0.055)
                if i >= 1125:
                    debut = False
                    gameSpeed(2)
                    i = 0
                    reaceleration = True

        if reaceleration:
            if i == 10:
                reaceleration20 += 1
                gameSpeed(getGameSpeed() + acceleration/15)
                i = 0
            if reaceleration20 == 15:
                reaceleration = False
                reaceleration20 = 0
        # --- Accelération progresssive
        # if i > 500 and debut == False:
        #     i = 0
        if not debut and not pause:
            acceleration += 0.001
            gameSpeed(getGameSpeed() + 0.001)

        # --- Pièces
        if coinSpawn <= 0:
            coin = Coin(screen, getGameSpeed())
            collision = False

            for tuyau in tuyaux:
                if tuyau.collision(coin):
                    collision = True

            if shield.collision(coin):
                collision = True

            if collision == False:
                coins.append(coin)
                coinSpawn = (random.randint(50, 150))

        for projectile in projectiles:
            for coin in coins:
                if coin.collision(projectile):
                    print("ddd")
                    score += 1
                    coin.x == 0

        # --- Bouclier
        if tuyaux[1].x == 864 and debut == False and freneticMode == False and shield.cooldown == 0:
            shield.spawn(random.randint(0, 0))
            for tuyau in tuyaux:
                if tuyau.collision(shield):
                    while tuyau.collision(shield):
                        shield.spawn(0)

        if hbShield:
            shieldMode = True
            shieldModeTimer = 500

        if shieldMode:
            shieldModeTimer += -1
            if shieldModeTimer == 0:
                invincible = 100
                shieldMode = "end"
            if shieldMode == "end":
                shieldModeTimer = -1
                invincible += -1
                if invincible == 0:
                    shieldMode = False
                    invincible = -1

        # --- Mode frénétique
        if tuyaux[1].x == 864 and debut == False and freneticMode == False:
            if star.cooldown == 0:
                star.luck(random.randint(0, 0))
            elif star.cooldown != 0:
                star.visible = False

        if freneticMode:
            oiseau.maxSaut = 8
            star.visible = False
            gameSpeed(getGameSpeed() + 0.005)
            if getGameSpeed() < 11.5:
                multiplierTxt = " (x2)"
            if 11.5 <= getGameSpeed() < 13.999:
                multiplier = 3
                multiplierTxt = " (x3 !)"
            if getGameSpeed() >= 14:
                multiplier = 4
                multiplierTxt = " (x4 !!!)"
                gameSpeed(14)

            if freneticMode == "end":
                tuyaux = []
                for i in range(5):
                    tuyaux.append(Tuyau(screen, 864 + 180 * i))
                gameSpeed(8)
                if debut == False:
                    i = 1000
                debut = True
                multiplier = 1
                multiplierTxt = ""
                oiseau.maxSaut = 12
                star.cooldown = 5
                star.visible = True
                freneticMode = False

        if hbFrenetic:
            star.visible = False
            freneticMode = True
            tuyaux = []
            for i in range(4):
                tuyaux.append(Tuyau(screen, 864 + 220 * i))
            for tuyau in tuyaux:
                gameSpeed(8)
                tuyau.randomMin = 100
                tuyau.randomMax = 200
                tuyau.hauteur = 130

        # --- Affichage
        decor.draw()
        star.draw()
        shield.draw()

        for coin in coins:
            coin.draw()

        for tuyau in tuyaux:
            tuyau.draw()

        sol.draw()

        if freneticMode:
            screen.blit(scoreTxt, (random.randint(
                7, 12), random.randint(447, 452)))
        else:
            screen.blit(scoreTxt, (10, 450))

        screen.blit(delayTxtBarRender, (oiseau.x, oiseau.y - 15))
        screen.blit(delayBracket, (oiseau.x - 3, oiseau.y - 15))

        if shieldMode == "end":
            oiseau.blink()
        else:
            oiseau.draw()

        if shieldMode and shieldMode != "end":
            screen.blit(imageShield, (oiseau.x, oiseau.y))

        for projectile in projectiles:
            projectile.draw()

        menu.draw()

        texte = txtFont.render(
            "Shield: [                                          ]", True, (0, 0, 0))
        screen.blit(texte, (400, 430))
        texte = txtFont.render(
            "Game speed: [                                          ]", True, (0, 0, 0))
        screen.blit(texte, (400, 455))
        texte = txtFont.render("TTTTTT", True, (0, 0, 0))
        screen.blit(texte, (400, 480))

        pygame.draw.rect(screen, (0, 0, 0), (484, 433, shieldModeTimer//2, 15))
        pygame.draw.rect(screen, (255, 0, 0),
                         (484, 433, invincible*(250/150), 15))
        if not debut:
            pygame.draw.rect(screen, (0, 0, 0), (542, 458,
                             getGameSpeed()*(250/14), 15))

        # --- Mise à jour à l'écran !
        pygame.display.flip()

        # --- Limiter la boucle à 60 FPS
        clock.tick(60)


start()
# -------- Sortie -----------
pygame.quit()
