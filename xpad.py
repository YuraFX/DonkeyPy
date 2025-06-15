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

import ctypes
from ctypes import wintypes

# Load XInput
xinput = ctypes.windll.xinput1_4  # Windows 8+ Support
if not xinput:
    xinput = ctypes.windll.xinput9_1_0  # Windows Vista/7 Support

# D-Pad constants
DPAD_UP = 0x0001
DPAD_DOWN = 0x0002
DPAD_LEFT = 0x0004
DPAD_RIGHT = 0x0008

# Structure for gamepad state
class XInputState(ctypes.Structure):
    _fields_ = [
        ('packet_number', wintypes.DWORD),
        ('buttons', wintypes.WORD),
        ('triggers', wintypes.BYTE * 2),
        ('thumb_lx', wintypes.SHORT),
        ('thumb_ly', wintypes.SHORT),
        ('thumb_rx', wintypes.SHORT),
        ('thumb_ry', wintypes.SHORT),
    ]

def get_dpad_state(controller=0):
    state = XInputState()
    if xinput.XInputGetState(controller, ctypes.byref(state)) == 0:
        return {
            'up': bool(state.buttons & DPAD_UP),
            'down': bool(state.buttons & DPAD_DOWN),
            'left': bool(state.buttons & DPAD_LEFT),
            'right': bool(state.buttons & DPAD_RIGHT)
        }
    return None