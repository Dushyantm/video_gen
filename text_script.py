from num2words import num2words
import json


input = [{'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Ceemox-250', 'type': 'Capsule', 'time': ['Morning'], 'quantity': '5', 'ba': 'before', 'days': '15', 'img_front': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Front.jpg', 'img_back': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Back.jpg', 'img_name': 'MP_medicineDB/Capsule/Ceemox-250_Anrose Pharma_Saralife Healthcare_Name.jpg', 'spcl_intr': ''}, {'patientId': '60efb3be62512a00158190ca', 'drug_name': 'Norcin-400', 'type': 'Tablet', 'time': ['Morning', 'Evening'], 'quantity': '2', 'ba': 'after', 'days': '10', 'img_front': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Front.jpg', 'img_back': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Back.jpg', 'img_name': 'MP_medicineDB/Tablet/Norcin-400_Omega Biotech_Name.jpg', 'spcl_intr': ''}]
medicine_data = " "
list1 = []

def getSentence(list):

    for i in range(len(list)):
        language = list[i]["language"]

        if language == "English":
            medicine_data = get_medicine_data_Eng(list, i)
            list1.append(medicine_data)
        
        elif language == "Marathi":
            medicine_data = get_medicine_data_Marathi(list, i)
            list1.append(medicine_data)
        
        elif language == "Hindi":
            medicine_data = get_medicine_data_Hindi(list, i)
            list1.append(medicine_data)

        else:
            print("Please enter the correct language")
    return list1

def get_medicine_data_Marathi(list, i):

        type = list[i]["type"]
        time = list[i]["time"]
        quantity = list[i]["quantity"]
        ba = list[i]["ba"]
        days = list[i]["days"]
        hee = "ही"
        diwas = "दिवस"

        if int(quantity) > 1:
            hee = "ह्या "

        if int(quantity) > 1:
            #adding 's' to the end of the type if the type is not already plural
            if type[-1] != 's':
                type = type + 's'
        else:
            #removing 's' to the end of the type if the quantity is greater than 1
            if type[-1] == 's':
                type = type[:-1]  

        #convert english to marathi for the type
        type_marathi = {
            "Tablet": "गोळी ",
            "Tablets": "गोळ्या  ",
            "Capsule": "कैप्सूल",
            "Capsules": "कैप्सूल",
            "Injection": "इंजेक्शन",
            "Injections": "इंजेक्शन",
            "Syrup": "सिरप",
            "Drops": "ड्रॉप",
            "Drop": "ड्रॉप",
            "Powder": "पावडर",
            "Powders": "पावडर",
            "Lotion": "लोशन",
            "Lotions": "लोशन",
            "Solution": "सोल्यूशन",
            "Solutions": "सोल्यूशन",
            "Gel": "जेल",
            "Gels": "जेल",
            "Cream": "क्रीम",
            "Creams": "क्रीम",
        }
        type = type_marathi[type]
        
        #convert english to marathi for the ba
        ba_marathi = {
            "before": "आधी",
            "after": "नंतर"
        }
        ba = ba_marathi[ba]
    
        #convert number to hindi for the days 
        num2marathi = {
             "1": "१",
            "2": "२",
            "3": "३",
            "4": "४",
            "5": "५",
            "6": "६",
            "7": "७",
            "8": "८",
            "9": "९",
            "10": "१०",
            "11": "११",
            "12": "१२",
            "13": "१३",
            "14": "१४",
            "15": "१५",
            "16": "१६",
            "17": "१७",
            "18": "१८",
            "19": "१९",
            "20": "२०",
            "21": "२१",
            "22": "२२",
            "23": "२३",
            "24": "२४",
            "25": "२५",
            "26": "२६",
            "27": "२७",
            "28": "२८",
            "29": "२९",
            "30": "३०",
        }
        quantity = num2marathi[quantity]

        if int(days) > 1:
            diwas = "दिवसांसाठी"
        #convert english to marathi for the days from 1 t0 100

        days = num2marathi[days]

        #convert english to marathi for the time
        time_marathi = {
            "Morning": "सकाळचा नाश्त्या",
            "Afternoon": "दुपारच्या जेवणा",
            "Evening": "रात्रीच्या जेवणा"
            # "Night": ""
        }
        time = [time_marathi[i] + " " + ba for i in time]
        time = " आणि ".join(time) 

        medicine_data = hee + " " + quantity + " " + type + " " + time + " "  + "घ्यावी. " + hee + " " + type + " " + days + " " + diwas +" घ्यावी."
        
        return medicine_data
        
