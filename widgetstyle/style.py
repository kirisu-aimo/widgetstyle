from widgetstyle.basestyle import BaseStyle

class Style(BaseStyle):
    def __init__(self, master: BaseStyle):
        super().__init__()
        self.master = master

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except:
            return super().__getattribute__('master').__getattribute__(name)
    def __setattr__(self, name, value):
        if name == 'master':
            if hasattr(self, name):
                return
        if value is None:
            if hasattr(self, name):
                self.__delattr__(name)
        else:
            super().__setattr__(name, value)

    # get sub attribute
    def get_bg_color(self, transparent: float = 0):
        over = self.bg_color[self.is_darkmode]
        under = self.master.bg_color[self.is_darkmode]
        return over.normal(under, alpha=transparent).hex


if __name__ == '__main__':
    pass