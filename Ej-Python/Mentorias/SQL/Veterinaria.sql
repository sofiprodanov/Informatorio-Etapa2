--CREAMOS LAS TABLAS
CREATE TABLE duenos (
	id_dueno SERIAL PRIMARY KEY,
	nombre VARCHAR(50),
	dni INTEGER UNIQUE NOT NULL
);

SELECT * FROM duenos;

CREATE TABLE mascotas (
	id_mascota SERIAL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	especie VARCHAR(50) NOT NULL,
	edad INTEGER NOT NULL
);

SELECT * FROM mascotas;

CREATE TABLE tienen (
	id_tiene SERIAL PRIMARY KEY,
	id_dueno INTEGER NOT NULL REFERENCES duenos(id_dueno),
	id_mascota INTEGER NOT NULL REFERENCES mascotas(id_mascota)
);

SELECT * FROM tienen;

-- SE AGREGAN LOS DATOS
INSERT INTO duenos (nombre, dni) VALUES
	('Sofia Prodanov','12312123'),
	('Lautaro Moreyra', '45665455');

INSERT INTO mascotas (nombre, especie, edad) VALUES
	('Milo','Perro', '4'),
	('Pupi', 'Perro', '3');

INSERT INTO tienen (id_dueno, id_mascota) VALUES
	(1, 1),
	(2, 2);

-- SE AGREGAN LOS DATOS
INSERT INTO duenos (nombre, dni) VALUES
	('Silvia Quarin', '78978879');

INSERT INTO mascotas (nombre, especie, edad) VALUES
	('Moro','Gato', '9');

INSERT INTO tienen (id_dueno, id_mascota) VALUES
	(3, 3);
