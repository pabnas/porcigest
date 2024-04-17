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
INSERT INTO inventario_animales (id_corral, raza, sexo, fecha_nacimiento, peso, estado_salud, origen)
VALUES
  (1, 'Raza 1', 'H', '2023-01-01', 50.00, 'Bueno', 'I'),
  (2, 'Raza 3', 'H', '2023-03-01', 45.20, 'Bueno', 'E'),
  (3, 'Raza 1', 'H', '2023-05-01', 52.10, 'Bueno', 'I'),
  (4, 'Raza 3', 'H', '2023-07-01', 47.30, 'Bueno', 'E'),
  (5, 'Raza 1', 'H', '2023-09-01', 54.20, 'Bueno', 'I');

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
INSERT INTO origen_externo (id_animal, fecha_compra, fecha_ingreso, finalidad_compra, etapa_productiva, granja_origen, edad, vendedor, peso_compra, observaciones)
VALUES
    (1, '2023-12-01', '2023-12-05', 'Reproducción', 'Crecimiento', 'Granja ABC', 3, 'Vendedor 1', 20.5, 'Buena condición física'),
    (2, '2024-01-10', '2024-01-15', 'Reproducción', 'Crecimiento', 'Granja XYZ', 4, 'Vendedor 2', 22.0, 'Algunas señales de enfermedad'),
    (3, '2024-02-05', '2024-02-10', 'Crecimiento', 'Crecimiento', 'Granja XYZ', 2, 'Vendedor 3', 18.3, 'Pequeño pero saludable'),
    (4, '2024-03-01', '2024-03-05', 'Reproducción', 'Crecimiento', 'Granja XYZ', 3, 'Vendedor 1', 21.7, 'Buen historial de reproducción'),
    (5, '2024-03-20', '2024-03-25', 'Reproducción', 'Crecimiento', 'Granja ABC', 4, 'Vendedor 2', 23.2, 'Buena salud general');

--8
INSERT INTO origen_interno (fecha_cambio_etapa, finalidad, etapa_productiva, id_madre, id_padre, observaciones)
VALUES
    ('2024-01-01', 'Reproducción', 'Crecimiento', 5, NULL, 'Cambio de etapa para reproducción'),
    ('2024-01-15', 'Crecimiento', 'Crecimiento',  4, NULL, 'Cambio de etapa después del destete'),
    ('2024-02-10', 'Reproducción', 'Crecimiento', 2, 5, 'Cambio de etapa para reproducción'),
    ('2024-02-25', 'Reproducción', 'Crecimiento', 1, 3, 'Cambio de etapa para reproducción'),
    ('2024-03-10', 'Reproducción', 'Crecimiento', 1, NULL, 'Cambio de etapa para reproducción');

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
INSERT INTO venta_unidad (fecha_venta, id_lote, peso_lechon, precio_unidad, destino, comprador, observaciones)
VALUES
    ('2024-01-10', 1, 15.0, 120.00, 'Matadero', 'Comprador 1', 'Venta de lechones pequeños'),
    ('2024-01-20', 2, 17.5, 130.00, 'Granja de reproducción', 'Comprador 2', 'Venta selectiva'),
    ('2024-02-15', 3, 19.0, 140.00, 'Matadero', 'Comprador 3', 'Venta a granel'),
    ('2024-03-05', 4, 16.5, 125.00, 'Granja de reproducción', 'Comprador 4', 'Venta regular'),
    ('2024-03-25', 5, 18.0, 135.00, 'Matadero', 'Comprador 5', 'Venta de lechones grandes');

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
INSERT INTO lotes_tratamientos (id_tratamiento, id_lote, fecha_aplicacion_lote, dosis_lote, observaciones_lote)
VALUES
    (1, 1, '2024-01-05', 15.0, 'Todos los lechones tratados'),
    (2, 2, '2024-02-10', 10.0, 'Vacunación en lote de reproducción'),
    (3, 3, '2024-03-15', 20.0, 'Tratamiento en lote de engorda'),
    (4, 4, '2024-04-20', 25.0, 'Suplemento administrado a cerdas gestantes'),
    (5, 5, '2024-05-25', 20.0, 'Tratamiento en lote con problemas de cojera');

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

--17
INSERT INTO roles (nombre_rol, descripcion_rol)
VALUES
    ('Administrador', 'Tiene acceso completo al sistema y puede gestionar usuarios y configuraciones'),
    ('Operario', 'Realiza tareas operativas en el sistema pero no tiene acceso a configuraciones'),
    ('Supervisor', 'Supervisa las actividades en el sistema y tiene permisos limitados de gestión'),
    ('Auditor', 'Realiza auditorías y análisis de datos en el sistema'),
    ('Invitado', 'Tiene acceso limitado a ciertas funciones del sistema');


--18
INSERT INTO usuarios (nombre_usuario, correo_electronico, contrasena, id_rol)
VALUES
    ('admin', 'admin@example.com', 'admin123', 1),
    ('operario1', 'operario1@example.com', 'operario123', 2),
    ('supervisor1', 'supervisor1@example.com', 'supervisor123', 3),
    ('auditor1', 'auditor1@example.com', 'auditor123', 4),
    ('invitado1', 'invitado1@example.com', 'invitado123', 5);
