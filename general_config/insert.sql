--1
INSERT INTO areas (nombre_area)
VALUES
('Gestación'),
('Lactancia'),
('Precebos'),
('Remplazos'),
('Engorde'),
('Reproductores');

--2
-- Gestación: id_area = 1
-- Lactancia: id_area = 2
-- Precebos: id_area = 3
-- Remplazos: id_area = 4
-- Engorde: id_area = 5
-- Reproductores: id_area = 6

-- Gestación: 35 jaulas individuales
INSERT INTO corrales (num_corral, id_area, aforo, estado) VALUES
(1, 1, 1, 'ocupado'),
(2, 1, 1, 'ocupado'),
(3, 1, 1, 'ocupado'),
(4, 1, 1, 'vacio'),
(5, 1, 1, 'ocupado'),
(6, 1, 1, 'vacio'),
(7, 1, 1, 'ocupado'),
(8, 1, 1, 'ocupado'),
(9, 1, 1, 'ocupado'),
(10, 1, 1, 'ocupado'),
(11, 1, 1, 'vacio'),
(12, 1, 1, 'ocupado'),
(13, 1, 1, 'ocupado'),
(14, 1, 1, 'vacio'),
(15, 1, 1, 'ocupado'),
(16, 1, 1, 'ocupado'),
(17, 1, 1, 'vacio'),
(18, 1, 1, 'ocupado'),
(19, 1, 1, 'vacio'),
(20, 1, 1, 'ocupado'),
(21, 1, 1, 'ocupado'),
(22, 1, 1, 'ocupado'),
(23, 1, 1, 'vacio'),
(24, 1, 1, 'ocupado'),
(25, 1, 1, 'ocupado'),
(26, 1, 1, 'vacio'),
(27, 1, 1, 'ocupado'),
(28, 1, 1, 'ocupado'),
(29, 1, 1, 'ocupado'),
(30, 1, 1, 'vacio'),
(31, 1, 1, 'ocupado'),
(32, 1, 1, 'ocupado'),
(33, 1, 1, 'vacio'),
(34, 1, 1, 'ocupado'),
(35, 1, 1, 'ocupado');

-- Lactancia: 9 jaulas individuales
INSERT INTO corrales (num_corral, id_area, aforo, estado) VALUES
(36, 2, 1, 'ocupado'),
(37, 2, 1, 'ocupado'),
(38, 2, 1, 'ocupado'),
(39, 2, 1, 'vacio'),
(40, 2, 1, 'ocupado'),
(41, 2, 1, 'ocupado'),
(42, 2, 1, 'vacio'),
(43, 2, 1, 'ocupado'),
(44, 2, 1, 'ocupado');

-- Precebos: 5 corrales, cada uno con capacidad de 25
INSERT INTO corrales (num_corral, id_area, aforo, estado) VALUES
(45, 3, 25, 'ocupado'),
(46, 3, 25, 'ocupado'),
(47, 3, 25, 'ocupado'),
(48, 3, 25, 'ocupado'),
(49, 3, 25, 'ocupado');

-- Remplazos: 1 corral, capacidad de 4 cerdas
INSERT INTO corrales (num_corral, id_area, aforo, estado) VALUES
(50, 4, 4, 'ocupado');

-- Engorde: 1 corral, capacidad de 4 animales
INSERT INTO corrales (num_corral, id_area, aforo, estado) VALUES
(51, 5, 4, 'ocupado');

-- Reproductores: 2 corrales, un animal por corral
INSERT INTO corrales (num_corral, id_area, aforo, estado) VALUES
(52, 6, 1,'ocupado'),
(53, 6, 1,'ocupado');


