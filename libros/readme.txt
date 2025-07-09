-- #############################################################
-- # Script para crear la Base de Datos y Tablas para una      #
-- #         Biblioteca de Libros con Gestión de Usuarios      #
-- #############################################################

-- --- PASO 1: Creación de la Base de Datos (Opcional) ---
-- Descomenta la siguiente línea si necesitas crear la base de datos desde cero.
-- En muchos sistemas, crearás la BD desde el panel de control.

CREATE DATABASE IF NOT EXISTS biblioteca_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE biblioteca_db;


-- --- PASO 2: Creación de la Tabla de Usuarios ---
-- Esta tabla almacenará la información de los usuarios que pueden iniciar sesión.

CREATE TABLE usuarios (
    -- `id`: Identificador único y numérico para cada usuario. Es la clave primaria.
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- `nombre_usuario`: Nombre único que el usuario utilizará para iniciar sesión.
    -- `UNIQUE` asegura que no haya dos usuarios con el mismo nombre.
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    
    -- `email`: Correo electrónico del usuario, también debe ser único.
    email VARCHAR(100) NOT NULL UNIQUE,
    
    -- `password_hash`: Aquí se guardará la contraseña de forma segura (hasheada), NUNCA en texto plano.
    -- Usamos VARCHAR(255) para dar espacio suficiente a cualquier algoritmo de hashing (bcrypt, etc.).
    password_hash VARCHAR(255) NOT NULL,
    
    -- `fecha_registro`: Guarda la fecha y hora en que se creó la cuenta.
    -- `DEFAULT CURRENT_TIMESTAMP` establece automáticamente la fecha y hora actual al insertar un nuevo usuario.
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- `rol`: Define el tipo de usuario (ej. 'admin', 'miembro'). Útil para gestionar permisos.
    -- `DEFAULT 'miembro'` asigna este rol si no se especifica otro.
    rol VARCHAR(20) NOT NULL DEFAULT 'miembro'
);

-- Comentario: La contraseña NUNCA debe guardarse directamente. En tu aplicación (Python/Flask),
-- deberás usar una librería como `werkzeug.security` o `passlib` para generar y verificar el hash.


-- --- PASO 3: Creación de la Tabla de Libros ---
-- Esta tabla contendrá toda la información sobre los libros de la biblioteca.

CREATE TABLE libros (
    -- `id`: Identificador único y numérico para cada libro. Clave primaria.
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- `titulo`: Título del libro. Es un campo obligatorio.
    titulo VARCHAR(255) NOT NULL,
    
    -- `autor`: Nombre del autor del libro.
    autor VARCHAR(150),
    
    -- `editorial`: Nombre de la editorial.
    editorial VARCHAR(100),
    
    -- `anio_publicacion`: Año en que se publicó el libro. Usamos `INT` para 4 dígitos (ej. 2023).
    anio_publicacion INT,
    
    -- `isbn`: Código ISBN del libro. Es único para cada edición de un libro.
    -- Lo hacemos `UNIQUE` para evitar duplicados exactos.
    isbn VARCHAR(20) UNIQUE,
    
    -- `ubicacion_fisica`: Dónde se encuentra el libro físicamente (ej. 'Estantería A-3').
    ubicacion_fisica VARCHAR(100),
    
    -- `estado`: Condición actual del libro (ej. 'Disponible', 'Prestado', 'En reparación').
    -- `DEFAULT 'Disponible'` lo establece como disponible al agregarlo.
    estado VARCHAR(50) NOT NULL DEFAULT 'Disponible',
    
    -- `fecha_adquisicion`: Fecha en que el libro fue agregado a la biblioteca.
    fecha_adquisicion DATE,
    
    -- `id_usuario_registro`: Clave foránea que relaciona el libro con el usuario que lo registró.
    -- Esto nos permite saber qué usuario agregó cada libro al sistema.
    id_usuario_registro INT,
    
    -- Creamos la restricción de clave foránea.
    -- `ON DELETE SET NULL`: Si el usuario que registró el libro es eliminado, el campo
    -- `id_usuario_registro` en esta tabla se pondrá a `NULL` en lugar de borrar el libro.
    -- Esto mantiene la integridad de los datos de los libros.
    FOREIGN KEY (id_usuario_registro) REFERENCES usuarios(id) ON DELETE SET NULL
);


-- --- PASO 4: Creación de Índices para Optimizar Búsquedas ---
-- Los índices aceleran las operaciones de búsqueda (SELECT) en las columnas especificadas.
-- Son cruciales para el rendimiento a medida que las tablas crecen.

-- Índice en la tabla `usuarios` para la columna `email`.
-- Acelerará las búsquedas por email, por ejemplo, al verificar si un email ya está registrado.
CREATE INDEX idx_usuarios_email ON usuarios(email);

