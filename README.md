# caffeine.py

Python script that prevents your system from going into sleep mode.

## Dependencies/Libaries:

- install [python 3.x](https://www.python.org/downloads/)<br>
- Install `tkinter` (usually included with Python, but if missing, install it using your package manager): <br>
  - On Ubuntu/Debian: `sudo apt-get install python3-tk` <br>
  - On Fedora: `sudo dnf install python3-tkinter` <br>
  - On macOS: Typically included with Python; reinstall Python if necessary <br>
  - On Windows: `tkinter` should be included by default with Python installation


## Setup Instructions

1. Clone the repository:
	```
	git clone <repository-url>
	cd <repository-directory>
	```

2. Install Python dependencies:
	```
	pip install -r requirements.txt
	```

3. Run the script:
	```
	python3 caffeine.py
	```

## Supported Platforms

- Windows 10 and later

## Additional Information

- The script simulates key presses to keep your system active.
- Ensure `pyautogui` is correctly installed and configured for it to work as intended.