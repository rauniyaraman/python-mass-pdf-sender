import random
text_to_send_with_pdf = [
    'D/O', 
    'D/O request', 
    'Delivery Order', 
    'Delivery Instruction',
    'Please find the attached delivery order for your review.',
    'Kindly review the attached delivery order.',
    'Attached is the delivery order for your reference.',
    'Please review the delivery order attached here.',
    'For your attention, the delivery order is attached.',
    'Enclosed you will find the delivery order.',
    'Please check the attached delivery order document.',
    'The delivery order is attached for your convenience.',
    'We have attached the delivery order for your perusal.',
    'Please see the attached delivery order for further details.',
    'Attached is the file please find the delivery order.',
    'The delivery order is attached for your review.',
    'Find attached the delivery order for your records.',
    'Please find attached the delivery order you requested.',
    'Here is the delivery order as per your request.',
    'Attached is the requested delivery order.',
    'The delivery order document is attached for your reference.',
    'We have enclosed the delivery order for your review.',
    'Please refer to the attached delivery order document.',
    'Attached you will find the delivery order.',
    'The delivery order has been attached for your information.',
    'Please find the attached document for the delivery order.',
    'Please find the attached document for the delivery summary.',
    'The delivery file is attached for your reference.',
    'Please see the attached delivery confirmation for further details.'
    'Kindly review the attached delivery instruction.',
]
def get_shuffled_text():
    return random.choice(text_to_send_with_pdf)
# shuffeled_text = random.choice(text_to_send_with_pdf)
# print(shuffeled_text)