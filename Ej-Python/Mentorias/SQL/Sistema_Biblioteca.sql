--CREAMOS LAS TABLAS
CREATE TABLE socios (
	id_socio SERIAL PRIMARY KEY,
	nombre VARCHAR(50),
	dni INTEGER UNIQUE NOT NULL
);

SELECT * FROM socios;

CREATE TABLE libros (
	id_libro SERIAL PRIMARY KEY,
	titulo VARCHAR(50) NOT NULL,
	autor VARCHAR(50) NOT NULL,
	categoria VARCHAR(50) NOT NULL
);

SELECT * FROM libros;

CREATE TABLE retiros (
	id_retiro SERIAL PRIMARY KEY,
	id_socio INTEGER NOT NULL REFERENCES socios(id_socio),
	id_libro INTEGER NOT NULL REFERENCES libros(id_libro)
);

SELECT * FROM retiros;

-- SE AGREGAN LOS DATOS
INSERT INTO socios (nombre, dni) VALUES
	('Sofia Prodanov','12312123'),
	('Lautaro Moreyra', '45665455');

INSERT INTO libros (titulo, autor, categoria) VALUES
	('Cuentos de Terror para Franco','Hugo Mitoire', 'Terror'),
	('Las Mujeres que Aman Demasiado', 'Robin Norwood', 'Autoayuda');

INSERT INTO retiros (id_socio, id_libro) VALUES
	(2, 1),
	(1, 2);

