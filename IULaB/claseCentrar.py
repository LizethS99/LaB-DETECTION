from screeninfo import get_monitors

class centerScreen:
    def situarLaB(self, AnchoLaB, AltoLaB):
        monitors = get_monitors()
        halfSx, halfSy = monitors[0].width, monitors[0].height
        Lx = AnchoLaB
        Ly = AltoLaB

        x = halfSx/2 - AnchoLaB/2
        #y = halfSy/2 - AltoLaB/2
        y = 0

        return f"{AnchoLaB}x{AltoLaB}+{int(x)}+{int(y)}"