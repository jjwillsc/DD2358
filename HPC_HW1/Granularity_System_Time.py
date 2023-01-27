import time
from timeit import default_timer as timer
import numpy as np

def checktick_time():
   M = 200
   timesfound = np.empty((M,))
   for i in range(M):
      t1 = time.time() # get timestamp from timer
      t2 = time.time() # get timestamp from timer
      while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
          t2 = time.time() # get timestamp from timer
      t1 = t2 # this is outside the loop
      timesfound[i] = t1 # record the time stamp
   minDelta = 1000000
   Delta = np.diff(timesfound) # it should be cast to int only when needed
   minDelta = Delta.min()
   print(f"The clock granularity for time.time() is: {minDelta} \n")
   return minDelta

def checktick_it():
   M = 200
   timesfound = np.empty((M,))
   for i in range(M):
      t1 = timer() # get timestamp from timer
      t2 = timer() # get timestamp from timer
      while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
          t2 = timer() # get timestamp from timer
      t1 = t2 # this is outside the loop
      timesfound[i] = t1 # record the time stamp
   minDelta = 1000000
   Delta = np.diff(timesfound) # it should be cast to int only when needed
   minDelta = Delta.min()
   print(f"The clock granularity for timeit is: {minDelta} seconds \n")
   return minDelta

def checktick_time_ns():
   M = 200
   timesfound = np.empty((M,))
   for i in range(M):
      t1 = time.time_ns() # get timestamp from timer
      t2 = time.time_ns() # get timestamp from timer
      while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
          t2 = time.time_ns() # get timestamp from timer
      t1 = t2 # this is outside the loop
      timesfound[i] = t1 # record the time stamp
   minDelta = 1000000
   Delta = np.diff(timesfound) # it should be cast to int only when needed
   minDelta = Delta.min()
   print(f"The clock granularity for time.time_ns() is: {minDelta} nanoseconds")
   return minDelta


if __name__ == "__main__":
    checktick_time()
    checktick_it()
    checktick_time_ns()

