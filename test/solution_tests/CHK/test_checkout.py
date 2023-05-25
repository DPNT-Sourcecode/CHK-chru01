from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        assert checkout_solution.checkout("ABCL") == -1
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
        
        
