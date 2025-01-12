import cv2

# Function to display the coordinates of the points clicked on the image
def click_event(event, x, y, flags, params):

	# checking for left mouse clicks
	if event == cv2.EVENT_LBUTTONDOWN:

		# displaying the coordinates on the Shell
		print(x, ' ', y)

		# displaying the coordinates on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' + str(y), (x,y), font, 1, (255, 0, 0), 2)
		cv2.imshow('Image', img)

	# checking for right mouse clicks
	if event==cv2.EVENT_RBUTTONDOWN:

		# displaying the coordinates on the Shell
		print(x, ' ', y)

		# displaying the coordinates on the image window
		font = cv2.FONT_HERSHEY_SIMPLEX
		b = img[y, x, 0]
		g = img[y, x, 1]
		r = img[y, x, 2]
		cv2.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x,y), font, 1, (255, 255, 0), 2)
		cv2.imshow('Image', img)

# driver function
if __name__=="__main__":

	# reading the image
	img = cv2.imread('assignment-001-given.jpg', 1)

	width = int(img.shape[1] * 0.5)  # 50% of original width
	height = int(img.shape[0] * 0.5)  # 50% of original height
	dim = (width, height)

	# Resize the image
	img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

	# Display the original and resized images
	# cv2.imshow('Image', img)
	cv2.imshow('Image', img)

	# setting mouse handler for the image and calling the click_event() function
	cv2.setMouseCallback('Image', click_event)

	cv2.waitKey(0)

	# closing the window
	cv2.destroyAllWindows()
