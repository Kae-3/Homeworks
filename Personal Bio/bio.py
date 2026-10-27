import tkinter as tk
from tkinter import messagebox


class PersonalBioForm:

  def __init__(self, root):
    self.root = root
    self.root.title("Personal Bio Form")
    self.root.geometry("450x550")
    self.root.config(bg="#f8fafc")

    # Header
    tk.Label(
        root,
        text="Personal Bio Registration",
        font=("Arial", 16, "bold"),
        bg="#f8fafc",
        fg="#1e293b",
    ).pack(pady=15)

    # Form Container Frame
    form_frame = tk.Frame(root, bg="#f8fafc")
    form_frame.pack(pady=10, padx=20)

    # Field 1: Full Name
    tk.Label(
        form_frame,
        text="Full Name:",
        font=("Arial", 10, "bold"),
        bg="#f8fafc",
    ).grid(row=0, column=0, sticky="w", pady=5)
    self.name_entry = tk.Entry(form_frame, width=30)
    self.name_entry.grid(row=0, column=1, pady=5)

    # Field 2: Age
    tk.Label(
        form_frame, text="Age:", font=("Arial", 10, "bold"), bg="#f8fafc"
    ).grid(row=1, column=0, sticky="w", pady=5)
    self.age_entry = tk.Entry(form_frame, width=30)
    self.age_entry.grid(row=1, column=1, pady=5)

    # Field 3: Gender
    tk.Label(
        form_frame, text="Gender:", font=("Arial", 10, "bold"), bg="#f8fafc"
    ).grid(row=2, column=0, sticky="w", pady=5)
    self.gender_var = tk.StringVar(value="Male")
    gender_frame = tk.Frame(form_frame, bg="#f8fafc")
    gender_frame.grid(row=2, column=1, sticky="w")
    tk.Radiobutton(
        gender_frame,
        text="Male",
        variable=self.gender_var,
        value="Male",
        bg="#f8fafc",
    ).pack(side="left")
    tk.Radiobutton(
        gender_frame,
        text="Female",
        variable=self.gender_var,
        value="Female",
        bg="#f8fafc",
    ).pack(side="left")

    # Field 4: Profession
    tk.Label(
        form_frame, text="Profession:", font=("Arial", 10, "bold"), bg="#f8fafc"
    ).grid(row=3, column=0, sticky="w", pady=5)
    self.prof_entry = tk.Entry(form_frame, width=30)
    self.prof_entry.grid(row=3, column=1, pady=5)

    # Field 5: Bio Summary / Hobbies
    tk.Label(
        form_frame,
        text="Short Bio / Hobbies:",
        font=("Arial", 10, "bold"),
        bg="#f8fafc",
    ).grid(row=4, column=0, sticky="nw", pady=5)
    self.bio_text = tk.Text(form_frame, width=23, height=4)
    self.bio_text.grid(row=4, column=1, pady=5)

    # Submit Button
    tk.Button(
        root,
        text="Submit Bio",
        font=("Arial", 11, "bold"),
        bg="#2563eb",
        fg="white",
        padx=15,
        pady=5,
        command=self.submit_bio,
    ).pack(pady=15)

    # Output Card Frame
    self.output_frame = tk.LabelFrame(
        root,
        text=" Completed Bio Card ",
        font=("Arial", 10, "bold"),
        bg="#ffffff",
        fg="#0f172a",
        width=380,
        height=140,
    )
    self.output_frame.pack(pady=10, fill="both", expand=True, padx=20)
    self.output_frame.pack_propagate(False)

    self.display_label = tk.Label(
        self.output_frame,
        text="Submit the form to generate your bio card here.",
        font=("Arial", 9, "italic"),
        bg="#ffffff",
        fg="#64748b",
        justify="left",
    )
    self.display_label.pack(padx=10, pady=10, anchor="w")

  def submit_bio(self):
    name = self.name_entry.get().strip()
    age = self.age_entry.get().strip()
    gender = self.gender_var.get()
    profession = self.prof_entry.get().strip()
    bio_content = self.bio_text.get("1.0", tk.END).strip()

    if not name or not age or not profession:
      messagebox.showwarning(
          "Missing Information", "Please fill in all required text fields!"
      )
      return

    bio_summary = (
        f"📌 Name: {name}\n"
        f"🎂 Age: {age} | Gender: {gender}\n"
        f"💼 Profession: {profession}\n"
        f"📝 About: {bio_content}"
    )

    self.display_label.config(
        text=bio_summary, font=("Arial", 10, "normal"), fg="#0f172a"
    )
    messagebox.showinfo("Success", "Personal Bio created successfully!")


if __name__ == "__main__":
  root = tk.Tk()
  app = PersonalBioForm(root)
  root.mainloop()