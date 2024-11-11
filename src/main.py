
import tkinter as tk
from gui import FinanceCalculatorGUI


def main():
    root = tk.Tk()
    app = FinanceCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
