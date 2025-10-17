import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------------
# Coffee Data
# -------------------------------
coffee_prices = {
    "Espresso": 2.5,
    "Latte": 3.5,
    "Cappuccino": 4.0
}

# -------------------------------
# Functions
# -------------------------------
def compute_price():
    coffee = coffee_var.get()
    if not coffee:
        return None
    price = coffee_prices.get(coffee, 0.0)
    size = size_var.get()
    if size == "Medium":
        price += 0.5
    elif size == "Large":
        price += 1.0
    # Add-ons: Milk and Sugar each cost $0.25
    if milk_var.get():
        price += 0.25
    if sugar_var.get():
        price += 0.25
    return price

def update_total_label(*args):
    price = compute_price()
    if price is None:
        total_label.config(text="Total: $0.00")
        place_order_button.config(state=tk.DISABLED)
    else:
        total_label.config(text=f"Total: ${price:.2f}")
        place_order_button.config(state=tk.NORMAL)

def calculate_total():
    price = compute_price()
    if price is None:
        messagebox.showwarning("Warning", "Please select a coffee!")
        return
    coffee = coffee_var.get()
    size = size_var.get()
    total_label.config(text=f"Total: ${price:.2f}")
    messagebox.showinfo(
        "Order Confirmed",
        f"You ordered a {size} {coffee} ☕\n\nTotal: ${price:.2f}\n\nThank you for visiting Python Coffee Shop!"
    )

def reset_order():
    coffee_var.set("")
    size_var.set("Small")
    milk_var.set(False)
    sugar_var.set(False)
    update_total_label()

# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()
root.title("☕ Python Coffee Shop")
root.geometry("650x690")  # Increased height for better visibility
root.config(bg="#f7ede2")
root.resizable(False, False)

# -------------------------------
# Title Section
# -------------------------------
title_frame = tk.Frame(root, bg="#6f4e37", height=80)
title_frame.pack(fill="x")

title_label = tk.Label(
    title_frame,
    text="☕ Python Coffee Shop",
    bg="#6f4e37",
    fg="white",
    font=("Poppins", 20, "bold")
)
title_label.pack(pady=20)

# -------------------------------
# Coffee Selection
# -------------------------------
coffee_frame = tk.LabelFrame(root, text="Select Your Coffee", font=("Poppins", 13, "bold"), bg="#f7ede2", padx=15, pady=10)
coffee_frame.pack(padx=20, pady=10, fill="x")

coffee_var = tk.StringVar()
for coffee, price in coffee_prices.items():
    ttk.Radiobutton(coffee_frame, text=f"{coffee} - ${price:.2f}", variable=coffee_var, value=coffee).pack(anchor="w", pady=3)

# -------------------------------
# Size Selection
# -------------------------------
size_frame = tk.LabelFrame(root, text="Choose Size", font=("Poppins", 13, "bold"), bg="#f7ede2", padx=15, pady=10)
size_frame.pack(padx=20, pady=10, fill="x")

size_var = tk.StringVar(value="Small")
for size in ["Small", "Medium", "Large"]:
    ttk.Radiobutton(size_frame, text=size, variable=size_var, value=size).pack(anchor="w", pady=3)

# -------------------------------
# Extras
# -------------------------------
extras_frame = tk.LabelFrame(root, text="Add Extras", font=("Poppins", 13, "bold"), bg="#f7ede2", padx=15, pady=10)
extras_frame.pack(padx=20, pady=10, fill="x")

# Separate options for Milk and Sugar so user can select one or both
milk_var = tk.BooleanVar()
sugar_var = tk.BooleanVar()
ttk.Checkbutton(extras_frame, text="Add Milk (+$0.25)", variable=milk_var).pack(anchor="w", pady=3)
ttk.Checkbutton(extras_frame, text="Add Sugar (+$0.25)", variable=sugar_var).pack(anchor="w", pady=3)

# -------------------------------
# Total Label
# -------------------------------
total_label = tk.Label(
    root,
    text="Total: $0.00",
    font=("Poppins", 16, "bold"),
    fg="#6f4e37",
    bg="#f7ede2"
)
total_label.pack(pady=20)

# -------------------------------
# Buttons
# -------------------------------
button_frame = tk.Frame(root, bg="#f7ede2")
button_frame.pack(pady=20)

style = ttk.Style()
style.configure("TButton", font=("Poppins", 11, "bold"), padding=8)

# create buttons (do not .grid() immediately on construction so we keep references)
place_order_button = ttk.Button(button_frame, text="☕ Place Order", command=calculate_total, width=18)
place_order_button.grid(row=0, column=0, padx=10, pady=5)
reset_button = ttk.Button(button_frame, text="🔁 Reset", command=reset_order, width=18)
reset_button.grid(row=0, column=1, padx=10, pady=5)

# -------------------------------
# Footer
# -------------------------------
footer = tk.Label(
    root,
    text="© 2025 Python Coffee Shop | Designed with ❤️ in Tkinter",
    bg="#f7ede2",
    fg="#7b6f63",
    font=("Poppins", 9)
)
footer.pack(side="bottom", pady=15)

# -------------------------------
# Traces to update total immediately when selections change
coffee_var.trace_add("write", update_total_label)
size_var.trace_add("write", update_total_label)
milk_var.trace_add("write", update_total_label)
sugar_var.trace_add("write", update_total_label)

# initialize UI state
update_total_label()

root.mainloop()
