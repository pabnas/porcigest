import psycopg2
import dotenv
import random
import os
import time
from multiprocessing import Process
from datetime import datetime, timedelta
from os.path import join, dirname
from twilio.rest import Client

dotenv_path = join('/django/porcigest/.env')
dotenv.load_dotenv(dotenv_path)

host = "db"
database = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
port = 5432

account_sid = os.getenv("IOT_ACCOUNT_SID")
auth_token = os.getenv("IOT_AUTH_TOKEN")
tiempo_muestreo = int(os.getenv("TIEMPO_DE_MUESTREO_MINUTOS"))
tiempo_muestreo = tiempo_muestreo * 60
print(f"Tiempo de muestreo: {tiempo_muestreo} segundos")
sensor_agua = os.getenv("SENSOR_AGUA")


def insert_records():
    cursor = None
    connection = None
    try:
        print("Conectando a la base de datos para inserciones...")
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        start_time = datetime.now()

        while True:
            nivel_agua_porcentaje = round(random.uniform(0.0, 100.0), 1)
            flujo_agua_litros_hora = round(random.uniform(0.0, 1000.0), 2)
            query = """
            INSERT INTO monitoreo_agua (fecha_hora, nivel_agua_porcentaje, flujo_agua_litros_hora)
            VALUES (%s, %s, %s);
            """
            cursor.execute(query, (start_time, nivel_agua_porcentaje, flujo_agua_litros_hora))
            connection.commit()
            print(f"Registro insertado: {start_time}, {nivel_agua_porcentaje}, {flujo_agua_litros_hora}")

            time.sleep(tiempo_muestreo)

    except Exception as error:
        print(f"Error al conectar a la base de datos para inserciones: {error}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


def notificar_proximos_partos(id_partos, cursor, client, Cellphones):
    query = """
        SELECT
        ri.id_inseminacion,
        ri.id_madre,
        ri.fecha_inseminacion,
        ia.numero_identificacion_animal
        FROM
        registro_inseminaciones ri
        JOIN
        inventario_animales ia ON ri.id_madre = ia.id_animal
        WHERE
        ri.fecha_inseminacion + INTERVAL '115 days' = CURRENT_DATE + INTERVAL '10 days';
            """
    cursor.execute(query)
    records = cursor.fetchall()

    for record in records:
        numero=record[0]
        print(record)
        if numero not in id_partos:
            id_partos.add(numero)
            for cellphone in Cellphones:
                print("Enviando mensaje a: ", cellphone)
                message = client.messages.create(to=cellphone,
                            from_="+4672500913",
                            body=f"Recordatorio!!, estimado Franki la cerda con número de identificación {record[3]} cumple el ciclo de gestación en 10 dias, Atentamente PorciGEST")
                print(message.sid)
        else:
            print("El mensaje de texto ya a sido enviado para el registro: ", record[0])


def notificar_nivel_agua(id_nivel, cursor, client, Cellphones):
    hace_una_hora = datetime.now() - timedelta(hours=1)
    query = """
    SELECT * FROM monitoreo_agua
    WHERE fecha_hora >= %s AND nivel_agua_porcentaje < 50;
    """
    cursor.execute(query, (hace_una_hora,))
    records = cursor.fetchall()

    for record in records:
        numero=record[0]
        if numero not in id_nivel:
            id_nivel.add(numero)
            for cellphone in Cellphones:
                print("Enviando mensaje a: ", cellphone)
                message = client.messages.create(to=cellphone,
                            from_="+4672500913",
                            body="Estimado Franki hemos detectado en la  fecha: " + str(record[1].date())+ " a las "+ str(record[1].time().strftime("%H:%M:%S"))+" horas que el nivel del tanque del agua esta por debajo del " + str(record[2])+ " % tome las acciones al respecto, Atentamente PorciGEST")
                print(message.sid)
        else:
            print("El mensaje de texto ya a sido enviado para el registro: ", record[0])


def read_records():
    cursor = None
    connection = None
    try:
        print("Conectando a la base de datos para lecturas...")
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        cursor = connection.cursor()

        client = Client(account_sid, auth_token)
        Cellphones = ["+573187809166"]

        id_partos = set()
        id_nivel = set()

        while True:
            notificar_proximos_partos(id_partos, cursor, client, Cellphones)
            notificar_nivel_agua(id_nivel, cursor, client, Cellphones)
            time.sleep(4)

    except Exception as error:
        print(f"Error al conectar a la base de datos para lecturas: {error}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    p2 = Process(target=read_records)

    if sensor_agua == "T":
        print("El sensor de agua está habilitado, iniciando ambos procesos...")
        p1 = Process(target=insert_records)
        p1.start()
        p2.start()
        p1.join()
    else:
        print("El sensor de agua no está habilitado, iniciando solo el proceso de lectura...")
        p2.start()

    p2.join()


