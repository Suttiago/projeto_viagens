from dotenv import load_dotenv
import os
import requests

load_dotenv()
hotel_api_key = os.getenv("API_KEY_HOTELS")

def pegar_hoteis():
    url = "https://serpapi.com/search"

# Parâmetros da requisição teste
    params = {
    "engine": "google_hotels",  
    "q":"mexico",
    "check_in_date": "2025-04-12",
    "check_out_date": "2025-04-13",
    "api_key": hotel_api_key
    }   

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 

        data = response.json()
        
        
        #array que vai listar os hoteis

        hotels = data.get("hoteis_reslults",[])
        hotel_list = []
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}") 


hoteis = pegar_hoteis()
for hotel in hoteis:
    print(hotel)