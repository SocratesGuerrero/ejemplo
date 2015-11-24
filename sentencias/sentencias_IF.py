""" Uso de sentencias, bucles, etc """
#   USANDO IF
#! /usr/bin

a = 0
b = float(raw_input('Ingresa un numero ', ))

if b > 5:
  a = b*1
elif b > 0:	
  a = b*5
else:
  a = 0

print 'El resultado es: ', a

raw_input()