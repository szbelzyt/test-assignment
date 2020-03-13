import numpy as np
from run import *

def test_min():
  assert min([1,2,3,4,5]) == 1
  assert min([4,5,6,2,1,2]) == 1
  assert min([5,6,3,-10,2]) == -10
  assert type(min([2,3,3,3,])).__module__ == np.__module__
