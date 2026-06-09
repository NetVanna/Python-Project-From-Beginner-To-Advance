import tkinter

# ==========================================================
# Calculator Button Layout
# Each inner list represents one row of buttons
# ==========================================================
button_values = [
    ["AC", "±", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

# Right-side operation buttons
right_sysmbols = ["÷", "×", "−", "+", "="]

# Top utility buttons
top_sysmbols = ["AC", "±", "%"]

# Number of rows and columns in calculator layout
row_count = len(button_values)
column_count = len(button_values[0])

# ==========================================================
# Color Configuration
# ==========================================================
color_light_gray = "#D4D4D4"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

# ==========================================================
# Window Setup
# ==========================================================

# Create main application window
window = tkinter.Tk()

# Window title
window.title("Calculator")

# Disable resizing
window.resizable(False, False)

# Container frame for calculator UI
frame = tkinter.Frame(window)

# Display label (calculator screen)
label = tkinter.Label(
    frame,
    text="0",
    font=("Arial", 40),
    background=color_black,
    foreground=color_white,
    anchor="e",      # Align text to the right
    width=column_count
)

# Place display at top of calculator
label.grid(
    row=0,
    column=0,
    columnspan=column_count,
    sticky="we"
)

# ==========================================================
# Create Calculator Buttons Dynamically
# ==========================================================
for row in range(row_count):
    for column in range(column_count):

        # Current button value
        value = button_values[row][column]

        # Create button
        button = tkinter.Button(
            frame,
            text=value,
            font=("Arail", 30),
            width=column_count - 1,
            height=1,
            command=lambda value=value: button_clicked(value)
        )

        # Apply different colors based on button type
        if value in top_sysmbols:
            button.config(
                foreground=color_black,
                background=color_light_gray
            )

        elif value in right_sysmbols:
            button.config(
                foreground=color_white,
                background=color_orange
            )

        else:
            button.config(
                foreground=color_white,
                background=color_dark_gray
            )

        # Position button on grid
        button.grid(row=row + 1, column=column)

# Display frame in window
frame.pack()

# ==========================================================
# Calculator State Variables
# Used for operations such as A + B, A - B, etc.
# ==========================================================

# First number
A = "0"

# Selected operator (+, -, ×, ÷)
operator = None

# Second number
B = None

# ==========================================================
# Helper Functions
# ==========================================================

def remove_zero_decimal(num):
    """
    Remove unnecessary decimal places.

    Example:
        10.0 -> "10"
        10.5 -> "10.5"
    """
    if num % 1 == 0:
        num = int(num)

    return str(num)


def clear_all():
    """
    Reset calculator state variables.
    """
    global A, operator, B

    A = "0"
    operator = None
    B = None


# ==========================================================
# Button Click Handler
# Called whenever a calculator button is pressed
# ==========================================================
def button_clicked(value):
    global right_sysmbols, top_sysmbols
    global label, A, B, operator

    # ------------------------------------------------------
    # Operation Buttons (+, -, ×, ÷, =)
    # ------------------------------------------------------
    if value in right_sysmbols:

        # Equal button pressed
        if value == "=":

            # Only calculate if operation exists
            if A is not None and operator is not None:

                B = label["text"]

                # Convert strings to numbers
                numA = float(A)
                numB = float(B)

                # Perform calculation
                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)

                elif operator == "−":
                    label["text"] = remove_zero_decimal(numA - numB)

                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)

                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)

                # Reset state after calculation
                clear_all()

        # Operator button pressed
        elif value in "+−×÷":

            # Save first operand only once
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value

    # ------------------------------------------------------
    # Top Buttons (AC, ±, %)
    # ------------------------------------------------------
    elif value in top_sysmbols:

        # Clear everything
        if value == "AC":
            clear_all()
            label["text"] = "0"

        # Toggle positive/negative
        elif value == "±":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        # Convert to percentage
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    # ------------------------------------------------------
    # Number and Decimal Input
    # ------------------------------------------------------
    else:

        # Decimal point
        if value == ".":

            # Prevent multiple decimal points
            if value not in label["text"]:
                label["text"] += value

        # Digits 0-9
        elif value in "0123456789":

            # Replace initial zero
            if label["text"] == "0":
                label["text"] = value

            # Append digit
            else:
                label["text"] += value


# ==========================================================
# Center Window on Screen
# ==========================================================

# Update window size information
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate center position
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# Set window geometry
window.geometry(
    f"{window_width}x{window_height}+{window_x}+{window_y}"
)

# ==========================================================
# Start Application Event Loop
# ==========================================================
window.mainloop()