def get_medicine_data_Hindi(list, i):

        type = list[i]["type"]
        time = list[i]["time"]
        quantity = list[i]["quantity"]
        ba = list[i]["ba"]
        days = list[i]["days"]
        hee = "यह"
        diwas = "दिन "
        tlh = " तक लेनी है।"


        if int(quantity) > 1:
            #adding 's' to the end of the type if the type is not already plural
            if type[-1] != 's':
                type = type + 's'
        else:
            #removing 's' to the end of the type if the quantity is greater than 1
            if type[-1] == 's':
                type = type[:-1]  

        #convert english to marathi for the type
        type_hindi = {
            "Tablet": "गोली ",
            "Tablets": "गोलियाँ ",
            "Capsule": "कैप्सूल",
            "Capsules": "कैप्सूल",
            "Injection": "इंजेक्शन",
            "Injections": "इंजेक्शन",
            "Syrup": "सिरप",
            "Drops": "ड्रॉप",
            "Drop": "ड्रॉप",
            "Powder": "पावडर",
            "Powders": "पावडर",
            "Lotion": "लोशन",
            "Lotions": "लोशन",
            "Solution": "सोल्यूशन",
            "Solutions": "सोल्यूशन",
            "Gel": "जेल",
            "Gels": "जेल",
            "Cream": "क्रीम",
            "Creams": "क्रीम",
        }
        type = type_hindi[type]
        
        #convert english to marathi for the ba
        ba_hindi = {
            "before": "के भोजन के पहले",
            "after": "के भोजन के बाद "
        }
        ba = ba_hindi[ba]
    
        
        num2hindi = {
             "1": "१",
            "2": "२",
            "3": "३",
            "4": "४",
            "5": "५",
            "6": "६",
            "7": "७",
            "8": "८",
            "9": "९",
            "10": "१०",
            "11": "११",
            "12": "१२",
            "13": "१३",
            "14": "१४",
            "15": "१५",
            "16": "१६",
            "17": "१७",
            "18": "१८",
            "19": "१९",
            "20": "२०",
            "21": "२१",
            "22": "२२",
            "23": "२३",
            "24": "२४",
            "25": "२५",
            "26": "२६",
            "27": "२७",
            "28": "२८",
            "29": "२९",
            "30": "३०",
        }
        quantity = num2hindi[quantity]

        if int(days) > 1:
            diwas = "दीनो"

        if int(days) < 1:    
            tlh = " लेनी है।"
        #convert english to marathi for the days from 1 t0 100

        days = num2hindi[days]

        #convert english to marathi for the time
        time_hindi = {
            "Morning": "सुबह",
            "Afternoon": "दोपहर",
            "Evening": "शाम"
            # "Night": ""
        }
        time = [time_hindi[i] + " " for i in time]
        time = " और ".join(time) 

        medicine_data = hee + " " + quantity + " " + type + " " + time + " " + ba + " लेनी है। " + hee + " " + type + " " + days + " " + diwas + tlh
        
        return medicine_data
    
def get_medicine_data_Eng(list,i):

        type = list[i]["type"]
        time = list[i]["time"]
        quantity = list[i]["quantity"]
        sbtit = "should be taken in the"
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

        #concatenating all the time in a string with comma and the last time with time if there are more than two times 
        if len(time) > 2:
            time_ = ", ".join(time[:-1]).lower() + " and " + time[-1].lower()
        else:
            time_ = " and ".join(time).lower()

        medicine_data = num2words(quantity).capitalize() + " " + type + " " + sbtit + " " + time_ + " " + ba + " " + "the meal. " + this + sbtft + " " + num2words(days) + days_
        #convert medicine_data into marathi language 
        # print(medicine_data)
        return medicine_data
