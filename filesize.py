import hyper
import time
import itertools

times = 10
file = "/index.html"
file2 = "/index0.html"

print("Test: Request file with different file sizes and HTTPv2 Stream")
raw_input("Press Enter to start testing HTTPv1")
start1 = time.time()
for x in range(0, times):
  con1 = hyper.HTTP11Connection('iot.local', '1100')
  con1.request('GET', file)
  con1.get_response().read()
  con2 = hyper.HTTP11Connection('iot.local', '1100') 
  con2.request('GET', file2)
  con2.get_response().read()
end1 = time.time()

print("HTTPv1")
#print(resp1.status)
print(end1 - start1)

raw_input("Press Enter to start testing HTTPv1 with SSL")
start2 = time.time()
for x in range(0, times):
  con3 = hyper.HTTP11Connection('iot.local', '1200', 'True')
  con3.request('GET', file)
  con3.get_response().read()
  con4 = hyper.HTTP11Connection('iot.local', '1200', 'True') 
  con4.request('GET', file2)
  con4.get_response().read()
end2 = time.time()

print("HTTPv1 with SSL")
#print(resp2.status)
print(end2 - start2)

raw_input("Press Enter to start testing HTTPv2 with SSL")
start3 = time.time()
con = hyper.HTTP20Connection('iot.local', '1300', 'True')
list = [con.request('GET', file) for i in range(times)]
list2 = [con.request('GET', file2) for i in range(times)]
for number, number2 in itertools.izip_longest(list, list2):
  con.get_response(number).read()
  con.get_response(number2).read()
end3 = time.time()

print("HTTPv2")
#print(resp3.status)
print(end3 - start3)
