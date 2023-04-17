import math;
print("1 : aX^4 + bX^2 + c = 0")
print('VD: 1X^4 + 2X^2 + 3 = 0')
print("2 : aX^4 + bX^2 + c = d")
print('VD: 1X^4 + 2X^2 + 3 = 4')
k = int(input('===> '))
if k == 2:
  a = float(input('nhap he so a : '))
  b = float(input('nhap he so b : '))
  c = float(input('nhap he so c : '))
  d = float(input('nhap he so d : ')) 
  cd = c-d
  dt = b*b-4*a*cd
  if dt < 0:
      print("phuong trinh vo nghiem")
  elif dt > 0:
     cdt = math.sqrt(dt)
     x1 = -b+cdt
     x2 = x1/2*a
     x3 = -b-cdt
     x4 = x3/2*a
     if x2 < 0:
        f1 = math.sqrt(x4)
        f2 = -f1
        print(' nghiem phuong trinh la : ',f1,f2)
     elif x4 < 0:
        f1 = math.sqrt(x2)
        f2 = -f1
     elif x2 and x4 < 0:
        print("phuong trinh vo nghien")
     elif x2 and x4 > 0:
        f1 = math.sqrt(x4)
        f2 = -f1
        f3 = math.sqrt(x2)
        f4 = -f3
        print("phuong trinh co nghiem la : ",f1,f2,f3,f4)
