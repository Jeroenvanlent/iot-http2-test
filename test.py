import hyper
import time

times = 100

start1 = time.clock()
for x in range(0, times):
  con1 = hyper.HTTP11Connection('iot.local', '1100')
  con1.request('GET', '/')
  resp1 = con1.get_response()
end1 = time.clock()

start2 = time.clock()
for x in range(0, times):
  con2 = hyper.HTTP11Connection('iot.local', '1200')
  con2.request('GET', '/')
  resp2 = con2.get_response()
end2 = time.clock()

start3 = time.clock()
for x in range(0, times):
  con3 = hyper.HTTP20Connection('iot.local', '1300')
  con3.request('GET', '/')
  resp3 = con3.get_response()
end3 = time.clock()

print("HTTPv1")
print(resp1.status)
print(end1 - start1)

print("HTTPv1 with SSL")
print(resp2.status)
print(end2 - start2)

print("HTTPv2")
print(resp3.status)
print(end3 - start3)
