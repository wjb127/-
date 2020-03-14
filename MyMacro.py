from pynput.keyboard import Key, Listener, KeyCode
import win32api
import pynput
import time
from pynput import mouse


key_memory = []


keyboard_button = pynput.keyboard.Controller()
keyboard_key = pynput.keyboard.Key

# 키보드 컨트롤링하기
def keyboard_con():
    for i in key_memory:
        keyboard_button.press(i)
        print(i)

#키를 누를때 출력 후 기억하기
def key_pressed(key):
    print("Pressed {}".format(key))
    key_memory.append(key)
    print(key_memory)

# 키를 땠을 때 출력
def key_released(key):
    print("Released {}".format(key))
    if key == Key.esc:
        return False

# 마우스 움직임
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

# 클릭
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

# 휠 스크롤
def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# 프로그램 실행중일 때 ESC키 누르기 전까지 누른 키 출력하기
with Listener(on_press = key_pressed, on_release = key_released) as listener:
    listener.join()
    #keyboard_con() 

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

if __name__ == "__main__":

    # 프로그램 종료 전까지 무한 반복
    while True:
        keyboard_con()
        time.sleep(1)
        


    
    