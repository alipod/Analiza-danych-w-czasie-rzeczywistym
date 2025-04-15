# Analiza-danych-w-czasie-rzeczywistym

## Zadanie 1

Model - regula decyzyjna

## Użycie 

1. Zbuduj obraz Dockera

docker build -t zadanie1 .

2. Uruchom kontener

docker run -p 5000:5000 zadanie1

3. Aby uzyskać prognozę wyślij żądanie GET do:

get localhost:5000/api/v1.0/predict?a=5&b=4

    Wynik:
        ("prediction": 1,
        "features": {
            "a": 5.0,
            "b": 4.0,
            "sum": 9.0}

