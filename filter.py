import cv2
img_name = raw_input("Enter the image filename:")
img = cv2.imread(img_name,0)
def menu():
    print "Select filter type:"
    print "Press '1' for Low Pass filter."
    print "Press '2' for High Pass filter."
    print "Press '3' for Band Pass filter."
    print "Press '4' for Notch filter."
    print "Press 'q' to quit the program."
menu()

minTh=100
maxTh=200
def lpf(minTh):
    l = img.shape[0]
    w = img.shape[1]
    for x in range(l):
        for y in range(w):
            if img[x,y]>minTh:
                img[x,y]=0
    cv2.imshow('Output',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def hpf(maxTh):
    l = img.shape[0]
    w = img.shape[1]
    for x in range(l):
        for y in range(w):
            if img[x,y]<maxTh:
                img[x,y]=0                
    cv2.imshow('Output',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def bpf():
    l = img.shape[0]
    w = img.shape[1]
def brf():
    l = img.shape[0]
    w = img.shape[1]


while(True):
    key = raw_input("Enter you choice:")
    if key=='1':
        cv2.namedWindow('Output',cv2.WINDOW_NORMAL)
        cv2.createTrackbar('minTh:','Output',minTh,255,lpf)
        print "You selected Low Pass filter"
        lpf(minTh)
    elif key=='2':
        cv2.namedWindow('Output',cv2.WINDOW_NORMAL)
        cv2.createTrackbar('maxTh:','Output',maxTh,255,hpf)
        print "You selected High Pass filter"
        hpf(maxTh)
    elif key=='3':
        print "You selected Band Pass filter"
        bpf()
    elif key=='4':
        print "You selected Notch filter"
        brf()
    elif key == 'q':
        print "Exit"
        break
    else:
        print "Invalid option"
