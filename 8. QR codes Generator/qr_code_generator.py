"""
QR Code Generator

This program generates a QR code image from a user-provided URL
and saves it as a PNG file.

Requirements:
    pip install qrcode[pil]

Example:
    Input:
        https://www.google.com

    Output:
        qrcode.png
"""

import qrcode


def generate_qr_code(url: str, file_path: str = "qrcode.png") -> None:
    """
    Generate a QR code from the provided URL and save it as an image.

    Args:
        url (str):
            The URL or text to encode into the QR code.

        file_path (str, optional):
            The output image filename.
            Defaults to 'qrcode.png'.

    Returns:
        None

    Example:
        generate_qr_code(
            "https://www.google.com",
            "google_qr.png"
        )
    """
    # Create a QRCode object
    qr = qrcode.QRCode()

    # Add data to the QR code
    qr.add_data(url)

    # Generate the QR code image
    img = qr.make_image()

    # Save the image to disk
    img.save(file_path)

    print(f"QR Code saved as '{file_path}'")


def main():
    """
    Main program entry point.

    Prompts the user for a URL and generates
    a QR code image from it.
    """
    # Get URL from the user
    url = input("Enter the URL: ").strip()

    # Output filename
    file_path = "qrcode.png"

    # Generate QR code
    generate_qr_code(url, file_path)

    print("QR Code was generated successfully!")


if __name__ == "__main__":
    main()