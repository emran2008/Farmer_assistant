import tkinter as tk

from tkinter import messagebox

from pond_predictor import predict_fish


# =====================================================
# WINDOW
# =====================================================

root = tk.Tk()

root.title(
    "Pond Fish Prediction System"
)

root.geometry("900x650")

root.resizable(False, False)


# =====================================================
# COLORS
# =====================================================

BG_COLOR = "#EAF6F6"

TITLE_COLOR = "#0B4F6C"

BUTTON_COLOR = "#087E8B"

WHITE = "#FFFFFF"


# =====================================================
# MAIN FRAME
# =====================================================

main_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

main_frame.pack(
    fill="both",
    expand=True
)


# =====================================================
# TITLE
# =====================================================

title = tk.Label(
    main_frame,
    text="POND FISH PREDICTION SYSTEM",
    font=("Arial", 24, "bold"),
    bg=BG_COLOR,
    fg=TITLE_COLOR
)

title.pack(
    pady=(30, 5)
)


subtitle = tk.Label(
    main_frame,
    text="Machine Learning Based Pond Fish Recommendation",
    font=("Arial", 12),
    bg=BG_COLOR
)

subtitle.pack(
    pady=(0, 25)
)


# =====================================================
# FORM FRAME
# =====================================================

form_frame = tk.Frame(
    main_frame,
    bg=WHITE,
    padx=30,
    pady=25
)

form_frame.pack(
    padx=80,
    fill="x"
)


# =====================================================
# INPUT VARIABLES
# =====================================================

pond_size_var = tk.StringVar()

pond_depth_var = tk.StringVar()

temperature_var = tk.StringVar()

ph_var = tk.StringVar()

do_var = tk.StringVar()

turbidity_var = tk.StringVar()


# =====================================================
# INPUT FUNCTION
# =====================================================

def create_input(
    row,
    label_text,
    variable
):

    label = tk.Label(
        form_frame,
        text=label_text,
        font=("Arial", 11, "bold"),
        bg=WHITE,
        anchor="w"
    )

    label.grid(
        row=row,
        column=0,
        sticky="w",
        pady=8
    )

    entry = tk.Entry(
        form_frame,
        textvariable=variable,
        font=("Arial", 11),
        width=35
    )

    entry.grid(
        row=row,
        column=1,
        padx=20,
        pady=8
    )

    return entry


# =====================================================
# CREATE INPUTS
# =====================================================

create_input(
    0,
    "Pond Size (decimal):",
    pond_size_var
)

create_input(
    1,
    "Pond Depth (meter):",
    pond_depth_var
)

create_input(
    2,
    "Temperature (°C):",
    temperature_var
)

create_input(
    3,
    "pH:",
    ph_var
)

create_input(
    4,
    "Dissolved Oxygen - DO (mg/L):",
    do_var
)

create_input(
    5,
    "Turbidity:",
    turbidity_var
)


# =====================================================
# PREDICTION
# =====================================================

def run_prediction():

    try:

        pond_size = float(
            pond_size_var.get()
        )

        pond_depth = float(
            pond_depth_var.get()
        )

        temperature = float(
            temperature_var.get()
        )

        ph = float(
            ph_var.get()
        )

        do = float(
            do_var.get()
        )

        turbidity = float(
            turbidity_var.get()
        )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values."
        )

        return


    if pond_size <= 0:

        messagebox.showerror(
            "Invalid Pond Size",
            "Pond size must be greater than 0."
        )

        return


    if pond_depth <= 0:

        messagebox.showerror(
            "Invalid Pond Depth",
            "Pond depth must be greater than 0."
        )

        return


    # -------------------------------------------------
    # CALL ML PREDICTION
    # -------------------------------------------------

    try:

        result = predict_fish(
            pond_size,
            pond_depth,
            temperature,
            ph,
            do,
            turbidity
        )

    except Exception as error:

        messagebox.showerror(
            "Prediction Error",
            str(error)
        )

        return


    if not result["success"]:

        messagebox.showwarning(
            "Management Data Missing",
            result["message"]
        )

        return


    # -------------------------------------------------
    # RESULT WINDOW
    # -------------------------------------------------

    show_result(result)


# =====================================================
# RESULT WINDOW
# =====================================================