--3
-- Gestación: 35 jaulas individuales
INSERT INTO inventario_animales (numero_identificacion_animal, id_corral, raza, sexo, edad, peso, estado_productivo, origen) VALUES
('001', 1, 'Duroc', 'H', 12, 150.00, 'gestacion', 'I'),
('002', 2, 'Duroc', 'H', 14, 155.00, 'gestacion', 'I'),
('003', 3, 'Duroc', 'H', 13, 148.50, 'gestacion', 'I'),
('004', 4, 'Duroc', 'H', 15, 152.00, 'gestacion', 'I'),
('005', 5, 'Duroc', 'H', 12, 149.00, 'gestacion', 'I'),
('006', 6, 'Duroc', 'H', 14, 151.00, 'gestacion', 'I'),
('007', 7, 'Duroc', 'H', 13, 153.50, 'gestacion', 'I'),
('008', 8, 'Duroc', 'H', 14, 150.20, 'gestacion', 'I'),
('009', 9, 'Duroc', 'H', 13, 152.00, 'gestacion', 'I'),
('010', 10, 'Duroc', 'H', 12, 154.00, 'gestacion', 'I'),
('011', 11, 'Duroc', 'H', 14, 149.00, 'gestacion', 'I'),
('012', 12, 'Duroc', 'H', 13, 150.00, 'gestacion', 'I'),
('013', 13, 'Duroc', 'H', 12, 148.00, 'gestacion', 'I'),
('014', 14, 'Duroc', 'H', 14, 151.00, 'gestacion', 'I'),
('015', 15, 'Duroc', 'H', 13, 149.50, 'gestacion', 'I'),
('016', 16, 'Duroc', 'H', 15, 152.50, 'gestacion', 'I'),
('017', 17, 'Duroc', 'H', 12, 150.00, 'gestacion', 'I'),
('018', 18, 'Duroc', 'H', 13, 148.50, 'gestacion', 'I'),
('019', 19, 'Duroc', 'H', 14, 149.00, 'gestacion', 'I'),
('020', 20, 'Duroc', 'H', 12, 150.00, 'gestacion', 'I'),
('021', 21, 'Duroc', 'H', 14, 151.00, 'gestacion', 'I'),
('022', 22, 'Duroc', 'H', 13, 152.00, 'gestacion', 'I'),
('023', 23, 'Duroc', 'H', 12, 150.00, 'gestacion', 'I'),
('024', 24, 'Duroc', 'H', 14, 148.50, 'gestacion', 'I'),
('025', 25, 'Duroc', 'H', 13, 151.00, 'gestacion', 'I'),
('026', 26, 'Duroc', 'H', 15, 152.00, 'gestacion', 'I'),
('027', 27, 'Duroc', 'H', 14, 149.00, 'gestacion', 'I'),
('028', 28, 'Duroc', 'H', 13, 150.00, 'gestacion', 'I'),
('029', 29, 'Duroc', 'H', 12, 148.00, 'gestacion', 'I'),
('030', 30, 'Duroc', 'H', 14, 150.50, 'gestacion', 'I'),
('031', 31, 'Duroc', 'H', 13, 151.00, 'gestacion', 'I'),
('032', 32, 'Duroc', 'H', 15, 152.00, 'gestacion', 'I'),
('033', 33, 'Duroc', 'H', 12, 149.50, 'gestacion', 'I'),
('034', 34, 'Duroc', 'H', 13, 150.00, 'gestacion', 'I'),
('035', 35, 'Duroc', 'H', 14, 151.00, 'gestacion', 'I');

-- Lactancia: 9 jaulas individuales (cerdas paridas)
INSERT INTO inventario_animales (numero_identificacion_animal, id_corral, raza, sexo, edad, peso, estado_productivo, origen) VALUES
('036', 36, 'Landrace', 'H', 30, 220.00, 'lactancia', 'I'),
('037', 37, 'Landrace', 'H', 28, 215.00, 'lactancia', 'I'),
('038', 38, 'Landrace', 'H', 29, 218.00, 'lactancia', 'I'),
('039', 39, 'Landrace', 'H', 27, 220.50, 'lactancia', 'I'),
('040', 40, 'Landrace', 'H', 30, 219.00, 'lactancia', 'I'),
('041', 41, 'Landrace', 'H', 28, 214.00, 'lactancia', 'I'),
('042', 42, 'Landrace', 'H', 29, 218.50, 'lactancia', 'I'),
('043', 43, 'Landrace', 'H', 27, 217.00, 'lactancia', 'I'),
('044', 44, 'Landrace', 'H', 30, 220.00, 'lactancia', 'I');

-- Remplazos: 1 corral, capacidad de 4 cerdas
INSERT INTO inventario_animales (numero_identificacion_animal, id_corral, raza, sexo, edad, peso, estado_productivo, origen) VALUES
('045', 50, 'Pietrain', 'H', 18, 140.00, 'remplazo', 'I'),
('046', 50, 'Pietrain', 'H', 19, 145.00, 'remplazo', 'I'),
('047', 50, 'Pietrain', 'H', 20, 142.00, 'remplazo', 'I'),
('048', 50, 'Pietrain', 'H', 18, 144.00, 'remplazo', 'I');

-- Engorde: 1 corral, capacidad de 4 animales
INSERT INTO inventario_animales (numero_identificacion_animal, id_corral, raza, sexo, edad, peso, estado_productivo, origen) VALUES
('049', 51, 'Hampshire', 'M', 6, 100.00, 'engorde', 'E'),
('050', 51, 'Hampshire', 'M', 7, 105.00, 'engorde', 'E'),
('051', 51, 'Hampshire', 'M', 6, 102.00, 'engorde', 'E'),
('052', 51, 'Hampshire', 'M', 7, 104.00, 'engorde', 'E');

-- Reproductores: 2 corrales, un animal por corral
INSERT INTO inventario_animales (numero_identificacion_animal, id_corral, raza, sexo, edad, peso, estado_productivo, origen) VALUES
('053', 52, 'Yorkshire', 'M', 24, 180.00, 'vendido', 'I'),
('054', 53, 'Yorkshire', 'M', 25, 185.00, 'vendido', 'I');



--4
-- Movimientos de cerdas de gestación a lactancia
INSERT INTO movimientos (id_animal, fecha, area_origen, area_destino) VALUES
(1, '2024-02-01', 1, 2),  -- De gestación a lactancia
(2, '2024-02-05', 1, 2),
(3, '2024-02-10', 1, 2),
(4, '2024-02-15', 1, 2),
(5, '2024-02-20', 1, 2);

