CREATE DATABASE IF NOT EXISTS 4thewords_prueba_juan_sebastian;
USE 4thewords_prueba_juan_sebastian;

CREATE TABLE IF NOT EXISTS leyendas (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(255) NOT NULL,
    category    VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    image_url   TEXT NOT NULL,
    created_at  DATETIME NOT NULL,
    province    VARCHAR(100) NOT NULL,
    canton      VARCHAR(100) NOT NULL,
    district    VARCHAR(100) NOT NULL
);

INSERT INTO leyendas (name, category, description, image_url, created_at, province, canton, district)
VALUES
    ('El Cadejos', 'Leyenda Costarricense',
    'El Cadejo es un espiritu o fantasma en forma de perro que aparece en las noches para cuidar o atormentar a los borrachos o trasnochadores.',
    'https://th.bing.com/th/id/OIP.ctUdPgo7KcIj-P5rG1aYDQHaEK?rs=1&pid=ImgDetMain', '1880-01-01 00:00:00', 'San José', 'Central', 'San José'),

    ('El Cuijen y la Pelona', 'Leyenda Costarricense',
    'El Cuijen es un espiritu maligno del folclore colombiano que asusta con su silbido, y La Pelona es la personificacion de la muerte como un esqueleto con tunica.',
    'https://i.pinimg.com/736x/06/25/92/062592dc4927183f07bb6614c1c24bd6.jpg', '1700-01-01 00:00:00', 'Alajuela', 'San Carlos', 'Florencia'),

    ('El Diablo Chingo', 'Leyenda Costarricense',
    'El Diablo Chingo es una figura del folclore costarricense representada como un diablo sin cuernos que castiga a los jugadores tramposos y borrachos, apareciendose en forma de un hombre misterioso para darles su merecido.',
    'https://i.pinimg.com/originals/e2/5f/68/e25f68e7296ef7db46eec89e3f8f5e4b.jpg', '1900-01-01 00:00:00', 'Puntarenas', 'Central', 'Puntarenas'),

    ('El Dueño del Monte', 'Leyenda Costarricense',
    'El Dueño del Monte es un hombre misterioso que es dueño de todo lo que ocurre en el bosque, controlando a los animales y personas que lo atraviesan.',
    'https://live.staticflickr.com/7064/6794621292_c3234d90d4_b.jpg', '1800-01-01 00:00:00', 'Cartago', 'Turrialba', 'Turrialba'),

    ('El Mico Malo', 'Leyenda Costarricense',
    'El Mico Malo es una criatura maligna con aspecto de mono, que aterroriza a las personas en los bosques costarricenses.',
    'https://th.bing.com/th/id/OIP.GaCocdIr6zFRb0I9xkBFkQHaHa?rs=1&pid=ImgDetMain', '1850-01-01 00:00:00', 'Heredia', 'Barva', 'Barva'),

    ('El Padre sin Cabeza', 'Leyenda Costarricense',
    'Un sacerdote que fue asesinado y cuya cabeza nunca aparecio. Se dice que su espiritu aun vaga por las noches buscando venganza.',
    'https://picfiles.alphacoders.com/464/thumb-1920-464007.jpg', '1900-01-01 00:00:00', 'San José', 'Escazú', 'Escazú'),

    ('El Sisimiqui', 'Leyenda Costarricense',
    'El Sisimiqui es un ser mitico que se dice habita en las montañas y actua como guardian, protegiendo las tierras y las personas de intrusos.',
    'https://picfiles.alphacoders.com/463/thumb-1920-463041.jpg', '1930-01-01 00:00:00', 'Puntarenas', 'Coto Brus', 'Canoas'),

    ('La Carreta sin Bueyes', 'Leyenda Costarricense',
    'Una carreta vieja, sin bueyes, que deambula por las noches, arrastrando cadenas y aterrorizando a los pueblos.',
    'https://picfiles.alphacoders.com/462/thumb-1920-462393.jpg', '1800-01-01 00:00:00', 'Guanacaste', 'Liberia', 'Liberia'),

    ('La Cegua', 'Leyenda Costarricense',
    'La Cegua es una mujer que se transforma en una criatura horrenda, buscando venganza contra los hombres que la deseen.',
    'https://images5.alphacoders.com/133/thumb-1920-1337139.png', '1850-01-01 00:00:00', 'San Jose', 'Central', 'San Jose'),

    ('La Llorona', 'Leyenda Costarricense',
    'Una mujer que llora por la perdida de sus hijos, deambulando por las noches buscando almas para reemplazar los suyos.',
    'https://th.bing.com/th/id/OIP.lp0VB5cpuZUymQf6jV6G9QHaE8?rs=1&pid=ImgDetMain', '1600-01-01 00:00:00', 'Heredia', 'San Rafael', 'San Rafael');

SELECT * FROM leyendas;