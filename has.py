import tkinter as tk
from tkinter import messagebox

def check_eligibility():
    try:
        grade = float(entry_grade.get())
        mentor_meetings = int(entry_meetings.get())
        webinars = int(entry_webinars.get())
        assignments_missed = int(entry_missed.get())
        assignments_caught = int(entry_caught.get())
        assignments_late = int(entry_late.get())

        if (
            grade > 70 and
            mentor_meetings >= 5 and
            webinars >= 1 and
            assignments_missed <= 3 and
            assignments_caught <= 2 and
            assignments_late <= 2
        ):
            result_text = "✅ Eligible"
            result_label.config(fg="green")
        else:
            result_text = "❌ Not Eligible"
            result_label.config(fg="red")

        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")


root = tk.Tk()
root.title("Eligibility Calculator")
root.geometry("400x400")


tk.Label(root, text="Final Grade (%)").pack()
entry_grade = tk.Entry(root)
entry_grade.pack()

tk.Label(root, text="Mentor Meetings Attended").pack()
entry_meetings = tk.Entry(root)
entry_meetings.pack()

tk.Label(root, text="Webinars Attended").pack()
entry_webinars = tk.Entry(root)
entry_webinars.pack()

tk.Label(root, text="Assignments Missed").pack()
entry_missed = tk.Entry(root)
entry_missed.pack()

tk.Label(root, text="Assignments Caught for AI").pack()
entry_caught = tk.Entry(root)
entry_caught.pack()

tk.Label(root, text="Assignments Late").pack()
entry_late = tk.Entry(root)
entry_late.pack()


check_button = tk.Button(root, text="Check Eligibility", command=check_eligibility, bg="blue", fg="white")
check_button.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()


root.mainloop()
