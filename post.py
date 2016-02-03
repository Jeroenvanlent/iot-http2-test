import hyper
import time

times = 10
file = "/index.html"

print("Test: Post  with HTTPv2")
raw_input("Press Enter to start testing HTTPv1")
start1 = time.clock()
for x in range(0, times):
  con1 = hyper.HTTP11Connection('iot.local', '1100')
  con1.request('POST', file, body=b'hello')
  con1.get_response().read()
end1 = time.clock()

print("HTTPv1")
#print(resp1.status)
print(end1 - start1)

raw_input("Press Enter to start testing HTTPv1 with SSL")
start2 = time.clock()
for x in range(0, times):
  con2 = hyper.HTTP11Connection('iot.local', '1200', 'True')
  con2.request('POST', file, body=b'hello')
  con2.get_response().read()
end2 = time.clock()

print("HTTPv1 with SSL")
#print(resp2.status)
print(end2 - start2)

raw_input("Press Enter to start testing HTTPv2 with SSL")
start3 = time.clock()
con = hyper.HTTP20Connection('iot.local', '1300', 'True')
list = [con.request('POST', file, body=b'hello') for i in range(times)]
for number in list:
  con.get_response(number).read()
end3 = time.clock()

print("HTTPv2")
#print(resp3.status)
print(end3 - start3)
