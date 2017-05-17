import os
import cv2  
import numpy as np  
from matplotlib import pyplot as plt
import time  

def zhenchuli():
	cap = cv2.VideoCapture(0)
	c = 1
	while(cap.isOpened()):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',gray) 
		if c % 2 == 0:
			cv2.imwrite('image/'+ '2' + '.jpg',frame)
			c = c+1
		else:
			cv2.imwrite('image/'+ '1' + '.jpg',frame)
			c = c+1    	 
		if c>=3:
			img1 = cv2.imread('image/1.jpg',0)
			#cv2.imshow('img1',img1)
			img2 = cv2.imread('image/2.jpg',0)
			#cv2.imshow('img2',img2)
			degree = classify_gray_hist(img1,img2)
			print (degree)
			#阈值设置
			if degree<0.86:
				msm()
				os.system('baojing.mp3')
				#time.sleep(10)
				cv2.waitKey(0)
				cap.release()
				cv2.destroyAllWindows()
				exit()


def classify_gray_hist(image1,image2,size = (256,256)):  
    image1 = cv2.resize(image1,size)  
    image2 = cv2.resize(image2,size)  
    hist1 = cv2.calcHist([image1],[0],None,[256],[0.0,255.0])  
    hist2 = cv2.calcHist([image2],[0],None,[256],[0.0,255.0])   
    #plt.plot(range(256),hist1,'r')  
    #plt.plot(range(256),hist2,'b')  
    #plt.show()    
    degree = 0  
    for i in range(len(hist1)):  
        if hist1[i] != hist2[i]:  
            degree = degree + (1 - abs(hist1[i]-hist2[i])/max(hist1[i],hist2[i]))  
        else:  
            degree = degree + 1  
    degree = degree/len(hist1)  
    return degree    


def msm():
	import twilio.rest as tr
	account_sid = "AC78b0aaaaaaaaaaaaaa9(你的)"
	auth_token = "assssssssssss(你的)"
	client = tr.TwilioRestClient(account_sid, auth_token)
	message = client.messages.create(to="+86你的手机", from_="+你的twilio手机",body="你们宿舍有贼，回来抓贼！！")

zhenchuli() 