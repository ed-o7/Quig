#Game about Quig
from allVariables import *#imports all the variables from the other script
#Game
def doAction(num,value,hp):#this is triggered after a dialogue is finished, executed upon escape key entered
    global stage_y#defining a few global variables
    global stage_x
    global endGame
    global cakes#cakes is the counter for how many cakes the player has collected
    global madmoder
    if num == 1:#do nothing
        pass
    elif num == 2:#add to inventory
        inventory.append(str(value))
    elif num == 3:#add health
        quig.health += int(value)
    elif num == 4:#remove health
        quig.health -= int(value)
    elif num == 5:#start a side quest (unused)
        value.started = True
    elif num == 6:#change a characters dialogue options
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
    elif num == 7:#change Quig's locaiton
        stage_y, stage_x = value[0],value[1]
    elif num == 8:#change 2 characters dialogue options
        (allCharacters[value[0][0]]).dia = allDialogues[value[0][1]]
        (allCharacters[value[1][0]]).dia = allDialogues[value[1][1]]
    elif num == 10:#triggers the endgame
        endGame = [True,value]
    elif num == 12:#adds something to quig's inventory and changes the dialogue
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        inventory.append(value[2])
    elif num == 13:#makes Quig mad
        madmoder = True
        s_backyard.doors[1] = [False,False,0]
        stage_y,stage_x = 0,0
    elif num == 14:#release from code
        pygame.quit()
        import quigUnshackled
        s_backyard.doors[1] = [False,False,0]
        stage_y,stage_x = 0,0
    elif num == 15:#pill options
        boda.dia.options.append([True,"Want some pills?"]) #(self,name,intro,options,responses,action,done,finalmove)
        boda.dia.responses.append("Yeah, sure. *takes Grag's pills*")
        boda.dia.action.append([16,0,True])
        inventory.append("Grag's Pills")
    elif num == 16:
        if boda in s_cult.npcs:
            s_cult.npcs.pop(s_cult.npcs.index(boda))
            s_cult.npcs.append(weirdBoda)
        else:
            s_campsite.npcs.pop(s_campsite.npcs.index(boda))
            s_campsite.npcs.append(weirdBoda)
        inventory.pop(inventory.index("Grag's Pills"))
    elif num == 50:#changes dergs dialogue to include ending dialogue
        derg.dia = dergDia2
        cakes += 1
        inventory.append(value[4])
        if value[2] == True:
            inventory.pop(inventory.index(value[3]))
        dergDia2.options.append([True,str("*give "+(inventory[-1])+"*")])#adds cake to options to the brother's dialogue
        dergDia2.responses.append(cakeResponses[(cakeList.index(inventory[-1]))])#adds responses
        dergDia2.action.append([10,(cakeList.index(inventory[-1])),True])
        if cakes == 6:
            dergDia2.options.append([True,str("*give all cakes*")])#adds cake to options to the brother's dialogue
            dergDia2.responses.append("Whoah... thanks man. That's a lotta cakes.")#adds responses
            dergDia2.action.append([10,5,True])
        if value[4] == "Angel Cake":#removes portal in back garden
            s_backyard.doors[1] = [False,False,0]
            s_backyard.objects[s_backyard.objects.index([brokenFence,(0,0)])] = [eastFence,(0,0)]
            
            stage_y,stage_x = 0,0
        if value[4] == "Belphegor Cake":
            s_cult.npcs.pop(0)
    elif num == 66:
        stage_y,stage_x = 4,4
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        s_campsite.npcs.clear()
        s_campsite.objects.pop(4)
        s_cult.npcs.append(boda)
    elif num == 67:#removes trugs quest so game functions thank you very much
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        global trugDia1
        trugDia1.options[0][1] = "Get out of my face."
        trugDia1.responses[0] = "No need to be rudealicious, bro."
        trugDia1.action[0] = [1,0,False]
        return trugDia1
    elif num == 69:
        s_bedroom.objects.append([westDoor,(0,0)])
        s_bedroom.doors[3] = [True,True,273]
        s_qhouse.objects.append([eastDoor,(5,0)])
        s_qhouse.doors[1] = [True,True,273]
    elif num == 75:
        s_mayor.npcs.pop(0)
        s_mayor.npcs.append(deadmayor)
        ghoul.dia = ghoulDia3
    elif num == 90:
        if [eastFence,(0,0)] in s_backyard.objects:
            s_backyard.doors[1] = [True,False,0]
            s_backyard.objects[s_backyard.objects.index([eastFence,(0,0)])] = [brokenFence,(0,0)]#replaces fence with broken fence
    elif num == 91:
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        s_dump.npcs.clear()
    elif num == 93:
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        inventory.pop(inventory.index("Ingredients"))
        inventory.append("Homemade Cake")
        cakes += 1
    elif num == 95:
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        inventory.pop(inventory.index("Love Letter"))
    elif num == 98:#packs up the camp 
        (allCharacters[value[0]]).dia = allDialogues[value[1]]
        s_campsite.npcs.clear()
        s_campsite.objects.pop(4)
    elif num == 99:
        stage_y,stage_x = 1,1
        quig.health -= 10
    else:
        print("huh?")
    if hp <= 10:
        endGame = [True,6]
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
    if stage_y > 8:
        stage_y = 0
    if stage_x > 7:
        stage_x = 0
    if stage_y < 0:
        stage_y = 8
    if stage_x < 0:
        stage_x = 7
    return stage_y,stage_x
