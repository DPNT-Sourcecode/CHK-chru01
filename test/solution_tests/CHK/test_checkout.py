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
        assert checkout_solution.checkout("KKK") == 120 + 70
        assert checkout_solution.checkout("LLL") == 270
        assert checkout_solution.checkout("MMM") == 45
        assert checkout_solution.checkout("MMMNNN") == 120 + 30     
        assert checkout_solution.checkout("OO") == 20
        assert checkout_solution.checkout("PPPPPPP") == 300
        assert checkout_solution.checkout("QQQQ") == 110
        assert checkout_solution.checkout("QQQQRRRR") == 80 + 200
        assert checkout_solution.checkout("S") == 20
        assert checkout_solution.checkout("T") == 20
        assert checkout_solution.checkout("UUUUU") == 160
        assert checkout_solution.checkout(5 * "V") == 130 + 90
        assert checkout_solution.checkout("W") == 20
        assert checkout_solution.checkout("X") == 90
        assert checkout_solution.checkout("Y") == 10
        assert checkout_solution.checkout(""), resp = 0
        assert checkout_solution.checkout("A"), resp = 50
        assert checkout_solution.checkout("B"), resp = 30
        assert checkout_solution.checkout("C"), resp = 20
        assert checkout_solution.checkout("D"), resp = 15
        assert checkout_solution.checkout("E"), resp = 40
        assert checkout_solution.checkout("F"), resp = 10
        assert checkout_solution.checkout("G"), resp = 20
        assert checkout_solution.checkout("H"), resp = 10
        assert checkout_solution.checkout("I"), resp = 35
        assert checkout_solution.checkout("J"), resp = 60
        assert checkout_solution.checkout("K"), resp = 80
        assert checkout_solution.checkout("L"), resp = 90
        assert checkout_solution.checkout("M"), resp = 15
        assert checkout_solution.checkout("N"), resp = 40
        assert checkout_solution.checkout("O"), resp = 10
        assert checkout_solution.checkout("P"), resp = 50
        assert checkout_solution.checkout("Q"), resp = 30
        assert checkout_solution.checkout("R"), resp = 50
        assert checkout_solution.checkout("S"), resp = 30
        assert checkout_solution.checkout("T"), resp = 20
        assert checkout_solution.checkout("U"), resp = 40
        assert checkout_solution.checkout("V"), resp = 50
        assert checkout_solution.checkout("W"), resp = 20
        assert checkout_solution.checkout("X"), resp = 90
        assert checkout_solution.checkout("Y"), resp = 10
        assert checkout_solution.checkout("Z"), resp = 50
        assert checkout_solution.checkout("a"), resp = -1
        assert checkout_solution.checkout("-"), resp = -1
        assert checkout_solution.checkout("ABCa"), resp = -1
        assert checkout_solution.checkout("AxA"), resp = -1
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), resp = 965
        assert checkout_solution.checkout("A"), resp = 50
        assert checkout_solution.checkout("AA"), resp = 100
        assert checkout_solution.checkout("AAA"), resp = 130
        assert checkout_solution.checkout("AAAA"), resp = 180
        assert checkout_solution.checkout("AAAAA"), resp = 200
        assert checkout_solution.checkout("AAAAAA"), resp = 250
        assert checkout_solution.checkout("AAAAAAA"), resp = 300
        assert checkout_solution.checkout("AAAAAAAA"), resp = 330
        assert checkout_solution.checkout("AAAAAAAAA"), resp = 380
        assert checkout_solution.checkout("AAAAAAAAAA"), resp = 400
        assert checkout_solution.checkout("P"), resp = 50
        assert checkout_solution.checkout("PP"), resp = 100
        assert checkout_solution.checkout("PPP"), resp = 150
        assert checkout_solution.checkout("PPPP"), resp = 200
        assert checkout_solution.checkout("PPPPP"), resp = 200
        assert checkout_solution.checkout("PPPPPP"), resp = 250
        assert checkout_solution.checkout("PPPPPPP"), resp = 300
        assert checkout_solution.checkout("PPPPPPPP"), resp = 350
        assert checkout_solution.checkout("PPPPPPPPP"), resp = 400
        assert checkout_solution.checkout("PPPPPPPPPP"), resp = 400
        assert checkout_solution.checkout("UUU"), resp = 120
        assert checkout_solution.checkout("UUUU"), resp = 120
        assert checkout_solution.checkout("UUUUU"), resp = 160
        assert checkout_solution.checkout("UUUUUUUU"), resp = 240
        assert checkout_solution.checkout("UUUUUUUU"), resp = 240
        assert checkout_solution.checkout("EE"), resp = 80
        assert checkout_solution.checkout("EEB"), resp = 80
        assert checkout_solution.checkout("EEEB"), resp = 120
        assert checkout_solution.checkout("EEEEBB"), resp = 160
        assert checkout_solution.checkout("BEBEEE"), resp = 160
        assert checkout_solution.checkout("RRR"), resp = 150
        assert checkout_solution.checkout("RRRQ"), resp = 150
        assert checkout_solution.checkout("RRRRQ"), resp = 200
        assert checkout_solution.checkout("RRRRRRQQ"), resp = 300
        assert checkout_solution.checkout("RRRQRQRR"), resp = 300
        assert checkout_solution.checkout("A"), resp = 50
        assert checkout_solution.checkout("AA"), resp = 100
        assert checkout_solution.checkout("AAA"), resp = 130
        assert checkout_solution.checkout("AAAA"), resp = 180
        assert checkout_solution.checkout("AAAAA"), resp = 200
        assert checkout_solution.checkout("AAAAAA"), resp = 250
        assert checkout_solution.checkout("H"), resp = 10
        assert checkout_solution.checkout("HH"), resp = 20
        assert checkout_solution.checkout("HHH"), resp = 30
        assert checkout_solution.checkout("HHHH"), resp = 40
        assert checkout_solution.checkout("HHHHH"), resp = 45
        assert checkout_solution.checkout("HHHHHH"), resp = 55
        assert checkout_solution.checkout("HHHHHHH"), resp = 65
        assert checkout_solution.checkout("HHHHHHHH"), resp = 75
        assert checkout_solution.checkout("HHHHHHHHH"), resp = 85
        assert checkout_solution.checkout("HHHHHHHHHH"), resp = 80
        assert checkout_solution.checkout("HHHHHHHHHHH"), resp = 90
        assert checkout_solution.checkout("HHHHHHHHHHHH"), resp = 100
        assert checkout_solution.checkout("HHHHHHHHHHHHH"), resp = 110
        assert checkout_solution.checkout("HHHHHHHHHHHHHH"), resp = 120
        assert checkout_solution.checkout("HHHHHHHHHHHHHHH"), resp = 125
        assert checkout_solution.checkout("HHHHHHHHHHHHHHHH"), resp = 135
        assert checkout_solution.checkout("HHHHHHHHHHHHHHHHH"), resp = 145
        assert checkout_solution.checkout("HHHHHHHHHHHHHHHHHH"), resp = 155
        assert checkout_solution.checkout("HHHHHHHHHHHHHHHHHHH"), resp = 165
        assert checkout_solution.checkout("HHHHHHHHHHHHHHHHHHHH"), resp = 160
        assert checkout_solution.checkout("V"), resp = 50
        assert checkout_solution.checkout("VV"), resp = 90
        assert checkout_solution.checkout("VVV"), resp = 130
        assert checkout_solution.checkout("VVVV"), resp = 180
        assert checkout_solution.checkout("VVVVV"), resp = 220
        assert checkout_solution.checkout("VVVVVV"), resp = 260
        assert checkout_solution.checkout("B"), resp = 30
        assert checkout_solution.checkout("BB"), resp = 45
        assert checkout_solution.checkout("BBB"), resp = 75
        assert checkout_solution.checkout("BBBB"), resp = 90
        assert checkout_solution.checkout("NNN"), resp = 120
        assert checkout_solution.checkout("NNNM"), resp = 120
        assert checkout_solution.checkout("NNNNM"), resp = 160
        assert checkout_solution.checkout("NNNNNNMM"), resp = 240
        assert checkout_solution.checkout("NNNMNMNN"), resp = 240
        assert checkout_solution.checkout("FF"), resp = 20
        assert checkout_solution.checkout("FFF"), resp = 20
        assert checkout_solution.checkout("FFFF"), resp = 30
        assert checkout_solution.checkout("FFFFFF"), resp = 40
        assert checkout_solution.checkout("FFFFFF"), resp = 40
        assert checkout_solution.checkout("K"), resp = 80
        assert checkout_solution.checkout("KK"), resp = 150
        assert checkout_solution.checkout("KKK"), resp = 230
        assert checkout_solution.checkout("KKKK"), resp = 300
        assert checkout_solution.checkout("Q"), resp = 30
        assert checkout_solution.checkout("QQ"), resp = 60
        assert checkout_solution.checkout("QQQ"), resp = 80
        assert checkout_solution.checkout("QQQQ"), resp = 110
        assert checkout_solution.checkout("QQQQQ"), resp = 140
        assert checkout_solution.checkout("QQQQQQ"), resp = 160
        assert checkout_solution.checkout("V"), resp = 50
        assert checkout_solution.checkout("VV"), resp = 90
        assert checkout_solution.checkout("VVV"), resp = 130
        assert checkout_solution.checkout("VVVV"), resp = 180
        assert checkout_solution.checkout("H"), resp = 10
        assert checkout_solution.checkout("HH"), resp = 20
        assert checkout_solution.checkout("HHH"), resp = 30
        assert checkout_solution.checkout("HHHH"), resp = 40
        assert checkout_solution.checkout("HHHHH"), resp = 45
        assert checkout_solution.checkout("HHHHHH"), resp = 55
        assert checkout_solution.checkout("HHHHHHH"), resp = 65
        assert checkout_solution.checkout("HHHHHHHH"), resp = 75
        assert checkout_solution.checkout("HHHHHHHHH"), resp = 85
        assert checkout_solution.checkout("HHHHHHHHHH"), resp = 80
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"), resp = 1880
        assert checkout_solution.checkout("LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH"), resp = 1880
        assert checkout_solution.checkout("AAAAAPPPPPUUUUEEBRRRQAAAHHHHHHHHHHVVVBBNNNMFFFKKQQQVVHHHHH"), resp = 1640
        assert checkout_solution.checkout("PPPPQRUVPQRUVPQRUVSU"), resp = 740
        assert checkout_solution.
