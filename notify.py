
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
tiempo_muestreo = tiempo_muestreo * 60 #convertir a segundos
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
            


#1. Notificar cuando falten 10 dias para el parto
def notificar_proximos_partos(id_partos, cursor, client, Cellphones, cellFrom):
    fecha=str(os.popen("date +%c").read()).rstrip()
    fecha_en_10_dias = datetime.now() + timedelta(days=10)
    ultima_hora = datetime.now() - timedelta(hours=1)
    
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
    cursor.execute(query, (ultima_hora,))
    records = cursor.fetchall()
    print("1. Proximos partos: REGISTROS CONSULTA: ", records)

    for record in records:
        numero=record[0]
        #print("Proximos partos: Mensajes ya enviados: id_parto: ", id_partos)
        if numero not in id_partos:
            id_partos.add(numero)
            for cellphone in Cellphones:
                print("Proximos partos: Enviando mensaje a: ", cellphone)
                #message = client.messages.create(to=cellphone,
                    #from_=cellFrom,
                    #body=f"|{fecha}| !!Recordatorio mover a area lactancia!!.  Hoy 105 dias la cerda {record[3]} cumple el ciclo de gestación en 10 dias ( {fecha_en_10_dias} ), Transladar a area de lactacia. Atentamente PorciGest")
                #print(message.sid)
                print("4. Proximos partos: Mensaje 105 dias enviado: ", record[0])
        else:
            print("Proximos partos: El mensaje de texto ya a sido enviado anteriormente para el registro: ", record[0])
    