-- Movimientos de cerdas de lactancia a reemplazo
INSERT INTO movimientos (id_animal, fecha, area_origen, area_destino) VALUES
(36, '2024-04-01', 2, 4),  -- De lactancia a reemplazo
(37, '2024-04-05', 2, 4),
(38, '2024-04-10', 2, 4),
(39, '2024-04-15', 2, 4),
(40, '2024-04-20', 2, 4);

-- Movimientos de cerdas de reemplazo a gestación
INSERT INTO movimientos (id_animal, fecha, area_origen, area_destino) VALUES
(45, '2024-05-01', 4, 1),  -- De reemplazo a gestación
(46, '2024-05-03', 4, 1),
(47, '2024-05-05', 4, 1),
(48, '2024-05-07', 4, 1);

-- Movimientos de animales de engorde a reproductores
INSERT INTO movimientos (id_animal, fecha, area_origen, area_destino) VALUES
(49, '2024-03-01', 5, 6),  -- De engorde a vendido
(50, '2024-03-05', 5, 6),
(51, '2024-03-10', 5, 6),
(52, '2024-03-15', 5, 6);

-- Movimientos de reproductores dentro del área de reproductores
INSERT INTO movimientos (id_animal, fecha, area_origen, area_destino) VALUES
(53, '2024-02-01', 6, 6),  -- Dentro del área de reproductores
(54, '2024-02-15', 6, 6);


--5
INSERT INTO registro_partos (id_animal, fecha_parto, nacidos_vivos, nacidos_muertos, vivos_48h, vivos_destete, observaciones) VALUES
(36, '2024-05-15', 10, 2, NULL, NULL, 'Dificultad en el parto'),
(37, '2024-05-12', 11, 1, 10, NULL, 'Buen parto, algunos cuidados necesarios'),
(38, '2024-05-10', 9, 3, 8, NULL, 'Problemas respiratorios en algunos lechones'),
(39, '2024-05-07', 12, 0, 11, 10, 'Parto sin complicaciones'),
(40, '2024-05-05', 10, 2, 9, 8, 'Lechones con buen peso al nacer'),
(41, '2024-05-03', 11, 1, 10, 9, 'Madre muy protectora'),
(42, '2024-04-30', 9, 3, 8, 7, 'Alta mortalidad inicial'),
(43, '2024-04-28', 12, 0, 11, 10, 'Lechones saludables'),
(44, '2024-04-25', 10, 2, 9, 8, 'Sin observaciones');


--6
INSERT INTO registro_inseminaciones (id_madre, id_padre, fecha_inseminacion, tipo_inseminacion, observaciones) VALUES
(1, 53, '2024-01-20', 'MN', 'Proceso exitoso'),
(2, 54, '2024-02-15', 'MN', 'Comportamiento natural observado'),
(3, 53, '2024-03-01', 'MN', 'Sin complicaciones'),
(4, 54, '2024-01-25', 'MN', 'Monta natural exitosa'),
(5, 53, '2024-02-10', 'MN', 'Necesidad de segunda inseminación'),
(6, 54, '2024-01-18', 'MN', 'Montas repetidas necesarias'),
(7, 53, '2024-03-05', 'MN', 'Buen comportamiento reproductivo'),
(8, 54, '2024-02-20', 'MN', 'Sin observaciones adicionales'),
(9, 53, '2024-01-30', 'MN', 'Tiempos de inseminación precisos'),
(10, 54, '2024-02-12', 'MN', 'Observaciones positivas generales'),
(11, 53, '2024-01-28', 'MN', 'Leve estrés post-inseminación'),
(12, 54, '2024-02-05', 'MN', 'Transferencia sin incidentes'),
(13, 53, '2024-02-22', 'MN', 'Buena respuesta del animal'),
(14, 54, '2024-01-15', 'MN', 'Sin problemas'),
(15, 53, '2024-01-18', 'MN', 'Observaciones mínimas'),
(16, 54, '2024-02-28', 'MN', 'Proceso normal'),
(17, 53, '2024-02-14', 'MN', 'Sin incidentes'),
(18, 54, '2024-01-23', 'MN', 'Leve irritación observada'),
(19, 53, '2024-03-02', 'MN', 'Buena condición física'),
(20, 54, '2024-02-18', 'MN', 'Inseminación exitosa'),
(21, 53, '2024-01-27', 'MN', 'Buen resultado'),
(22, 54, '2024-02-19', 'MN', 'Proceso sin incidentes'),
(23, 53, '2024-01-22', 'MN', 'Animal tranquilo'),
(24, 54, '2024-02-25', 'MN', 'Buena aceptación de la técnica'),
(25, NULL, '2024-01-26', 'IA', 'Comportamiento reproductivo normal'),
(26, NULL, '2024-02-02', 'IA', 'Repeticiones necesarias'),
(27, NULL, '2024-02-07', 'TE', 'Proceso estándar'),
(28, NULL, '2024-03-06', 'TE', 'Transferencia sin complicaciones'),
(29, NULL, '2024-01-29', 'IA', 'Buena respuesta observada'),
(30, 54, '2024-02-13', 'MN', 'Montas exitosas'),
(31, NULL, '2024-02-01', 'IA', 'Resultados esperados'),
(32, NULL, '2024-02-26', 'TE', 'Transferencia efectiva'),
(33, NULL, '2024-02-08', 'IA', 'Proceso sin complicaciones'),
(34, 54, '2024-01-19', 'MN', 'Buen comportamiento'),
(35, NULL, '2024-02-09', 'IA', 'Inseminación normal');


