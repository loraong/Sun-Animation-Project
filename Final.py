# Ma. Lora Drizella M. Ong- Lab #10- Sunrise

import time
CurrentFrame= 0
BaseFolder = ""

def INT(N):
    return int(round(N))
    
def SaveFrame (Canvas):
    global CurrentFrame, BaseFolder
    CurrentFrame = CurrentFrame + 1
    Suffix = str(CurrentFrame) 
    while (len(Suffix) < 5): Suffix = "0" + Suffix
    Filename = BaseFolder + "Image" + Suffix + ".jpg"
    writePictureTo(Canvas, Filename)
    print Filename
    return
    
def Scroller (Canvas,Frames,NewText,BackgroundColor,TextColor):
    Y=getHeight(Canvas)+20 
    Ydiff=(Y+20)/Frames
    while (Y>-20):
        setAllPixelsToAColor(Canvas,BackgroundColor)
        Style=makeStyle(sansSerif, plain, 24)
        addTextWithStyle (Canvas,10, INT(Y), NewText, Style, TextColor)
        repaint (Canvas)
        SaveFrame(Canvas)
        time.sleep(0.02)
        Y=Y-Ydiff
    return
    
def addCircle(Canvas, Xc, Yc, R, NewColor):
    addOval(Canvas, Xc-R, Yc-R, 2*R+1, 2*R+1, NewColor)
    return
    
def addCircleFilled(Canvas, Xc, Yc, R, NewColor):
    addOvalFilled(Canvas, Xc-R, Yc-R, 2*R+1, 2*R+1, NewColor)
    return
    

def Car (Canvas, X, Y, NewColor):

        def Wheel (Canvas, X, Y):
            addCircleFilled(Canvas, X, Y, 18, black)
            addCircleFilled(Canvas, X, Y, 8, white)
            return    

        def Body (Canvas, X, Y, NewColor):
            addRectFilled(Canvas, X, Y, 110, 40, NewColor)
            return
    
        def Window (Canvas, X, Y):
            addRectFilled(Canvas, X, Y, 20, 20, black)
            addRect(Canvas,X, Y, 20, 20, black)
            return    
        def Cab (Canvas, X, Y, NewColor):
            addRectFilled(Canvas, X, Y, 70, 30, NewColor)
            Window(Canvas, X+10, Y+5)
            Window(Canvas, X+40, Y+5)
            return   
       
        Body (Canvas, X-20, Y-40, NewColor)
        Cab (Canvas, X, Y-65, NewColor)
        Wheel(Canvas, X, Y)
        Wheel(Canvas, X+65, Y)  
        repaint(Canvas)
        time.sleep(0.05)
        return
def Ground (Canvas, Xg, Yg, NewColor):
    addRectFilled (Canvas, Xg,Yg, getWidth(Canvas), Yg, NewColor)
    return        


def Blend (P0,P1,T):
    return (P1-P0)*float(T) + P0
    
def BlendColor (C0,C1,T):   #C0,C1,C2 are colors
    R = INT(Blend(C0.getRed(), C1.getRed(),T))
    G =INT( Blend(C0.getGreen(), C1.getGreen(),  T))
    B = INT(Blend(C0.getBlue(), C1.getBlue(), T))
    return makeColor(R,G,B) 

def Sun(Canvas, Xs, Ys,R, NewColor):
         addCircleFilled(Canvas,Xs, Ys,R, yellow)
         return 

    
