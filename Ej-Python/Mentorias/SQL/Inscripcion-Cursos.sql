--CREAMOS LAS TABLAS
CREATE TABLE usuarios (
	id_usuario SERIAL PRIMARY KEY,
	nombre VARCHAR(50),
	email VARCHAR(50) UNIQUE NOT NULL,
	pais VARCHAR(50)
);

SELECT * FROM usuarios;

CREATE TABLE cursos (
	id_curso SERIAL PRIMARY KEY,
	titulo VARCHAR(50) NOT NULL,
	categoria VARCHAR(50) NOT NULL,
	duracion_hs INTEGER NOT NULL
);

SELECT * FROM cursos;

CREATE TYPE medio_pago_enum AS ENUM ('TRANSFERENCIA', 'TARJETA DE CREDITO');

CREATE TABLE inscripciones (
	id_inscripcion SERIAL PRIMARY KEY,
	id_usuario INTEGER NOT NULL REFERENCES usuarios(id_usuario),
	id_curso INTEGER NOT NULL REFERENCES cursos(id_curso),
	fecha_inscripcion DATE,
	medio_pago medio_pago_enum NOT NULL
);

SELECT * FROM inscripciones;

-- SE AGREGAN LOS DATOS
INSERT INTO usuarios (nombre, email, pais) VALUES
	('Sofia Prodanov','sofia@gmail.com', 'Argentina'),
	('Lautaro Moreyra', 'lautaro@gmail.com', 'Argentina');

INSERT INTO cursos (titulo, categoria, duracion_hs) VALUES
	('Python','Programacion', 40),
	('Chef', 'Cocina', 50);

INSERT INTO inscripciones (id_usuario, id_curso, fecha_inscripcion, medio_pago) VALUES
	(1, 1, '2025/07/04', 'TRANSFERENCIA'),
	(2, 2, '2025/07/05', 'TARJETA DE CREDITO');

-- AGREGO MAS DATOS
INSERT INTO usuarios (nombre, email, pais) VALUES
	('Nadia Prodanov','nadia@gmail.com', 'Argentina');

INSERT INTO cursos (titulo, categoria, duracion_hs) VALUES
	('Ninez','Psicologia', 40);

INSERT INTO inscripciones (id_usuario, id_curso, fecha_inscripcion, medio_pago) VALUES
	(3, 3, '2025/07/06', 'TRANSFERENCIA');