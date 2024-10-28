CREATE DATABASE IF NOT EXISTS BrokerArg3;
Use BrokerArg3;

CREATE TABLE inversores (
    cuil INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    email VARCHAR(255),
    telefono VARCHAR(20),
    direccion VARCHAR(200),
    contraseña varchar(20) not null,
    bloqueado BOOLEAN NOT NULL DEFAULT 0
);

CREATE TABLE portafolios (
    IdPortafolio INT AUTO_INCREMENT PRIMARY KEY,
    cuil INT NOT NULL,
    descripcion VARCHAR(255),
    fecha_creacion timestamp DEFAULT CURRENT_TIMESTAMP,
    saldo_actual decimal(10, 2),
    FOREIGN KEY (cuil) REFERENCES Inversores(cuil) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE empresas (
    cuit VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    direccion_fiscal VARCHAR(255),
    razon_social VARCHAR(255),
    email VARCHAR(255),
    telefono VARCHAR(20)
);

CREATE TABLE acciones (
    idAccion INT AUTO_INCREMENT PRIMARY KEY,
    simbolo VARCHAR(10) NOT NULL,
    Cuit VARCHAR(20),
    cantidad_en_existencia INT NOT NULL,
    precio_actual DECIMAL(10, 2) NOT NULL,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (Cuit) REFERENCES Empresas(Cuit) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE detalleOperaciones (
    idOperaciones INT AUTO_INCREMENT PRIMARY KEY,
    idPortafolio INT,
    idAccion INT,
    cantidad INT NOT NULL,
    tipo_operacion ENUM('Compra', 'Venta') NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    comision DECIMAL(10, 2) NOT NULL,
    valor_accion DECIMAL(10, 2),
    FOREIGN KEY (idPortafolio) REFERENCES Portafolios(IdPortafolio) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (idAccion) REFERENCES Acciones(idAccion) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE historialAcciones (
    idHistorial INT AUTO_INCREMENT PRIMARY KEY,
    idAccion INT NOT NULL,
    fecha DATE NOT NULL,
    precioMaximo DECIMAL(10, 2) NOT NULL,
    precioMinimo DECIMAL(10, 2) NOT NULL,
    precioApertura DECIMAL(10, 2) NOT NULL,
    precioCierre DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (idAccion) REFERENCES Acciones(idAccion) ON DELETE CASCADE ON UPDATE CASCADE
);

