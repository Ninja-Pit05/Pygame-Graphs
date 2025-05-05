def txtWidth(txt,size):
    '''
    Intern pygameGraph function, outputs string width for internal calculations.
    '''
    from pygame import font
    font.init()
    texto=font.SysFont("Arial",size)
    text=texto.render(str(txt),False,"black")
    return(text.get_width())

def simpleText(screen,font,txt,color,coords):
    '''
    Intern pygameGraph function, renders strings into the screen.
    '''
    text = font.render(str(txt),False,(color))
    screen.blit(text,coords)

class Bargraph:
    """Deals with Bar Graphs"""
    
    
    
    def __init__(self):
            pass
            
    
    
    #Calculaton
    def calc(cords,size,verticalValue,verticalOverlayFunction=None,horizontalDisplay=None,fontSize=20,border=20,horPointy=10,verPointy=10,formatSeconds=False,amountHorLines=9):
        '''
        Pre-calculates and outputs all data in form of a dictionary to a given object for future use.
        '''
        outDic = {}
        outDic = {"type":("bars"),"background":(),"bars":{},"lines":{"vertical":{},"horizontal":{}},"labels":{}}
        
        
        ##first bars data, labels, values, rawvalues....
        for key in range(len(verticalValue)):
            if verticalOverlayFunction != None:
                outDic["bars"][key] = [verticalValue[key],verticalOverlayFunction(verticalValue[key])]
            else:
                outDic["bars"][key] = [verticalValue[key],None]
            if horizontalDisplay==None:
                outDic["bars"][key]+=[None]
            else:
                outDic["bars"][key]+=[horizontalDisplay[key]]
            
        #!!#calc to find lateral space
        if verticalOverlayFunction != None:
            try:
                verticalSpace = txtWidth(outDic["bars"][0][1](outDic["bars"][0][0]), fontSize)
            except:
                verticalSpace = txtWidth(outDic["bars"][0][1](outDic["bars"][0][0]), fontSize[0])
        else:
            try:
                verticalSpace = txtWidth(str(outDic["bars"][0][0])+".0", fontSize)
            except:
                verticalSpace = txtWidth(str(outDic["bars"][0][0])+".0", fontSize[0])
        
        #!!#calc to find upper space.
        if horizontalDisplay != None:
            try:
                horizontalSpace = fontSize[1]/2
            except:
                horizontalSpace = fontSize/2
        else:
            horizontalSpace = 0
        #!!#helper variables 2 to borders and last about amount of bars
        heigtHelp=size[1]-border*4-horizontalSpace
        widtHelp=size[0]-border*2-verticalSpace
        bAm=len(verticalValue) #bars Amount
        
        ## back to bars (x,y),(width,height)
        vertList=[outDic["bars"][key][0] for key in outDic["bars"].keys()] #inside helper variable
        for key in range(bAm):
            tispieceheight= round(int(outDic["bars"][key][0])/ int(max(vertList)) * (int(size[1])-border*4-horizontalSpace),1)
            outDic["bars"][key]+=[
                (cords[0]+border+round((key+1)/(bAm+1)*widtHelp-border/2,1)+verticalSpace,cords[1]+size[1]-border*2-tispieceheight-horizontalSpace),#(x,y)
                (border, (cords[1]+size[1]-border*2)-round(cords[1]+size[1]-border*2-tispieceheight-0.3)) #(w,h)
                ]
        ##background coords
        outDic["background"]=(cords,size)
        ##lines position
        #aproveita verticalspace pro dictionario
        outDic["txtSpace"]=verticalSpace
        #horizonral
        for i in range(amountHorLines+1):
            #lines (x,y)(x,y)
            outDic["lines"]["horizontal"][i] = (cords[0]+border-horPointy+verticalSpace,cords[1]+size[1]-border*2-horizontalSpace-round(i/amountHorLines*heigtHelp,1)) , (cords[0]+size[0]-border,cords[1]+size[1]-border*2-horizontalSpace-round(i/amountHorLines*heigtHelp,1))
        #vertical
        for i in range(bAm+2):
            #lines (x,y)(x,y)
            outDic["lines"]["vertical"][i] = (cords[0]+border+round(i/(bAm+1)*widtHelp,1)+verticalSpace,cords[1]+border*2) , (cords[0]+border+round(i/(bAm+1)*widtHelp,1)+verticalSpace,cords[1]+size[1]-border*2-horizontalSpace+verPointy)
        #labels size
        outDic["txtSize"]=fontSize
        #get values for vertical lines label
        valMax=0
        for i in range(len(outDic["bars"])):
            if int(outDic["bars"][i][0]) > valMax:
                valMax=int(outDic["bars"][i][0])
        for i in range(amountHorLines):
            outDic["labels"][i]=str(round(valMax-(i)/amountHorLines*valMax,1))
        if formatSeconds==True:
            for i in range(amountHorLines):
                outDic["labels"][i] = secToFormat(outDic["labels"][i])
        #font object
        from pygame import font
        font.init()
        try:
            outDic["font"]= font.SysFont("Arial",fontSize)
        except:
            outDic["font"]=(font.SysFont("Arial",fontSize[0]),font.SysFont("Arial",fontSize[1]))
        return outDic
        #end
    
    
    
    #drawing
    def draw(screen,dic,outline=5,style=0):
        '''
        Draws the given dictionary object to a given pygame display.
        '''
        #background and outline
        import pygame
        if outline != None:
            pygame.draw.rect(screen,"gray",(dic["background"][0][0]-outline,dic["background"][0][1]-outline,dic["background"][1][0]+outline*2,dic["background"][1][1]+outline*2))
            pygame.draw.rect(screen,"white",(dic["background"]))
        #lines
        for i in dic["lines"]["horizontal"]:
            pygame.draw.line(screen,"black",dic["lines"]["horizontal"][i][0],dic["lines"]["horizontal"][i][1], 2 if i == 0 else 1)
        for i in dic["lines"]["vertical"]:
            pygame.draw.line(screen,"black",dic["lines"]["vertical"][i][0],dic["lines"]["vertical"][i][1], 2 if i == 0 else 1)
        #horizontal label values.
        if style==0:
            for i in dic["labels"]:
                if dic["labels"][i] != None:
                    try:
                        simpleText(screen,dic["font"],dic["labels"][i],"black",(dic["lines"]["horizontal"][i][0][0]-dic["txtSpace"],dic["lines"]["horizontal"][len(dic["labels"])-i][0][1]))
                    except:
                        simpleText(screen,dic["font"][0],dic["labels"][i],"black",(dic["lines"]["horizontal"][i][0][0]-dic["txtSpace"],dic["lines"]["horizontal"][len(dic["labels"])-i][0][1]))
        #vertical label values.
        if style==0:
            for i in dic["bars"]:
                if dic["bars"][i][2] != None:
                    try:
                        simpleText(screen,dic["font"],dic["bars"][i][2],"black",(dic["lines"]["vertical"][i+1][0][0]-dic["txtSpace"]/2,dic["lines"]["vertical"][len(dic["bars"])-i-1][1][1]))
                    except:
                        simpleText(screen,dic["font"][1],dic["bars"][i][2],"black",(dic["lines"]["vertical"][i+1][0][0]-dic["txtSpace"]/2,dic["lines"]["vertical"][len(dic["bars"])-i-1][1][1]))
        #bars
        for i in dic["bars"]:
            pygame.draw.rect(screen,"blue",(dic["bars"][i][3][0],dic["bars"][i][3][1],dic["bars"][i][4][0],dic["bars"][i][4][1]))
        
    
    
    #updates x,y axis give an amount in pixels
    def move(dic,y=0,x=0):
        '''
        Changes the coordinates of a pygameGraph dictionary. Moving the coordinates a given amount of pixels in both axis.
        '''
        if x != 0 or y!=0:
            dic["background"] = (dic["background"][0][0]+x,dic["background"][0][1]+y),(dic["background"][1][0],dic["background"][1][1])
            for i in dic["bars"]:
                dic["bars"][i][3] = (dic["bars"][i][3][0]+x,dic["bars"][i][3][1]+y)
            for axis in dic["lines"]:
                for i in dic["lines"][axis]:
                    dic["lines"][axis][i] = (dic["lines"][axis][i][0][0]+x,dic["lines"][axis][i][0][1]+y),(dic["lines"][axis][i][1][0]+x,dic["lines"][axis][i][1][1]+y)
        return dic




