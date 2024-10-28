
INSERT INTO Empresas (Cuit, Nombre, direccion_fiscal, razon_social, Email, Telefono)
VALUES ('30-98765432-1', 'FinanceCorp', 'Calle Principal 123', 'FinanceCorp S.A.', 'contacto@financecorp.com', '4567-8901');

INSERT INTO Empresas (Cuit, Nombre, direccion_fiscal, razon_social, Email, Telefono)
VALUES ('30-56789012-3', 'EnergyGlobal', 'Avenida Industrial 500', 'EnergyGlobal S.A.', 'info@energyglobal.com', '2345-6789');

INSERT INTO Empresas (Cuit, Nombre, direccion_fiscal, razon_social, Email, Telefono)
VALUES ('30-34567890-4', 'HealthPlus', 'Calle Médicos 55', 'HealthPlus S.A.', 'soporte@healthplus.com', '9876-5432');

INSERT INTO Empresas (Cuit, Nombre, direccion_fiscal, razon_social, Email, Telefono)
VALUES ('30-78901234-5', 'RetailMarket', 'Bulevar Comercial 400', 'RetailMarket S.A.', 'ventas@retailmarket.com', '1234-5678');

INSERT INTO Acciones (simbolo, cantidad_en_existencia, precio_actual, Cuit)
VALUES ('FINC', 1500, 210.75, '30-98765432-1');

INSERT INTO Acciones (simbolo, cantidad_en_existencia, precio_actual, Cuit)
VALUES ('ENRG', 3000, 120.50, '30-56789012-3');

INSERT INTO Acciones (simbolo, cantidad_en_existencia, precio_actual, Cuit)
VALUES ('HLTH', 2500, 89.99, '30-34567890-4');

INSERT INTO Acciones (simbolo, cantidad_en_existencia, precio_actual, Cuit)
VALUES ('RETL', 4000, 175.25, '30-78901234-5');


INSERT INTO Inversores (cuil, nombre, apellido, email, telefono, direccion, contraseña)
VALUES (99999999, 'María', 'Gómez', 'maria.gomez@example.com', '4321-8765', 'Avenida Principal 456', 'pass1234');

INSERT INTO Inversores (cuil, nombre, apellido, email, telefono, direccion, contraseña)
VALUES (11223344, 'Carlos', 'López', 'carlos.lopez@example.com', '9876-5432', 'Calle Secundaria 789', 'carl0sLopez');

INSERT INTO Inversores (cuil, nombre, apellido, email, telefono, direccion, contraseña)
VALUES (99887766, 'Laura', 'Fernández', 'laura.fernandez@example.com', '7654-3210', 'Plaza Central 321', 'lauFern88');

INSERT INTO Inversores (cuil, nombre, apellido, email, telefono, direccion, contraseña)
VALUES (55667788, 'Roberto', 'Martínez', 'roberto.martinez@example.com', '5432-1098', 'Boulevard del Sol 654', 'robMart9');

INSERT INTO Portafolios (cuil, descripcion, saldo_actual)
VALUES (99999999, 'Portafolio de María Gómez', '1000000');

INSERT INTO Portafolios (cuil, descripcion, saldo_actual)
VALUES (11223344, 'Portafolio de Carlos López', '1000000');

INSERT INTO Portafolios (cuil, descripcion, saldo_actual)
VALUES (99887766, 'Portafolio de Laura Fernández', '1000000');

INSERT INTO Portafolios (cuil, descripcion, saldo_actual)
VALUES (55667788, 'Portafolio de Roberto Martínez', '1000000');


INSERT INTO detalleOperaciones (idPortafolio, idAccion, cantidad, tipo_operacion, comision, valor_accion)
SELECT 1, 4, 100, 'Compra', ROUND(100 * precio_actual * 0.015), precio_actual
FROM Acciones
WHERE idAccion = 4;

INSERT INTO detalleOperaciones (idPortafolio, idAccion, cantidad, tipo_operacion, comision, valor_accion)
SELECT 1, 4, 50, 'Venta', ROUND(50 * precio_actual * 0.015), precio_actual
FROM Acciones
WHERE idAccion = 4;

INSERT INTO detalleOperaciones (idPortafolio, idAccion, cantidad, tipo_operacion, comision, valor_accion)
SELECT 3, 2, 88, 'Compra', ROUND(88 * precio_actual * 0.015), precio_actual
FROM Acciones
WHERE idAccion = 2;

INSERT INTO detalleOperaciones (idPortafolio, idAccion, cantidad, tipo_operacion, comision, valor_accion)
SELECT 2, 1, 20, 'Compra', ROUND(20 * precio_actual * 0.015), precio_actual
FROM Acciones
WHERE idAccion = 1;

INSERT INTO historialAcciones (idAccion, fecha, precioMaximo, precioMinimo, precioApertura, precioCierre) VALUES
(1, '2024-10-01', 150.00, 145.00, 147.50, 148.75),
(2, '2024-10-02', 200.00, 195.00, 198.00, 199.50),
(3, '2024-10-03', 300.00, 295.00, 298.00, 299.00),
(4, '2024-10-04', 250.00, 245.00, 247.00, 248.50);
