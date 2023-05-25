from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        assert checkout_solution.checkout("ABCL") == -1
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("AAABBABCD") == 130 + 45 + 115
