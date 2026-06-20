import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

isSharp = False
isShift = False

# setup a keyboard device
kbd = Keyboard(usb_hid.devices)

rows = [board.GP0, board.GP1, board.GP2, board.GP5, board.GP3, board.GP4]
cols = [board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21]
matrix = keypad.KeyMatrix(rows, cols, columns_to_anodes=False)

# all print statements are for debugging purposes
while True:
    event = matrix.events.get()
    if event:
        if (event.key_number == 0):
            # octave up
            kbd.send(Keycode.CONTROL, Keycode.UP_ARROW)
        elif (event.key_number == 1):
            # octave down
            kbd.send(Keycode.CONTROL, Keycode.DOWN_ARROW)
        elif (event.key_number == 2):
            # toggle sharp flat
            isSharp = not isSharp
        elif (event.key_number == 3):
            # 8th notes
            kbd.send(Keycode.FOUR)
        elif (event.key_number == 4):
            # 16th notes
            kbd.send(Keycode.THREE)
        elif (event.key_number == 5):
            # fake shift
            isShift = not isShift
        elif (event.key_number == 6):
            # quarter note
            kbd.send(Keycode.FIVE)
        elif (event.key_number == 7):
            # half note
            kbd.send(Keycode.SIX)
        elif (event.key_number == 8):
            # whole note
            kbd.send(Keycode.SEVEN)
        elif (event.key_number == 9):
            # dotted note
            kbd.send(Keycode.PERIOD)
        elif event.key_number == 10:
            # rest
            kbd.send(Keycode.ZERO)
        elif event.key_number == 11:
            # tenuto
            kbd.send(Keycode.SHIFT, Keycode.N)
        elif event.key_number == 12:
            # staccato
            kbd.send(Keycode.SHIFT, Keycode.S)
        elif event.key_number == 13:
            # accent
            kbd.send(Keycode.SHIFT, Keycode.V)
        elif event.key_number == 14:
            # marcato
            kbd.send(Keycode.SHIFT, Keycode.O)
        elif event.key_number == 15:
            # tie
            kbd.send(Keycode.T)
        elif event.key_number == 16:
            # slur
            kbd.send(Keycode.S)
        elif event.key_number == 17:
            # chord naming
            kbd.send(Keycode.CONTROL, Keycode.K)
        elif event.key_number == 18:
            # decrescendo
            kbd.send(Keycode.SHIFT, Keycode.PERIOD)
        elif event.key_number == 19:
            # crescendo
            kbd.send(Keycode.SHIFT, Keycode.COMMA)
        elif event.key_number == 20:
            # dynamics
            kbd.send(Keycode.CONTROL, Keycode.D)
        elif event.key_number == 21:
            if isSharp:
                # d sharp
                kbd.send(Keycode.KEYPAD_PLUS)
                if isShift:
                    kbd.press(Keycode.SHIFT)
                kbd.send(Keycode.D)
                kbd.release(Keycode.SHIFT)
            else:
                # e flat
                kbd.send(Keycode.KEYPAD_MINUS)
                if isShift:
                    kbd.press(Keycode.SHIFT)
                kbd.send(Keycode.E)
                kbd.release(Keycode.SHIFT)
        elif event.key_number == 22:
            if isSharp:
                # C sharp
                kbd.send(Keycode.KEYPAD_PLUS)
                if isShift:
                    kbd.press(Keycode.SHIFT)
                kbd.send(Keycode.C)
                kbd.release(Keycode.SHIFT)
            else:
                # D flat
                kbd.send(Keycode.KEYPAD_MINUS)
                if isShift:
                    kbd.press(Keycode.SHIFT)
                kbd.send(Keycode.D)
                kbd.release(Keycode.SHIFT)
        elif event.key_number == 23:
            # E
            if isShift:
                kbd.press(Keycode.SHIFT)
            kbd.send(Keycode.E)
            kbd.release(Keycode.SHIFT)
        elif event.key_number == 24:
            # F
            if isShift:
                kbd.press(Keycode.SHIFT)
            kbd.send(Keycode.F)
            kbd.release(Keycode.SHIFT)
        elif event.key_number == 25:
            # G
            if isShift:
                kbd.press(Keycode.SHIFT)
            kbd.send(Keycode.G)
            kbd.release(Keycode.SHIFT)
        elif event.key_number == 26:
            # C
            if isShift:
                kbd.press(Keycode.SHIFT)
            kbd.send(Keycode.C)
            kbd.release(Keycode.SHIFT)
        elif event.key_number == 27:
            # D
            if isShift:
                kbd.press(Keycode.SHIFT)
            kbd.send(Keycode.D)
            kbd.release(Keycode.SHIFT)
        elif event.key_numbder == 28:
            # A
            if isShift:
                kbd.press(Keycode.SHIFT)
            kbd.send(Keycode.A)
            kbd.release(Keycode.SHIFT)
        elif event.key_number == 29:
            # B
            if isShift:
                kbd.press(Keycode.SHIFT)
            kbd.send(Keycode.B)
            kbd.release(Keycode.SHIFT)
        elif event.key_number == 30:
            if isSharp:
                # f sharp
                kbd.send(Keycode.KEYPAD_PLUS)
                if isShift:
                    kbd.press(Keycode.SHIFT)
                kbd.send(Keycode.F)
                kbd.release(Keycode.SHIFT)
            else:
                # g flat
                kbd.send(Keycode.KEYPAD_MINUS)
                if isShift:
                    kbd.press(Keycode.SHIFT)
                kbd.send(Keycode.G)
                kbd.release(Keycode.SHIFT)
        elif event.key_number == 31:
            if isSharp:
                # g sharp
                kbd.send(Keycode.KEYPAD_PLUS)
                if isShift:
                    kbd.press(Keycode.SHIFT)
                kbd.send(Keycode.G)
                kbd.release(Keycode.SHIFT)
            else:
                # a flat
                kbd.send(Keycode.KEYPAD_MINUS)
                if isShift:
                    kbd.press(Keycode.SHIFT)
                kbd.send(Keycode.A)
                kbd.release(Keycode.SHIFT)
        elif event.key_number == 32:
            if isSharp:
                # a sharp
                kbd.send(Keycode.KEYPAD_PLUS)
                if isShift:
                    kbd.press(Keycode.SHIFT)
                kbd.send(Keycode.A)
                kbd.release(Keycode.SHIFT)
            else:
                # b flat
                kbd.send(Keycode.KEYPAD_MINUS)
                if isShift:
                    kbd.press(Keycode.SHIFT)
                kbd.send(Keycode.B)
                kbd.release(Keycode.SHIFT)