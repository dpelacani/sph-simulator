# -*- coding: utf-8 -
# by observation t-slosh for the data trial2.csv should be arround 3

def test_task5():
    Cx, Cy, ts, tslosh = peak('trial2.csv', 20, mv_avN=1)
    assert  (tslosh < 3.5)
    assert  (tslosh < 2.5)