import tkinter as tk
import random
import time
from threading import Thread

def start_hack_simulation():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.configure(bg='black')

    text_widget = tk.Text(root, bg='black', fg='white', insertbackground='white',
                          font=('Courier', 16), wrap='none', borderwidth=0)
    text_widget.pack(expand=True, fill='both')

    def simulate_code():
        start_time = time.time()
        while time.time() - start_time < 5:
            line = ''.join(random.choices(['0', '1'], k=120))
            text_widget.insert('end', line + '\n')
            text_widget.see('end')
            time.sleep(0.02)

        # After 5 seconds, clear and show centered message
        text_widget.pack_forget()
        message = tk.Label(root, text="You are Hacked", font=('Arial', 60), fg='lime', bg='black')
        message.place(relx=0.5, rely=0.5, anchor='center')

    # Exit only if key 'p' is pressed
    def on_key(event):
        if event.char.lower() == 'p':
            root.destroy()

    root.bind("<Key>", on_key)

    Thread(target=simulate_code, daemon=True).start()
    root.mainloop()

start_hack_simulation()
