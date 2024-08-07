from app.ocr.ocr import extract_products
from app.utils.query_services import register_foods_in_db
from lidl import preprocess_image, perform_ocr, extract_info, handle_image
import pandas as pd
async def kaufland_service(image,date):
    open_cv_image = await handle_image(image)
    enhanced_image = preprocess_image(open_cv_image)
    text = perform_ocr(enhanced_image)
    extracted_data = extract_info(text)
    product_prices = extract_products(extracted_data)
    await register_foods_in_db(product_prices,date)
    return product_prices