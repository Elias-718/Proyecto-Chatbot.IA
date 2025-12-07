import spacy # Es un modulo o libreria crucial para proyectos de este tipo, para usar en procesamiento de lenguaje natural
# Es crucial para que el chatbot pueda entender de mejor manera lo que uno quiere decir y como lo interpreta
import sqlite3
import re # Es un modulo que se usa para buscar un patron de texto muy especifico como en este caso Ryzen, Core (Intel) o Geforce, tambien para usar en expresiones regulares
from typing import Dict, Optional

pln = spacy.load("es_core_news_sm") # Se carga el modelo de PLN en español

pc_db = "pc_gamer.db" # Variable que guarda el nombre de la base de datos

def conectar_db(db_nombre="pc_gamer.db"):
    conexion = sqlite3.connect(db_nombre)
    return conexion

# Esta funcion analizara la pregunta del usuario para extraer nombres especificos como modelos y requisitos
# pregunta: str indica que pregunta debe ser string
# -> Dict[str, Optional[str]]: indica que la funcion debe devolver un diccionario donde las llaves son cadenas "str" y los valores son cadenas "str" o "None" debido a Optional
def analisis_pregunta(pregunta: str) -> Dict[str, Optional[str]]:
    doc = pln(pregunta.lower()) # La variable doc contiene la pregunta o palabra del usuario ya procesada anteriormente

# Identifica el tipo de componente, modelo y uso, None indica que no hay ningun valor asignado en el momento en el que se escribe    
# Al iniciar con { (diccionario), indica que al comenzar el analisis de la pregunta, todavia no sabes que busca el usuario con respecto al uso, componente o modelo
# En otras palabras, al iniciar con None indicamos que la funcion analisis_pregunta llene esos espacios a medida que procesa la frase del usuario
    requerimientos = {
    "tipo_componente": None,
    "modelo_especifico": None,
    "uso": None
}

# token o Tokenizacion: divide el texto en tokens, que son unidades individuales de un texto
# Puede estar basada en palabras completas ejemplo (casa, perro) o caracteres individuales en los que cada caracter es un token (a,b,7,$)
# Tambien basada en sub-palabras como automovil -> auto, movil
    for token in doc:
    # El chatbot identifica los tipos de componentes

        if "cpu" in token.text.lower() or "procesador" in token.text.lower():
            requerimientos["tipo_componente"] = 'Cpu'
        elif "gpu" in token.text.lower() or "grafica" in token.text.lower() or "tarjeta" in token.text.lower():
            requerimientos["tipo_componente"] = 'Gpu'
        elif "ram" in token.text.lower() or "memoria" in token.text.lower():
            requerimientos["tipo_componente"] = 'Ram'
        # El chatbot identifica el uso que le dara el usuario
        if "gaming" in token.text.lower() or "jugar" in token.text.lower():
            requerimientos["uso"] = 'Gaming'
        elif "edicion" in token.text.lower() or "edición" in token.text.lower() or "render" in token.text.lower() or "trabajar" in token.text.lower():
            requerimientos["uso"] = "Edición"
        elif "placa" in token.text.lower() or "motherboard" in token.text.lower():
            requerimientos["tipo_componente"] = "PlacaMadre"
        elif "fuente" in token.text.lower() or "poder" in token.text.lower():
            requerimientos["tipo_componente"] = "FuentePoder"    

                            #  Es un patron de busqueda para identificar de forma automatica nombres de modelos o componentes dentro de la pregunta del usuario
                            # () define un grupo de captura de palabras, el | tambien llamado O/o permite que el patron coincida con el patron dentro de ()
                            # i/d busca patrones similares entre si como i7 o i5, /s* busca espacios en blanco, [] define un conjunto de caracteres permitidos
                            # /d hace que la busqueda coincida con cualquier digito 0-9, /s coincide con espacios en blanco, + indica que debe haber uno o mas digitos o espacios
                            # En otras palabras es un filtro para escanear la pregunta del usuario buscando las palabras en la base de datos
    patron_especificio_modelo = r'(ryzen|core|i\d|rtx|rx)\s*[\d\s]+[xmgti]?'

    # Aqui se usa el patron anterior, que intenta encontrar el patron de marca y numero ejemplo rtx 4080, i7 en la pregunta del usuario
    # Si se encuentra el patron, la variable match contendra el texto marcado pero si no encuentra nada, sera None
    # Como se menciono casi al principio, re es un modulo o libreria que busca patrones muy especificos y search busca lo busca dentro de patron_especifico_modelo
    coincidencia = re.search(patron_especificio_modelo, pregunta.lower())
    # Si el patron anterior lo encuentra, se comenzaran a ejecutar las siguientes condiciones
    if coincidencia:
        for ent in doc.ents: # ent viene de entidad, por cada entidad en doc que viene de documentos, doc.ents es una lista de entidades nombradas que spacy detecto
            if ent.label_ == "producto" or ent.label_ == "organizacion" or ent.label_ == "persona": # ent.label_ busca si la o las entidades son un producto, organizacion o persona, estos son los que nombres que spacy suele asignar a los nombres de hardware
                if coincidencia.group(0) in ent.text.lower(): # Por cada entidad o coincidencia englobada en un grupo es 0, agarrara las entidades y textos y los hara minuscula
                    requerimientos["modelo_especifico"] = ent.text.strip() # Si la entidad completa por ejemplo es AMD Ryzen 5 7600X pero la expresion regular (re) solo encuentra Ryzen 5, se captura la entidad completa para tener el nombre mas limpio y completo
                    

        if not requerimientos["modelo_especifico"]: # Si no se pudo encontrar la entidad completa pero la expresion regular si encontro un patron, lo usamos en coincidencia.group(0). Es como un respaldo
            requerimientos["modelo_especifico"] = coincidencia.group(0) .strip()

    # Revisamos si pregunta contiene 1080p o 4k para definir su uso al usuario    
    if "1080p" in pregunta.lower():
        requerimientos["uso"] = "1080p" 
    elif "4k" in pregunta.lower():
        requerimientos["uso"] = "4k"
    return requerimientos # Es el paso que traduce la intencion del usuario del lenguaje humano a un conjunto de datos procesables por la base de datos