--7
INSERT INTO origen_externo (id_animal, fecha_compra, fecha_ingreso, finalidad_compra, etapa_productiva_ingreso, vendedor, peso_compra, observaciones) VALUES
(49, '2024-01-01', '2024-01-05', 'engorde', 'engorde', 'Porcicola Colanta', 100.00, 'Animal en buenas condiciones'),
(50, '2024-01-01', '2024-01-05', 'engorde', 'engorde', 'Porcicola El Hato', 105.00, 'Requiere seguimiento por pequeña herida'),
(51, '2024-01-01', '2024-01-05', 'engorde', 'engorde', 'Porcicola Colanta', 102.00, ''),
(52, '2024-01-01', '2024-01-05', 'engorde', 'engorde', 'Porcicola El Hato', 104.00, 'Peso dentro del rango esperado');


--8
INSERT INTO origen_interno (fecha_cambio_etapa, finalidad, etapa_productiva_ingreso, id_madre, id_padre, observaciones) VALUES
('2024-02-01', 'reemplazo', 'gestacion', 36, 53, 'Buen desarrollo durante la gestación'),
('2024-02-02', 'reemplazo', 'lactancia', 37, 54, 'Madre saludable, parto exitoso'),
('2024-02-03', 'reemplazo', 'gestacion', 38, NULL, 'Sin complicaciones durante la gestación'),
('2024-02-04', 'reemplazo', 'lactancia', 39, 53, 'Observaciones en desarrollo óptimo'),
('2024-02-05', 'reemplazo', 'gestacion', 40, 54, 'Parto normal, madre en buen estado'),
('2024-02-06', 'reemplazo', 'lactancia', 41, NULL, 'Parto sin complicaciones'),
('2024-02-07', 'reemplazo', 'gestacion', 42, 53, 'Buen comportamiento de la madre'),
('2024-02-08', 'reemplazo', 'lactancia', 43, 54, 'Observaciones durante la lactancia'),
('2024-02-09', 'reemplazo', 'gestacion', 44, NULL, 'Desarrollo normal durante la gestación'),
('2024-02-10', 'reemplazo', 'lactancia', 36, 53, 'Madre en buena condición física'),
('2024-02-11', 'reemplazo', 'gestacion', 37, 54, 'Madre y cría en buen estado'),
('2024-02-12', 'reemplazo', 'lactancia', 38, NULL, 'Observaciones sin complicaciones'),
('2024-02-13', 'reemplazo', 'gestacion', 39, 53, 'Desarrollo sin problemas'),
('2024-02-14', 'reemplazo', 'lactancia', 40, 54, 'Madre y cría saludables'),
('2024-02-15', 'reemplazo', 'gestacion', 41, NULL, 'Parto y lactancia sin complicaciones'),
('2024-02-16', 'reemplazo', 'lactancia', 42, 53, 'Observaciones positivas durante la lactancia'),
('2024-02-17', 'reemplazo', 'gestacion', 43, 54, 'Madre con buen comportamiento'),
('2024-02-18', 'reemplazo', 'lactancia', 44, NULL, 'Lactancia exitosa, sin observaciones negativas');


--9
INSERT INTO lotes_lechones (id_corral, cantidad_lechones, fecha_ingreso_lote, observaciones) VALUES
(45, 15, '2024-01-15', 'Ingreso de lechones en buen estado'),
(46, 20, '2024-02-10', 'Ingreso con seguimiento especial por salud'),
(47, 25, '2024-03-20', 'Corral lleno, lechones en óptimas condiciones'),
(48, 10, '2024-04-25', 'Menor cantidad debido a condiciones de salud'),
(49, 18, '2024-05-30', 'Ingreso normal, sin observaciones especiales');

--antiguos
INSERT INTO lotes_lechones (id_corral, cantidad_lechones, fecha_ingreso_lote, observaciones) VALUES
(45, 20, '2023-10-03', 'Ingreso de lechones para completar el corral'),
(46, 24, '2023-09-06', 'Ingreso adicional para alcanzar el aforo máximo'),
(47, 25, '2023-11-09', 'Corral vacío, lechones vendidos anteriormente'),
(48, 14, '2023-12-15', 'Reemplazo de lechones por nuevos de mejor estado'),
(49, 25, '2023-12-25', 'Ingreso de lechones adicionales para mantener el corral lleno');

--10
INSERT INTO venta_lotes (fecha_venta, id_lote, peso_promedio, precio_lote, destino, comprador, observaciones) VALUES
('2024-01-14', 6, 25.00, 3000.00, 'Frigorífico Guadalupe', 'Comprador A', 'Venta realizada sin contratiempos'),
('2024-02-09', 7, 27.00, 4000.00, 'Frigorífico San Martín', 'Comprador B', 'Lechones en buen estado'),
('2024-03-19', 8, 26.50, 3750.00, 'Matadero El Recreo', 'Comprador C', 'Peso promedio adecuado'),
('2024-04-24', 9, 24.00, 3200.00, 'Frigorífico Tunja', 'Comprador D', 'Menor peso debido a condiciones de salud'),
('2024-05-29', 10, 28.00, 4500.00, 'Matadero Chocontá', 'Comprador E', 'Venta sin observaciones especiales');

