from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        assert checkout_solution.checkout("ABCl") == -1
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("AAABBABCD") == 130 + 45 + 115
        assert checkout_solution.checkout("BBBBBEEEE") == 75 + 160
        assert checkout_solution.checkout("BBEEEE") == 160
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("GGGG") == 80
        assert checkout_solution.checkout(10 * "H" + 7 * "H") == 80 + 45 + 20
        assert checkout_solution.checkout("IIII") == 140
        assert checkout_solution.checkout("JJ") == 120
        assert checkout_solution.checkout("KKK") == 150 + 80
        assert checkout_solution.checkout("LLL") == 270
        assert checkout_solution.checkout("MMM") == 45
        assert checkout_solution.checkout("MMMNNN") == 120 + 30     
        assert checkout_solution.checkout("OO") == 20
        assert checkout_solution.checkout("PPPPPPP") == 300
        assert checkout_solution.checkout("QQQQ") == 110
        assert checkout_solution.checkout("QQQQRRRR") == 80 + 200
        assert checkout_solution.checkout("S") == 30
        assert checkout_solution.checkout("T") == 20
        assert checkout_solution.checkout("UUUUU") == 160
        assert checkout_solution.checkout(5 * "V") == 130 + 90
        assert checkout_solution.checkout("W") == 20
        assert checkout_solution.checkout("X") == 90
        assert checkout_solution.checkout("Y") == 10
        assert checkout_solution.checkout("Z") == 50
