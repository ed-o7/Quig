#Game about Quig
from allVariables import *
#Game
def doAction(num,value):
    global stage_y
    global stage_x
    global endGame
    if num == 1:
        pass
    elif num == 2:
        inventory.append(str(value))
    elif num == 3:
        quig.health += int(value)
    elif num == 4:
        quig.health -= int(value)
    elif num == 5:
        value.started = True
    elif num == 6:
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
    elif num == 7:
        stage_y, stage_x = value[0],value[1]
    elif num == 10:
        endGame = [True,value]
    elif num == 11:
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        inventory.append("Belphegor Cake")
        (allCharacters[4]).dia = allDialogues[8]
        stage_y,stage_x = 2,0
    elif num == 66:
        stage_y,stage_x = 4,4
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        s_campsite.npcs.clear()
        s_campsite.objects.pop(4)
        s_cult.npcs.append(boda)
    elif num == 69:
        s_bedroom.objects.append([westDoor,(0,0)])
        s_bedroom.doors[3] = [True,True,273]
        s_qhouse.objects.append([eastDoor,(5,0)])
        s_qhouse.doors[1] = [True,True,273]
    elif num == 74:
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        inventory.append("Goblin Cake")
        (allCharacters[11]).dia = allDialogues[28]
    elif num == 75:
        mayor.pic = deadmayorPic
        mayor.dia = mayorDia5
        ghoul.dia = ghoulDia3
    elif num == 91:
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        s_dump.npcs.clear()
    elif num == 89:
        inventory.append("Storebought Cake")
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
    elif num == 92:
        inventory.append("Money")
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
    elif num == 93:
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        inventory.pop(inventory.index("Ingredients"))
        inventory.append("Homemade Cake")
    elif num == 94:
        inventory.append("Ingredients")
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
    elif num == 95:
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        inventory.pop(inventory.index("Love Letter"))
    elif num == 96:
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        inventory.append("Love Letter")
    elif num == 97:
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        inventory.append("Antique")
    elif num == 98:#packUp
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        s_campsite.npcs.clear()
        s_campsite.objects.pop(4)
    elif num == 99:
        import zeta
    else:
        print("huh?")
def makeText(line,colour,x,y,font):
    img = font.render(line, True, (colour))
    screen.blit(img,(x,y))
    #rect = img.get_rect()

def findOverlap(qw,qh,qx,qy,kx,ky):
    if ((kx) >= (qx-(qw))) and ((kx) <= (qx+(qw))) and ((ky) >= (qy-(qh))) and ((ky) <= (qy+(qh))):
        return True

