import asyncio
import bleak

# UUID del servicio Bluetooth
SERVICE_UUID = "00001101-0000-1000-8000-00805F9B34FB"

async def test_connection_and_pairing():
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        try:
            # Escanear dispositivos BLE cercanos
            devices = await bleak.discover()

            # Buscar el dispositivo ESP32 por su nombre
            esp32_device = next((device for device in devices if "ESP32_BLE_Test" in device.name), None)
            if esp32_device is None:
                raise Exception("No se encontró el dispositivo ESP32")

            # Conectar al dispositivo ESP32
            async with bleak.BleakClient(esp32_device) as client:
                # Verificar la conexión
                if not client.is_connected:
                    raise Exception("No se pudo conectar al dispositivo ESP32")

                print("Conexión establecida con el dispositivo ESP32")

                # Leer una característica del dispositivo ESP32 (opcional)
                value = await client.read_gatt_char("00001101-0000-1000-8000-00805F9B34FB")
                print("Valor de la característica leída:", value)

            print("Prueba de conexión y emparejamiento Bluetooth completada con éxito")
            return  # Salir del bucle si la prueba se completa con éxito

        except Exception as e:
            print(f"Intento {attempt}/{max_attempts}: Error durante la prueba:", e)

    print("No se pudo establecer la conexión después de", max_attempts, "intentos")

if __name__ == "__main__":
    asyncio.run(test_connection_and_pairing())
