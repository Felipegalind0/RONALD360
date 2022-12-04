from m5stack import *
from m5ui import *
from uiflow import *
import espnow
import wifiCfg
import time
import hat


setScreenColor(0x111111)

hat_roverc_3 = hat.get(hat.ROVERC)

mac = None
data = None
i = None
cmd = None
val = None
j = None
FWD_BACK = None
L_R = None
R = None

wifiCfg.wlan_ap.active(True)
wifiCfg.wlan_sta.active(True)
espnow.init()



def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)



def recv_cb(_):
  global mac,data,i,cmd,val,FWD_BACK,L_R,R,j
  mac, _, data = espnow.recv_data(encoder='str')
  lcd.font(lcd.FONT_DejaVu18)
  lcd.rect((-10), 0, 200, 20, fillcolor=0x000000)
  lcd.print(i, 0, 0, 0xffff33)
  if i % 100 == 0:
    lcd.clear()
    lcd.print(((str('T:') + str(("%.2f"%((axp.getTempInAXP192())))))), 0, 20, 0xffffff)
    lcd.print(((str('Vbt:') + str((axp.getBatVoltage())))), 0, 200, 0xffffff)
    lcd.print(((str('CHG:') + str((axp.getChargeState())))), 0, 220, 0xffffff)
  i = i + 1
  cmd = data[0]
  val = ''
  j_end = float(len(data))
  for j in (2 <= j_end) and upRange(2, j_end, 1) or downRange(2, j_end, 1):
    val = (str(val) + str(data[int(j - 1)]))
  lcd.font(lcd.FONT_DejaVu40)
  if cmd == 'X':
    FWD_BACK = val
    lcd.rect((-10), 50, 200, 35, fillcolor=0x000000)
    lcd.print(((str('X') + str(FWD_BACK))), 0, 50, 0xffffff)
  elif cmd == 'Y':
    L_R = val
    lcd.rect((-10), 100, 200, 35, fillcolor=0x000000)
    lcd.print(((str('Y') + str(L_R))), 0, 100, 0xffffff)
  elif cmd == 'R':
    R = val
    lcd.rect((-10), 150, 200, 35, fillcolor=0x000000)
    lcd.print(((str('R') + str(R))), 0, 150, 0xffffff)
  elif cmd == 'S':
    hat_roverc_3.SetServoPulse(0, (10 * val))
  hat_roverc_3.SetSpeed(int(FWD_BACK), int(L_R), int(R))

  pass
espnow.recv_cb(recv_cb)


def buttonA_wasPressed():
  global mac, data, i, cmd, val, FWD_BACK, L_R, R, j
  hat_roverc_3.SetSpeed(0, 0, 0)
  pass
btnA.wasPressed(buttonA_wasPressed)


hat_roverc_3.SetSpeed(0, 0, 0)
lcd.fill(0x000000)
i = 0
lcd.font(lcd.FONT_DefaultSmall)
lcd.print('Designed By', 25, 200, 0xffffff)
lcd.print('Felipe Galindo', 20, 210, 0xffffff)
lcd.print('in Minnesota', 25, 220, 0xffffff)
lcd.print('Connecting To Remote', 0, 100, 0xffffff)
lcd.print('MAC', 60, 20, 0xffffff)
lcd.print((espnow.get_mac_addr()), 20, 30, 0xffffff)
espnow.add_peer('4c:75:25:9f:9e:f9', id=1)
espnow.set_pmk('101GOLDY010')
wait(5)
lcd.clear()
lcd.font(lcd.FONT_DejaVu18)
lcd.print(((str('T:') + str(("%.2f"%((axp.getTempInAXP192())))))), 0, 20, 0xffffff)
lcd.print(((str('Vbt:') + str((axp.getBatVoltage())))), 0, 200, 0xffffff)
lcd.print(((str('CHG:') + str((axp.getChargeState())))), 0, 220, 0xffffff)
