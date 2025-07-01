-- SE CREAN LAS TABLAS
CREATE TABLE usuarios (
	id_usuario SERIAL PRIMARY KEY, -- INCREMENTAL > SERIAL / SI SE LE PONE UUID ES INCREMENTAL AUTOMATICAMENTE
	email VARCHAR(50) UNIQUE NOT NULL, -- 50 CARACTERES//EMAIL UNICO // NO NULO
	nombre VARCHAR(50) NOT NULL,
	fecha_nacimiento DATE,
	pais VARCHAR(50)
);

SELECT * FROM usuarios;

CREATE TABLE peliculas (
	id_pelicula SERIAL PRIMARY KEY,
	titulo VARCHAR(150) UNIQUE NOT NULL,
	genero VARCHAR(50),
	duracion INT
);

SELECT * FROM peliculas;

CREATE TYPE modo_visualizacion_enum AS ENUM ('ONLINE', 'DESCARGADA');

CREATE TABLE alquileres (
	id_alquiler SERIAL PRIMARY KEY,
	id_usuario INTEGER NOT NULL REFERENCES usuarios (id_usuario), -- HACEMOS REFERENCIA A LA TABLA USUARIOS ID 
	-- id_usuario INTEGER NOT NULL REFERENCES usuarios(id_usuario) > PARA QUE APAREZCA EL NOMBRE DEL USUARIO EN VEZ DEL ID
	id_pelicula INTEGER NOT NULL REFERENCES peliculas (id_pelicula), -- HACEMOS REFERENCIA A LA TABLA PELICULAS ID
	fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- PARA QUE TOME AUTOMATICAMENTE LA FECHA
	precio DECIMAL (10,2), -- (10, 2) HASTA 10 NROS (INCLUYENDO DECIMALES) + 2 DECIMALES
	modo_visualizacion modo_visualizacion_enum NOT NULL -- nombre columna > tipo de dato > no nulo
);

SELECT * FROM alquileres;


-- SE AGREGAN LOS DATOS
INSERT INTO usuarios (email, nombre, fecha_nacimiento, pais) VALUES -- para pasar los valores
	('ana@gmail.com', 'Ana López', '1995-03-12', 'Argentina'),
	('marcos@mail.com', 'Marcos Díaz', '1988-07-21', 'Chile');
	
INSERT INTO peliculas (titulo, genero, duracion) VALUES
	('Matrix', 'Ciencia Ficción', 136),
	('El Padrino', 'Drama', 175);
	
INSERT INTO alquileres (id_usuario, id_pelicula, precio, modo_visualizacion) VALUES
	(1, 1, 450.00, 'ONLINE'),
	(2, 2, 550.00, 'DESCARGADA');

-- AGREGAR OTRO USUARIO
INSERT INTO usuarios (email, nombre, fecha_nacimiento, pais) VALUES -- para pasar los valores
	('pablo@gmail.com', 'Pablo Colleti', '1990-07-21', 'Uruguay');
	




