--1
CREATE TABLE areas (
  id_area SERIAL PRIMARY KEY,
  nombre_area VARCHAR(50) NOT NULL
);

--2
CREATE TABLE corrales (
  num_corral integer PRIMARY KEY,
  id_area integer,
  aforo integer not null,
  cantidad_dentro integer not null,
  foreign key (id_area) references areas (id_area)
);

--3 I: interno, E externo
CREATE TABLE inventario_animales (
  id_animal SERIAL PRIMARY KEY,
  id_corral INTEGER NOT NULL,
  raza VARCHAR(50) NOT NULL,
  sexo VARCHAR(1) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  peso DECIMAL(10,2) NOT NULL,
  estado_salud VARCHAR(50) NOT NULL,
  origen VARCHAR(1) NOT NULL CHECK (origen IN ('I', 'E')),
  FOREIGN KEY (id_corral) REFERENCES corrales (num_corral)
);

--4
CREATE TABLE movimientos (
  id_movimiento SERIAL PRIMARY KEY,
  id_animal INTEGER NOT NULL,
  fecha DATE NOT NULL,
  area_origen INTEGER NOT NULL,
  area_destino INTEGER NOT NULL,
  FOREIGN KEY (id_animal) REFERENCES inventario_animales (id_animal),
  FOREIGN KEY (area_origen) REFERENCES areas (id_area),
  FOREIGN KEY (area_destino) REFERENCES areas (id_area)
);

--5
CREATE TABLE registro_partos (
  id_parto SERIAL PRIMARY KEY,
  id_animal INTEGER NOT NULL,
  fecha_parto DATE NOT NULL,
  nacidos_vivos INTEGER NOT NULL,
  nacidos_muertos INTEGER NOT NULL,
  vivos_48h INTEGER NOT NULL,
  vivos_destete INTEGER NOT NULL,
  observaciones VARCHAR(255),
  FOREIGN KEY (id_animal) REFERENCES inventario_animales (id_animal)
);

--6 // MN: Monta Natural, IA: Inseminación Artificial, TE: Transferencia de Embriones, O: Otros (Especificar en observaciones)
CREATE TABLE registro_inseminaciones (
  id_inseminacion SERIAL PRIMARY KEY,
  id_madre INTEGER NOT NULL,
  id_padre INTEGER,
  fecha_inseminacion DATE NOT NULL,
  tipo_inseminacion VARCHAR(2) NOT NULL CHECK (tipo_inseminacion IN ('MN', 'IA', 'TE', 'O')),
  observaciones VARCHAR(255),
  FOREIGN KEY (id_madre) REFERENCES inventario_animales (id_animal),
  FOREIGN KEY (id_padre) REFERENCES inventario_animales (id_animal)
);

--7
CREATE TABLE origen_externo (
  id_origen_externo SERIAL PRIMARY KEY,
  id_animal INTEGER NOT NULL,
  fecha_compra DATE NOT NULL,
  fecha_ingreso DATE NOT NULL,
  finalidad_compra VARCHAR(50) NOT NULL,
  etapa_productiva VARCHAR(50) NOT NULL,
  granja_origen VARCHAR(255) NOT NULL,
  edad INTEGER NOT NULL,
  vendedor VARCHAR(255),
  peso_compra DECIMAL(10,2),
  observaciones VARCHAR(255),
  FOREIGN KEY (id_animal) REFERENCES inventario_animales (id_animal)
);

--8
CREATE TABLE origen_interno (
  id_origen_interno SERIAL PRIMARY KEY,
  fecha_cambio_etapa DATE NOT NULL,
  finalidad VARCHAR(50) NOT NULL,
  etapa_productiva VARCHAR(50) NOT NULL,
  id_madre INTEGER NOT NULL,
  id_padre INTEGER,
  observaciones VARCHAR(255),
  FOREIGN KEY (id_madre) REFERENCES inventario_animales (id_animal),
  FOREIGN KEY (id_padre) REFERENCES inventario_animales (id_animal)
);

--9
CREATE TABLE lotes_lechones (
  id_lote SERIAL PRIMARY KEY,
  id_corral INTEGER NOT NULL,
  cantidad_lechones INTEGER NOT NULL,
  fecha_ingreso_lote DATE NOT NULL,
  dias_precebo INTEGER,
  observaciones VARCHAR(255),
  FOREIGN KEY (id_corral) REFERENCES corrales (num_corral)
);

