import cv2

img=cv2.imread('E:\College Memories\WhatsApp Image 2021-12-30 at 11.23.13 PM (1).jpeg',1)
img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img=cv2.rotate(img,cv2.cv2.ROTATE_90_CLOCKWISE)    
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()