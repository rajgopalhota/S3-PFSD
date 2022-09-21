import pytest
@pytest.mark.parametrize(("num","output"),[(1,1),(2,2),(3,6),(4,24)])
def test_factorial(num,output):
    fact=1
    for i in range (1,num+1):
        fact=fact*i
    assert fact==output

