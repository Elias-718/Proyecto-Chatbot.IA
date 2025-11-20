# Tokenizacion: Divide el texto en tokens
# Los tokens son unidades individuales de un texto, por ejemplo las palabras son tokens en un proceso de tokens basado en palabras
# Puede estar basada en palabras (casa, perro, etc)
# Basada en caracteres (a, d, 7, $, etc)
# Basada en sub-palabras (automóvil => auto, móvil)
# Consideraciones: Diferentes casos de letras (tildes por ejemplo)
# Tokenizar por palabras completas, caracteres, o sub-palabras
# Puntuacion (parte de la palbra o token separado)

texto = "Hola, ¿Cómo estás?"
tokens = texto.split()
print (tokens)

# Manejo de los casos de las letras (mayusculas y minusculas)
# La palabra "Hola" no es la misma que "hola para una maquina"
texto = "Hola, ¿Cómo estás?"
texto = texto.lower()
print (texto)
tokens = texto.split()
print (tokens)



# Stop Words o Palabras en parada: Son palabras de uso comun excluidas de las tareas de procesamiento de textos
# Por ejemplo al ejecutar desde este punto, el texto solo mostrara las palabras gato, negro, perro, blanco. Excluyendo "El", "es", "y", "el" al ser palabras comunes
# Dicho de otra forma, son palabras como articulos, pronombres y preposiciones, no se añaden al diccionario de busqueda, palabras que aparecen con frecuencia y aportando poco a la oracion
texto = "El gato es negro y el perro es blanco"

import nltk #Importamos la libreria nltk
nltk.download('stopwords')
nltk.download('punkt_tab')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words("spanish"))
print (stop_words)

texto = texto.lower()
tokens = word_tokenize(texto)
texto_filtrado = [word for word in tokens if not word in stop_words]
print(texto_filtrado)



# Stemming y Lematizacion:
# El stemming es una tecnica mas simple que elimina los sufijos de las palabras, ejemplo "caminar", "caminando" y "camina" se convierten simplemente en "caminar" mejorando resultados
# La lematizacion es una tecnica mas sofisticada que utiliza las reglas del lenguaje para obtener la base o raiz de una palabra
import nltk
nltk.download('wordnet')
from nltk.stem import SnowballStemmer

# Crear el stemmer en español
stemmer = SnowballStemmer('spanish')

# Probarlo en la palabra "caminar"
print(stemmer.stem('caminando'))
print(stemmer.stem('caminar'))
print(stemmer.stem('caminó'))

import spacy # Lo descargue desde GitBash con python3 -m pip install spacy y luego python3 -m spacy download es_core_news_sm para que este en español

# Cargar el modelo en español
nlp = spacy.load('es_core_news_sm')
# Crear un documento
doc = nlp("caminar caminando caminó")
# Imprimir el texto y el lema de cada token
for token in doc:
    print(token.text, "->", token.lemma_)
# Particularidades de Lematizacion y recomendaciones para su uso:
# La lematizacion puede ser mas efectiva que el stemming pero tambien es mas costosa computacionalmente
# El uso de lematizacion puede requerir el etiquetado previo

# Aplicaciones de Stemming y lematizacion en situaciones reales:
# Asistentes virtuales y chatbots, analisis de sentimientos, motores de busqueda, sistema de recomendacion, aplicaciones en publicidad online y etiquetas en redes sociales







