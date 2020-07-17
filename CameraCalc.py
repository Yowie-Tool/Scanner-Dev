import math
Fnumber=[0.7,0.8,0.9,1,1.1,1.2,1.4,1.6,1.8,2,2.2,2.5,2.8,3.2,3.5,4,4.5,5,5.6,6.3,7.1,8,9,10,11,13,14,16,18,20,22]
xrescam1=0
xrescam2=0
xrescam3=0
yrescam1=0
yrescam2=0
yrescam3=0
sensorh1=0
sensorh2=0
sensorh3=0
sensorv1=0
sensorv2=0
sensorv3=0
sensorf1=0
sensorf2=0
sensorf3=0
cam1fps=0
cam2fps=0
cam3fps=0
oversamples=1
C1Focus=0
C2Focus=0
C3Focus=0
#scantype=input("Enter Scanner type: 1 - 2D or 2 - 3D")
#scantype=int(scantype)
cameranum=int(input("Enter proposed number of cameras (1-2): "))
overinc=input("Include oversampling in calculations (y/n): ")
if overinc == "y":
    oversamples=int(input("Enter proposed number of samples per measurement: "))
print("1. Raspberry Pi Camera 8mp £24 15fps Max")
# 1/4" (4.6mm diagonal) IMX219 sensor 15 fps at full resolution 1.12μm x 1.12μm Pixel size 3280 x 2464
print("1. Arducam Camera 8mp (CS Mount lens) £60 15fps Max")
print("2. Arducam Camera 9mp (m12 lens) £40 9.7 fps Max")
# 1/2.3" (7.7mm diagonal) MT9N001 sensor 9.7 fps at full resolution 1.75 x 1.75 um Pixel size 3488 x 2616
print("3. Arducam Camera 10mp (m12 lens) £60 7.5 fps Max")
# 1/2.3" (7.7mm diagonal) MT9J003 sensor 7.5 fps at full resolution 1.67 x 1.67 um Pixel size 3856 x 2764
print("4. Arducam Camera 13mp £50 12 fps Max")
# 1/3" (6mm diagonal) IMX135 sensor 12 fps at full resolution 1.12μm x 1.12μm Pixel size 4224H x 3136V
print("5. Arducam Camera 14mp (m12 lens) £65 6.3fps Max")
# 1/2.3" (7.7mm diagonal) MT9F001 sensor 6.3 fps at full resolution 1.4 x 1.4 um Pixel size 4608 x 3288
print("6. Arducam Camera 16mp £60 7fps Max")
# 1/2.8" (6.521mm diagonal)IMX298 sensor 7 fps at full resolution 1.12um x 1.12um Pixel size 4656 H × 3496 V
print("7. Arducam Camera 18mp (m12 lens) £120 24 fps Max")
# 1/2.3" (7.7mm diagonal) AR1820HS sensor 24 fps at full resolution 1.25um x 1.25um Pixel size 4912 x 3684
print("8. Raspberry Pi Camera 12.3MP HQ £51")
# 1/2.3" (7.9mm diagonal) IMX477 sensor 30 fps at full resolution 1.55um x 1.55um Pixel size 4056 x 3040
selectcam1=int(input("Select Camera 1: "))
#All camera's should probably be the same as we are planning on using a multi way CSI interface and this requires all to be the same,
# but in the event some are run through USB, I've left the option to include different cameras in.
if selectcam1==1:
    xrescam1=3280
    #X resolution
    sensorf1=4.6
    #sensor frame size
    sensorh1=(sensorf1*4)/5
    #Sensor horizontal size
    yrescam1=2464
    #Y Resolution
    sensorv1=(sensorf1*3)/5
    #Sensor vertical size
    cam1fps=1/(15/2)
    #Time taken to take 2 photo's (needed per measure).
if selectcam1==2:
    xrescam1=3488
    sensorf1=7.7
    sensorh1 = (sensorf1 * 4) / 5
    yrescam1 = 2616
    sensorv1 = (sensorf1 * 3) / 5
    cam1fps = 1 / (9.7 / 2)
if selectcam1==3:
    xrescam1=3856
    sensorf1=7.7
    sensorh1 = (sensorf1 * 4) / 5
    yrescam1 = 2764
    sensorv1 = (sensorf1 * 3) / 5
    cam1fps = 1 / (7.5 / 2)
