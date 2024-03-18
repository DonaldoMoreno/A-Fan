#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

// UUID del servicio Bluetooth
#define SERVICE_UUID "00001101-0000-1000-8000-00805F9B34FB"

class MyServerCallbacks : public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
      Serial.println("Dispositivo central conectado");
    }

    void onDisconnect(BLEServer* pServer) {
      Serial.println("Dispositivo central desconectado");
    }
};

void setup() {
  Serial.begin(115200);

  BLEDevice::init("ESP32_BLE_Test");
  BLEServer *pServer = BLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());

  BLEService *pService = pServer->createService(SERVICE_UUID);
  BLECharacteristic *pCharacteristic = pService->createCharacteristic(
                                         BLEUUID(SERVICE_UUID),
                                         BLECharacteristic::PROPERTY_READ |
                                         BLECharacteristic::PROPERTY_WRITE
                                       );

  pCharacteristic->setValue("Hello World!");
  pService->start();
  BLEAdvertising *pAdvertising = pServer->getAdvertising();
  pAdvertising->start();
}

void loop() {
  delay(1000);
}
