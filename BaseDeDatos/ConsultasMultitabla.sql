
SELECT Nombre, direccion_fiscal, Email FROM Empresas;

SELECT I.nombre, I.apellido, P.saldo_actual
FROM Inversores I
JOIN Portafolios P ON I.cuil = P.cuil
WHERE P.saldo_actual > 500000;

SELECT A.simbolo, A.precio_actual, E.Nombre AS Empresa
FROM Acciones A
JOIN Empresas E ON A.Cuit = E.Cuit;

SELECT idPortafolio, idAccion, cantidad, tipo_operacion, comision
FROM detalleOperaciones
WHERE idPortafolio = 1 AND tipo_operacion = 'Compra';

SELECT idAccion, fecha, precioMaximo, precioMinimo, precioApertura, precioCierre
FROM historialAcciones
WHERE precioMaximo > 200;

UPDATE Portafolios
SET saldo_actual = 1200000
WHERE cuil = 11223344;

UPDATE Acciones
SET precio_actual = 215.00
WHERE simbolo = 'FINC';

UPDATE Empresas
SET Email = 'info@healthplus.com'
WHERE Nombre = 'HealthPlus';

UPDATE Acciones
SET cantidad_en_existencia = cantidad_en_existencia * 2
WHERE Cuit = '30-78901234-5';

UPDATE inversores
SET nombre = 'Alejandro'
WHERE cuil = 11223344;

SELECT 
            i.nombre AS Titular,
            p.saldo_actual AS SaldoActual,
            SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN d.cantidad * d.valor_accion ELSE 0 END) AS TotalInvertido,
            SUM(CASE WHEN d.tipo_operacion = 'Venta' THEN (d.valor_accion * d.cantidad) ELSE 0 END) 
            - SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN d.cantidad * d.valor_accion ELSE 0 END) 
            + (SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN (d.cantidad * a.precio_actual) ELSE 0 END)
                - SUM(CASE WHEN d.tipo_operacion = 'Venta' THEN (d.cantidad * a.precio_actual) ELSE 0 END))
            AS RendimientoActualTotal
        FROM portafolios p
        LEFT JOIN detalleOperaciones d ON p.IdPortafolio = d.idPortafolio
        LEFT JOIN acciones a ON d.idAccion = a.idAccion
        LEFT JOIN inversores i ON p.cuil = i.cuil
        WHERE p.IdPortafolio = 1
        GROUP BY p.descripcion, p.saldo_actual;
        
SELECT 
            a.simbolo AS Accion,
            e.nombre AS Empresa,
            a.precio_actual AS PrecioActual,
            SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN d.cantidad ELSE 0 END) - 
            SUM(CASE WHEN d.tipo_operacion = 'Venta' THEN d.cantidad ELSE 0 END) AS CantidadEnExistencia,
            SUM(CASE WHEN d.tipo_operacion = 'Venta' THEN (d.valor_accion * d.cantidad) ELSE 0 END) 
	            - SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN d.cantidad * d.valor_accion ELSE 0 END) 
                + (SUM(CASE WHEN d.tipo_operacion = 'Compra' THEN (d.cantidad * a.precio_actual) ELSE 0 END)
			    -SUM(CASE WHEN d.tipo_operacion = 'Venta' THEN (d.cantidad * a.precio_actual) ELSE 0 END))
                AS RendimientoActual
            FROM inversores i
            JOIN portafolios p ON i.cuil = p.cuil
            JOIN detalleOperaciones d ON p.IdPortafolio = d.idPortafolio
            JOIN acciones a ON d.idAccion = a.idAccion
            JOIN empresas e ON a.Cuit = e.Cuit
            WHERE p.IdPortafolio = 3
            GROUP BY a.simbolo, e.nombre, a.precio_actual
            HAVING CantidadEnExistencia > 0;
            
	SELECT 
    I.nombre AS Inversor,
    I.apellido AS Apellido,
    I.email AS Email,
    E.Nombre AS Empresa,
    A.simbolo AS Simbolo_Accion,
    DO.tipo_operacion AS TipoOperacion,
    DO.cantidad AS Cantidad,
    DO.valor_accion AS ValorAccion,
    DO.comision AS Comision,
    (DO.cantidad * DO.valor_accion) AS MontoTotal,
    P.descripcion AS DescripcionPortafolio
FROM 
    detalleOperaciones DO
JOIN 
    Portafolios P ON DO.idPortafolio = P.idPortafolio
JOIN 
    Inversores I ON P.cuil = I.cuil
JOIN 
    Acciones A ON DO.idAccion = A.idAccion
JOIN 
    Empresas E ON A.Cuit = E.Cuit
WHERE 
    DO.tipo_operacion IN ('Compra', 'Venta')
ORDER BY 
    I.nombre, DO.tipo_operacion;
