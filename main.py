import qrcode

def generate_qr_code(data, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image
    img.save(filename)
    print(f"QR code saved as '{filename}'")

if __name__ == "__main__":
    # Input data to encode in the QR code
    data_to_encode = input("Enter the data to encode in the QR code: ")
    
    # Specify the filename to save the generated QR code
    file_name = input("Enter the filename to save the QR code (with extension, e.g., qr_code.png): ")
    
    # Generate QR code
    generate_qr_code(data_to_encode, file_name)
