import numpy as np
import run

def test_min():
  assert run.min([1,2,3,4,5]) == 1
  assert run.min([4,5,6,2,1,2]) == 1
  assert run.min([5,6,3,-10,2]) == -10
  assert type(run.min([2,3,3,3,])).__module__ == np.__name__