if selectcam1==4:
    xrescam1=4224
    sensorf1=6
    sensorh1 = (sensorf1 * 4) / 5
    yrescam1 = 3136
    sensorv1 = (sensorf1 * 3) / 5
    cam1fps = 1 / (12 / 2)
if selectcam1==5:
    xrescam1=4608
    sensorf1 = 7.7
    sensorh1 = (sensorf1 * 4) / 5
    yrescam1 = 3288
    sensorv1 = (sensorf1 * 3) / 5
    cam1fps = 1 / (6.3 / 2)
if selectcam1==6:
    xrescam1=4656
    sensorf1=6.521
    sensorh1 = (sensorf1 * 4) / 5
    yrescam1 = 3496
    sensorv1 = (sensorf1 * 3) / 5
    cam1fps = 1 / (7 / 2)
if selectcam1==7:
    xrescam1=4912
    sensorf1=7.7
    sensorh1 = (sensorf1 * 4) / 5
    yrescam1 = 3684
    sensorv1 = (sensorf1 * 3) / 5
    cam1fps = 1 / (24 / 2)
if selectcam1==8:
    xrescam1=4056
    sensorf1=7.9
    sensorh1 = 6.287
    yrescam1 = 3040
    sensorv1 = 4.712
    cam1fps = 1 / (30 / 2)
maxres1=float(input("Maximum resolution between measurements camera 1: "))
#resolution in this case being the the maximum distance between possible measurements, where every pixel is a possible measurement.
camdist1=int(input("Camera 1 offset from laser: "))
#The difference between the laser and the centre of the camera
if cameranum > 1:
    selectcam2=int(input("Select Camera 2 (type 0 for same as camera 1): "))
    if selectcam2 == 0:
        sensorf2=sensorf1
        xrescam2 = xrescam1
        sensorh2 = sensorh1
        yrescam2 = yrescam1
        sensorv2 = sensorv1
        cam2fps=cam1fps
    if selectcam2 == 1:
        xrescam2 = 3280
        sensorf2=4.6
        sensorh2 = (sensorf2 * 4) / 5
        yrescam2 = 2464
        sensorv2 = (sensorf2 * 3) / 5
        cam2fps = 1 / (15 / 2)
    if selectcam2 == 2:
        xrescam2 = 3488
        sensorf2=7.7
        sensorh2 = (sensorf2 * 4) / 5
        yrescam2 = 2616
        sensorv2 = (sensorf2 * 3) / 5
        cam2fps = 1 / (9.7 / 2)
    if selectcam2 == 3:
        xrescam2 = 3856
        sensorf2=7.7
        sensorh2 = (sensorf2 * 4) / 5
        yrescam2 = 2764
        sensorv2 = (sensorf2 * 3) / 5
        cam2fps = 1 / (7.5 / 2)
    if selectcam2 == 4:
        xrescam2 = 4224
        sensorf2=6
        sensorh2 = (sensorf2 * 4) / 5
        yrescam2 = 3136
        sensorv2 = (sensorf2 * 3) / 5
        cam2fps = 1 / (12 / 2)
    if selectcam2 == 5:
        xrescam2 = 4608
        sensorf2=7.7
        sensorh2 = (sensorf2 * 4) / 5
        yrescam2 = 3288
        sensorv2 = (sensorf2 * 3) / 5
        cam2fps = 1 / (6.3 / 2)
    if selectcam2 == 6:
        xrescam2 = 4656
        sensorf2=6.521
        sensorh2 = (sensorf2 * 4) / 5
        yrescam2 = 3496
        sensorv2 = (sensorf2 * 3) / 5
        cam2fps = 1 / (7 / 2)
    if selectcam2 == 7:
        xrescam2 = 4912
        sensorf2=7.7
        sensorh2 = (sensorf2 * 4) / 5
        yrescam2 = 3684
        sensorv2 = (sensorf2 * 3) / 5
        cam2fps = 1 / (24 / 2)
    if selectcam2 == 8:
        xrescam2 = 4056
        sensorf2 = 7.9
        sensorh2 = 6.287
        yrescam2 = 3040
        sensorv2 = 4.712
        cam2fpsfps = 1 / (30 / 2)
    maxres2 = float(input("Maximum resolution between measurements camera 2: "))
    camdist2 = int(input("Camera 2 offset from laser: "))
    overlap1 = int(input("mm overlap between Camera 1 and Camera 2: "))
    #If both cameras were at the same distance from the laser, this would give an overlap of x degrees.
    # As the cameras have to be offset, at 0 degrees we would end up with a measurement void, so experimentation is needed. Perhaps a better metric could be used.