# Se conecta la base de datos donde estan todos los campos
def compatibilidad_db(conexion: sqlite3.Connection, actual_modelo: str) -> Optional[Dict[str, str]]:
    
    cursordb = conexion.cursor()

    sql_check = "SELECT socket, tipo_ram FROM componentesPC WHERE modelo LIKE ?"
    
    # Preparamos el dato con los comodines % para que busque coincidencias parciales
    parametro = ('%' + actual_modelo + '%',)
    
    cursorb = conexion.cursor()
    cursorb.execute(sql_check, parametro)
    
    # IMPORTANTE: Definir resultado para que no falle si no encuentra nada
    resultado = cursorb.fetchone()
    
    if resultado:
        # Devolvemos un diccionario para usarlo facil despues
        return {'socket': resultado[0], 'tipo_ram': resultado[1]}
    else:
        return None
    
def recomendacion_db(conexion: sqlite3.Connection, requerimientos: Dict[str, Optional[str]]) -> str:
# Genera una consulta SQL para recomendar el mejor componente basado en los requerimientos PLN.
    tipo = requerimientos.get("tipo_componente")
    uso = requerimientos.get("uso")
    actual_modelo = requerimientos.get("modelo_especifico")
    sql_consulta = None

    # 1Actualizacion de componente especifico (Recomendacion de Compatibilidad)
    if actual_modelo and tipo in ('Cpu', 'Gpu', 'Ram', 'PlacaMadre', 'FuentePoder'): # Se asegura que el usuario haya mencionado un componente de hardware existente, tambien se ejecuta solo cuando la funcion analisis pregunta haya identificado un modelo especifico
        compatibilidad = compatibilidad_db(conexion, actual_modelo) # Llama a la funcion y esta va a la base de datos y busca el actual modelo y devuelve el socket y su tipo de ram

        if not compatibilidad: # Si la funcion anterior no se cumple, termina la recomendacion 
            return f"No encuentro detalles de compatibilidad del componente '{actual_modelo}' en la base de datos."

        if tipo == 'Cpu': # Al usuario preguntar por Cpu, necesitara una placa madre compatible con su socket
            sql_consulta = f"""
                                SELECT modelo, precio, socket FROM componentesPC
                                WHERE tipo = 'PlacaMadre' AND socket = ? 
                                ORDER BY precio DESC LIMIT 1
                           """
            cursordb = conexion.cursor()
            cursordb.execute(sql_consulta, (compatibilidad['socket'],))
            resultado = cursordb.fetchone() # Intenta recuperar la placa madre mas potente y compatible
            if resultado:                                                                                                                                  # El simbolo de la moneda y 1f te dira las decimales del precio      
                return f"Debido a tu {actual_modelo} (socket {compatibilidad['socket']}), te recomiendo una Placa Madre compatible, como la {resultado[0]} por ${resultado[1]:.1f}."
            return f"No encuentro Placa Madre compatibles con el socket {compatibilidad['socket']} de tu {actual_modelo}."
        
        elif tipo == 'Gpu':
            sql_consulta = f"""
                                SELECT modelo, precio FROM componentesPC
                                WHERE tipo = 'Gpu'
                                ORDER BY precio DESC LIMIT 1
                            """
            cursordb = conexion.cursor()
            cursordb.execute(sql_consulta)
            resultado = cursordb.fetchone()
            if resultado:                                                                                                      
                return f"Para mejorar tu {actual_modelo}, la mejor Gpu en venta es la {resultado[0]} por ${resultado[1]:.1f}."
            return "No hay Gpus disponibles en mi base de datos para ti"
        
        elif tipo == 'Ram':
            sql_consulta = f"""
                                SELECT modelo, precio FROM componentesPC
                                WHERE tipo = 'Ram' AND tipo_ram = ?
                                ORDER BY potencia_w DESC LIMIT 1
                            """ 
            cursordb = conexion.cursor()
            cursordb.execute(sql_consulta, (compatibilidad['tipo_ram'],))
            resultado = cursordb.fetchone()
            if resultado:                                                                                                       
                return f"Con tu {actual_modelo} ({compatibilidad['tipo_ram']}), te recomiendo una memoria Ram {resultado[0]} por ${resultado[1]:.1f}."
            return f"No pude encontrar Ram tipo {compatibilidad['tipo_ram']} disponible para ti"
        
        elif tipo == 'PlacaMadre':
            sql_consulta = "SELECT modelo, precio FROM componentesPC WHERE tipo = 'PlacaMadre' AND socket = ? ORDER BY precio DESC LIMIT 1"
        cursordb = conexion.cursor()
        cursordb.execute(sql_consulta, (compatibilidad['socket'],))
        resultado = cursordb.fetchone()
        if resultado:
            return f"Debido a tu {actual_modelo} (socket {compatibilidad['socket']}), te recomiendo una Placa Madre compatible, como la {resultado[0]} por ${resultado[1]:.1f}."
        return f"No encuentro Placa Madre compatible con el socket {compatibilidad['socket']} de tu {actual_modelo}."
    
    # 2A partir de este punto, en base al uso que le dara al usuario, osea, si pone 4k, buscara lo mas caro para el        
    elif uso: # Si pone 1080p o Gaming o Edicion, buscara algo mas economico o equilibrado
        sql_consulta = None
        uso_str = str(uso).lower()

        if '4k' in uso_str or 'ultra' in uso_str:
            sql_consulta = "SELECT nombre, estimacion_minima FROM construccionPC ORDER BY estimacion_minima DESC LIMIT 1"
        elif 'edicion' in uso_str or 'edición' in uso_str or 'trabajo' in uso_str or 'diseño' in uso_str:
            sql_consulta = "SELECT nombre, estimacion_minima FROM construccionPC WHERE nombre LIKE '%workstation%' LIMIT 1"
        elif 'gaming' in uso_str or '1080p' in uso_str or 'entrada' in uso_str:
            sql_consulta = "SELECT nombre, estimacion_minima FROM construccionPC ORDER BY estimacion_minima ASC LIMIT 1"    
        else:
            sql_consulta = "SELECT nombre, estimacion_minima FROM construccionPC ORDER BY estimacion_minima ASC LIMIT 1"

        if sql_consulta is not None:
            cursordb = conexion.cursor()
            cursordb.execute(sql_consulta)
            resultado = cursordb.fetchone()

        if resultado:
            return f"Para un uso de {uso}, te recomiendo el emsamble {resultado[0]} con un costo aproximado o mayor de ${resultado[1]:.2f}, Esta build esta optimizada para el uso que le daras"
        else:
            return "No tengo emsambles diseñados para lo que exiges"
    else:
            return "Buenas, si quieres mejorar tu dispositivo, dime los componentes que buscas (Gpu, Cpu) o el uso que piensas darle (Gaming 1080p, Edicion, lo que sea)"
        
