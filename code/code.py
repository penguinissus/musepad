import board
import keypad
import digitalio
rows = [board.GP0, board.GP1, board.GP2, board.GP5, board.GP3, board.GP4]
cols = [board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21]
matrix = keypad.KeyMatrix(rows, cols, columns_to_anodes=False)

while True:
    event = matrix.events.get()
    if event:
        print(event.key_number, event.pressed)