minmeasure1=int(input("Minimum Measurement: "))
#Relatively self explanatory, but obviously there needs to be a minimum distance of more than 0 over which the scanner can measure.
#We need to take into account the rotation of the unit, and make sure that the minimum distance will allow the unit to rotate without hitting anything.

cam1angled=math.atan(minmeasure1/camdist1)
#This gives the first cameras angle
camangle1=0
camangle2=0
maxrescam1=0
maxrescam2=0
minrescam1=0
minrescam2=0
avrescam1=0
avrescam2=0
maxrangecam1=0
maxrangecam2=0
minrangecam2=0
camangleddeg=cam1angled*(180/math.pi)
camout1=[]
camout2=[]
camout1diff=[]
camout2diff=[]

camoutcombdiff=[]
maxresallcams=0
minresallcams=0
avresallcams=0
while maxrescam1<maxres1:
    camangle1=camangle1+0.1
    #Increase camera Horizontal field of view in 0.1 degree increments
    camanglerad=camangle1/(180/math.pi)
    camout1.clear()
    camout1diff.clear()
    camout1diff=[]
    Bcalc=((180-camangle1)/2)
    #Angle B for the cosine rule, always constant in our calculation
    Bconst = (Bcalc/(180/math.pi))
    cosB=math.cos(Bconst)
    aconst=(xrescam1*(math.sin(Bconst)))/(math.sin(camanglerad))
    #Length a is also a constant in our calculation
    aconstsqrd=math.pow(aconst,2)
    for int1 in range(xrescam1):
        cosC=((2*aconstsqrd)-(2*aconst*(int1+1)*cosB))/((2*aconst*(math.sqrt((aconstsqrd+((int1+1)*(int1+1))-(2*aconst*(int1+1)*cosB))))))
        #This is the formula I derived from the cosine rule for calculating the angle across the horizontal part of the frame
        angle=math.acos(cosC)
        totalangle=angle+cam1angled
        oppcalc=camdist1*(math.tan(totalangle))
        #Here we have the distance output. In the main calculation in the scanner, this is then adjusted for the distance from the origin, and rotation of the unit.
        camout1.append(oppcalc)
        if int1>0:
            diff=oppcalc-camout1[int1-1]
            camout1diff.append(diff)
    maxrescam1=camout1diff[-1]
    minrescam1=camout1diff[0]
    avrescam1=sum(camout1diff)/len(camout1diff)
    maxrangecam1=camout1[-1]
    focallengthcam1=(sensorh1*(2*minmeasure1))/((2*(2*minmeasure1)*(math.tan((camangle1/2)/(180/math.pi))))+sensorh1)
    #Calculates the focal length of the lens needed to achieve the horizontal field of view specified, based on CCD sensor width and minimum focal distance
    cam1vanglerad = 2 * math.atan((sensorv1 * (minmeasure1 - focallengthcam1)) / (2 * minmeasure1 * focallengthcam1))
    #Angle that the camera needs to be mounted at
    cam1vangle=cam1vanglerad*(180/math.pi)
    circleofconfusion=sensorf1/1500
    camera1aperture = (math.pow(focallengthcam1, 2)) / (circleofconfusion * ((minmeasure1 * 2) - focallengthcam1))
