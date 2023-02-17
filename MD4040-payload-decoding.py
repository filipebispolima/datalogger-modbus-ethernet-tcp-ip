"""Dica: Usar o microcontrolador ESP32 devkit v1 com firmware MicroPython versao 1.17 e o software jupyter notebook, para poder executar o codigo abaixo.""" 

import struct

#starting_address=0x41
#register_quantity=120

a = [16928, 0, 17008, 64163, 17241, 11969, 17240, 52448, 17241, 0, 0, 0, 0, 3988, 16384, 0, 0, 0, 0, 54437, 50007, 54437, 50007, 0, 0, 0, 0, 19986, 17341, 19986, 17341, 0, 0, 0, 0, 59234, 17369, 59234, 17369, 0, 16256, 0, 16256, 36985, 16125, 36985, 16125, 45046, 16442, 23399, 16421, 45162, 16417, 0, 0, 0, 0, 13650, 17226, 1742, 15549, 14632, 15803, 7736, 17231, 15240, 17231, 40558, 17060, 29211, 15844, 12832, 16020, 34472, 17059, 64396, 15442, 29422, 15923, 7813, 17391, 13976, 17391, 17285, 17200, 4376, 15545, 64961, 16082, 45773, 17200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32704, 0, 32704, 0, 0, 8369, 18787, 21938, 18927, 0, 0, 20264, 18739, 50376, 18876, 0, 0, 28349, 19485, 47516]

#========== Tensoes de Fase A, B e C ========#
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
#======= Potencia Trifasica e Energia =======#
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
#===== DHT das Tensoes de Fase A, B e C =====#
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
#========= Fator de Potencia e Var ==========#
z1 = struct.pack('>h',a[45])
w1 = struct.pack('>h',a[46])
w1z1 = w1 + z1
            
p1 = struct.pack('>h',a[29])
q1 = struct.pack('>h',a[30])
q1p1 = q1 + p1
#============================================#
k3 = struct.unpack('>f', w1z1)[0]
k4 = struct.unpack('>f', q1p1)[0]
print(r1,s1,t1,r2,s2,t2,k1,k2,r3,s3,t3,r4,s4,t4,k3,k4)
#================== Result ==================# 
""" 217.979 216.1826 217.8003 0.0 0.0 2.000951 -215.8306 81.763 2.91699 2.583704 2.526392 0.0 0.0 202.2083 0.4952429 378.6099 """
