from fastapi.testclient import TestClient
from app.main import app
from app.models import Leyenda
from app.database import create_db_and_tables
from sqlmodel import Session

client = TestClient(app)


create_db_and_tables()

def test_create_leyenda():
    leyendas = [
        {
            "image_url": "https://wallpapercave.com/wp/wp6074813.jpg",
            "name": "El Cadejos",
            "category": "Leyenda Costarricense",
            "description": "El Cadejos es un perro espectral que aparece en las noches para asustar a los borrachos y guiar a las personas perdidas.",
            "created_at": "1880-01-01T00:00:00",
            "province": "San José",
            "canton": "Central",
            "district": "San José"
        },
        {
            "image_url": "https://artfiles.alphacoders.com/146/thumb-1920-146789.jpg",
            "name": "El Cuijen y la Pelona",
            "category": "Leyenda Costarricense",
            "description": "El Cuijen es un animal mitológico que vive en el monte y la Pelona es la muerte personificada que se aparece para llevarse a las almas.",
            "created_at": "1700-01-01T00:00:00",
            "province": "Alajuela",
            "canton": "San Carlos",
            "district": "Florencia"
        },
        {
            "image_url": "https://artfiles.alphacoders.com/424/thumb-1920-42490.jpg",
            "name": "El Diablo Chingo",
            "category": "Leyenda Costarricense",
            "description": "El Diablo Chingo es una figura demoníaca que se aparece en caminos solitarios, creando caos y confundiendo a los viajeros.",
            "created_at": "1900-01-01T00:00:00",
            "province": "Puntarenas",
            "canton": "Central",
            "district": "Puntarenas"
        },
        {
            "image_url": "https://picfiles.alphacoders.com/465/thumb-1920-465252.jpg",
            "name": "El Dueño del Monte",
            "category": "Leyenda Costarricense",
            "description": "El Dueño del Monte es un hombre misterioso que es dueño de todo lo que ocurre en el bosque, controlando a los animales y personas que lo atraviesan.",
            "created_at": "1800-01-01T00:00:00",
            "province": "Cartago",
            "canton": "Turrialba",
            "district": "Turrialba"
        },
        {
            "image_url": "https://images6.alphacoders.com/135/thumb-1920-1352224.jpeg",
            "name": "El Mico Malo",
            "category": "Leyenda Costarricense",
            "description": "El Mico Malo es una criatura maligna con aspecto de mono, que aterroriza a las personas en los bosques costarricenses.",
            "created_at": "1850-01-01T00:00:00",
            "province": "Heredia",
            "canton": "Barva",
            "district": "Barva"
        },
        {
            "image_url": "https://picfiles.alphacoders.com/464/thumb-1920-464007.jpg",
            "name": "El Padre sin cabeza",
            "category": "Leyenda Costarricense",
            "description": "Un sacerdote que fue asesinado y cuya cabeza nunca apareció. Se dice que su espíritu aún vaga por las noches buscando venganza.",
            "created_at": "1900-01-01T00:00:00",
            "province": "San José",
            "canton": "Escazú",
            "district": "Escazú"
        },
        {
            "image_url": "https://picfiles.alphacoders.com/463/thumb-1920-463041.jpg",
            "name": "El Sisimiqui",
            "category": "Leyenda Costarricense",
            "description": "El Sisimiqui es un ser mítico que se dice habita en las montañas y actúa como guardián, protegiendo las tierras y las personas de intrusos.",
            "created_at": "1930-01-01T00:00:00",
            "province": "Puntarenas",
            "canton": "Coto Brus",
            "district": "Canoas"
        },
        {
            "image_url": "https://picfiles.alphacoders.com/462/thumb-1920-462393.jpg",
            "name": "La Carreta sin Bueyes",
            "category": "Leyenda Costarricense",
            "description": "Una carreta vieja, sin bueyes, que deambula por las noches, arrastrando cadenas y aterrorizando a los pueblos.",
            "created_at": "1800-01-01T00:00:00",
            "province": "Guanacaste",
            "canton": "Liberia",
            "district": "Liberia"
        },
        {
            "image_url": "https://images5.alphacoders.com/133/thumb-1920-1337139.png",
            "name": "La Cegua",
            "category": "Leyenda Costarricense",
            "description": "La Cegua es una mujer que se transforma en una criatura horrenda, buscando venganza contra los hombres que la deseen.",
            "created_at": "1850-01-01T00:00:00",
            "province": "San José",
            "canton": "Central",
            "district": "San José"
        },
        {
            "image_url": "https://images4.alphacoders.com/134/thumb-1920-1345123.jpeg",
            "name": "La Llorona",
            "category": "Leyenda Costarricense",
            "description": "Una mujer que llora por la pérdida de sus hijos, deambulando por las noches buscando almas para reemplazar los suyos.",
            "created_at": "1600-01-01T00:00:00",
            "province": "Heredia",
            "canton": "San Rafael",
            "district": "San Rafael"
        },
        {
            "image_url": "https://images6.alphacoders.com/133/thumb-1920-1338169.png",
            "name": "La Procesión de las Animas",
            "category": "Leyenda Costarricense",
            "description": "Se dice que las almas de los muertos caminan en una procesión nocturna, buscando redención.",
            "created_at": "1700-01-01T00:00:00",
            "province": "Cartago",
            "canton": "Cartago",
            "district": "Cartago"
        },
        {
            "image_url": "https://picfiles.alphacoders.com/323/thumb-1920-323363.jpg",
            "name": "La Tulevieja",
            "category": "Leyenda Costarricense",
            "description": "Una mujer que aparece en las orillas de los ríos, pidiendo ayuda y luego atrapando a los incautos en el agua.",
            "created_at": "1900-01-01T00:00:00",
            "province": "Alajuela",
            "canton": "San Carlos",
            "district": "La Fortuna"
        },
    ]
    
    for leyenda in leyendas:
        response = client.post("/leyendas/", json=leyenda)
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert "created_at" in data

def test_read_leyendas():
    response = client.get("/leyendas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_leyenda():
    leyenda_data = {
        "image_url": "https://wallpapercave.com/wp/wp6074813.jpg",
        "name": "El Cadejos",
        "category": "Leyenda Costarricense",
        "description": "Actualización de descripción del Cadejos.",
        "created_at": "1880-01-01T00:00:00",
        "province": "San José",
        "canton": "Central",
        "district": "San José"
    }
    create_response = client.post("/leyendas/", json=leyenda_data)
    leyenda_id = create_response.json()["id"]

    updated_data = {
        "name": "Espantos",
        "description": "Tienen un origen antiguo, muchas veces con raíces precolombinas, originados en mitos indígenas",
        "image_url": "https://images2.alphacoders.com/722/thumb-1920-72270.jpg",
        "category": "Leyenda Costarricense",
        "created_at": "1880-01-01T00:00:00",
        "province": "San José",
        "canton": "Central",
        "district": "San José"
    }
    response = client.put(f"/leyendas/{leyenda_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Espantos"

def test_delete_leyenda():
    leyenda_data = {
        "image_url": "https://artfiles.alphacoders.com/424/thumb-1920-42490.jpg",
        "name": "El Diablo Chingo",
        "category": "Leyenda Costarricense",
        "description": "Descripción del Diablo Chingo.",
        "created_at": "1900-01-01T00:00:00",
        "province": "Puntarenas",
        "canton": "Central",
        "district": "Puntarenas"
    }
    create_response = client.post("/leyendas/", json=leyenda_data)
    leyenda_id = create_response.json()["id"]

    response = client.delete(f"/leyendas/{leyenda_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Leyenda eliminada con éxito"}