#2. Notificar parto, 113 dias de gestacion
def notificar_parto(id_parto, cursor, client, Cellphones, cellFrom):
    fecha=str(os.popen("date +%c").read()).rstrip()
    ultima_hora = datetime.now() - timedelta(hours=1)
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
        ri.fecha_inseminacion + INTERVAL '113 days' = CURRENT_DATE;
            """
    cursor.execute(query, (ultima_hora,))
    records = cursor.fetchall()
    print("2. Parto: REGISTROS CONSULTA: ", records)

    for record in records:
        numero=record[0]
        #print("2. Parto: Mensajes ya enviados: id_parto: ", id_parto)
        if numero not in id_parto:
            id_parto.add(numero)
            for cellphone in Cellphones:
                print("Parto: Enviando mensaje a: ", cellphone)
                #message = client.messages.create(to=cellphone,
                    #from_=cellFrom,
                    #body=f"|{fecha}| !!Recordatorio Parto!!. Hoy 113 dias, la cerda {record[3]}. Atentamente PorciGest")
                #print(message.sid)
                print("4. Parto: Mensaje parto enviado: id_inseminacion:", record[0])
        else:
            print("5. Parto: El mensaje de texto ya a sido enviado anteriormente para el registro: ", record[0])




#3. Notificar vacuna de parvovirus. 11 dias postparto, 
def notificar_vacuna_parvovirus(id_lactancia, cursor, client, Cellphones, cellFrom):
    fecha_en_11_dias = datetime.now() + timedelta(days=11)
    ultima_hora = datetime.now() - timedelta(hours=1)
    fecha=str(os.popen("date +%c").read()).rstrip()
    query = """
        SELECT
        rp.id_parto,
        rp.id_animal,
        rp.fecha_parto,
        ia.numero_identificacion_animal
        FROM
        registro_partos rp
        JOIN
        inventario_animales ia ON rp.id_animal = ia.id_animal
        WHERE rp.fecha_parto + INTERVAL '11 days' = CURRENT_DATE;
        """
    cursor.execute(query, (ultima_hora,))
    records = cursor.fetchall()
    print("3. Parvovirus: REGISTROS CONSULTA: ", records)
   
    for record in records:
        numero=record[0]
        #print("2. Mensajes ya enviados: id_parto: ", id_lactancia)
        if numero not in id_lactancia:
            id_lactancia.add(numero)
            for cellphone in Cellphones:
                print("Enviando mensaje a: ", cellphone)
                #message = client.messages.create(to=cellphone,
                    #from_=cellFrom,
                    #body=f"|{fecha}| !!Recordatorio vacuna: Parvovirus!!. A cerda numero: {record[3]}. Atentamente PorciGest")
                #print(message.sid)
                print("Parvovirus: MENSAJE PARVOVIRUS ENVIADO, ID_lactancia:", record[0] )
        else:
            print("Parvovirus: El mensaje de texto ya a sido enviado anteriormente para el registro: ", record[0])




#4. Notificar vacuna Respisure. 6 y 21 dias postparto, a lechones. 
def notificar_vacuna_respisure(id_vacunaRespisure, cursor, client, Cellphones, cellFrom):
    fecha=str(os.popen("date +%c").read()).rstrip()
    ultima_hora = datetime.now() - timedelta(hours=1)
    query = """
        SELECT
        rp.id_parto,
        rp.id_animal,
        rp.fecha_parto,
        ia.numero_identificacion_animal
        FROM
        registro_partos rp
        JOIN
        inventario_animales ia ON rp.id_animal = ia.id_animal
        WHERE (rp.fecha_parto + INTERVAL '6 days' = CURRENT_DATE OR rp.fecha_parto + INTERVAL '21 days' = CURRENT_DATE);
        """
    cursor.execute(query, (ultima_hora,))
    records = cursor.fetchall()
    print("4. Vacuna respisure: REGISTROS CONSULTA: ", records)
   
    for record in records:
        numero=record[0]
        #print(record[0])
        #print("2. Vacuna respisure: Mensajes ya enviados: id_parto: ", id_vacunaRespisure)
        if numero not in id_vacunaRespisure:
            id_vacunaRespisure.add(numero)
            for cellphone in Cellphones:
                print("Vacuna respisure: Enviando mensaje a: ", cellphone)
                #message = client.messages.create(to=cellphone,
                    #from_=cellFrom,
                    #body=f"|{fecha}| !!Recordatorio vacuna Respisure!!. A camada de cerda numero: {record[3]}. Atentamente PorciGest")
                #print(message.sid)
                print("Vacuna respisure: MENSAJE RESPISURE ENVIADO, ID_PARTO:", record[0] )
        else:
            print("Vacuna respisure: El mensaje de texto ya a sido enviado anteriormente para el registro: ", record[0])




#5. Notificar destete. 28 dias postparto, 
def notificar_destete(id_destete, cursor, client, Cellphones, cellFrom):
    fecha=str(os.popen("date +%c").read()).rstrip()
    ultima_hora = datetime.now() - timedelta(hours=1)
    query = """
        SELECT
        rp.id_parto,
        rp.id_animal,
        rp.fecha_parto,
        ia.numero_identificacion_animal
        FROM
        registro_partos rp
        JOIN
        inventario_animales ia ON rp.id_animal = ia.id_animal
        WHERE rp.fecha_parto + INTERVAL '28 days' = CURRENT_DATE;
        """
    cursor.execute(query, (ultima_hora,))
    records = cursor.fetchall()
    print("5. Destete: REGISTROS CONSULTA: ", records)
   
    for record in records:
        numero=record[0]
        #print(record[0])
        #print("2. Destete Mensajes ya enviados: id_destete: ", id_destete)
        if numero not in id_destete:
            id_destete.add(numero)
            for cellphone in Cellphones:
                print("Destete: Enviando mensaje a: ", cellphone)
                print("Destete: MENSAJE DESTETE ENVIADO, ID_parto:", record[0] )
                #message = client.messages.create(to=cellphone,
                    #from_=cellFrom,
                    #body=f"|{fecha}| !!Recordatorio destete y vacunacion!!. A cerda numero: {record[3]}. Atentamente PorciGest")
                #print(message.sid)
        else:
            print("Destete: El mensaje de texto ya a sido enviado anteriormente para el registro: ", record[0])



#6. Notificar desparacitacion lechones lotes, 15 dias duspues de ingresar a precebos
def notificar_desparacitacion(id_lechones, cursor, client, Cellphones, cellFrom):
    fecha=str(os.popen("date +%c").read()).rstrip()
    ultima_hora = datetime.now() - timedelta(hours=1)
    query = """
        SELECT
        lotes.id_lote,
        lotes.fecha_ingreso_lote,
        lotes.cantidad_lechones
        FROM
        lotes_lechones lotes
        WHERE lotes.fecha_ingreso_lote + INTERVAL '15 days' = CURRENT_DATE;
        """
    cursor.execute(query, (ultima_hora,))
    records = cursor.fetchall()
    print("6. Desparacitacion lotes: REGISTROS CONSULTA: ", records)
   
    for record in records:
        numero=record[0]
        #print(record[0])
        #print("2. Lotes: Mensajes ya enviados: id_lote: ", id_lechones)
        if numero not in id_lechones:
            id_lechones.add(numero)
            for cellphone in Cellphones:
                print("Desparacitacion lotes: Enviando mensaje a: ", cellphone)
                #message = client.messages.create(to=cellphone,
                    #from_=cellFrom,
                    #body=f"|{fecha}| !!Recordatorio desparacitacion lote!!. A lote numero: {record[3]}. Atentamente PorciGest")
                #print(message.sid)
                print("Desparacitacion lotes: MENSAJE LECHONES ENVIADO, ID_lote:", record[0] )
        else:
            print("Desparacitacion lotes: El mensaje de texto ya a sido enviado anteriormente para el registro: ", record[0])




#7. Notificar vacuna ecoli. 90 dias despues del servicio, 
def notificar_vacuna_ecoli(id_ecoli, cursor, client, Cellphones, cellFrom):
    fecha=str(os.popen("date +%c").read()).rstrip()
    ultima_hora = datetime.now() - timedelta(hours=1)
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
        ri.fecha_inseminacion + INTERVAL '90 days' = CURRENT_DATE;
        """
    cursor.execute(query, (ultima_hora,))
    records = cursor.fetchall()
    print("7. Vacuna ecoli: REGISTROS CONSULTA: ", records)
   
    for record in records:
        numero=record[0]
        print(record[0])
        #print("2. vacuna ecoli: Mensajes ya enviados: id_inseminacion: ", id_ecoli)
        if numero not in id_ecoli:
            id_ecoli.add(numero)
            for cellphone in Cellphones:
                print("Vacuna ecoli: Enviando mensaje a: ", cellphone)
                #message = client.messages.create(to=cellphone,
                #    from_=cellFrom,
                #    body=f"|{fecha}| !!Recordatorio vacuna: ecoli!!. A cerda numero: {record[3]}. Atentamente PorciGest")
                #print(message.sid)
                print("Vacuna ecoli: MENSAJE ecoli ENVIADO, ID_Inseminacion:", record[0] )
        else:
            print("Vacuna ecoli: El mensaje de texto ya a sido enviado anteriormente para el registro: ", record[0])



