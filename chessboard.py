# Chess board
def chessboard():
    size = 8
    for row in range(size):
        for col in range(size):
            if (row + col) % 2 == 0:
                print(" ", end =" ")
            else:
                print("⬜",end =" ")
        print()
chessboard()


# chessboard matplot lib
import matplotlib.pyplot as plt
import numpy as np

def draw_chessboard(size=8):
    chessboard = np.zeros((size, size))
    for row in range(size):
        for col in range(size):
            chessboard[row, col] = (row + col) % 2  # Black = 1, White = 0
    plt.imshow(chessboard, cmap="gray")
    plt.xticks([])  # Hide x-axis labels
    plt.yticks([])  # Hide y-axis labels
    plt.show()

draw_chessboard()