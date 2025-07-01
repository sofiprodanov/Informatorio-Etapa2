CREATE TABLE posts (
	id SERIAL PRIMARY KEY,
	Titulo VARCHAR(200) NOT NULL,
	contenido TEXT NOT NULL,
	fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM posts;

CREATE TABLE usuarios (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL, 
	email VARCHAR(100) UNIQUE NOT NULL,
	contrasenia VARCHAR(255) NOT NULL
);

INSERT INTO usuarios (nombre, email, contrasenia)
VALUES 
	('Sofia', 'sofia@gmailfalso.com', 'facil123'),
	('Elias', 'elias@gmailfalso.com', 'refacil123');

SELECT * FROM usuarios;

ALTER TABLE posts
ADD COLUMN usuario_id INT REFERENCES usuarios(id);

-- INSERTAR POST EN LA TABLA POST
INSERT INTO posts (titulo, contenido)
VALUES 
	('Primer Post', 'La vida como programador'),
	('Segundo Post', 'Agarrini la palini');

ALTER TABLE posts
ALTER COLUMN usuario_id SET NOT NULL;

UPDATE posts
SET usuario_id = 2
WHERE id = 1;

UPDATE posts
SET usuario_id = 2
WHERE id = 2;

-- INSERTAR POST EN LA TABLA POST
INSERT INTO posts (titulo, contenido, usuario_id)
VALUES 
	('Tercer Post', 'La vida como programador II', 1);

CREATE TYPE user_status_enum AS ENUM ('ACTIVO', 'INACTIVO', 'PENDIENTE'); 

ALTER TABLE usuarios
ADD COLUMN estado user_status_enum DEFAULT 'PENDIENTE'; -- que sea de tipo user_status_enu






