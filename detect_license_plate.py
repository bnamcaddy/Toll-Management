
import cv2
import easyocr

def detect_license_plate(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Unable to open image file {image_path}")
        return None
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply edge detection
    edged = cv2.Canny(gray, 30, 200)
    
    # Find contours
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Sort contours based on area and keep the largest one
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    
    license_plate = None
    for contour in contours:
        # Approximate the contour
        approx = cv2.approxPolyDP(contour, 10, True)
        
        if len(approx) == 4:  # Assuming the license plate is rectangular
            license_plate = approx
            break
    
    if license_plate is None:
        return None
    
    # Mask the part other than the license plate
    mask = cv2.fillPoly(image.copy(), [license_plate], (0, 0, 0))
    masked_image = cv2.bitwise_and(image, mask)
    
    # Crop the license plate area
    x, y, w, h = cv2.boundingRect(license_plate)
    cropped_image = gray[y:y+h, x:x+w]
    
    # Use EasyOCR to extract text
    reader = easyocr.Reader(['en'])
    result = reader.readtext(cropped_image)
    
    license_plate_text = ''
    for res in result:
        license_plate_text += res[1] + ' '
    
    return license_plate_text.strip()

# Test the function
if __name__ == "__main__":
    print(detect_license_plate('path_to_image.jpg'))