print('X angle: [%f] Y Angle: [%f] Max Res: [%f] Min Res [%f] Av Res [%f] Range [%f] to [%f]'%(camangle1,cam1vangle,maxrescam1,minrescam1,avrescam1,minmeasure1,maxrangecam1))
print ('Camera 1 Angled at :[%f] degrees'%(camangleddeg+(camangle1/2)))
print ('Camera 1 with ideal focal length of [%f] and minimum aperture of F[%f]'%(focallengthcam1,camera1aperture))
changecam1=input("To change focal length to standard lens type new focal length or n to keep proposed lens: ")
if changecam1 != "n":
    changecam1=float(changecam1)
    camanglerad=2*math.atan((sensorh1*((2*minmeasure1)-changecam1))/(2*(2*minmeasure1)*changecam1))
    #Gives horizontal field of view based on focal length (standard equation from the internet...)
    camangle1=camanglerad*(180/math.pi)
    camout1.clear()
    camout1diff.clear()
    camout1diff = []
    Bcalc = ((180 - camangle1) / 2)
    Bconst = (Bcalc / (180 / math.pi))
    cosB = math.cos(Bconst)
    aconst = (xrescam1 * (math.sin(Bconst))) / (math.sin(camanglerad))
    aconstsqrd = math.pow(aconst, 2)
    for int1 in range(xrescam1):
        cosC = ((2 * aconstsqrd) - (2 * aconst * (int1 + 1) * cosB)) / (
        (2 * aconst * (math.sqrt((aconstsqrd + ((int1 + 1) * (int1 + 1)) - (2 * aconst * (int1 + 1) * cosB))))))
        angle = math.acos(cosC)
        totalangle = angle + cam1angled
        oppcalc = camdist1 * (math.tan(totalangle))
        camout1.append(oppcalc)
        if int1 > 0:
            diff = oppcalc - camout1[int1 - 1]
            camout1diff.append(diff)
    maxrescam1 = camout1diff[-1]
    minrescam1 = camout1diff[0]
    avrescam1 = sum(camout1diff) / len(camout1diff)
    maxrangecam1 = camout1[-1]
    cam1vanglerad = 2 * math.atan((sensorv1 * (minmeasure1 - changecam1)) / (2 * minmeasure1 * changecam1))
    cam1vangle=cam1vanglerad*(180/math.pi)
    threesixtysteps = round(360 / cam1vangle)
    #Number of steps in a complete scan - gearing on 2D scan must be adjusted to suit, as only full steps of stepper motor are accurate without a feedback loop.
    threesixtytime = threesixtysteps * (cam1fps + ((cam1vangle / 1.8) * 3 * 16 * 0.001))
    #Theoretical fastest 2D scan time, based on number of photo's needed and fps at maximum resolution of camera
    print('X angle: [%f] Y Angle: [%F] Max Res: [%f] Min Res [%f] Av Res [%f] Range [%f] to [%f]\r' % (camangle1,cam1vangle, maxrescam1, minrescam1, avrescam1, minmeasure1, maxrangecam1), end="")
    print("")
    print('Camera 1 Angled at :[%f] degrees' % (camangleddeg + (camangle1 / 2)))