--11 Ajustar ------------->
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
INSERT INTO medicamentos (nombre_medicamento, principio_activo, laboratorio, presentacion, fecha_vencimiento, stock, lote_medicamento, vendedor_medicamento, precio_unidad, fecha_compra, observaciones) VALUES
('Amoxicilina', 'Amoxicilina', 'Bayer', 'Suspensión Oral 250 mg', '2024-12-31', 100, 'ABC123', 'Distribuidora Veterinaria S.A.', 55000.00, '2024-05-01', 'Antibiótico de amplio espectro'),
('Eritromicina', 'Eritromicina', 'Pfizer', 'Polvo Oral 100 mg', '2024-11-30', 80, 'DEF456', 'VetCorp S.A.S.', 48000.00, '2024-04-15', 'Antibiótico para infecciones bacterianas'),
('Ivermectina', 'Ivermectina', 'Zoetis', 'Solución Inyectable 1%', '2025-02-28', 120, 'GHI789', 'Veterinaria San José', 80000.00, '2024-06-10', 'Antiparasitario interno y externo'),
('Enrofloxacina', 'Enrofloxacina', 'MSD Animal Health', 'Tabletas 50 mg', '2024-10-31', 90, 'JKL012', 'Distribuidora Agropecuaria Ltda.', 61000.00, '2024-03-20', 'Antibiótico de amplio espectro'),
('Ceftiofur', 'Ceftiofur', 'Boehringer Ingelheim', 'Solución Inyectable 5%', '2024-09-30', 70, 'MNO345', 'VetFarma S.A.', 75000.00, '2024-07-05', 'Antibiótico para enfermedades respiratorias'),
('Tilmicosina', 'Tilmicosina', 'Elanco', 'Solución Inyectable 300 mg/mL', '2024-08-31', 60, 'PQR678', 'Distribuidora Veterinaria San Marcos', 91000.00, '2024-02-18', 'Antibiótico para enfermedades respiratorias'),
('Oxitetraciclina', 'Oxitetraciclina', 'Virbac', 'Polvo Oral 100 g', '2024-07-31', 110, 'STU901', 'Veterinaria El Ganadero', 70000.00, '2024-01-10', 'Antibiótico de amplio espectro'),
('Florfenicol', 'Florfenicol', 'Ceva', 'Suspensión Oral 50 mg/mL', '2025-01-31', 85, 'VWX234', 'Distribuidora Agroveterinaria Ltda.', 85000.00, '2024-08-15', 'Antibiótico para infecciones respiratorias'),
('Fenbendazol', 'Fenbendazol', 'Intervet', 'Suspensión Oral 10%', '2024-12-31', 100, 'YZA567', 'Veterinaria El Porcino', 55000.00, '2024-05-25', 'Antiparasitario interno'),
('Sulfadimetoxina', 'Sulfadimetoxina', 'Vetoquinol', 'Polvo Oral 20%', '2024-11-30', 75, 'BCD890', 'Distribuidora de Productos Veterinarios S.A.S.', 70000.00, '2024-03-28', 'Antibiótico para coccidiosis'),
('Tetraciclina', 'Tetraciclina', 'Syntex', 'Polvo Oral 50 g', '2024-10-31', 95, 'EFG123', 'Distribuidora de Insumos Agropecuarios', 60000.00, '2024-09-12', 'Antibiótico de amplio espectro'),
('Doxiciclina', 'Doxiciclina', 'Vetanco', 'Tabletas 100 mg', '2024-09-30', 65, 'HIJ456', 'Distribuidora de Medicamentos Veterinarios S.A.', 69000.00, '2024-04-05', 'Antibiótico para infecciones respiratorias'),
('Lincomicina', 'Lincomicina', 'Labiana', 'Solución Inyectable 300 mg/mL', '2024-08-31', 85, 'KLM789', 'Laboratorio Veterinario ABC', 95000.00, '2024-01-30', 'Antibiótico para infecciones gastrointestinales'),
('Tiamulina', 'Tiamulina', 'Huvepharma', 'Polvo Oral 50 g', '2024-07-31', 105, 'NOP012', 'VetSupply S.A.S.', 80000.00, '2024-06-08', 'Antibiótico para infecciones respiratorias'),
('Colistina', 'Colistina', 'Nicosia', 'Suspensión Oral 50 mg/mL', '2025-01-31', 80, 'QRS345', 'Distribuidora de Productos Agropecuarios y Veterinarios', 90000.00, '2024-02-20', 'Antibiótico para infecciones gastrointestinales'),
('Neomicina', 'Neomicina', 'Merial', 'Solución Inyectable 10%', '2024-12-31', 90, 'TUV678', 'Distribuidora Veterinaria Porcina', 75000.00, '2024-07-10', 'Antibiótico para infecciones gastrointestinales');