def findBoundaries(x,y,w,h,stage,stage_y,stage_x,doorwidth):
    #north
    if not (y-(h//2))-100+h > 0:
        if stage.doors[0][0] == True:
            if stage.doors[0][1] == True:
                doorcoord = stage.doors[0][2]
                if ((doorcoord) >= (x-(doorwidth))) and ((doorcoord) <= (x+(doorwidth))):
                    stage_y -= 1
                    quig.y = scr_height-(3*h)
            else:
                stage_y -= 1
                quig.y = scr_height-(3*h)
    #east
    elif not x-(w//2)+100 < scr_width - w:
        if stage.doors[1][0] == True:
            if stage.doors[1][1] == True:
                doorcoord = stage.doors[1][2]
                if ((doorcoord) >= (y-(doorwidth))) and ((y) <= (y+(doorwidth))):
                    stage_x+=1
                    quig.x = 3*w
            else:
                stage_x+=1
                quig.x = 3*w
    #south
    elif not (y-(h//2)+100) < scr_height - h:
        if stage.doors[2][0] == True:
            if stage.doors[2][1] == True:
                doorcoord = stage.doors[2][2]
                if ((doorcoord) >= (x-(doorwidth))) and ((doorcoord) <= (x+(doorwidth))):
                    stage_y +=1
                    quig.y = (3*h)
            else:
                stage_y+=1
                quig.y = (3*h)
    #west
    elif not x-(w//2)-100 > 0:
        if stage.doors[3][0] == True:
            if stage.doors[3][1] == True:
                doorcoord = stage.doors[3][2]
                if ((doorcoord) >= (y-(doorwidth))) and ((y) <= (y+(doorwidth))):
                    stage_x-= 1
                    quig.x = scr_width-(3*w)
            else:
                stage_x-=1
                quig.x = scr_width-(3*w)
    return stage_y,stage_x
#main loop

while active:
    quig.vel = 2
    if count > 1:
        count = 0
    quigPic = imgs[count]
    pygame.time.delay(5)
    currentTick = pygame.time.get_ticks()
    #overlapping
    for i in range(0,len(stage.npcs)):
        ch = stage.npcs[i]
        if findOverlap(quig.width,quig.height,quig.x,quig.y,ch.x,ch.y):
            ch.overlap,quig.overlap = True,True
        


    #Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    keys = pygame.key.get_pressed()
    
    if quig.overlap == False:
        if (keys[pygame.K_g]==True) and (keys[pygame.K_r]==True) and (keys[pygame.K_y]==True):
            quig.health = 1000
            if "Gareth" not in inventory:
                inventory.append("Gareth")
            s_backyard.npcs.append(zorg)
        if (keys[pygame.K_LSHIFT]):
            quig.vel = quig.vel*5
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) == True and quig.x-(quig.width//2) > 0:
            quig.x -= quig.vel
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) == True and quig.x-(quig.width//2) < scr_width - quig.width:
            quig.x += quig.vel
        if (keys[pygame.K_UP] or keys[pygame.K_w]) == True and (quig.y-(quig.height//2))-100+quig.height > 0:
            quig.y -= quig.vel
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) == True and quig.y-(quig.height//2) < scr_height - quig.height:
            quig.y += quig.vel

        
        if keys[pygame.K_e] == True:
            if showInvent == False and (pygame.time.get_ticks()-tickStart)>600:
                showInvent = True
                tickStart = pygame.time.get_ticks()
            elif showInvent == True and (pygame.time.get_ticks()-tickStart)>600:

                showInvent = False
                tickStart = pygame.time.get_ticks()
        if keys[pygame.K_m] == True:
            if showMap == False and (pygame.time.get_ticks()-tickStart)>600:
                showMap = True
                tickStart = pygame.time.get_ticks()
            elif showMap == True and (pygame.time.get_ticks()-tickStart)>600:

                showMap = False
                tickStart = pygame.time.get_ticks()
        if (keys[pygame.K_z]==True):
            if -1< stage_y < 7:
                if -1< stage_x < 7:
                    if (keys[pygame.K_i]) == True:
                        stage_y-=1
                    if (keys[pygame.K_j]) == True:
                        stage_x+=1
                    if(keys[pygame.K_k]) == True:
                        stage_y+=1
                    if (keys[pygame.K_l]) == True:
                        stage_x-=1
        if keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_UP] or keys[pygame.K_RIGHT] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT]:
            if currentTick % 10 == 0:
                count += 1
        else:
            quigPic = quig1

            
            
        stage_y,stage_x = findBoundaries(quig.x,quig.y,quig.width,quig.height,stage,stage_y,stage_x,155)
        stage = stages[stage_y][stage_x]
        

    
    #Rendering
        
    screen.fill((stage.colour[0]))
    pygame.draw.rect(screen, (stage.colour[1]), (0, 0, scr_width, 100))
    #Rendering Quig
    #pygame.draw.rect(screen, (quig.colours), (quig.x-(quig.width//2), quig.y-(quig.height//2), quig.width, quig.height))
    #rendering objects
    for i in range(0,len(stage.objects)):
        screen.blit(stage.objects[i][0],(stage.objects[i][1]))
    #renders all characters
    for i in range(0,len(stage.npcs)):
        ch = stage.npcs[i]
        #pygame.draw.rect(screen, (ch.colours), (ch.x-(ch.width//2), ch.y-(ch.height//2), ch.width, ch.height))
        screen.blit(ch.pic, (ch.x-25, ch.y-25))
    screen.blit(quigPic, (quig.x-(quig.width//2), quig.y-(quig.height//2)))


    #rendering overlay    

    if showInvent == True:
        pygame.draw.rect(screen, (255,255,255), (scr_width-200, 20, scr_width-1020, scr_height-(670-((len(inventory)+1)*15))))#1200,700
        pygame.draw.rect(screen, (0,0,0), (scr_width-195, 25, scr_width-1030, scr_height-(680-(len(inventory)+1)*15)))
        makeText("H "+str(quig.health),(255,255,255),scr_width-190,23,smallfont)
        iy = 23+15
        makeText("Inventory:",(255,255,255),scr_width-190,iy,smallfont)
        for i in range(0,len(inventory)):
            iy += 15
            makeText(inventory[i],(255,255,255),scr_width-190,iy,smallfont)
    elif showMap == True:
        screen.blit(mapPic, (0, 0))
    elif showInvent == False:
        pygame.draw.rect(screen, (255,255,255), (scr_width-200, 20, scr_width-1020, scr_height-670))#1200,700
        pygame.draw.rect(screen, (0,0,0), (scr_width-195, 25, scr_width-1030, scr_height-680))
        makeText("H "+str(quig.health),(255,255,255),scr_width-190,23,smallfont)
    pygame.draw.rect(screen, (255,255,255), (20, 20, len(stage.title)*13, 30))#1200,700
    pygame.draw.rect(screen, (0,0,0), (25, 25, len(stage.title)*13-10, 20))
    makeText(str(stage.title),(255,255,255),25,24,smallfont)

    #Dialogue
    for i in range(0,len(stage.npcs)):
        ch = stage.npcs[i]
        if ch.overlap ==  True:#ch is the current character in use
            current_Dia = ch.dia
            currentCharacterNumber = i
            currentOptions = ch.dia.options
            currentResponses = ch.dia.responses
            currentActions = ch.dia.action
            #dia is the current dialogue in use
            break

     
    if stage.npcs:
        
        if ch.overlap == True:
            if currentOptions:
                inputDia = list(((str(keys)[236:290])).split(" "))
                pygame.draw.rect(screen, (255,255,255), (20, 400, scr_width-40, scr_height-420))
                pygame.draw.rect(screen, (0,0,0), (25, 405, scr_width-50, scr_height-430))
                #nameplate
                pygame.draw.rect(screen, (255,255,255), (25, 385, len(current_Dia.name)*13, 20))
                makeText(current_Dia.name,(0,0,0),30,382,smallfont)
                if current_Dia.done == True:
                    line = (currentResponses[choice-1])
                    makeText(line,(255,255,255),dx,dy,font)
                    dy += textSize+70
                    line = ("Press [ESC] to leave")
                    makeText(line,(255,255,255),dx,dy,font)
                    if keys[pygame.K_ESCAPE]:
                        quig.x,quig.y = current_Dia.finalmove
                        ch.overlap = False
                        quig.overlap = False
                        ch.dia.done = False
                        doAction((currentActions)[choice-1][0],((currentActions)[choice-1][1]))
                        if remove == True:      
                            currentOptions.pop(choice-1)
                            currentResponses.pop(choice-1)
                            currentActions.pop(choice-1)
                            

                else:
                    pygame.draw.rect(screen, (0,0,0), (25, 405, scr_width-50, scr_height-430))
                    dx,dy = 40,420
                    makeText(current_Dia.intro,(255,255,255),dx,dy,font)
                    dy += textSize+5
                    for i in range(0,(len(currentOptions))):
                        if currentOptions[i][0] == True:
                            line = (str(i+1)+":"+currentOptions[i][1]) # displays text options (IE: 1, 2, 3, 4)
                            makeText(line,(255,255,255),dx,dy,font)
                            dy += textSize-5
                            
                    if "True," in inputDia:
                        choice = inputDia.index("True,")
                        if choice <= len(currentOptions):
                            if (currentActions)[choice-1][2] == True:
                                #currentOptions[choice-1][0] = False
                                remove = True
                            else:
                                remove = False

                            ch.dia.done = True # dy is the y value for the text



            dy = 420
    if endGame[0] == True:
        dy = 30
        pygame.draw.rect(screen, (255,255,255), (20, 20, scr_width-40, 610))
        pygame.draw.rect(screen, (0,0,0), (25, 25, scr_width-50, 600))
        if "Storebought Cake"  in inventory:
            endGame[1] = 1
            cakes += 1
        if "Homemade Cake" in inventory:
            endGame[1] = 0
            cakes += 1
        if "Belphegor Cake" in inventory:
            endGame[1] = 2
            cakes += 1
        if "Goblin Cake" in inventory:
            endGame[1] = 5
            cakes += 1
        if (("Storebought Cake" and "Homemade Cake") or ("Homemade Cake" and "Belphegor Cake") or ("Belphegor Cake" and "Storebought Cake")) in inventory:
            endGame[1] = 3
        if cakes == 3:
            endGame[1] = 3
        if ("Storebought Cake" in inventory and "Homemade Cake" in inventory and "Belphegor Cake" in inventory and "Goblin Cake" in inventory):
            endGame[1] = 6

        for i in range(0,len(endings[endGame[1]])):
            line = endings[endGame[1]][i] # displays text options (IE: 1, 2, 3, 4)
            makeText(line,(255,255,255),30,dy,font)
            dy += textSize-10
            
#ඞ🔪ඞ🔪 - Stewman (find me on instagram @stewseller)

    #Update screen
    pygame.display.update()
pygame.quit()

