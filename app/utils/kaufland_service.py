from app.data_streams.queries import register_receipt_in_db
from app.ocr.ocr import handle_image, preprocess_image, perform_ocr, extract_info, extract_products
from app.utils.openAI_services import classify_products


async def kaufland_service(image, date):
    open_cv_image = await handle_image(image)
    enhanced_image = preprocess_image(open_cv_image)
    text = perform_ocr(enhanced_image)
    extracted_data = extract_info(text)
    product_prices = extract_products(extracted_data)
    products = classify_products(product_prices)
    await register_receipt_in_db(products, date)
    return product_prices


async def lidl_service(image, date):
    open_cv_image = await handle_image(image)
    enhanced_image = preprocess_image(open_cv_image)
    text = perform_ocr(enhanced_image)
    extracted_data = extract_info(text)
    product_prices = extract_products(extracted_data)
    products = classify_products(product_prices)
    await register_receipt_in_db(products, date)
    return product_prices