--13
INSERT INTO tratamientos (tipo_tratamiento, detalle_tratamiento, id_medicamento, dosis, observaciones) VALUES
('Antibiótico', 'Tratamiento para infecciones bacterianas', 1, 0.2, 'Administrar 0.2 ml por cada kg de peso, cada 12 horas durante 5 días'),
('Antibiótico', 'Tratamiento para infecciones respiratorias', 4, 0.175, 'Administrar 0.175 ml por cada kg de peso, cada 24 horas durante 7 días'),
('Antibiótico', 'Tratamiento para enfermedades gastrointestinales', 12, 0.2, 'Administrar 0.2 ml por cada kg de peso, cada 24 horas durante 5 días'),
('Antiparasitario', 'Tratamiento para parásitos intestinales', 9, 0.3, 'Administrar 0.3 ml por cada kg de peso, una vez por día durante 3 días'),
('Antibiótico', 'Tratamiento para coccidiosis', 10, 0.35, 'Administrar 0.35 ml por cada kg de peso, cada 24 horas durante 5 días'),
('Antibiótico', 'Tratamiento para infecciones bacterianas', 7, 0.225, 'Administrar 0.225 ml por cada kg de peso, cada 12 horas durante 7 días'),
('Antibiótico', 'Tratamiento para infecciones respiratorias', 11, 0.15, 'Administrar 0.15 ml por cada kg de peso, cada 24 horas durante 5 días'),
('Antiparasitario', 'Tratamiento para gusanos redondos', 3, 0.275, 'Administrar 0.275 ml por cada kg de peso, una vez por día durante 3 días'),
('Antibiótico', 'Tratamiento para infecciones bacterianas', 6, 0.2, 'Administrar 0.2 ml por cada kg de peso, cada 12 horas durante 7 días'),
('Antibiótico', 'Tratamiento para infecciones respiratorias', 13, 0.16, 'Administrar 0.16 ml por cada kg de peso, cada 24 horas durante 5 días'),
('Antibiótico', 'Tratamiento para infecciones bacterianas', 5, 0.21, 'Administrar 0.21 ml por cada kg de peso, cada 12 horas durante 7 días'),
('Antibiótico', 'Tratamiento para infecciones respiratorias', 8, 0.19, 'Administrar 0.19 ml por cada kg de peso, cada 24 horas durante 5 días'),
('Antibiótico', 'Tratamiento para enfermedades gastrointestinales', 14, 0.25, 'Administrar 0.25 ml por cada kg de peso, cada 24 horas durante 5 días'),
('Antibiótico', 'Tratamiento para coccidiosis', 2, 0.3, 'Administrar 0.3 ml por cada kg de peso, cada 24 horas durante 5 días'),
('Antiparasitario', 'Tratamiento para gusanos redondos', 15, 0.325, 'Administrar 0.325 ml por cada kg de peso, una vez por día durante 3 días'),
('Antibiótico', 'Tratamiento para infecciones bacterianas', 1, 0.225, 'Administrar 0.225 ml por cada kg de peso, cada 12 horas durante 7 días'),
('Antibiótico', 'Tratamiento para infecciones respiratorias', 4, 0.16, 'Administrar 0.16 ml por cada kg de peso, cada 24 horas durante 5 días'),
('Antibiótico', 'Tratamiento para enfermedades gastrointestinales', 12, 0.215, 'Administrar 0.215 ml por cada kg de peso, cada 24 horas durante 5 días'),
('Antiparasitario', 'Tratamiento para parásitos intestinales', 9, 0.31, 'Administrar 0.31 ml por cada kg de peso, una vez por día durante 3 días'),
('Antibiótico', 'Tratamiento para coccidiosis', 10, 0.35, 'Administrar 0.35 ml por cada kg de peso, cada 24 horas durante 5 días'),
('Antibiótico', 'Tratamiento para infecciones bacterianas', 7, 0.235, 'Administrar 0.235 ml por cada kg de peso, cada 12 horas durante 7 días'),
('Antibiótico', 'Tratamiento para infecciones respiratorias', 11, 0.175, 'Administrar 0.175 ml por cada kg de peso, cada 24 horas durante 5 días'),
('Antiparasitario', 'Tratamiento para gusanos redondos', 3, 0.285, 'Administrar 0.285 ml por cada kg de peso, una vez por día durante 3 días'),
('Antibiótico', 'Tratamiento para infecciones bacterianas', 6, 0.225, 'Administrar 0.225 ml por cada kg de peso, cada 12 horas durante 7 días');

--14
INSERT INTO tratamiento_lotes (id_tratamiento, id_lote, fecha_aplicacion_lote, dosis_lote, observaciones_lote)
VALUES
(1, 1, '2024-01-20', 1, 'Aplicación exitosa'),
(2, 2, '2024-02-15', 1.5, 'Requiere seguimiento adicional'),
(3, 3, '2024-03-25', 1, 'Todos los lechones recibieron la dosis adecuada'),
(4, 4, '2024-04-30', 1, 'Dosis ajustada debido a condiciones de salud'),
(5, 5, '2024-06-05', 1, 'Aplicación estándar, sin complicaciones');


