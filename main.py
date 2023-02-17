from uModBusSerial import uModBusSerial
from uModBusTCP import uModBusTCP
import network
from network import WLAN
import machine
from machine import Pin
import struct
import time
from umqtt.simple import MQTTClient

WiFi_SSID = "TP-LINK_890A"  # Enter Wifi SSID
WiFi_PASS = "12345678"  # Enter Wifi Pasword

PUB_TIME_SEC = 30

SERVER = "mqtt3.thingspeak.com"

# Enter Mqtt Broker Name

PORT = 1883

CHANNEL_ID_1 = "1624156"

CHANNEL_ID_2 = "1505840"

USER = "BRQ2ChgRBTQEKSg4LDUeCCc"  # Enter User Id here

CLIENT_ID = "BRQ2ChgRBTQEKSg4LDUeCCc" #Enter Client Id here

PASSWORD = "FT88kiporHl1oDUVgjEcUHNO" #Enter Password here

#create topic to publish the message

topic_1 = "channels/" + CHANNEL_ID_1 + "/publish" 

topic_2 = "channels/" + CHANNEL_ID_2 + "/publish" 


led = Pin(2, Pin.OUT)  #Led pin is initialise as Output

# Function to implement wifi connection

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WiFi_SSID, WiFi_PASS)
        while not wlan.isconnected():
            pass
    print("Connected to Wifi Router")
    
        
def main():
    while(1):
        try:
            #connect esp32 to wifi
            wifi_connect()
            led.on()
            slave_ip = '10.46.16.40'
            modbus_obj = uModBusTCP(slave_ip)
            slave_addr=0x01
            starting_address=0x41
            register_quantity=80
            signed=False
            a = modbus_obj.read_holding_registers(slave_addr, starting_address, register_quantity, signed)

            #========== Energia elétrica ativa consumida =========#

            #z1 = struct.pack('>h',a[63])
            #w1 = struct.pack('>h',a[64])
            #w1z1 = w1 + z1

            #========== Energia elétrica reativa indutiva ========#
            
            #p1 = struct.pack('>h',a[81])
            #q1 = struct.pack('>h',a[82])
            #q1p1 = q1 + p1

            #========== Energia elétrica ativa gerada ============#
            
            #z = struct.pack('>h',a[73])
            #w = struct.pack('>h',a[74])
            #wz = w + z

            #========== Energia elétrica reativa capacitiva ======#
            
            #p = struct.pack('>h',a[89])
            #q = struct.pack('>h',a[90])
            #qp = q + p
            
            #========== Tensões de Fase A, B e C ========#
            
            u = struct.pack('>h',a[3])
            v = struct.pack('>h',a[4])
            vu = v + u
            
            b = struct.pack('>h',a[5])
            c = struct.pack('>h',a[6])
            cb = c + b
            
            d = struct.pack('>h',a[7])
            e = struct.pack('>h',a[8])
            ed = e + d
            
            #========== Correntes de Fase A, B e C ======#
            
            x = struct.pack('>h',a[9])
            y = struct.pack('>h',a[10])
            yx = y + x
            f = struct.pack('>h',a[11])
            g = struct.pack('>h',a[12])
            gf = g + f
            h = struct.pack('>h',a[13])
            i = struct.pack('>h',a[14])
            ih = i + h
            
            #======= Potência Trifásica e Energia =======#
            
            z = struct.pack('>h',a[21])
            w = struct.pack('>h',a[22])
            wz = w + z
            p = struct.pack('>h',a[73])
            q = struct.pack('>h',a[74])
            qp = q + p
            
            #============================================#
            
            r1 = struct.unpack('>f', vu)[0]
            s1 = struct.unpack('>f', cb)[0]
            t1 = struct.unpack('>f', ed)[0]
            
            r2 = struct.unpack('>f', yx)[0]
            s2 = struct.unpack('>f', gf)[0]
            t2 = struct.unpack('>f', ih)[0]
            
            k1 = struct.unpack('>f', wz)[0]
            k2 = struct.unpack('>f', qp)[0]
            
            #===== DHT das Tensões de Fase A, B e C =====#
            
            u1 = struct.pack('>h',a[47])
            v1 = struct.pack('>h',a[48])
            v1u1 = v1 + u1
            
            b1 = struct.pack('>h',a[49])
            c1 = struct.pack('>h',a[50])
            c1b1 = c1 + b1
            
            d1 = struct.pack('>h',a[51])
            e1 = struct.pack('>h',a[52])
            e1d1 = e1 + d1
            
            #==== DHT das Correntes de Fase A, B e C ====#
            
            x1 = struct.pack('>h',a[53])
            y1 = struct.pack('>h',a[54])
            y1x1 = y1 + x1
            
            f1 = struct.pack('>h',a[55])
            g1 = struct.pack('>h',a[56])
            g1f1 = g1 + f1
            
            h1 = struct.pack('>h',a[57])
            i1 = struct.pack('>h',a[58])
            i1h1 = i1 + h1
            
            #============================================#
            
            r3 = struct.unpack('>f', v1u1)[0]
            s3 = struct.unpack('>f', c1b1)[0]
            t3 = struct.unpack('>f', e1d1)[0]
            
            r4 = struct.unpack('>f', y1x1)[0]
            s4 = struct.unpack('>f', g1f1)[0]
            t4 = struct.unpack('>f', i1h1)[0]
            
            #========= Fator de Potência e Var ==========#
            
            z1 = struct.pack('>h',a[45])
            w1 = struct.pack('>h',a[46])
            w1z1 = w1 + z1
            
            p1 = struct.pack('>h',a[29])
            q1 = struct.pack('>h',a[30])
            q1p1 = q1 + p1
            
            #============================================#
            
            k3 = struct.unpack('>f', w1z1)[0]
            k4 = struct.unpack('>f', q1p1)[0]
            
            payload_1 = "field1="+str(r1)+"&field2="+str(s1)+"&field3="+str(t1)+"&field4="+str(r2)+"&field5="+str(s2)+"&field6="+str(t2)+"&field7="+str(k1)+"&field8="+str(k2)
            
            payload_2 = "field1="+str(r3)+"&field2="+str(s3)+"&field3="+str(t3)+"&field4="+str(r4)+"&field5="+str(s4)+"&field6="+str(t4)+"&field7="+str(k3)+"&field8="+str(k4)
            
            #create a client, connect to the mqtt broker
            
            client = MQTTClient(CLIENT_ID, SERVER, PORT, USER, PASSWORD)
            
            client.connect()
            
            print("Mqtt connected")
            
            client.check_msg()
            
            client.publish(topic_1, payload_1)
            
            client.publish(topic_2, payload_2)
            
            client.disconnect()
            
            led.off()
            
            time.sleep(PUB_TIME_SEC)
            
        except:
            
            machine.reset()
            
main()
