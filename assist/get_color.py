from colorama import Fore, Back, Style, init

init(autoreset=True)  # 自动回复到默认颜色


class Color():
    """指定终端展示的颜色"""

    def red(self, s):
        """指定颜色为红色"""
        return Fore.LIGHTRED_EX + s + Fore.RESET

    def green(self, s):
        """指定颜色为绿色"""
        return Fore.LIGHTGREEN_EX + s + Fore.RESET

    def magenta(self, s):
        """指定颜色为洋红色"""
        return Fore.LIGHTMAGENTA_EX + s + Fore.RESET

    def cyan(self, s):
        """指定颜色为青色"""
        return Fore.LIGHTCYAN_EX + s + Fore.RESET
    def yellow(self, s):
        """指定颜色为青色"""
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET
    def white(self, s):
        return Fore.LIGHTWHITE_EX + s + Fore.RESET

color = Color()
