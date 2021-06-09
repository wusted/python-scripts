def translator(sentence):
    
    spanish = {}
    spanish["sir"] = "señor"
    spanish["hotel"] = "hotel"
    spanish["student"] = "estudiante"
    spanish["boy"] = "niño"
    spanish["restaurant"] = "restaurante"
    spanish["hello"] = "hola"
    spanish["students"] = "estudiantes"
    spanish["are"] = "están"
    spanish["lawyer"] = "abogado"
    spanish["the"] = "(el o la)"
    spanish["restroom"] = "baño"
    spanish["my"] = "mi"
    spanish["madam"] = "señora"
    spanish["your"] = "tu"
    spanish["excuse"] = "disculpa"
    spanish["is"] = "(es o esta)"
    spanish["women"] = "mujeres"
    spanish["men"] = "hombres"
    spanish["where"] = "donde"
    spanish["in"] = "en"

    psentence = []
    words = sentence.split()
    for aword in words:
        if aword in spanish:
            psentence.append(spanish[aword])
        else:
            psentence.append(aword)
    return " ".join(psentence)

sent = "where is the restroom in the hotel ?"
print("In English: " + " ' " + sent + " ' " + " in Spanish " + " ' " + translator(sent) + " '.")