--15
INSERT INTO tratamientos_animales (id_tratamiento, id_animal, fecha_tratamiento_animal, observaciones_animal)
VALUES
(1, 23, '2024-01-15', 'Aplicado antibiótico para infecciones bacterianas, seguimiento recomendado'),
(2, 8, '2024-01-20', 'Lechón tratado con antiparasitario para gusanos intestinales, sin efectos adversos'),
(3, 36, '2024-01-25', 'Aplicado antibiótico para infecciones respiratorias, lechón mostrando mejoría'),
(4, 14, '2024-02-05', 'Antibiótico administrado para enfermedades gastrointestinales, continuar monitoreo'),
(5, 42, '2024-02-10', 'Tratamiento antiparasitario para gusanos redondos, sin reacciones adversas'),
(6, 30, '2024-02-15', 'Antibiótico aplicado para coccidiosis, lechón respondiendo favorablemente'),
(7, 7, '2024-03-01', 'Lechón tratado con antibiótico para infecciones bacterianas, recuperación en curso'),
(8, 49, '2024-03-05', 'Aplicado antiparasitario para parásitos intestinales, sin complicaciones reportadas'),
(9, 18, '2024-03-10', 'Antibiótico administrado para infecciones respiratorias, lechón mostrando mejoría'),
(10, 51, '2024-03-15', 'Tratamiento antiparasitario para gusanos redondos, sin efectos secundarios detectados'),
(11, 3, '2024-04-01', 'Antibiótico aplicado para enfermedades gastrointestinales, sin recaídas observadas'),
(12, 27, '2024-04-05', 'Aplicado antibiótico para infecciones respiratorias, seguimiento programado');


--16
INSERT INTO ingreso_vehiculos (fecha_ingreso, hora_ingreso, placa_vehiculo, nombre_conductor, nombres_acompanantes, telefono_conductor, empresa_transportista, tipo_vehiculo, motivo_ingreso, ultimo_predio_visitado, observaciones)
VALUES
('2023-01-05', '09:30:00', 'ABC123', 'Juan Pérez', 'Pedro Gómez, María López', '1234567890', 'Transportes ABC', 'Camión', 'Entrega de alimentos', 'Granja Porcícola Los Pinos', 'Ninguna'),
('2023-02-10', '11:45:00', 'DEF456', 'María Gutiérrez', 'José Martínez', '9876543210', 'Transportes DEF', 'Furgoneta', 'Inspección sanitaria', 'Granja Porcícola El Recuerdo', 'Revisar temperatura de los vehículos'),
('2023-03-15', '14:20:00', 'GHI789', 'Luis Torres', '', '6549873210', 'Transportes GHI', 'Camioneta', 'Recolección de productos', 'Granja Porcícola La Esperanza', 'Entrega puntual'),
('2023-04-20', '08:00:00', 'JKL012', 'Ana Martínez', 'Carlos Ramírez', '7894561230', 'Transportes JKL', 'Camión', 'Entrega de suministros', 'Granja Porcícola La Primavera', 'Necesita asistencia al descargar'),
('2023-05-25', '10:10:00', 'MNO345', 'Pedro Gómez', 'Juan Pérez', '3216549870', 'Transportes MNO', 'Furgoneta', 'Mantenimiento de equipos', 'Granja Porcícola El Paraíso', 'Reparación de la furgoneta'),
('2023-06-30', '13:45:00', 'PQR678', 'María López', 'Luis Torres', '5647891230', 'Transportes PQR', 'Camioneta', 'Recolección de desechos', 'Granja Porcícola San José', 'Carga completa'),
('2023-07-05', '16:30:00', 'STU901', 'Carlos Ramírez', 'Ana Martínez', '8901234560', 'Transportes STU', 'Camión', 'Entrega de medicamentos', 'Granja Porcícola La Aurora', 'Necesita escolta de seguridad'),
('2023-08-10', '09:00:00', 'VWX234', 'José Martínez', 'María Gutiérrez', '4567890123', 'Transportes VWX', 'Furgoneta', 'Inspección de seguridad', 'Granja Porcícola San Miguel', 'Inspección rutinaria'),
('2023-09-15', '11:15:00', 'YZA567', 'Carlos Torres', '', '9876543210', 'Transportes YZA', 'Camioneta', 'Reabastecimiento de insumos', 'Granja Porcícola La Floresta', 'Entrega rápida'),
('2023-10-20', '14:40:00', 'BCD890', 'María Gómez', 'Juan Torres', '6789012345', 'Transportes BCD', 'Camión', 'Entrega de productos terminados', 'Granja Porcícola El Tesoro', 'Producto frágil, manejar con cuidado'),
('2023-11-25', '08:30:00', 'EFG123', 'Pedro Ramírez', 'Ana López', '8901234567', 'Transportes EFG', 'Furgoneta', 'Mantenimiento de instalaciones', 'Granja Porcícola Santa Cruz', 'Revisar sistemas de seguridad'),
('2023-12-30', '10:50:00', 'HIJ456', 'Luis Gómez', 'Carlos Pérez', '5678901234', 'Transportes HIJ', 'Camioneta', 'Recolección de muestras', 'Granja Porcícola Los Alpes', 'Muestras perecederas, transportar en frío'),
('2022-01-05', '09:30:00', 'KLM789', 'Ana Martínez', 'Juan Torres', '1234567890', 'Transportes KLM', 'Camión', 'Entrega de alimentos', 'Granja Porcícola El Porvenir', 'Ninguna'),
('2022-02-10', '11:45:00', 'NOP012', 'José Pérez', 'María Gutiérrez', '9876543210', 'Transportes NOP', 'Furgoneta', 'Inspección sanitaria', 'Granja Porcícola San Juan', 'Revisión exhaustiva'),
('2022-03-15', '14:20:00', 'QRS345', 'Carlos Ramírez', 'Ana Martínez', '6549873210', 'Transportes QRS', 'Camioneta', 'Recolección de productos', 'Granja Porcícola Los Robles', 'Entrega inmediata'),
('2022-04-20', '08:00:00', 'TUV678', 'María López', 'Luis Torres', '3216549870', 'Transportes TUV', 'Camión', 'Entrega de suministros', 'Granja Porcícola El Rosal', 'Necesita asistencia para cargar'),
('2022-05-25', '10:10:00', 'WXY901', 'Pedro Gómez', 'Juan Pérez', '7894561230', 'Transportes WXY', 'Furgoneta', 'Mantenimiento de equipos', 'Granja Porcícola La Cabaña', 'Reparación urgente'),
('2022-06-30', '13:45:00', 'ZAB234', 'Luis Torres', 'María López', '5647891230', 'Transportes ZAB', 'Camioneta', 'Recolección de desechos', 'Granja Porcícola La Granja', 'Carga peligrosa, manejar con precaución'),
('2022-07-05', '16:30:00', 'CDE567', 'Carlos Ramírez', 'Ana Martínez', '8901234560', 'Transportes CDE', 'Camión', 'Entrega de medicamentos', 'Granja Porcícola Los Laureles', 'Entrega nocturna');


