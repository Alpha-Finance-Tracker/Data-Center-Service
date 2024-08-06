import pandas as pd
from fastapi import APIRouter
from fastapi import  File, UploadFile

from app.ocr.ocr import extract_products
from lidl import preprocess_image, perform_ocr, extract_info, handle_image

receipts_router = APIRouter(prefix='/receipts')


@receipts_router.post('/')
async def receipt(image: UploadFile = File(...)):
    # Handle image and preprocess it
    open_cv_image = await handle_image(image)
    enhanced_image = preprocess_image(open_cv_image)

    # Perform OCR on the preprocessed image
    text = perform_ocr(enhanced_image)
    extracted_data = extract_info(text)

    # Convert extracted data to DataFrame and print
    df = pd.DataFrame(extracted_data, columns=['Extracted Data'])

    product_prices = extract_products(extracted_data)
    for product, price in product_prices.items():
        print(f"Product: {product}, Price: {price}")
    return product_prices