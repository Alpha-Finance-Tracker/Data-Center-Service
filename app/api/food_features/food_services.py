from app.api.food_features.food_queries import register_receipt_in_db
from app.ocr.ocr import handle_image, preprocess_image, perform_ocr, extract_info, extract_products


async def kaufland_service(image,date):
    open_cv_image = await handle_image(image)
    enhanced_image = preprocess_image(open_cv_image)
    text = perform_ocr(enhanced_image)
    extracted_data = extract_info(text)
    product_prices = extract_products(extracted_data)
    await register_receipt_in_db(product_prices,date)
    return product_prices