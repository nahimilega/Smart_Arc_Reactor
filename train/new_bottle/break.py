import cv2 
import imutils
# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        

        # Saves the frames with frame-count 
        rotated = imutils.rotate(image, 270)
		#cv2.imwrite("frame0.jpg" , rotated)
        cv2.imwrite("frame%d.jpg" % count, rotated)
		
  
        count += 1
  
# Driver Code
def rotate():
	# load the image from disk
	image = cv2.imread("frame0.jpg")
	
	
	
	print("hi")
	
	print("h2i")
	# loop over the rotation angles
	
	rotated = imutils.rotate(image, 270)
	cv2.imwrite("frame0.jpg" , rotated) 
		
		


if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture("bottle.mp4")
