from m5stack import *
from m5ui import *
from uiflow import *
import espnow
import wifiCfg
import time
import hat


setScreenColor(0x111111)

hat_joyc_5 = hat.get(hat.JOYC)

I = None
FWD_BACK = None
L_R = None
R = None
S = None

wifiCfg.wlan_ap.active(True)
wifiCfg.wlan_sta.active(True)
espnow.init()


import math




lcd.font(lcd.FONT_DefaultSmall)
lcd.print('Designed By', 25, 200, 0xffffff)
lcd.print('Felipe Galindo', 20, 210, 0xffffff)
lcd.print('in Minnesota', 25, 220, 0xffffff)
lcd.print('Connecting To RONALD', 5, 100, 0xffffff)
lcd.print('MAC', 60, 20, 0xffffff)
lcd.print((espnow.get_mac_addr()), 20, 30, 0xffffff)
espnow.add_peer('4c:75:25:9e:9a:b1', id=2)
espnow.set_pmk('101GOLDY010')
wait(5)
lcd.fill(0x000000)
I = 0
lcd.font(lcd.FONT_DejaVu24)
lcd.print(((str('T:') + str(("%.2f"%((axp.getTempInAXP192())))))), 0, 170, 0xffffff)
lcd.print(((str('V:') + str(("%.2f"%((axp.getBatVoltage())))))), 0, 190, 0xffffff)
lcd.print(((str('CHG:') + str((axp.getChargeState())))), 0, 210, 0xffffff)
while True:
  lcd.rect((-10), (-1), 150, 25, fillcolor=0x000000)
  lcd.print((I * 3), 0, 0, 0xffff00)
  I = I + 1
  FWD_BACK = (hat_joyc_5.GetX(0)) - 100
  L_R = -((hat_joyc_5.GetY(0)) - 100)
  R = math.ceil(((hat_joyc_5.GetX(1)) - 100) / 2)
  S = hat_joyc_5.GetY(1)
  if math.fabs(FWD_BACK) < 10:
    FWD_BACK = 0
  if math.fabs(L_R) < 10:
    L_R = 0
  if math.fabs(R) < 10:
    R = 0
  if math.fabs(S) < 10:
    S = 0
  hat_joyc_5.SetLedColor(0xff)
  espnow.send(id=2, data=str(((str('X') + str(FWD_BACK)))))
  wait_ms(50)
  hat_joyc_5.SetLedColor(0xff0000)
  espnow.send(id=2, data=str(((str('Y') + str(L_R)))))
  wait_ms(50)
  hat_joyc_5.SetLedColor(0xff00)
  espnow.send(id=2, data=str(((str('R') + str(R)))))
  wait_ms(50)
  hat_joyc_5.SetLedColor(0xffffff)
  espnow.send(id=2, data=str(((str('S') + str(S)))))
  wait_ms(10)
  lcd.rect((-10), 25, 150, 120, fillcolor=0x000000)
  lcd.print(((str('X') + str(FWD_BACK))), 0, 30, 0xffffff)
  lcd.print(((str('Y') + str(L_R))), 0, 60, 0xffffff)
  lcd.print(((str('R') + str(R))), 0, 90, 0xffffff)
  lcd.print(((str('S') + str(S))), 0, 120, 0xffffff)
  if I % 33 == 0:
    lcd.clear()
    lcd.print(((str('T:') + str(("%.2f"%((axp.getTempInAXP192())))))), 0, 170, 0xffffff)
    lcd.print(((str('V:') + str(("%.2f"%((axp.getBatVoltage())))))), 0, 190, 0xffffff)
    lcd.print(((str('CHG:') + str((axp.getChargeState())))), 0, 210, 0xffffff)
  wait_ms(2)