--10
CREATE TABLE venta_lotes (
  id_venta_lotes SERIAL PRIMARY KEY,
  fecha_venta DATE NOT NULL,
  id_lote INTEGER NOT NULL,
  peso_promedio NUMERIC(5,2) NOT NULL,
  precio_lote NUMERIC(10,2) NOT NULL,
  destino VARCHAR(50) NOT NULL,
  comprador VARCHAR(50) NOT NULL,
  observaciones VARCHAR(255),
  FOREIGN KEY (id_lote) REFERENCES lotes_lechones (id_lote)
);

--11
CREATE TABLE venta_unidad (
  id_venta_unidad SERIAL PRIMARY KEY,
  fecha_venta DATE NOT NULL,
  id_lote INTEGER NOT NULL,
  peso_lechon NUMERIC(5,2) NOT NULL,
  precio_unidad NUMERIC(10,2) NOT NULL,
  destino VARCHAR(50) NOT NULL,
  comprador VARCHAR(50) NOT NULL,
  observaciones VARCHAR(255),
  FOREIGN KEY (id_lote) REFERENCES lotes_lechones (id_lote)
);

--12
CREATE TABLE medicamentos (
  id_medicamento SERIAL PRIMARY KEY,
  nombre_medicamento VARCHAR(50) NOT NULL,
  principio_activo VARCHAR(50) NOT NULL,
  laboratorio VARCHAR(50) NOT NULL,
  presentacion VARCHAR(50) NOT NULL,
  fecha_vencimiento DATE NOT NULL,
  stock INTEGER NOT NULL,
  lote_medicamento VARCHAR(50),
  vendedor_medicamento VARCHAR(50),
  precio_unidad NUMERIC(10,2) NOT NULL,
  fecha_compra DATE,
  observaciones VARCHAR(255)
);

--13
CREATE TABLE tratamientos (
  id_tratamiento SERIAL PRIMARY KEY,
  tipo_tratamiento VARCHAR(50) NOT NULL,
  detalle_tratamiento VARCHAR(255) NOT NULL,
  id_medicamento INTEGER,
  dosis NUMERIC(10,2),
  observaciones VARCHAR(255),
  FOREIGN KEY (id_medicamento) REFERENCES medicamentos (id_medicamento)
);

--14
CREATE TABLE lotes_tratamientos (
  id_lote_tratamiento SERIAL PRIMARY KEY,
  id_tratamiento INTEGER NOT NULL,
  id_lote INTEGER NOT NULL,
  fecha_aplicacion_lote DATE NOT NULL,
  dosis_lote NUMERIC(10,2),
  observaciones_lote VARCHAR(255),
  FOREIGN KEY (id_tratamiento) REFERENCES tratamientos (id_tratamiento),
  FOREIGN KEY (id_lote) REFERENCES lotes_lechones (id_lote)
);

--15
CREATE TABLE tratamientos_animales (
  id_tratamiento_animal SERIAL PRIMARY KEY,
  id_tratamiento INTEGER NOT NULL,
  id_animal INTEGER NOT NULL,
  fecha_tratamiento_animal DATE NOT NULL,
  observaciones_animal VARCHAR(255),
  FOREIGN KEY (id_tratamiento) REFERENCES tratamientos (id_tratamiento),
  FOREIGN KEY (id_animal) REFERENCES inventario_animales (id_animal)
);

--16
CREATE TABLE ingreso_vehiculos (
  id_ingreso_vehiculo SERIAL PRIMARY KEY,
  fecha_ingreso DATE NOT NULL,
  hora_ingreso TIME NOT NULL,
  placa_vehiculo VARCHAR(20) NOT NULL UNIQUE,
  nombre_conductor VARCHAR(50) NOT NULL,
  telefono_conductor VARCHAR(20),
  empresa_transportista VARCHAR(50) NOT NULL,
  tipo_vehiculo VARCHAR(50) NOT NULL,
  motivo_ingreso VARCHAR(255) NOT NULL,
  ultimo_predio_visitado VARCHAR(50),
  observaciones VARCHAR(255)
);

-- Crear la tabla monitoreo_agua
CREATE TABLE monitoreo_agua (
  id_monitoreo serial PRIMARY KEY,
  fecha_hora timestamp NOT NULL,
  nivel_agua_porcentaje numeric(3,1) NOT NULL CHECK (nivel_agua_porcentaje BETWEEN 0.0 AND 100.0),
  flujo_agua_litros_hora numeric(10,2) NOT NULL
);



























