--1
INSERT INTO areas (nombre_area)
VALUES
('Área 1'),
('Área 2'),
('Área 3'),
('Área 4'),
('Área 5');

--2
INSERT INTO corrales (num_corral, id_area, aforo, cantidad_dentro)
VALUES
  (1, 1, 50, 20),
  (2, 1, 50, 35),
  (3, 2, 60, 42),
  (4, 2, 60, 38),
  (5, 3, 40, 25);

--3
INSERT INTO inventario_animales (id_corral, raza, sexo, edad, peso, estado_productivo, origen)
VALUES
  (1, 'Duroc', 'H', 6, 120.50, 'engorde', 'I'),
  (1, 'Pietrain', 'H', 5, 105.25, 'engorde', 'E'),
  (2, 'Landrace', 'H', 4, 87.75, 'engorde', 'I'),
  (2, 'Yorkshire', 'H', 4, 85.00, 'engorde', 'E'),
  (3, 'Berkshire', 'H', 7, 142.00, 'engorde', 'I'),
  (3, 'Tamworth', 'M', 7, 135.75, 'engorde', 'E'),
  (4, 'Hampshire', 'M', 5, 110.50, 'gestacion', 'I'),
  (4, 'Poland China', 'M', 5, 108.25, 'gestacion', 'E'),
  (5, 'Chester White', 'M', 3, 67.00, 'lactancia', 'I'),
  (5, 'Mulefoot', 'M', 3, 65.75, 'lactancia', 'E');


--4
INSERT INTO movimientos (id_animal, fecha, area_origen, area_destino)
VALUES
  (1, '2023-11-15', 1, 2),
  (2, '2023-11-20', 2, 3),
  (3, '2023-11-25', 3, 4),
  (4, '2023-11-30', 4, 5),
  (5, '2023-12-05', 1, 2);

--5
INSERT INTO registro_partos (id_animal, fecha_parto, nacidos_vivos, nacidos_muertos, vivos_48h, vivos_destete, observaciones)
VALUES
    (1, '2024-01-01', 8, 2, 8, 7, 'Parto exitoso'),
    (2, '2024-01-15', 7, 1, 6, 6, 'Parto sin complicaciones'),
    (3, '2024-02-05', 9, 0, 9, 8, 'Gran camada'),
    (4, '2024-02-20', 6, 3, 5, 4, 'Algunos problemas de salud en la camada'),
    (5, '2024-03-10', 10, 0, 10, 9, 'Gran cantidad de nacidos');

--6
INSERT INTO registro_inseminaciones (id_madre, id_padre, fecha_inseminacion, tipo_inseminacion, observaciones)
VALUES
    (1, 1, '2023-12-15', 'IA', 'Inseminación exitosa'),
    (2, 3, '2024-01-20', 'MN', 'Monta natural programada'),
    (3, 5, '2024-02-10', 'IA', 'Inseminación por razones de salud'),
    (4, NULL, '2024-02-25', 'O', 'Otro método de reproducción'),
    (5, 5, '2024-03-15', 'TE', 'Transferencia de embriones exitosa');

--7
INSERT INTO origen_externo (id_animal, fecha_compra, fecha_ingreso, finalidad_compra, etapa_productiva_ingreso, vendedor, peso_compra, observaciones) VALUES
(2, '2023-01-15', '2023-01-20', 'Producción de leche', 'lactancia', 'Vendedor A', 450.30, 'Animal en buen estado'),
(4, '2023-02-10', '2023-02-15', 'Reproducción', 'gestacion', 'Vendedor B', 320.40, 'Requiere revisión médica'),
(6, '2023-03-05', '2023-03-10', 'Engorde', 'remplazo', 'Vendedor C', 250.25, 'Buen potencial de crecimiento'),
(8, '2023-04-12', '2023-04-17', 'Producción de leche', 'lactancia', 'Vendedor D', 420.50, 'Animal saludable'),
(10, '2023-05-20', '2023-05-25', 'Reproducción', 'gestacion', 'Vendedor E', 340.90, 'Animal joven y fuerte'),
(2, '2023-06-15', '2023-06-20', 'Producción de leche', 'lactancia', 'Vendedor F', 450.30, 'Animal en buen estado'),
(4, '2023-07-10', '2023-07-15', 'Reproducción', 'gestacion', 'Vendedor G', 320.40, 'Requiere revisión médica'),
(6, '2023-08-05', '2023-08-10', 'Engorde', 'remplazo', 'Vendedor H', 250.25, 'Buen potencial de crecimiento'),
(8, '2023-09-12', '2023-09-17', 'Producción de leche', 'lactancia', 'Vendedor I', 420.50, 'Animal saludable'),
(10, '2023-10-20', '2023-10-25', 'Reproducción', 'gestacion', 'Vendedor J', 340.90, 'Animal joven y fuerte');


