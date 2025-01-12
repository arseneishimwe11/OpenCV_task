import cv2

# File paths
output_path = "assignment-001-result.jpg"

# Loading the input image
image = cv2.imread("assignment-001-given.jpg")

# Defining the bounding box coordinates (x1, y1, x2, y2) and text
bounding_box = (260, 185, 1000, 925)
plate_number = "RAH972U"
text_position = (820, 158)

# Drawing the bounding box
cv2.rectangle(image, (bounding_box[0], bounding_box[1]), (bounding_box[2], bounding_box[3]), (0, 255, 0), 9)

# Defining ROI for the text and its background
roi_y1, roi_y2, roi_x1, roi_x2 = 78, 180, 815, 1255
text_and_its_bg = image[roi_y1:roi_y2, roi_x1:roi_x2].copy()

# Creating an overlay for semi-transparent effect
overlay = text_and_its_bg.copy()

# Plate number background
cv2.rectangle(overlay, (0, 0), (roi_x2 - roi_x1, roi_y2 - roi_y1), (20, 10, 20), -1)

# Blending the overlay with the ROI
transparency_factor = 0.5
blended = cv2.addWeighted(overlay, transparency_factor, text_and_its_bg, 1 - transparency_factor, 0)

# Replacing the blended ROI back into the image
image[roi_y1:roi_y2, roi_x1:roi_x2] = blended

# Adding the plate number text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, plate_number, text_position, font, 3, (0, 255, 0), 8, cv2.LINE_AA)

# Saving the processed image
cv2.imwrite(output_path, image)

print(f"Processed image saved to {output_path}")
