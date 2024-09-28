import tkinter as tk
from tkinter import scrolledtext, font, messagebox
from nltk_utils import get_response
from unrecognised_responses import cluster_unrecognized_questions


def send():
    user_input = entry.get()
    if user_input:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {user_input}\n")
        response = get_response(user_input)
        chat_window.insert(tk.END, f"Chatbot: {response}\n\n")
        chat_window.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        chat_window.yview(tk.END)


def show_about():
    messagebox.showinfo("About", "Chatbot Application\nVersion 1.0")


def view_clustered_questions():
    # Call the clustering function and store the results
    clustered_questions = cluster_unrecognized_questions()

    # Create a new window to display clusters
    cluster_window = tk.Toplevel(root)
    cluster_window.title("Clustered Questions")
    cluster_window.geometry("400x400")

    # Create a scrolled text area for displaying the clusters
    cluster_text = scrolledtext.ScrolledText(cluster_window, wrap=tk.WORD, state=tk.NORMAL, height=20, width=50,
                                             bg="#fff0f5", fg="#d36c6c", font=chat_font, borderwidth=2,
                                             relief=tk.SUNKEN)
    cluster_text.pack(padx=10, pady=10)

    # Insert clustered questions into the text area
    for i, cluster in enumerate(clustered_questions):
        cluster_text.insert(tk.END, f"Cluster {i}:\n")
        for question in cluster:
            cluster_text.insert(tk.END, f"  - {question}\n")
        cluster_text.insert(tk.END, "\n")

    cluster_text.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("SereneBot")
root.geometry("500x500")
root.configure(bg="#ffe4e1")

# Create the chat window
chat_font = font.Font(family="Arial", size=15)
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, height=20, width=50,
                                        bg="#fff0f5", fg="#d36c6c", font=chat_font, borderwidth=2, relief=tk.SUNKEN)
chat_window.pack(padx=10, pady=10)

# Insert the welcome message
chat_window.config(state=tk.NORMAL)
chat_window.insert(tk.END, "Welcome to SereneBot AI! How can I assist you today?\n\n")
chat_window.config(state=tk.DISABLED)

# Create the entry widget
entry_font = font.Font(family="Arial", size=15)
entry = tk.Entry(root, width=60, font=entry_font, bg="#ffffff", fg="#d36c6c", bd=2, relief=tk.SOLID)
entry.pack(padx=10, pady=(0, 10))

# Create the send button
button_font = font.Font(family="Arial", size=14, weight="bold")
send_button = tk.Button(root, text="Send", command=send, bg="#ff69b4", fg="black", font=button_font,
                        relief=tk.RAISED, bd=2, height=2, width=15)
send_button.pack(padx=10, pady=10)

# Add a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

# Add the cluster menu item
view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="View Unrecognised Questions", command=view_clustered_questions)

# Bind keyboard shortcut
root.bind('<Return>', lambda event: send())

# Run the Tkinter event loop
root.mainloop()
