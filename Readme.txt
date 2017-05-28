Connection:
1. For Arduino

I2C_LCD2004 -------- Arduino uno
    GND ---------------- GND
    VCC ---------------- 5V
    SDA ---------------- A4
    SCL ---------------- A5

2. For Raspberry Pi

I2C_LCD2004 -------- Raspberry Pi
    GND ----------------- GND
    VCC ----------------- 5V
    SDA ----------- GPIO2(I2C1_SDA)
    SCL ----------- GPIO3(I2C1_SCL)