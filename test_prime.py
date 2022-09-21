import pytest
@pytest.mark.parametrize(("n","ou"),[(1,"not prime"),(2,"prime"),(3,"prime")])
def test_k(n,ou):
      for i in range (1,n+1):
        c=0
        for j in range(1,(n+1)):
          if(i%j==0):
            c=c+1
      if(c==2):
         ot="prime"
      else:
         ot="not prime"
      assert ot==ou
