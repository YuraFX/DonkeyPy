# Foobar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
import time
from random import randint
import winsound
from xpad import get_dpad_state

# Create the main application window
window = tk.Tk()

# Setting the window icon
window.iconbitmap('resources\icon.ico')

# Setting the window title
window.title('DonkeyPy 1.1')

# Get the width and height of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the width and height of the window
window_width = 718
window_height = 418

# Calculate coordinates for placing the window in the centre of the screen
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Apply window size and position
window.geometry(f'{window_width}x{window_height}+{x}+{y}')
# Prohibit window resizing
window.resizable(False, False)

# Set the background of the window
window.image = tk.PhotoImage(file='resources\zf.png')
bg = tk.Label(window, image=window.image)
bg.grid(row=0, column=0)
bg.config(bg='#555555')

# Escape key label
esc_lbl = tk.Label(window, text='Press Esc to exit', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
esc_lbl.place(x=500, y=345)

# Window closing function
def exit(event):
    if event.keysym == 'Escape':
        window.destroy()

window.bind('<KeyPress-Escape>', exit)

# Donkey labels
donkey_lbl = tk.Label(window, text='Donkey', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
donkey_lbl.place(x=26, y=40)

donkey_count = tk.Label(window, text=0, bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
donkey_count.place(x=26, y=90)

donkey_loses = tk.Label(window, text='Donkey loses!', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
donkey_loses.place(x=1000, y=1000)

# Donkey scoring function
def donkey_points_count():
    donkey_count['text'] = int(donkey_count['text']) + 1

donkey_wins = tk.PhotoImage(file='resources\donkey_wins.png')
donkey_wins_label = tk.Label(window)
donkey_wins_label.image = donkey_wins
donkey_wins_label['image'] = donkey_wins_label.image
donkey_wins_label.place(x=1000, y=1000)
donkey_wins_label.config(bg='#555555')

# Car labels
car_lbl = tk.Label(window, text='Driver', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
car_lbl.place(x=500, y=40)

car_count = tk.Label(window, text=0, bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
car_count.place(x=500, y=90)

driver_loses = tk.Label(window, text='Driver loses!', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
driver_loses.place(x=1000, y=1000)

# Driver scoring function
def driver_points_count():
    car_count['text'] = int(car_count['text']) + 1

driver_wins = tk.PhotoImage(file='resources\driver_wins.png')
driver_wins_label = tk.Label(window)
driver_wins_label.image = driver_wins
driver_wins_label['image'] = driver_wins_label.image
driver_wins_label.place(x=1000, y=1000)
driver_wins_label.config(bg='#555555')

# Uploading car image
car = tk.PhotoImage(file='resources\car.png')
car_label = tk.Label(window)
car_label.image = car
car_label['image'] = car_label.image
car_y = 280
car_label.place(x=250, y=car_y)
car_label.config(bg='#555555')

car_y_initial = 280

# Car move function
def move_car(event):
    if car_y == 100:
        return
    else:
        if event.keysym == 'Right':
            car_label.place(x=380)
        elif event.keysym == 'Left':
            car_label.place(x=250)
        winsound.PlaySound('sounds\move_car.wav', 1)

window.bind('<KeyPress-Right>', move_car)
window.bind('<KeyPress-Left>', move_car)

# Car move function with gamepad
def gamepad_move_car():
    if car_y == 100:
        return
    else:
        try:
            dpad = get_dpad_state()
            if dpad['right']:
                car_label.place(x=380)
                winsound.PlaySound('sounds\move_car.wav', 1)
            elif dpad['left']:
                car_label.place(x=250)
                winsound.PlaySound('sounds\move_car.wav', 1)
        except:
            pass

    window.after(50, gamepad_move_car)  # Check every 50ms

# Game restart function
def restart_game():
    global car_y, car_y_initial

    car_y = car_y_initial

    car_label.place(x=250)

    donkey_loses.place(x=1000, y=1000)

    driver_wins_label.place(x=1000, y=1000)

    if car_count['text'] == 10:
        car_count['text'] = int(car_count['text']) * 0
        donkey_count['text'] = int(donkey_count['text']) * 0

    change_road()
    gamepad_move_car()

# Uploading donkey image
donkey = tk.PhotoImage(file='resources\donkey.png')
donkey_label = tk.Label(window)
donkey_label.image = donkey
donkey_label['image'] = donkey_label.image
donkey_x = 365
donkey_y = -40
donkey_label.place(x=donkey_x, y=donkey_y)
donkey_label.config(bg='#555555')

donkey_y_initial = -1340

# Game restart function in case of a donkey win
def restart_game_2():
    global car_y, car_y_initial, donkey_y, donkey_y_initial

    car_y = car_y_initial
    car_label.place(x=250, y=car_y)

    donkey_y = donkey_y_initial

# Label hiding function
def driver_loses_f():
    driver_loses.place(x=1000, y=1000)

# Game restart function in case a donkey wins with a score of 10
def restart_game_3():
    global car_y, car_y_initial, donkey_y, donkey_y_initial

    car_y = car_y_initial
    car_label.place(x=250, y=car_y)

    donkey_y = donkey_y_initial

    if donkey_count['text'] == 10:
        donkey_count['text'] = int(donkey_count['text']) * 0
        car_count['text'] = int(car_count['text']) * 0

# Hiding the picture with the text about the donkey's victory
def donkey_wins_f():
    donkey_wins_label.place(x=1000, y=1000)

# Function for checking image collision
def check_collision():
    car_x = car_label.winfo_rootx()
    car_y = car_label.winfo_rooty()

    donkey_x = donkey_label.winfo_rootx()
    donkey_y = donkey_label.winfo_rooty()

    # Condition, if the donkey wins
    if car_x >= donkey_x and car_x <= donkey_x + donkey.width() and \
            car_y >= donkey_y and car_y <= donkey_y + donkey.height():
        donkey_points_count()

        winsound.PlaySound('sounds\image_collision.wav', 1)

        if donkey_count['text'] < 10:
            driver_loses.place(x=26, y=140)

            restart_game_2()

            window.after(2500, driver_loses_f)
        else:
            donkey_wins_label.place(x=498, y=225)

            restart_game_3()

            window.after(2500, donkey_wins_f)

is_moving = False

# Donkey move function
def move_donkey():
    global is_moving, donkey_y, car_y

    # If the function is already in progress, exit
    if is_moving:
        return

    # Set the flag that the function is running
    is_moving = True

    donkey_y += 50
    donkey_label.place(y=donkey_y)

    # Checking for collision
    window.after(1000, check_collision)

    # Condition, if the donkey reaches a certain y-coordinate
    if donkey_y == 360:
        donkey_x = 365 if randint(1, 2) == 1 else 230

        donkey_y = -40
        donkey_label.place(x=donkey_x, y=donkey_y)

        car_y -= 20
        car_label.place(y=car_y)

        # Condition, if the driver wins
        if car_y == 100:
            driver_points_count()

            donkey_x = 1000
            donkey_label.place(x=donkey_x)

            if car_count['text'] < 10:
                donkey_loses.place(x=500, y=140)

                window.after(2500, move_donkey)
                window.after(2500, restart_game)
            else:
                driver_wins_label.place(x=498, y=225)

                window.after(2500, move_donkey)
                window.after(2500, restart_game)
        else:
                window.after(110, move_donkey)

    else:
        window.after(110, move_donkey)

    # Reset flag on function termination
    is_moving = False

# Create one Label for the road
road_label = tk.Label(window)

road_label.place(x=308, y=5)

# The function responsible for animating road markings
def change_road():
    if car_y == 100:
        return
    else:
        current_time = (int(time.time() * 20) % 3) + 1
        road = tk.PhotoImage(file='resources\doroga_{}.png'.format(current_time))
        road_label.image = road
        road_label['image'] = road_label.image
        road_label.config(bg='#555555')
        window.after(10, change_road)

move_donkey()
change_road()
gamepad_move_car()

window.mainloop()