--8
INSERT INTO origen_interno (fecha_cambio_etapa, finalidad, etapa_productiva_ingreso, id_madre, id_padre, observaciones) VALUES
('2023-01-15', 'Producción de leche', 'lactancia', 1, 3, 'Crecimiento saludable'),
('2023-02-20', 'Reproducción', 'gestacion', 2, 4, 'Buen estado de salud'),
('2023-03-25', 'Engorde', 'engorde', 5, NULL, 'Padre desconocido'),
('2023-04-10', 'Venta', 'vendido', 6, 7, 'Vendida por razones económicas'),
('2023-05-30', 'Remplazo', 'remplazo', 8, NULL, 'Padre desconocido'),
('2023-06-15', 'Producción de leche', 'lactancia', 1, 3, 'Buen potencial de producción'),
('2023-07-05', 'Reproducción', 'gestacion', 2, 4, 'Animal fuerte y saludable'),
('2023-08-22', 'Engorde', 'engorde', 5, NULL, 'Crecimiento rápido'),
('2023-09-11', 'Venta', 'vendido', 6, 7, 'Buen peso al momento de la venta'),
('2023-10-18', 'Remplazo', 'remplazo', 8, NULL, 'Requiere monitoreo constante');


--9
INSERT INTO lotes_lechones (id_corral, cantidad_lechones, fecha_ingreso_lote, dias_precebo, observaciones)
VALUES
    (1, 50, '2024-01-01', NULL, 'Lote grande de lechones'),
    (2, 40, '2024-01-15', NULL, 'Lechones para precebo'),
    (3, 30, '2024-02-05', 30, 'Lechones recién destetados'),
    (4, 20, '2024-02-20', 20, 'Lote pequeño para engorda'),
    (5, 10, '2024-03-10', NULL, 'Lechones de reemplazo');

--10
INSERT INTO venta_lotes (fecha_venta, id_lote, peso_promedio, precio_lote, destino, comprador, observaciones)
VALUES
    ('2024-01-10', 1, 20.5, 5000.00, 'Matadero', 'Comprador 1', 'Venta regular'),
    ('2024-01-20', 2, 18.7, 4800.00, 'Granja de reproducción', 'Comprador 2', 'Venta con descuento'),
    ('2024-02-15', 3, 22.0, 5500.00, 'Matadero', 'Comprador 3', 'Venta a granel'),
    ('2024-03-05', 4, 19.8, 4900.00, 'Granja de reproducción', 'Comprador 4', 'Venta regular'),
    ('2024-03-25', 5, 21.5, 5300.00, 'Matadero', 'Comprador 5', 'Venta a precio premium');

--11
INSERT INTO venta_unidad (fecha_venta, id_lote, id_animal, peso, precio_unidad, destino, comprador, observaciones) VALUES
('2023-01-10', 1, 1, 350.50, 1200.00, 'Planta de procesamiento', 'Comprador A', 'Venta rápida y eficiente'),
('2023-02-15', 1, 2, 450.30, 1500.00, 'Granja vecina', 'Comprador B', 'Animal en excelente condición'),
('2023-03-20', 2, 3, 380.75, 1300.00, 'Carnicería local', 'Comprador C', 'Precio negociado'),
('2023-04-25', 2, 4, 320.40, 1100.00, 'Feria ganadera', 'Comprador D', 'Animal premiado en la feria'),
('2023-05-30', 3, 5, 500.00, 2000.00, 'Exportación', 'Comprador E', 'Venta internacional'),
('2023-06-05', 3, 6, 250.25, 900.00, 'Mercado regional', 'Comprador F', 'Venta al por menor'),
('2023-07-10', 4, 7, 360.60, 1250.00, 'Granja orgánica', 'Comprador G', 'Animal certificado orgánico'),
('2023-08-15', 4, 8, 420.50, 1400.00, 'Planta de procesamiento', 'Comprador H', 'Venta rápida y eficiente'),
('2023-09-20', 5, 9, 310.80, 1000.00, 'Carnicería local', 'Comprador I', 'Animal en buen estado'),
('2023-10-25', 5, 10, 340.90, 1150.00, 'Feria ganadera', 'Comprador J', 'Buen precio obtenido');


--12
INSERT INTO medicamentos (nombre_medicamento, principio_activo, laboratorio, presentacion, fecha_vencimiento, stock, lote_medicamento, vendedor_medicamento, precio_unidad, fecha_compra, observaciones)
VALUES
    ('Antibiótico A', 'Principio Activo 1', 'Laboratorio 1', 'Tabletas', '2024-12-31', 100, 'Lote 001', 'Proveedor 1', 15.50, '2024-04-01', 'Tratamiento de infecciones bacterianas'),
    ('Vitamina B12', 'Principio Activo 2', 'Laboratorio 2', 'Ampollas', '2024-11-30', 50, 'Lote 002', 'Proveedor 2', 20.00, '2024-03-15', 'Suplemento vitamínico para cerdos en crecimiento'),
    ('Desparasitante C', 'Principio Activo 3', 'Laboratorio 3', 'Suspensión', '2024-10-31', 75, 'Lote 003', 'Proveedor 3', 12.80, '2024-02-20', 'Tratamiento contra parásitos intestinales'),
    ('Antiinflamatorio D', 'Principio Activo 4', 'Laboratorio 4', 'Crema', '2024-09-30', 60, 'Lote 004', 'Proveedor 4', 18.75, '2024-01-10', 'Reducción de la inflamación en heridas y lesiones'),
    ('Vacuna E', 'Principio Activo 5', 'Laboratorio 5', 'Inyectable', '2024-08-31', 80, 'Lote 005', 'Proveedor 5', 25.00, '2024-05-05', 'Prevención de enfermedades comunes en cerdos');