INSERT INTO monitoreo_agua (fecha_hora, nivel_agua_porcentaje, flujo_agua_litros_hora) VALUES
('2024-05-01 00:00:00', 78.5, 450.25),
('2024-05-01 01:00:00', 82.3, 460.75),
('2024-05-01 02:00:00', 80.1, 470.50),
('2024-05-01 03:00:00', 85.4, 480.25),
('2024-05-01 04:00:00', 79.9, 490.00),
('2024-05-01 05:00:00', 81.2, 500.25),
('2024-05-01 06:00:00', 83.8, 510.50),
('2024-05-01 07:00:00', 77.3, 520.75),
('2024-05-01 08:00:00', 80.5, 530.00),
('2024-05-01 09:00:00', 81.7, 540.25),
('2024-05-01 10:00:00', 84.2, 550.50),
('2024-05-01 11:00:00', 78.9, 560.75),
('2024-05-01 12:00:00', 80.6, 570.00),
('2024-05-01 13:00:00', 82.4, 580.25),
('2024-05-01 14:00:00', 79.5, 590.50),
('2024-05-01 15:00:00', 81.3, 600.75),
('2024-05-01 16:00:00', 83.7, 610.00),
('2024-05-01 17:00:00', 78.2, 620.25),
('2024-05-01 18:00:00', 80.0, 630.50),
('2024-05-01 19:00:00', 81.5, 640.75),
('2024-05-01 20:00:00', 84.1, 650.00),
('2024-05-01 21:00:00', 78.7, 660.25),
('2024-05-01 22:00:00', 80.3, 670.50),
('2024-05-01 23:00:00', 82.9, 680.75),
('2024-05-02 00:00:00', 79.2, 690.00),
('2024-05-02 01:00:00', 81.6, 700.25),
('2024-05-02 02:00:00', 84.0, 710.50),
('2024-05-02 03:00:00', 78.8, 720.75),
('2024-05-02 04:00:00', 80.4, 730.00),
('2024-05-02 05:00:00', 83.1, 740.25),
('2024-05-02 06:00:00', 78.5, 750.50),
('2024-05-02 07:00:00', 82.0, 760.75),
('2024-05-02 08:00:00', 84.3, 770.00),
('2024-05-02 09:00:00', 79.9, 780.25),
('2024-05-02 10:00:00', 81.1, 790.50),
('2024-05-02 11:00:00', 83.5, 800.75),
('2024-05-02 12:00:00', 78.7, 810.00),
('2024-05-02 13:00:00', 80.9, 820.25),
('2024-05-02 14:00:00', 82.7, 830.50),
('2024-05-02 15:00:00', 79.3, 840.75),
('2024-05-02 16:00:00', 81.4, 850.00),
('2024-05-02 17:00:00', 83.9, 860.25),
('2024-05-02 18:00:00', 78.6, 870.50),
('2024-05-02 19:00:00', 81.0, 880.75),
('2024-05-02 20:00:00', 83.2, 890.00),
('2024-05-02 21:00:00', 79.4, 900.25),
('2024-05-02 22:00:00', 80.8, 910.50),
('2024-05-02 23:00:00', 82.6, 920.75),
('2024-05-03 00:00:00', 78.9, 930.00);


