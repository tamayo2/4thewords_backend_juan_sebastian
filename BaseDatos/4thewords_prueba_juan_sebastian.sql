CREATE DATABASE IF NOT EXISTS 4thewords_prueba_juan_sebastian;
USE 4thewords_prueba_juan_sebastian;

CREATE TABLE IF NOT EXISTS leyendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    image_url TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    province VARCHAR(100) NOT NULL,
    canton VARCHAR(100) NOT NULL,
    district VARCHAR(100) NOT NULL
);

INSERT INTO leyendas (name, category, description, image_url, created_at, province, canton, district) VALUES
('El Cadejos', 'Leyenda Costarricense', 'El Cadejos es un perro espectral que aparece en las noches para asustar a los borrachos y guiar a las personas perdidas.', 'https://wallpapercave.com/wp/wp6074813.jpg', '1880-01-01 00:00:00', 'San José', 'Central', 'San José'),
('El Cuijen y la Pelona', 'Leyenda Costarricense', 'El Cuijen es un animal mitológico que vive en el monte y la Pelona es la muerte personificada que se aparece para llevarse a las almas.', 'https://artfiles.alphacoders.com/146/thumb-1920-146789.jpg', '1700-01-01 00:00:00', 'Alajuela', 'San Carlos', 'Florencia'),
('El Diablo Chingo', 'Leyenda Costarricense', 'El Diablo Chingo es una figura demoníaca que se aparece en caminos solitarios, creando caos y confundiendo a los viajeros.', 'https://artfiles.alphacoders.com/424/thumb-1920-42490.jpg', '1900-01-01 00:00:00', 'Puntarenas', 'Central', 'Puntarenas'),
('El Dueño del Monte', 'Leyenda Costarricense', 'El Dueño del Monte es un hombre misterioso que es dueño de todo lo que ocurre en el bosque, controlando a los animales y personas que lo atraviesan.', 'https://picfiles.alphacoders.com/465/thumb-1920-465252.jpg', '1800-01-01 00:00:00', 'Cartago', 'Turrialba', 'Turrialba'),
('El Mico Malo', 'Leyenda Costarricense', 'El Mico Malo es una criatura maligna con aspecto de mono, que aterroriza a las personas en los bosques costarricenses.', 'https://images6.alphacoders.com/135/thumb-1920-1352224.jpeg', '1850-01-01 00:00:00', 'Heredia', 'Barva', 'Barva'),
('El Padre sin Cabeza', 'Leyenda Costarricense', 'Un sacerdote que fue asesinado y cuya cabeza nunca apareció. Se dice que su espíritu aún vaga por las noches buscando venganza.', 'https://picfiles.alphacoders.com/464/thumb-1920-464007.jpg', '1900-01-01 00:00:00', 'San José', 'Escazú', 'Escazú'),
('El Sisimiqui', 'Leyenda Costarricense', 'El Sisimiqui es un ser mítico que se dice habita en las montañas y actúa como guardián, protegiendo las tierras y las personas de intrusos.', 'https://picfiles.alphacoders.com/463/thumb-1920-463041.jpg', '1930-01-01 00:00:00', 'Puntarenas', 'Coto Brus', 'Canoas'),
('La Carreta sin Bueyes', 'Leyenda Costarricense', 'Una carreta vieja, sin bueyes, que deambula por las noches, arrastrando cadenas y aterrorizando a los pueblos.', 'https://picfiles.alphacoders.com/462/thumb-1920-462393.jpg', '1800-01-01 00:00:00', 'Guanacaste', 'Liberia', 'Liberia'),
('La Cegua', 'Leyenda Costarricense', 'La Cegua es una mujer que se transforma en una criatura horrenda, buscando venganza contra los hombres que la deseen.', 'https://images5.alphacoders.com/133/thumb-1920-1337139.png', '1850-01-01 00:00:00', 'San José', 'Central', 'San José'),
('La Llorona', 'Leyenda Costarricense', 'Una mujer que llora por la pérdida de sus hijos, deambulando por las noches buscando almas para reemplazar los suyos.', 'https://images4.alphacoders.com/134/thumb-1920-1345123.jpeg', '1600-01-01 00:00:00', 'Heredia', 'San Rafael', 'San Rafael');

