import hyper
import time
import timeit

times = 1

print("Test: Request single file (regular requests)")
raw_input("Press Enter to start testing HTTPv1")
start1 = time.time()
for x in range(0, times):
  con1 = hyper.HTTP11Connection('iot.local', '1100')
  con1.request('GET', '/')
  con1.get_response().read()
end1 = time.time()

print("HTTPv1")
print(end1 - start1)

raw_input("Press Enter to start testing HTTPv1 with SSL")
start2 = time.time()
for x in range(0, times):
  con2 = hyper.HTTP11Connection('iot.local', '1200', 'True')
  con2.request('GET', '/')
  resp2 = con2.get_response().read()
end2 = time.time()

print("HTTPv1 with SSL")
print(end2 - start2)

raw_input("Press Enter to start testing HTTPv2 with SSL")
start3 = time.time()
for x in range(0, times):
  con3 = hyper.HTTP20Connection('iot.local', '1300', 'True')
  con3.request('GET', '/')
  resp3 = con3.get_response()
end3 = time.time()

print("HTTPv2")
print(end3 - start3)