#8. Notificacion cuando nivel agua es menor igual al 60%
def notificar_nivel_agua(id_nivel, cursor, client, Cellphones, cellFrom):
    hace_una_hora = datetime.now() - timedelta(hours=1)
    query = """
    SELECT * FROM monitoreo_agua
    WHERE fecha_hora >= %s AND nivel_agua_porcentaje <= 60;
    """
    cursor.execute(query, (hace_una_hora,))
    records = cursor.fetchall()
    print("8. Nivel de agua: REGISTROS CONSULTA: ", records)

    for record in records:
        numero=record[0]
        if numero not in id_nivel:
            id_nivel.add(numero)
            for cellphone in Cellphones:
                print("Nivel agua: Enviando mensaje a: ", cellphone)
                #message = client.messages.create(to=cellphone,
                    #from_=cellFrom,
                    #body="!!Alerta!! Hemos detectado en la  fecha: " + str(record[1].date())+ " a las "+ str(record[1].time().strftime("%H:%M"))+" horas que el nivel del tanque del agua esta al " + str(record[2])+ " % tome las acciones al respecto, Atentamente PorciGest")
                #print(message.sid)
                print("Nivel de agua: MENSAJE NIVEL AGUA ENVIADO: ", record[0])
        else:
            print("Nivel de agua: El mensaje de texto ya a sido enviado para el registro: ", record[0])


def read_records():
    cursor = None
    connection = None
    try:
        print("8. Conectando a la base de datos para lecturas...")
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        cursor = connection.cursor()

        client = Client(account_sid, auth_token)
        Cellphones = ["+573219948081"]
        cellFrom = "+4672500913"

        id_partos = set()
        id_parto = set()
        id_nivel = set()
        id_lactancia = set()
        id_destete = set()
        id_ecoli = set()
        id_vacunaRespisure = set()
        id_lechones = set()

        while True:
            notificar_proximos_partos(id_partos, cursor, client, Cellphones, cellFrom)
            notificar_parto(id_parto, cursor, client, Cellphones, cellFrom)
            notificar_vacuna_parvovirus(id_lactancia, cursor, client, Cellphones, cellFrom)
            notificar_vacuna_respisure(id_vacunaRespisure, cursor, client, Cellphones, cellFrom)
            notificar_destete(id_destete, cursor, client, Cellphones, cellFrom)
            notificar_desparacitacion(id_lechones, cursor, client, Cellphones, cellFrom)
            notificar_vacuna_ecoli(id_ecoli, cursor, client, Cellphones, cellFrom)
            notificar_nivel_agua(id_nivel, cursor, client, Cellphones, cellFrom)
            print("\n")
            time.sleep(5)

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
        print("El sensor de agua (virtual) no está habilitado, iniciando solo el proceso de lectura...")
        p2.start()

    p2.join()
    


#if __name__ == "__main__":
#    p2 = Process(target=read_records)
#    print("El sensor de agua (virtual) no está habilitado, iniciando solo el proceso de lectura...")
#    p2.start()
