#pre-calculated and outputs a dic like object to future use based on user's input.
def bargraph_calc(cords,size,verticalDisplay,vertical=None,verticalDisplaySize=20,horizontalDisplay=None,horizontal=None,horizontalDisplaySize=20,border=20,horPointy=0,verPointy=0,formatSeconds=False):
    outDic={}
    outDic = {"background":(),"bars":{},"lines":{"vertical":{},"horizontal":{}},"labels":{}}
    
    
    ##first bars data, labels, values, rawvalues....
    for key in range(len(verticalDisplay)):
        outDic["bars"][key] = [verticalDisplay[key],vertical[key]]
        outDic["bars"][key]+=[horizontalDisplay[key], horizontal]
        
    #!!#calc to find lateral space
    if verticalDisplay != None:
        verticalSpace = txtWidth(outDic["bars"][0][0],20)
    else:
        verticalSpace=0
    #!!#helper variables 2 to borders and last about amount of bars
    heigtHelp=size[1]-border*4
    widtHelp=size[0]-border*2-verticalSpace
    bAm=len(verticalDisplay) #bars Amount
    
    ## back to bars (x,y),(width,height)
    vertList=[outDic["bars"][key][1] for key in outDic["bars"].keys()] #inside helper variable
    for key in range(bAm):
        tispieceheight= round(int(outDic["bars"][key][1])/ int(max(vertList)) * (int(size[1])-border*4),1)
        outDic["bars"][key]+=[
            (cords[0]+border+round((key+1)/(bAm+1)*widtHelp-border/2,1)+verticalSpace,cords[1]+size[1]-border*2-tispieceheight),#(x,y)
            (border, (cords[1]+size[1]-border*2)-round(cords[1]+size[1]-border*2-tispieceheight-0.3)) #(w,h)
            ]
    ##background coords
    outDic["background"]=(cords,size)
    ##lines position
    #aproveita verticalspace pro dictionario
    outDic["txtSpace"]=verticalSpace
    #horizonral
    for i in range(10):
        #lines (x,y)(x,y)
        outDic["lines"]["horizontal"][i] = (cords[0]+border-horPointy+verticalSpace,cords[1]+size[1]-border*2-round(i/9*heigtHelp,1)) , (cords[0]+size[0]-border,cords[1]+size[1]-border*2-round(i/9*heigtHelp,1))
    #vertical
    for i in range(bAm+2):
        #lines (x,y)(x,y)
        outDic["lines"]["vertical"][i] = (cords[0]+border+round(i/(bAm+1)*widtHelp,1)+verticalSpace,cords[1]+border*2) , (cords[0]+border+round(i/(bAm+1)*widtHelp,1)+verticalSpace,cords[1]+size[1]-border*2+verPointy)
    #labels size
    outDic["txtSize"]=verticalDisplaySize
    #get values for vertical lines label
    valMax=0
    for i in range(len(outDic["bars"])):
        if int(outDic["bars"][i][1]) > valMax:
            valMax=int(outDic["bars"][i][1])
    for i in range(9):
        outDic["labels"][i]=round(valMax/(i+1))
    if formatSeconds==True:
        for i in range(9):
            outDic["labels"][i] = secToFormat(outDic["labels"][i])
    return outDic




#draws the bargraph out of a dic
def bargraph_draw(screen,dic,outline=5,style=0):
    #background and outline
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
            simpleText(20,dic["labels"][i],"black",(dic["lines"]["horizontal"][i][0][0]-dic["txtSpace"],dic["lines"]["horizontal"][len(dic["labels"])-i][0][1]))
    #vertical label values.
    if style==0:
        for i in dic["bars"]:
            simpleText(20,dic["bars"][i][2],"black",(dic["lines"]["vertical"][i+1][0][0]-dic["txtSpace"]/2,dic["lines"]["vertical"][len(dic["bars"])-i-1][1][1]))
    #bars
    for i in dic["bars"]:
        pygame.draw.rect(screen,"blue",(dic["bars"][i][4][0],dic["bars"][i][4][1],dic["bars"][i][5][0],dic["bars"][i][5][1]))



#updates x,y axis given an amount in pixels
def bargraph_move(dic,y=0,x=0):
    if x != 0 or y!=0:
        dic["background"] = (dic["background"][0][0]+x,dic["background"][0][1]+y),(dic["background"][1][0],dic["background"][1][1])
        for i in dic["bars"]:
            dic["bars"][i][4] = (dic["bars"][i][4][0]+x,dic["bars"][i][4][1]+y)
        for axis in dic["lines"]:
            for i in dic["lines"][axis]:
                dic["lines"][axis][i] = (dic["lines"][axis][i][0][0]+x,dic["lines"][axis][i][0][1]+y),(dic["lines"][axis][i][1][0]+x,dic["lines"][axis][i][1][1]+y)
    return dic