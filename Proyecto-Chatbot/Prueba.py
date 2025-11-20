import spacy

# Asegúrate de que el modelo esté cargado
nlp = spacy.load('es_core_news_sm')

# 1. Frase de prueba
frase = "Necesito unos zapatos deportivos en la talla cuarenta y dos."
doc = nlp(frase)

print("--- Lematización y POS Tagging ---")
for token in doc:
    # 2. Imprime la palabra, su forma base, y su etiqueta POS
    print(f"Palabra: {token.text}, Base: {token.lemma_}, Tipo: {token.pos_}")

print("\n--- Extracción de Entidades (NER) ---")
# 3. Itera sobre las entidades (NER)
for ent in doc.ents:
    print(f"Entidad: {ent.text}, Tipo: {ent.label_}")
    