from __future__ import print_function
import grpc

import randnum_pb2
import randnum_pb2_grpc

def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = randnum_pb2_grpc.RandomNumbersStub(channel)
  gen = stub.GetNext(randnum_pb2.EmptyRequest())
  count = 0
  for num in gen:
    if count % 10000 == 0:
      print(num.value)
      count = 0
    count += 1

if __name__ == '__main__':
  run()