if cameranum > 1:
    while maxrescam2<maxres2:
        cam2angled = math.atan((maxrangecam1-overlap1) / camdist2)
        camangle2=camangle2+0.1
        camanglerad=camangle2/(180/math.pi)
        camout2.clear()
        camout1diff.clear()
        camout1diff=[]
        Bcalc=((180-camangle2)/2)
        Bconst = (Bcalc/(180/math.pi))
        cosB=math.cos(Bconst)
        aconst=(xrescam1*(math.sin(Bconst)))/(math.sin(camanglerad))
        aconstsqrd=math.pow(aconst,2)
        for int1 in range(xrescam2):
            cosC=((2*aconstsqrd)-(2*aconst*(int1+1)*cosB))/((2*aconst*(math.sqrt((aconstsqrd+((int1+1)*(int1+1))-(2*aconst*(int1+1)*cosB))))))
            angle=math.acos(cosC)
            totalangle=angle+cam2angled
            oppcalc=camdist2*(math.tan(totalangle))
            camout2.append(oppcalc)
            if int1>0:
                diff=oppcalc-camout2[int1-1]
                camout2diff.append(diff)
        maxrescam2=camout2diff[-1]
        minrescam2=camout2diff[0]
        avrescam2=sum(camout2diff)/len(camout2diff)
        maxrangecam2=camout2[-1]
        minrangecam2=camout2[0]
        focallengthcam2 = (sensorh2 * minrangecam2*2) / ((4 * minrangecam2 * (math.tan((camangle2 / 2) / (180 / math.pi)))) + sensorh2)
        cam2vanglerad = 2 * math.atan((sensorv2 * (minrangecam2 - focallengthcam2)) / (2 * minrangecam2 * focallengthcam2))
        cam2vangle = cam2vanglerad * (180 / math.pi)
        threesixtysteps = round(360 / cam2vangle)
        threesixtytime = threesixtysteps * (cam1fps + cam2fps + ((cam2vangle / 1.8) * 3 * 16 * 0.001))
        circleofconfusion = sensorf2 / 1000
        camera2aperture = (math.pow(focallengthcam2, 2)) / (circleofconfusion * ((minrangecam2 * 2) - focallengthcam2))
        camangle2ddeg = cam2angled * (180 / math.pi)
    print('X angle: [%f] Y Angle: [%F] Max Res: [%f] Min Res [%f] Av Res [%f] Range [%f] to [%f]'%(camangle2,cam2vangle,maxrescam2,minrescam2,avrescam2,minrangecam2,maxrangecam2))
    print('Camera 2 Angled at :[%f] degrees' % (camangle2ddeg + (camangle2/2)))
    print('Camera 2 with ideal focal length of [%f] and minimum aperture of F[%f]' % (focallengthcam2,camera2aperture))
    changecam2 = input("To change focal length to standard lens type new focal length or n to keep proposed lens: ")
    if changecam2 != "n":
        changecam2 = float(changecam2)
        camanglerad = 2 * math.atan((sensorh2 * ((2*minrangecam2) - changecam2)) / (4 * minrangecam2 * changecam2))
        camangle2 = camanglerad * (180 / math.pi)
        camout2.clear()
        camout1diff.clear()
        camout1diff = []
        Bcalc = ((180 - camangle2) / 2)
        Bconst = (Bcalc / (180 / math.pi))
        cosB = math.cos(Bconst)
        aconst = (xrescam1 * (math.sin(Bconst))) / (math.sin(camanglerad))
        aconstsqrd = math.pow(aconst, 2)
        for int1 in range(xrescam2):
            cosC = ((2 * aconstsqrd) - (2 * aconst * (int1 + 1) * cosB)) / (
            (2 * aconst * (math.sqrt((aconstsqrd + ((int1 + 1) * (int1 + 1)) - (2 * aconst * (int1 + 1) * cosB))))))
            angle = math.acos(cosC)
            totalangle = angle + cam2angled
            oppcalc = camdist2 * (math.tan(totalangle))
            camout2.append(oppcalc)
            if int1 > 0:
                diff = oppcalc - camout2[int1 - 1]
                camout2diff.append(diff)
        maxrescam2 = camout2diff[-1]
        minrescam2 = camout2diff[0]
        avrescam2 = sum(camout2diff) / len(camout2diff)
        maxrangecam2 = camout2[-1]
        minrangecam2 = camout2[0]
        cam2vanglerad = 2 * math.atan((sensorv2 * ((2*minrangecam2) - changecam2)) / (4 * minrangecam2 * changecam2))
        cam2vangle = cam2vanglerad * (180 / math.pi)
        threesixtysteps = round(360 / cam2vangle)
        threesixtytime = threesixtysteps * (cam1fps + cam2fps + ((cam2vangle / 1.8) * 3 * 16 * 0.001))
        circleofconfusion = sensorf2 / 1500
        camangle2ddeg = cam2angled * (180 / math.pi)
        print('X angle: [%f] Y Angle: [%F] Max Res: [%f] Min Res [%f] Av Res [%f] Range [%f] to [%f]' % (camangle2, cam2vangle, maxrescam2, minrescam2, avrescam2, minrangecam2, maxrangecam2))
        print('Camera 2 Angled at :[%f] degrees' % (camangle2ddeg + (camangle2/2)))

if (overinc == 'n') or (overinc == 'y' and oversamples == 1 and cameranum == 1):
    #If oversamples are included, but only one camera is included, and oversamples is set to 1, then oversampling is ignored.
    camoutcomb=[]
    camoutcomb=camout1+camout2
    #combine outputs of all (up to 2) cameras
    camoutcomb.sort()
    #sort them all into ascending order.
    datanum=len(camoutcomb)
    finalmax=camoutcomb[datanum-1]
    numofranges=(finalmax-minmeasure1)/250
    numofranges=int(numofranges)
    valbym=[]
    valbym2=[]
    metrerange=minmeasure1+250
    for int3 in range (numofranges):
        valbym.append(sum(map(lambda x : x < metrerange, camoutcomb)))
        metrerange=metrerange+250
        if int3==0:
            valbym2.append(valbym[0])
        if int3>0:
            valbym2.append((valbym[int3])-(valbym[int3-1]))
    metrerange=minmeasure1+250
    for int4 in range (numofranges):
        camoutcombdiff.clear()
        for int5 in range ((valbym2[int4])-1):
            if int4>0:
                int6=(valbym[int4-1])
            if int4==0:
                int6=0
            camoutcombdiff.append((camoutcomb[int5+int6])-(camoutcomb[int5+int6-1]))
        maxresallcams = max(camoutcombdiff)
        minresallcams = min(camoutcombdiff)
        avresallcams = sum(camoutcombdiff)/len(camoutcombdiff)
        print('Between [%f]mm And [%f]mm Min Res [%f] Av Res [%f] Max Res [%f] with [%d] points with no oversampling' % ((metrerange-250), metrerange, minresallcams, avresallcams, maxresallcams,valbym2[int4]))
        metrerange = metrerange + 250
    print('2D Photographic Minimum Scan time [%F] Seconds' % (threesixtytime))
