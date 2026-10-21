meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "67": "fenómeno viral, meme y jerga de internet de la Generación Alpha que no tiene un significado literal o fijo",      "xd": "emoticono de internet que representa una cara riéndose con los ojos fuertemente apretados y la boca muy abierta por una gran carcajada", 
            "aura": "concepto de la cultura de internet y de la Generación Z que utiliza la idea metafórica de un campo de energía personal para medir el carisma, el estilo, la seguridad o el ridículo de alguien"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(word:, meme_dict[word])
    
else:
    print("buscalo en google")
    
