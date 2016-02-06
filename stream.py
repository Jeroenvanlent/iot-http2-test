import hyper
import time

times = 100
file = "/index.html"

print("Test: Request file with HTTPv2 Stream")
raw_input("Press Enter to start testing HTTPv1")
start1 = time.time()
for x in range(0, times):
  con1 = hyper.HTTP11Connection('iot.local', '1100')
  con1.request('GET', file)
  con1.get_response().read()
end1 = time.time()

print("HTTPv1")
#print(resp1.status)
print(end1 - start1)

raw_input("Press Enter to start testing HTTPv1 with SSL")
start2 = time.time()
for x in range(0, times):
  con2 = hyper.HTTP11Connection('iot.local', '1200', 'True')
  con2.request('GET', file)
  con2.get_response().read()
end2 = time.time()

print("HTTPv1 with SSL")
#print(resp2.status)
print(end2 - start2)

raw_input("Press Enter to start testing HTTPv2 with SSL")
start3 = time.time()
con = hyper.HTTP20Connection('iot.local', '1300', 'True')
list = [con.request('GET', file) for i in range(times)]
for number in list:
  con.get_response(number).read()
end3 = time.time()

print("HTTPv2")
#print(resp3.status)
print(end3 - start3)
