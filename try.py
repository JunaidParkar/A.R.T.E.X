from PyQt5 import QtCore, QtWidgets
import sys
import socket

# Function to check if the internet is enabled
def is_internet_enabled():
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

# Function to display a GUI window with an error message
def display_error_message(message):
    # Create a new QApplication
    app = QtWidgets.QApplication(sys.argv)

    # Set the application style sheet
    app.setStyleSheet('''
        QWidget {
            background-color: rgba(0, 0, 0, 0.8);
            border: 2px solid #00ff00;
            border-radius: 10px;
        }
        QLabel {
            color: #00ff00;
            font-family: "Orbitron";
            font-size: 24px;
            qproperty-alignment: AlignCenter;
            padding: 10px 20px;
        }
    ''')

    # Create a new QWidget
    window = QtWidgets.QWidget()
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # Create a layout for the window
    layout = QtWidgets.QVBoxLayout()

    # Create a label with the error message
    label = QtWidgets.QLabel(message)
    layout.addWidget(label)

    # Set the layout for the window
    window.setLayout(layout)

    # Show the window
    window.show()

    # Start a timer to update the GUI window
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: update_gui(window, label, app))
    timer.start(1000)

    # Run the QApplication main loop
    app.exec_()

# Function to update the GUI window
def update_gui(window, label, app):
    if is_internet_enabled():
        # Update the label with a success message
        label.setText('Internet connection is restored.')
        QtCore.QTimer.singleShot(3000, app.quit) # close after 3 seconds
    else:
        # Update the label with an error message
        label.setText('Internet connection is off. Please connect to the internet.')

# Display a GUI window with an error message
display_error_message('Internet connection is off. Please connect to the internet.')
