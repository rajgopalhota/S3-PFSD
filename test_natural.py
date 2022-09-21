import pytest
@pytest.mark.parametrize("num,output",[(1,1),(2,3),(3,6),(4,10)])
def test_natural(num,output):
 assert (num*(num+1)/2)==output
