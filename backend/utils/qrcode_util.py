# backend/utils/qrcode_util.py
import qrcode
import io
import base64

def generate_qr_code(data: str) -> str:
    """
    Returns base64-encoded PNG image of QR code
    """
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()