def show_result(result):

    result_window = tk.Toplevel(root)

    result_window.title(
        "Prediction Result"
    )

    result_window.geometry(
        "650x600"
    )

    result_window.configure(
        bg=BG_COLOR
    )


    title = tk.Label(
        result_window,
        text="PREDICTION RESULT",
        font=("Arial", 22, "bold"),
        bg=BG_COLOR,
        fg=TITLE_COLOR
    )

    title.pack(
        pady=25
    )


    result_frame = tk.Frame(
        result_window,
        bg=WHITE,
        padx=30,
        pady=20
    )

    result_frame.pack(
        padx=50,
        fill="both",
        expand=True
    )


    # -------------------------------------------------
    # RESULT TEXT
    # -------------------------------------------------

    fish_text = (
        f"🐟 Recommended Fish: "
        f"{result['fish_name']}"
    )

    confidence_text = (
        f"Confidence: "
        f"{result['confidence']:.2f}%"
    )


    tk.Label(
        result_frame,
        text=fish_text,
        font=("Arial", 18, "bold"),
        bg=WHITE,
        fg=TITLE_COLOR
    ).pack(
        pady=8
    )


    tk.Label(
        result_frame,
        text=confidence_text,
        font=("Arial", 12),
        bg=WHITE
    ).pack(
        pady=5
    )


    separator = tk.Frame(
        result_frame,
        height=2,
        bg="#DDDDDD"
    )

    separator.pack(
        fill="x",
        pady=15
    )


    # -------------------------------------------------
    # FORMAT VALUES
    # -------------------------------------------------

    density = result[
        "stocking_density"
    ]

    if density is None:

        density_text = "Data unavailable"

    else:

        density_text = (
            f"{density:.0f} "
            f"{result['density_unit']}"
        )


    total_fish = result[
        "total_fish"
    ]

    if total_fish is None:

        total_fish_text = "Data unavailable"

    else:

        total_fish_text = (
            f"{total_fish} fish"
        )


    daily_feed = result[
        "daily_feed"
    ]

    if daily_feed is None:

        feed_text = "Data unavailable"

    else:

        feed_text = (
            f"{daily_feed:.2f} kg/day"
        )


    growth = result[
        "expected_growth"
    ]

    if growth is None:

        growth_text = "Data unavailable"

    else:

        growth_text = (
            f"{growth:.3f} kg/fish"
        )


    culture = result[
        "culture_period_days"
    ]

    if culture is None:

        culture_text = "Data unavailable"

    else:

        culture_text = (
            f"{culture} days"
        )


    production = result[
        "estimated_production"
    ]

    if production is None:

        production_text = "Data unavailable"

    else:

        production_text = (
            f"{production:.2f} kg"
        )


    # -------------------------------------------------
    # DISPLAY RESULTS
    # -------------------------------------------------

    results = [

        (
            "Recommended Stocking Density:",
            density_text
        ),

        (
            "Recommended Total Fish:",
            total_fish_text
        ),

        (
            "Expected Growth:",
            growth_text
        ),

        (
            "Recommended Daily Feed:",
            feed_text
        ),

        (
            "Estimated Culture Period:",
            culture_text
        ),

        (
            "Estimated Production:",
            production_text
        ),

    ]


    for label_text, value_text in results:

        row = tk.Frame(
            result_frame,
            bg=WHITE
        )

        row.pack(
            fill="x",
            pady=6
        )


        tk.Label(
            row,
            text=label_text,
            font=("Arial", 11, "bold"),
            bg=WHITE,
            anchor="w"
        ).pack(
            side="left"
        )


        tk.Label(
            row,
            text=value_text,
            font=("Arial", 11),
            bg=WHITE,
            anchor="e"
        ).pack(
            side="right"
        )


    # -------------------------------------------------
    # CLOSE BUTTON
    # -------------------------------------------------

    tk.Button(
        result_window,
        text="CLOSE",
        font=("Arial", 11, "bold"),
        bg=BUTTON_COLOR,
        fg=WHITE,
        padx=25,
        pady=8,
        command=result_window.destroy
    ).pack(
        pady=20
    )


# =====================================================
# PREDICT BUTTON
# =====================================================

predict_button = tk.Button(
    main_frame,
    text="PREDICT FISH",
    font=("Arial", 13, "bold"),
    bg=BUTTON_COLOR,
    fg=WHITE,
    padx=40,
    pady=10,
    command=run_prediction
)

predict_button.pack(
    pady=25
)


# =====================================================
# START APPLICATION
# =====================================================

root.mainloop()