#main loop

while active:
    #pygame.time.delay(10)
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
        if (keys[pygame.K_r]==True) and (keys[pygame.K_t]==True) and (keys[pygame.K_b]==True):
            for i in range(len(stages)):
                for j in range(len(stages[i])):
                    for k in range(0,4):
                        (stages[i][j]).doors[k] = [True,False,0]
        if keys[pygame.K_c]==True and keys[pygame.K_k]==True:
            inventory.append("Homemade Cake")
            inventory.append("")
        if (keys[pygame.K_LSHIFT]):
            if keys[pygame.K_RSHIFT]:
                quig.vel = quig.vel*10
            else:
                quig.vel = quig.vel*2
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
        if keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_UP] or keys[pygame.K_RIGHT] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT]:
            if currentTick % 20 == 0:
                count += 1
        else:
            quigPic = quig1
        if (keys[pygame.K_b]==True) and madmoder == True:
            madmoder = False
        if (keys[pygame.K_l]==True):
            cakes = 5
            doAction(50,[11,21,False,"Leaves","Woody Cake"],True)

            
            
        stage_y,stage_x = findBoundaries(quig.x,quig.y,quig.width,quig.height,stage,stage_y,stage_x,155)
        stage = stages[stage_y][stage_x]
    #will owes me £2.50
    if madmoder:
        stage.npcs.clear()
        stage.colour = [((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))),((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))]
        for i in stage.objects:
            i[1] = ((random.randint(-600,600)),(random.randint(-350,350)))
        stage_y , stage_x = random.randint(0,8) , random.randint(0,7)
        quig.health = (random.randint(0,1000000000000000000000000000))
        quig.x,quig.y = (random.randint(0,1200)),(random.randint(0,700))
    
    
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
        pygame.draw.rect(screen, (255,255,255), (scr_width-200, 20, scr_width-1020, scr_height-(670-((len(inventory)+1)*15))))#1200,700 this makes the white outer box, depending on number of lines needed to overlay
        pygame.draw.rect(screen, (0,0,0), (scr_width-195, 25, scr_width-1030, scr_height-(680-(len(inventory)+1)*15)))#this makes the black outer box
        makeText("H "+str(quig.health),(255,255,255),scr_width-190,23,smallfont)#makes the health value in the corner
        iy = 23+15#iy is the variable that is where the text is going to be rendered (the y value)
        makeText("Inventory:",(255,255,255),scr_width-190,iy,smallfont)#makes the text of inventory title
        for i in range(0,len(inventory)):#loop that makes the different things in the inventory display on the screen
            iy += 15#increases the "iy" value so text is not on top itself
            makeText(inventory[i],(255,255,255),scr_width-190,iy,smallfont)
    elif showMap == True:
        screen.blit(mapPic, (0, 0))# displays the map on screen
    elif showInvent == False:#inventory and map cannot be displayed at the same time
        pygame.draw.rect(screen, (255,255,255), (scr_width-200, 20, scr_width-1020, scr_height-670))#1200,700
        pygame.draw.rect(screen, (0,0,0), (scr_width-195, 25, scr_width-1030, scr_height-680))
        makeText("H "+str(quig.health),(255,255,255),scr_width-190,23,smallfont)#mini display of inventory
    pygame.draw.rect(screen, (255,255,255), (20, 20, len(stage.title)*13, 30))#1200,700
    pygame.draw.rect(screen, (0,0,0), (25, 25, len(stage.title)*13-10, 20))
    makeText(str(stage.title),(255,255,255),25,24,smallfont)#makes the title in the top left


    #Dialogue
    for i in range(0,len(stage.npcs)):#detects and runs this code for how many character are on screen
        ch = stage.npcs[i]#sets the current character to whichever is being seen on the list
        if ch.overlap ==  True:#ch is the current character in use
            current_Dia = ch.dia#the current used dialogue is changed to whichever one currently in use by ch
            currentCharacterNumber = i#no clue what this one does ill be honest but im too scared to remove it :)
            currentOptions = ch.dia.options#options is the list of things the player can ask in the format [[True,"Hello"],[True,"Goodbye"]] where the boolean is whether or not it is to be displayed. good for easy changing of which ones shouldn't be displayed multiple times
            currentResponses = ch.dia.responses#ok that was a long comment above so we'll take a breather here.
            currentActions = ch.dia.action#erm this is the things that a specific action does, honestly if youre wondering how this works just ask me IRL cos its a bit too complicated
            #dia is the current dialogue in use
            break#stops "for" loop if someone is overlapping


    if stage.npcs:#checks if there is an NPC in the stage
        if ch.overlap == True:#checks if theyre overlapping
            textbox_y = 625-len(currentOptions)*70#oh god it starts getting complicated here
            textbox_h = 70*len(currentOptions)#i'll be honest I was drunk when I made this but it works and I refuse to change it.
            if len(currentOptions) < 3:#makes the height of the texbox bigger if its a smaller set of options
                textbox_h += 50#ok ill come back to annotating the code later imma do some actual coding now
            inputDia = list(((str(keys)[236:290])).split(" "))
            pygame.draw.rect(screen, (255,255,255), (20, textbox_y, 1160, textbox_h+10))
            pygame.draw.rect(screen, (0,0,0), (25, (textbox_y+5), 1150, textbox_h))
            #nameplate
            pygame.draw.rect(screen, (255,255,255), (25, (textbox_y-15), len(current_Dia.name)*13, 20))
            makeText(current_Dia.name,(0,0,0),30,(textbox_y-18),smallfont)
            
            if current_Dia.done == True:
                line = (currentResponses[choice-1])
                makeText(line,(255,255,255),dx,dy,font)
                dy += textSize+30
                line = ("Press [ESC] to leave")
                makeText(line,(255,255,255),dx,dy,font)
                if keys[pygame.K_ESCAPE]:
                    quig.x,quig.y = current_Dia.finalmove
                    ch.overlap = False
                    quig.overlap = False
                    ch.dia.done = False
                    doAction((currentActions)[choice-1][0],((currentActions)[choice-1][1]),quig.health)
                    if remove == True:      
                        currentOptions.pop(choice-1)
                        currentResponses.pop(choice-1)
                        currentActions.pop(choice-1)
                        

            else:
                textbox_y = 625-len(currentOptions)*70
                textbox_h = 70*len(currentOptions)
                pygame.draw.rect(screen, (0,0,0), (25, (textbox_y+5), 1150, textbox_h))
                dx,dy = 40,(textbox_y+20)
                makeText(current_Dia.intro,(255,255,255),dx,textbox_y+10,font)
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



        dy = textbox_y + 10
    if endGame[0] == True:
        dy = 30
        pygame.draw.rect(screen, (255,255,255), (20, 20, scr_width-40, 610))
        pygame.draw.rect(screen, (0,0,0), (25, 25, scr_width-50, 600))
        for i in range(0,len(endings[endGame[1]])):
            line = endings[endGame[1]][i] # displays text options (IE: 1, 2, 3, 4)
            makeText(line,(255,255,255),30,dy,font)
            dy += textSize-10
            
#ඞ🔪ඞ🔪 - Stewman (find me on instagram @stewseller)

    #Update screen
    pygame.display.update()
pygame.quit()