def respuesta_botsito(pregunta: str) -> str: # Esta funcion es primordial ya que en ella se recibe la pregunta y regresa la respuesta
    conexion = conectar_db()
    if conexion is None:
        return "No se pudo conectar a la base de datos, el que este leyendo esto, revisa el codigo para ver que falloxd"
    requerimientos = analisis_pregunta(pregunta)

    respuesta = recomendacion_db(conexion, requerimientos)
    conexion.close()
    return respuesta
                                
# Llegados a este punto, __name__ sera el bloque principal por el cual se ejecutara el codigo, como en la base de datos
if __name__ == '__main__':
    print ("🤖 Chatbot de recomendacion de componentes para tu PC para que ganes en tus jueguitos, si ya no quieres nada, escribe 'salir' ")
    pln = spacy.load("es_core_news_sm")
    print (f"Ha cargado el spacy: {pln.meta['name']}") 

while True:
        ingresar_usuario = input("Tu:")
        if ingresar_usuario.lower() == 'salir':
            break
        
        # Aqui se llama a la logica completa del chatbot de la funcion respuesta_botsito y a raiz de ahi se obtiene la respuesta 
        respuesta = respuesta_botsito(ingresar_usuario)
        # Se muestra la respuesta del Chatbot al usuario
        print (f"Chatbot: {respuesta}")
