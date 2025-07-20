#include <Adafruit_ADS1015.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_MCP4725.h>
#include <math.h>

#define DDS_FREQ_PIN 9
#define SENSOR_HALL A0
#define SENSOR_RTD A1
#define SENSOR_PHOTO A2

Adafruit_ADS1115 ads;       // For precision ADC
Adafruit_MCP4725 dds_dac;   // Digital to analog (for DDS freq control)

float omega_base = 314.159;  // 50 Hz base frequency * 2π (rads)
float harmonic_coeffs[] = {3.0, 6.0, 9.0};
float amp_base = 1.5;        // Nominal DDS amplitude

void setup() {
  Serial.begin(115200);
  Wire.begin();

  ads.begin();
  dds_dac.begin(0x60); // I2C address

  pinMode(DDS_FREQ_PIN, OUTPUT);
  analogWrite(DDS_FREQ_PIN, 0);
}

void loop() {
  // Read sensors
  int hall_raw = ads.readADC_SingleEnded(0);
  int rtd_raw = ads.readADC_SingleEnded(1);
  int photo_raw = ads.readADC_SingleEnded(2);

  float mag_field = (hall_raw * 0.000125); // Convert to Tesla approx
  float temp_c = (rtd_raw * 0.03125);      // Simplified
  float optical_v = (photo_raw * 0.001);   // Volts approximation

  // Compute harmonic phase response
  float omega = omega_base;
  float signal = 0.0;
  float t = millis() / 1000.0;

  for (int i = 0; i < 3; i++) {
    signal += amp_base * sin(harmonic_coeffs[i] * omega * t);
  }

  // Normalize and output to DAC
  float output_v = (signal + 3.0) / 6.0 * 4095.0; // Normalize to 0–4095
  dds_dac.setVoltage((uint16_t)output_v, false);

  // Serial Output
  Serial.print("T:"); Serial.print(temp_c);
  Serial.print(" | M:"); Serial.print(mag_field);
  Serial.print(" | L:"); Serial.print(optical_v);
  Serial.print(" | DDS:"); Serial.println(output_v);

  delay(100);  // 10 Hz sampling rate
}