if (overinc == 'y' and cameranum > 1) or (overinc == 'y' and oversamples > 1):
    #If there is more than one camera, the first camera will always be oversampled, otherwise, oversampling can be added.
    if oversamples > 1:
        #oversampling being the Y field of view of the longest range camera divided by the number of samples -1. 1 sample being only one measurement (minimum) per point,
        # obviously there will be some overlap, but not on all points.
        cammultisample=cam1vanglerad/(oversamples-1)
        if camangle2 !=0:
            cammultisample=cam2vanglerad/(oversamples-1)
    if oversamples == 1:
        #if there is only 1 sample, oversampling will only occur on the cameras below maximum range, with the angle being that of the longest range camera.
        #Oversampling then requires more than one camera. Ie, 2 cameras, camera 1 will oversample only.
        if cameranum ==2:
            cammultisample=cam2vanglerad
    camout1num=len(camout1)
    camout2num=len(camout2)   
    camout1multi = []
    camout2multi = []
    if cameranum==1:
        camoutmulti = []
        for int7 in range (camout1num):
            for int8 in range(oversamples):
                calcis=(camout1[int7])*(math.cos(cammultisample*int8))
                camout1multi.append(calcis)
    if cameranum==2 and oversamples > 1:
        cam1oversample=int((cam1vangle/cam2vangle)*oversamples)
        camoutmulti=[]
        for int7 in range (camout1num):
            for int8 in range(cam1oversample):
                calcis=(camout1[int7])*(math.cos(cammultisample*int8))
                camout1multi.append(calcis)
        for int9 in range (camout2num):
            for int10 in range(oversamples):
                calcis=(camout2[int9])*(math.cos(cammultisample*int10))
                camout2multi.append(calcis)
    if cameranum==2 and oversamples == 1:
        cam1oversample=int((cam1vangle/cam2vangle))
        camoutmulti=[]
        for int7 in range (camout1num):
            for int8 in range(cam1oversample):
                calcis=(camout1[int7])*(math.cos(cammultisample*int8))
                camout1multi.append(calcis)
        for int9 in range (camout2num):
            camout2multi.append(camout2[int9])
    camout1multi.sort()
    camout2multi.sort()
    camoutmulti=camout1multi+camout2multi
    camoutmulti.sort()
    datanum=len(camoutmulti)
    finalmax = camoutmulti[datanum - 1]
    finalmin=camoutmulti[0]
    print('All Cameras combined - Min Range [%f] Max Range [%f]' %(finalmin,finalmax))
    numofranges = (finalmax - finalmin) / 250
    numofranges = int(numofranges)
    valbym = []
    valbym2 = []
    metrerange = finalmin + 250
    for int14 in range(numofranges):
        valbym.append(sum(map(lambda x : x < metrerange, camoutmulti)))
        metrerange = metrerange + 250
        if int14 == 0:
            valbym2.append(valbym[0])
        if int14 > 0:
            valbym2.append((valbym[int14]) - (valbym[int14 - 1]))
    metrerange = minmeasure1 + 250
    for int15 in range(numofranges):
        camoutcombdiff.clear()
        for int16 in range((valbym2[int15]) - 1):
            if int15 > 0:
                int17 = (valbym[int15 - 1])
            if int15 == 0:
                int17 = 0
            camoutcombdiff.append((camoutmulti[int16 + int17]) - (camoutmulti[int16 + int17 - 1]))
        maxresallcams = max(camoutcombdiff)
        minresallcams = min(camoutcombdiff)
        avresallcams = sum(camoutcombdiff) / len(camoutcombdiff)
        print('Between [%f]mm And [%f]mm Min Res [%f] Av Res [%f] Max Res [%f] with [%d] points with oversampling' % ((metrerange - 250), metrerange, minresallcams, avresallcams, maxresallcams, valbym2[int15]))
        metrerange = metrerange + 250
    print('2D Photographic Minimum Scan time [%F] Seconds' % (threesixtytime*oversamples))

