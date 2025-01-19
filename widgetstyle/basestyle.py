from optcolor import Color


class WidgetStyle():
    def __init__(self):
        """widget style attribute for tkinter"""
        # mode
        self.is_darkmode: bool
        # color
        self.main_color: tuple[Color, Color]
        self.sub_color: tuple[Color, Color]
        self.system_color: tuple[Color, Color]
        self.bg_color: tuple[Color, Color]
        # pad
        self.frame_pad: int
        self.pad: int
        # font
        self.font_type: str
        self.font_size: int


    # set attribute
    def set(self, **kwargs):
        """
        set style attribute

        Parameters
        ----------
        is_darkmode : bool | None
        main_color : tuple[Color, Color] | None
        sub_color : tuple[Color, Color] | None
        system_color : tuple[Color, Color] | None
        bg_color : tuple[Color, Color] | None
        frame_pad : int | None
        pad : int | None
        font_type : str | None
        font_size : int | None
        """
        for name, value in kwargs.items():
            self.__setattr__(name, value)


    # get sub attribute

    # mode
    @property
    def mode(self):
        return ['light', 'dark'][self.is_darkmode]
    # color
    def get_main_color(self, transparent: float = 0):
        over = self.main_color[self.is_darkmode]
        under = self.bg_color[self.is_darkmode]
        return over.normal(under, alpha=transparent).hex
    def get_bg_color(self):
        return self.bg_color[self.is_darkmode].hex
    # pad
    def get_frame_pad(self, is_first=False):
        pad = 0 if is_first else self.frame_pad
        return pad, 0
    def get_pad(self, is_first=False):
        pad = 0 if is_first else self.pad
        return pad, 0
    # font
    @property
    def font(self):
        return (self.font_type, self.font_size)


if __name__ == '__main__':
    pass