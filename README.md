# Biocerto.AI RAG

Sistema chatbot intelligente con Retrieval-Augmented Generation per rispondere su prodotti certificati Biocerto e fonti scientifiche.

## Deploy su Render

1. Crea un Web Service su https://render.com
2. Collegalo a questo repo GitHub
3. Imposta:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python main.py`
4. Nella sezione Environment:
   - `OPENAI_API_KEY = la tua chiave OpenAI`
5. Carica i PDF dei certificati nella cartella `data/`
