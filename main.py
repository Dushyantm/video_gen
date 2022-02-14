from PIL import Image, ImageDraw
from text_script import text_script
from aws_image import import_image
list = []


input = [{'id': '1644402640913', 'data': {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'ADR_Carewin', 'type': 'Injections', 'time': ['Morning'], 'quantity': '5', 'ba': 'before', 'days': '15', 'img_front': 'MP_medicineDB/Injections/ADR_Carewin Pharmaceuticals_American Remedies_Front.jpg', 'img_back': 'MP_medicineDB/Injections/ADR_Carewin Pharmaceuticals_American Remedies_Back.jpg', 'img_name': 'MP_medicineDB/Injections/ADR_Carewin Pharmaceuticals_American Remedies_Name.jpg', 'spcl_intr': ''}}, {'id': '1644402655353', 'data': {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Norcin-400', 'type': 'Tablet', 'time': ['Morning', 'Evening'], 'quantity': '2', 'ba': 'after', 'days': '10', 'img_front': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Front.jpg', 'img_back': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Back.jpg', 'img_name': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Name.jpg', 'spcl_intr': ''}}]
for i in range (len(input)):
    dict = input[i] 
    data = dict["data"]
    list.append(data)
    
aws_image = import_image(list)
text_script(list)
