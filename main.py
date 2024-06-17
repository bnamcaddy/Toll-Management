
from detect_license_plate import detect_license_plate
from database import initialize_database, record_transaction

def main():
    image_path = 'path_to_image.jpg'  # Replace with the path to your image
    license_plate = detect_license_plate(image_path)
    
    if license_plate:
        amount = 5.0  # Toll amount
        record_transaction(license_plate, amount)
        print(f'Transaction recorded for {license_plate}')
    else:
        print('License plate not detected')

if __name__ == "__main__":
    initialize_database()
    main()