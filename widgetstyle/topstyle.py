from widgetstyle.basiccolor import BasicColor
from widgetstyle.basicpad import BasicPad
from widgetstyle.basestyle import BaseStyle

class TopStyle(BaseStyle):
    def __init__(self):
        """top window style attribute for tkinter"""
        super().__init__()
        # mode
        self.is_darkmode = True
        # color
        self.main_color = BasicColor.CONTENTS
        self.sub_color = BasicColor.SYSTEM
        self.system_color = BasicColor.SYSTEM
        self.bg_color = BasicColor.PADDING
        # pad
        self.frame_pad = BasicPad.PX
        self.pad = BasicPad.MEDIUM
        # font
        self.font_type = 'Arial'
        self.font_size = 12
    def __setattr__(self, name, value):
        if value is not None:
            super().__setattr__(name, value)


if __name__ == '__main__':
    pass