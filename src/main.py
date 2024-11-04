
import tkinter as tk
from src.gui import FinanceCalculatorGUI


def main():
    root = tk.Tk()
    app = FinanceCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()