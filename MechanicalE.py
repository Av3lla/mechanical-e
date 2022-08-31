from vpython import *

m = 0.5         # 질량
k = 20.0        # 용수철상수
v0 = 4.0        # v0
 
# 그래픽창, 바닥, 벽 생성
scene = canvas(width=600, height=400, background=vector(0.2, 0.2, 0.2))
bottom = box(length=3, height=0.01, width=1, texture=textures.wood)
wall = box(length=0.01, height=0.5, width=1, texture=textures.wood)
 
 
# 물체와 용수철 생성
square = box(length=0.2, height=0.2, width=0.2, texture=textures.metal)
spring = helix(pos=vector(-bottom.length/2, 0,0), coils=15, radius=0.08, thickness=0.02)
 
 
# 바닥과 벽의 위치를 정해주고 초기속도 v0으로 설정
bottom.pos = vector(0, -square.height/2, 0)
wall.pos = vector(-bottom.length/2, 0.5/2-square.height/2, 0)
square.vx = v0
 
 
# 운동에너지, 탄성에너지, 역학적에너지를 표현하는 막대 생성
rod_k = cylinder(pos=vector(-bottom.length/2, -0.5,0), axis=vector(0.1,0,0), radius=0.05, opacity=0.5)
rod_u = cylinder(pos=vector(-bottom.length/2, -0.7,0), axis=vector(0.1,0,0), radius=0.05, opacity=0.5)
rod_e = cylinder(pos=vector(-bottom.length/2, -0.9,0), axis=vector(0.1,0,0), radius=0.05, opacity=0.5)
 
 
# 텍스트 표시용 라벨 객체 생성
label_Ek = label(pos=vector(-bottom.length/2-0.1, -0.5, 0), text='Ek')
label_Ep = label(pos=vector(-bottom.length/2-0.2, -0.7, 0), text='Ep(탄)')
label_E = label(pos=vector(-bottom.length/2-0.25, -0.9, 0), text='역학적E')

label_x = label(pos=vector(-bottom.length/2, 1.2, 0))
label_l = label(pos=vector(-bottom.length/2+2.9, 1, 0))
label_info = label(pos=vector(-bottom.length/2+2.75, 1.2, 0))

label_EkNum = label(pos=vector(-bottom.length/2+1, -0.5, 0))
label_EpNum = label(pos=vector(-bottom.length/2+1, -0.7, 0))
label_ENum = label(pos=vector(-bottom.length/2+1, -0.9, 0))

label_watermark = label(pos=vector(-bottom.length/2+3.1, -1.2, 0), text="20614 이지원")
 
#------------------------------------------------------------------
# 애니메이션 코드 
#------------------------------------------------------------------
 
dt = 0.0001
 
while True:
    rate(2000)  # 2000 hz의 속도로 루프
 
    # 운동방정식을 통해 가속도를 구하고
    square.a = -(k/m) * square.pos.x
 
    # 속도와 위치 구함
    square.vx += square.a*dt
    square.pos.x += square.vx*dt
 
    # 스프링의 길이를 계산
    spring.length = (square.pos.x - square.length/2) - spring.pos.x
 
    # 운동에너지, 탄성에너지, 역학적에너지를 계산하여 표시
    Ek = 0.5*m*square.vx**2/5
    Ep = 0.5*k*square.pos.x**2/5
    rod_k.axis.x = Ek
    label_EkNum.text = '%.2f' % Ek
    rod_u.axis.x = Ep
    label_EpNum.text = '%.2f' % Ep
    rod_e.axis.x = Ek+Ep
    label_ENum.text = '%.2f' % (Ek+Ep)
 
    label_x.text = '물체 위치 = %.2f' % square.pos.x
    label_l.text = '물체 길이 = %.2f kg' % square.length
    label_info.text = 'm = %.2f kg, k = %.2f N/m' % (m,k)