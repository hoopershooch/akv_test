import pytest
import even_s



def test_even_s():
    arr = [
        [2,2,2,2,2],
        [2,1,1,1,2],
        [2,1,2,1,2],
        [2,1,1,1,2],
        [2,2,2,2,2]
    ]
    assert even_s.calc_sum(arr,4,4)==32
    assert even_s.calc_sum(arr,2,2)==2
