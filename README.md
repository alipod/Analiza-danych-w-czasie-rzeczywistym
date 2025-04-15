# Analiza-danych-w-czasie-rzeczywistym

## Zadanie 1

Model - regula decyzyjna

## Spis treści

- [Instalacja](#instalacja)
- [Użycie](#użycie)

## Instalacja

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/alipod/Analiza-danych-w-czasie-rzeczywistym.git

2. Przejdź do katalogu projektu:

  cd Analiza-danych-w-czasie-rzeczywistym

3. Zainstaluj wymagane zależności:

  pip install -r requirements.txt

4. Uruchom aplikację:

  python app.py

## Użycie

Aby uzyskać prognozę wyślij żądanie GET do:

http://localhost:5050/api/v1.0/predict?a=5&b=4

    Wynik:
        ("prediction": 1,
        "features": {
            "a": 5.0,
            "b": 4.0,
            "sum": 9.0}