class Linegraph:
    '''
    Deals with line graphs
    '''
    
    def __init__(self):
        pass
    
    
    #Calculaton
    def calc(cords,size,verticalValue,verticalOverlayFunction=None,horizontalDisplay=None,fontSize=20,border=20,horPointy=10,verPointy=10,formatSeconds=False,amountHorLines=9):
        '''
        Pre-calculates and outputs all data in form of a dictionary to a given object for future use.
        '''
        outDic = {}
        outDic = {"type":("lines"),"background":(),"values":{},"lines":{"vertical":{},"horizontal":{}},"labels":{}}
        
        
        ##first bars data, labels, values, rawvalues....
        for key in range(len(verticalValue)):
            if verticalOverlayFunction != None:
                outDic["values"][key] = [verticalValue[key],verticalOverlayFunction(verticalValue[key])]
            else:
                outDic["values"][key] = [verticalValue[key],None]
            if horizontalDisplay==None:
                outDic["values"][key]+=[None]
            else:
                outDic["values"][key]+=[horizontalDisplay[key]]
            
        #!!#calc to find lateral space
        if verticalOverlayFunction != None:
            try:
                verticalSpace = txtWidth(outDic["values"][0][1](outDic["values"][0][0]), fontSize)
            except:
                verticalSpace = txtWidth(outDic["values"][0][1](outDic["values"][0][0]), fontSize[0])
        else:
            try:
                verticalSpace = txtWidth(str(outDic["values"][0][0])+".0", fontSize)
            except:
                verticalSpace = txtWidth(str(outDic["values"][0][0])+".0", fontSize[0])
        
        #!!#calc to find upper space.
        if horizontalDisplay != None:
            try:
                horizontalSpace = fontSize[1]/2
            except:
                horizontalSpace = fontSize/2
        else:
            horizontalSpace = 0
        #!!#helper variables 2 to borders and last about amount of bars
        heigtHelp=size[1]-border*4-horizontalSpace
        widtHelp=size[0]-border*2-verticalSpace
        bAm=len(verticalValue) #bars Amount
        
        ## back to bars (x,y),(width,height)
        vertList=[outDic["values"][key][0] for key in outDic["values"].keys()] #inside helper variable
        for key in range(bAm):
            tispieceheight= round(int(outDic["values"][key][0])/ int(max(vertList)) * (int(size[1])-border*4-horizontalSpace),1)
            outDic["values"][key]+=[
                (cords[0]+border+verticalSpace+round((key)/(bAm-1)*widtHelp,1),cords[1]+size[1]-border*2-tispieceheight-horizontalSpace),#(x,y)
                ]
            print(key,bAm)
        ##background coords
        outDic["background"]=(cords,size)
        ##lines position
        #aproveita verticalspace pro dictionario
        outDic["txtSpace"]=verticalSpace
        #horizonral
        for i in range(amountHorLines+1):
            #lines (x,y)(x,y)
            outDic["lines"]["horizontal"][i] = (cords[0]+border-horPointy+verticalSpace,cords[1]+size[1]-border*2-horizontalSpace-round(i/amountHorLines*heigtHelp,1)) , (cords[0]+size[0]-border,cords[1]+size[1]-border*2-horizontalSpace-round(i/amountHorLines*heigtHelp,1))
        #vertical
        for i in range(bAm):
            #lines (x,y)(x,y)
            outDic["lines"]["vertical"][i] = (cords[0]+border+round(i/(bAm-1)*widtHelp,1)+verticalSpace,cords[1]+border*2) , (cords[0]+border+round(i/(bAm-1)*widtHelp,1)+verticalSpace,cords[1]+size[1]-border*2-horizontalSpace+verPointy)
        #labels size
        outDic["txtSize"]=fontSize
        #get values for vertical lines label
        valMax=0
        for i in range(len(outDic["values"])):
            if int(outDic["values"][i][0]) > valMax:
                valMax=int(outDic["values"][i][0])
        for i in range(amountHorLines):
            outDic["labels"][i]=str(round(valMax-(i)/amountHorLines*valMax,1))
        if formatSeconds==True:
            for i in range(amountHorLines):
                outDic["labels"][i] = secToFormat(outDic["labels"][i])
        #font object
        from pygame import font
        font.init()
        try:
            outDic["font"]= font.SysFont("Arial",fontSize)
        except:
            outDic["font"]=(font.SysFont("Arial",fontSize[0]),font.SysFont("Arial",fontSize[1]))
        return outDic
        #end
    
    
    
    def draw(screen,dic,outline=5,style=0):
        '''
        Draws the given dictionary object to a given pygame display.
        '''
        
        if dic["type"] != "lines":
            raise Exception(" Incompatible graph type. {} instead of lines".format(dic["type"]))
        
        #background and outline
        import pygame
        if outline != None:
            pygame.draw.rect(screen,"gray",(dic["background"][0][0]-outline,dic["background"][0][1]-outline,dic["background"][1][0]+outline*2,dic["background"][1][1]+outline*2))
            pygame.draw.rect(screen,"white",(dic["background"]))
        #lines
        for i in dic["lines"]["horizontal"]:
            pygame.draw.line(screen,"black",dic["lines"]["horizontal"][i][0],dic["lines"]["horizontal"][i][1], 2 if i == 0 else 1)
        for i in dic["lines"]["vertical"]:
            pygame.draw.line(screen,"black",dic["lines"]["vertical"][i][0],dic["lines"]["vertical"][i][1], 2 if i == 0 else 1)
        #horizontal label values.
        if style==0:
            for i in dic["labels"]:
                if dic["labels"][i] != None:
                    try:
                        simpleText(screen,dic["font"],dic["labels"][i],"black",(dic["lines"]["horizontal"][i][0][0]-dic["txtSpace"],dic["lines"]["horizontal"][len(dic["labels"])-i][0][1]))
                    except:
                        simpleText(screen,dic["font"][0],dic["labels"][i],"black",(dic["lines"]["horizontal"][i][0][0]-dic["txtSpace"],dic["lines"]["horizontal"][len(dic["labels"])-i][0][1]))
        #vertical label values.
        if style==0:
            for i in dic["values"]:
                if dic["values"][i][2] != None:
                    try:
                        simpleText(screen,dic["font"],dic["values"][i][2],"black",(dic["lines"]["vertical"][i][0][0]-dic["txtSpace"]/2,dic["lines"]["vertical"][len(dic["values"])-i-1][1][1]))
                    except:
                        simpleText(screen,dic["font"][1],dic["values"][i][2],"black",(dic["lines"]["vertical"][i][0][0]-dic["txtSpace"]/2,dic["lines"]["vertical"][len(dic["values"])-i-1][1][1]))
        #bars
        for i in dic["values"]:
            try: pygame.draw.line(screen,"blue",dic["values"][i][3],dic["values"][i-1][3], 4)
            except: pass