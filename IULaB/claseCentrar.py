from win32api import GetSystemMetrics

class centerScreen:
    def situarLaB(self, AnchoLaB, AltoLaB):
        halfSx, halfSy = GetSystemMetrics(0), GetSystemMetrics(1)
        Lx = AnchoLaB
        Ly = AltoLaB

        x = halfSx/2 - AnchoLaB/2
        y = halfSy/2 - AltoLaB/2

        return f"{AnchoLaB}x{AltoLaB}+{int(x)}+{int(y)}"