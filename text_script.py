from num2words import num2words

input = [{'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Ceemox-250', 'type': 'Capsule', 'time': ['Morning'], 'quantity': '5', 'ba': 'before', 'days': '15', 'img_front': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Front.jpg', 'img_back': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Back.jpg', 'img_name': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Name.jpg', 'spcl_intr': ''}, {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Norcin-400', 'type': 'Tablet', 'time': ['Morning', 'Evening'], 'quantity': '2', 'ba': 'after', 'days': '10', 'img_front': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Front.jpg', 'img_back': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Back.jpg', 'img_name': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Name.jpg', 'spcl_intr': ''}]
def text_script(list):
    list1 = []
    for i in range(len(list)):
        type = list[i]["type"]
        time = list[i]["time"]
        quantity = list[i]["quantity"]
        sbtit = "should be taken\nin the"
        sbtft = "should be taken for"
        ba = list[i]["ba"]
        days = list[i]["days"]
        this =  "This "
        days_ = " day."

        if int(quantity) > 1:
            this = "These "
            #adding 's' to the end of the type if the type is not already plural
            if type[-1] != 's':
                type = type + 's'
        else:
            #removing 's' to the end of the type if the quantity is greater than 1
            if type[-1] == 's':
                type = type[:-1]    

        if int(days) > 1:
            days_ = " days."    
      
        #capitalizing the first letter of the type if it is not already
        if type[0] != type[0].lower():
            type = type[0].lower() + type[1:]

        #concatenating all the time in a string
        if len(time) > 2:
            time_ = ", ".join(time[:-1]).lower() + " and " + time[-1].lower()
        else:
            time_ = " and ".join(time).lower()

        medicine_data = num2words(quantity).capitalize() + " " + type + " " + sbtit + " " + time_ + " " + ba + " " + "the meal. " + this + sbtft + " " + num2words(days) + days_
        
        # print(medicine_data)
        list1.append(medicine_data)
    return list1