--13
INSERT INTO tratamientos (tipo_tratamiento, detalle_tratamiento, id_medicamento, dosis, observaciones)
VALUES
    ('Desparasitación', 'Tratamiento preventivo contra parásitos intestinales', 3, 15.0, 'Administrado a todos los lechones'),
    ('Vacunación', 'Vacunación contra enfermedad X', 5, 10.0, 'Vacuna aplicada a cerdos de 3 meses de edad'),
    ('Antibiótico', 'Tratamiento para infección respiratoria', 1, 20.0, 'Administrado a cerdos con síntomas de tos'),
    ('Suplemento', 'Suplemento vitamínico para cerdas gestantes', NULL, NULL, 'Administrado a cerdas durante la gestación'),
    ('Antiinflamatorio', 'Tratamiento para inflamación en patas', 4, 25.0, 'Administrado a cerdos con cojera');

--14
INSERT INTO tratamiento_lotes (id_tratamiento, id_lote, fecha_aplicacion_lote, dosis_lote, observaciones_lote) VALUES
(1, 1, '2023-01-05', 10.50, 'Aplicación preventiva contra enfermedades comunes'),
(2, 1, '2023-02-10', 12.00, 'Tratamiento para mejorar la salud digestiva'),
(3, 2, '2023-03-15', 8.75, 'Vacunación general'),
(4, 2, '2023-04-20', 9.60, 'Suplemento vitamínico'),
(5, 3, '2023-05-25', 15.30, 'Tratamiento antiparasitario'),
(1, 3, '2023-06-30', 11.20, 'Refuerzo de aplicación preventiva'),
(2, 4, '2023-07-05', 13.40, 'Mejora de la salud ósea'),
(3, 4, '2023-08-10', 7.90, 'Vacunación adicional'),
(4, 5, '2023-09-15', 10.00, 'Suplemento para crecimiento'),
(5, 5, '2023-10-20', 14.50, 'Tratamiento antiparasitario anual');


--15
INSERT INTO tratamientos_animales (id_tratamiento, id_animal, fecha_tratamiento_animal)
VALUES
    (1, 1, '2024-01-05'),
    (2, 2, '2024-02-10'),
    (3, 3, '2024-03-15'),
    (4, 4, '2024-04-20'),
    (5, 5, '2024-05-25');

--16
INSERT INTO ingreso_vehiculos (fecha_ingreso, hora_ingreso, placa_vehiculo, nombre_conductor, telefono_conductor, empresa_transportista, tipo_vehiculo, motivo_ingreso, ultimo_predio_visitado, observaciones)
VALUES
    ('2024-01-01', '08:00:00', 'ABC123', 'Juan Pérez', '1234567890', 'Transportes XYZ', 'Camión', 'Entrega de suministros', 'Granja A', 'Entrega puntual'),
    ('2024-01-05', '10:30:00', 'DEF456', 'María Rodríguez', '0987654321', 'Transportes ABC', 'Camioneta', 'Recolección de productos', 'Granja B', 'Cliente habitual'),
    ('2024-01-10', '12:15:00', 'GHI789', 'Carlos Sánchez', '1357924680', 'Transportes DEF', 'Camión', 'Retiro de desechos', 'Granja C', 'Problemas con la entrega'),
    ('2024-01-15', '09:45:00', 'JKL012', 'Ana Martínez', '2468013579', 'Transportes GHI', 'Camioneta', 'Entrega de alimentos', 'Granja D', 'Entrega urgente'),
    ('2024-01-20', '11:00:00', 'MNO345', 'Luis González', '9876543210', 'Transportes JKL', 'Camión', 'Servicio de mantenimiento', 'Granja E', 'Acceso restringido');

INSERT INTO monitoreo_agua (fecha_hora, nivel_agua_porcentaje, flujo_agua_litros_hora) VALUES
('2023-01-01 08:00:00', 75.5, 120.50),
('2023-01-01 12:00:00', 70.0, 110.75),
('2023-01-01 16:00:00', 65.2, 130.20),
('2023-01-01 20:00:00', 60.8, 115.30),
('2023-01-02 08:00:00', 85.0, 140.45),
('2023-01-02 12:00:00', 80.3, 125.60),
('2023-01-02 16:00:00', 78.7, 135.50),
('2023-01-02 20:00:00', 74.1, 128.75),
('2023-01-03 08:00:00', 90.0, 145.90),
('2023-01-03 12:00:00', 88.5, 138.65);

