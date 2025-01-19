from optcolor import Color


class BasicColor():
    CONTENTS = Color(80), Color(213)
    SYSTEM = Color(0,120,212), Color(0,120,212)
    FRONT = Color(255), Color(25)
    BACK = Color(248), Color(32)
    PADDING = Color(209), Color(68)


if __name__ == '__main__':
    print(BasicColor.CONTENTS[1].hex)
    pass