def Sunrise (Canvas,Frames):
    X = 0
    X2=0
    Y =INT((3.0/5)*getHeight(Canvas))
    Xs=INT((1.0/5)*getWidth(Canvas))
    Ys=INT((4.0/5)*getHeight(Canvas))
    Xk=0
    Yk=0
    Xg=0
    Yg=INT((3.0/5)*getHeight(Canvas))
    Xd = 6
    C0=makeColor(30,30,30)
    C1=makeColor(255,128,0)
    C2=makeColor(0,0,0)
    C3=makeColor(0,255,255)
    Ccar=makeColor(30,30,30)
    Ccar2=makeColor(255,0,0)
    Cc=makeColor(205,205,193)
    Cc2=makeColor(255,255,255)
    P0=[INT((1.0/5)*getWidth(Canvas)),INT((4.0/5)*getHeight(Canvas))]
    P1=[getWidth(Canvas)/2, 0]
    Xc=getWidth(Canvas)-1
    Xc2=getWidth(Canvas)-1
    Yc=getHeight(Canvas)/4
    Cr=makeColor(0,0,0)
    Cr2=makeColor(139,136,120)
    Ct=makeColor(25,12,12)
    Ct2=makeColor(218,165,32)
    Cd=makeColor(0,0,0)
    Cd2=makeColor(112,138,144)
    Ch=makeColor(165,42,42)
    Ch2=makeColor(233,150,122)
    T=0.0
  
    while (Xs<Frames):
        Xc=Xc-1
        Cs=BlendColor(C2,C3,T)

        addRectFilled(Canvas,Xk,Yk,getWidth(Canvas), INT((3.0/5)*getHeight(Canvas)), Cs)
        T=T+0.008
        Sun(Canvas,Xs,Ys,getHeight(Canvas)/6, yellow)
        Xs=Xs+2
        Ys=Ys-2
        
        Cc3=BlendColor(Cc,Cc2,T)
        addCircleFilled(Canvas,Xc,Yc+20,getHeight(Canvas)/10,Cc3)
        addCircleFilled(Canvas,Xc+50,Yc+15, getHeight(Canvas)/10,Cc3)
        addCircleFilled(Canvas,Xc+100,Yc+20,getHeight(Canvas)/10,Cc3)
        Xc=Xc-4
        addCircleFilled(Canvas,X2,Yc+20,getHeight(Canvas)/10,Cc3)
        addCircleFilled(Canvas,X2+50,Yc+15, getHeight(Canvas)/10,Cc3)   #clouds move different speed depending on wind
        addCircleFilled(Canvas,X2+100,Yc+20,getHeight(Canvas)/10,Cc3)
        X2=X2+2
        Cg=BlendColor(C0,C1,T)
        Ground(Canvas,Xg,Yg,Cg)
        Cd3=BlendColor(Cd,Cd2,T) 
        Ch3=BlendColor(Ch,Ch2,T)
        addRectFilled(Canvas, getWidth(Canvas)/2,Yg-88,(getWidth(Canvas)/2)-50,Yg-200, Ch3)
        addRectFilled(Canvas, getWidth(Canvas)/2+50, Yg-38,getWidth(Canvas)/2-150, Yg-250,Cd3)
        addLine(Canvas,0,Yg,getWidth(Canvas),Yg,black)
        Cr3=BlendColor(Cr,Cr2,T)
        addLine(Canvas,0,Yg,getWidth(Canvas),Yg,black)
        addRectFilled(Canvas,0,INT((3.0/5)*getHeight(Canvas))+50,getWidth(Canvas),INT((3.0/5)*getHeight(Canvas))-200,Cr3)
        Ct3=BlendColor(Ct,Ct2,T)
        addCircleFilled(Canvas,Xc,INT((4.0/5)*getHeight(Canvas))+50,getHeight(Canvas)/10,Ct3) 
        Ccar3=BlendColor(Ccar,Ccar2,T)
        Car(Canvas,X,Y+55,Ccar3)
        X=X+Xd
        repaint(Canvas)
        SaveFrame(Canvas)
        time.sleep(0.00001)
    return
    

def Run():
    global CurrentFrame, BaseFolder
    CurrentFrame = 0
    BaseFolder = pickAFolder()
    Message = "Copyright "+chr(169)+"2015 Ma.Lora Drizella Ong"
    Canvas = makeEmptyPicture(640,480)
    Sunrise (Canvas, 500)
    Scroller (Canvas, 100, Message, blue, yellow)
    return
    
def MakeMovie():
    global BaseFolder
    if (BaseFolder == ""): BaseFolder = pickAFolder()
    MyMovie = makeMovieFromInitialFile(BaseFolder + "Image00000.jpg")
    writeQuicktime(MyMovie, BaseFolder + "Ong_Ma.Lora Drizella_Sunrise.mov", 16)
    return