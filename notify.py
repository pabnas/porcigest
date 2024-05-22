import psycopg2
import dotenv
import random
import os
import time
from multiprocessing import Process
from datetime import datetime, timedelta
from twilio.rest import Client

dotenv.load_dotenv()

host = "localhost"
database = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
port = 5432

account_sid = os.getenv("IOT_ACCOUNT_SID")
auth_token = os.getenv("IOT_AUTH_TOKEN")


def insert_records():
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
            time.sleep(10)

    except Exception as error:
        print(f"Error al conectar a la base de datos para inserciones: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def read_records():
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
        Cellphones = ["+573187809166","+573219948081"]

        numeros = set()
        while True:
            # hace_una_hora = datetime.now() - timedelta(hours=1)
            # query = """
            # SELECT * FROM monitoreo_agua
            # WHERE fecha_hora >= %s AND nivel_agua_porcentaje < 50;
            # """
            # cursor.execute(query, (hace_una_hora,))
            # records = cursor.fetchall()

            # for record in records:
            #     _ = "-"*50
            #     numero=record[0]
            #     if numero not in numeros:
            #         numeros.add(numero)
            #         for cellphone in Cellphones:
            #             print("Enviando mensaje a: ", cellphone)
            #             message = client.messages.create(to=cellphone,
            #                         from_="+4672500913",
            #                         body="Estido Franki hemos detectado en la  fecha: " + str(record[1].date())+ " a las "+ str(record[1].time().strftime("%H:%M:%S"))+" horas que el nivel del tanque del agua esta por debajo del " + str(record[2])+ " % tome las acciones al respecto, Atentamente PorciGEST")
            #             print(message.sid)
            #     else:
            #         print("El mensaje de texto ya a sido enviado para el registro: ", record[0])

            #     print(_)
            #     print(record)

            time.sleep(6)

    except Exception as error:
        print(f"Error al conectar a la base de datos para lecturas: {error}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    p1 = Process(target=insert_records)
    p2 = Process(target=read_records)

    p1.start()
    p2.start()

    p1.join()
    p2.join()