-- Índice en la tabla `libros` para la columna `titulo`.
-- La búsqueda por título será una de las operaciones más frecuentes.
CREATE INDEX idx_libros_titulo ON libros(titulo);

-- Índice en la tabla `libros` para la columna `autor`.
-- Útil si se implementa una funcionalidad de búsqueda por autor.
CREATE INDEX idx_libros_autor ON libros(autor);


-- --- PASO 5: Inserción de Datos de Ejemplo (Opcional) ---
-- Aquí puedes agregar un usuario administrador y algunos libros de ejemplo para probar.
-- Recuerda que el hash de la contraseña debe ser generado por tu aplicación.
-- Este es solo un ejemplo de HASH para 'admin_password'. ¡NUNCA USES ESTO EN PRODUCCIÓN!

INSERT INTO usuarios (nombre_usuario, email, password_hash, rol) VALUES
('admin', 'admin@biblioteca.com', 'pbkdf2:sha256:600000$....(hash generado por python)...', 'admin');

INSERT INTO libros (titulo, autor, editorial, anio_publicacion, isbn, ubicacion_fisica, id_usuario_registro) VALUES
('Cien Años de Soledad', 'Gabriel García Márquez', 'Sudamericana', 1967, '978-0307350438', 'Sección A-1', 1),
('1984', 'George Orwell', 'Secker & Warburg', 1949, '978-0451524935', 'Sección B-2', 1),
('El Señor de los Anillos', 'J.R.R. Tolkien', 'Allen & Unwin', 1954, '978-0618640157', 'Sección A-1', 1);

-- --- Fin del Script ---











-- --- PASO ADICIONAL: Creación de la Tabla de Préstamos ---
-- Esta tabla registrará las transacciones de préstamos, vinculando
-- un usuario de MySQL con un libro cuya información está en MongoDB.

USE biblioteca_db; -- Asegúrate de estar en la base de datos correcta

CREATE TABLE prestamos (
    -- `id`: Identificador único y numérico para cada préstamo.
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- `id_usuario`: Clave foránea que referencia al usuario que solicita el préstamo.
    -- Es un campo obligatorio, ya que todo préstamo debe tener un solicitante.
    id_usuario INT NOT NULL,
    
    -- `id_libro_mongo`: Aquí guardaremos el ObjectId del libro de MongoDB.
    -- Es un string porque el ObjectId de MongoDB es alfanumérico (ej: '65f1a2b3c4d5e6f7a8b9c0d1').
    -- Lo hacemos de 24 caracteres, que es la longitud estándar de un ObjectId.
    id_libro_mongo VARCHAR(24) NOT NULL,
    
    -- `titulo_libro`: Guardamos una copia del título del libro para facilitar consultas rápidas
    -- sin tener que ir siempre a MongoDB. Ayuda a la legibilidad.
    titulo_libro VARCHAR(255),
    
    -- `fecha_solicitud`: Fecha y hora en que se realizó la solicitud del préstamo.
    -- Se establece automáticamente a la fecha y hora actual.
    fecha_solicitud TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- `fecha_devolucion_prevista`: Fecha en la que se espera que el libro sea devuelto.
    -- Puede ser NULL si el préstamo aún no ha sido aprobado.
    fecha_devolucion_prevista DATE,
    
    -- `fecha_devolucion_real`: Fecha en que el libro fue efectivamente devuelto.
    -- Será NULL hasta que el libro se devuelva.
    fecha_devolucion_real DATE,
    
    -- `estado`: Estado actual del préstamo.
    -- ENUM limita los valores posibles, asegurando la consistencia de los datos.
    -- 'pendiente': El usuario lo solicitó, esperando aprobación del admin.
    -- 'aprobado': El admin lo aprobó, listo para ser entregado.
    -- 'entregado': El usuario ya tiene el libro.
    -- 'devuelto': El libro fue devuelto a la biblioteca.
    -- 'rechazado': La solicitud fue denegada por un admin.
    estado ENUM('pendiente', 'aprobado', 'entregado', 'devuelto', 'rechazado') NOT NULL DEFAULT 'pendiente',
    
    -- Creamos la restricción de clave foránea para `id_usuario`.
    -- `ON DELETE CASCADE`: Si se elimina un usuario, todos sus registros de préstamos
    -- también se eliminarán automáticamente. Esto mantiene la base de datos limpia.
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Creamos un índice para búsquedas rápidas por estado del préstamo.
CREATE INDEX idx_prestamos_estado ON prestamos(estado);

-- Creamos un índice para búsquedas rápidas por el ID del usuario.
CREATE INDEX idx_prestamos_id_usuario ON prestamos(id_usuario);