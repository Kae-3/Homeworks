import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class PhotoAlbumApp:

  def __init__(self, root):
    self.root = root
    self.root.title("My Photo Album")
    self.root.geometry("450x520")
    self.root.config(bg="#f0f4f8")

    # Title Header
    tk.Label(
        root,
        text="📷 My Digital Photo Album",
        font=("Segoe UI", 16, "bold"),
        bg="#f0f4f8",
        fg="#1a365d",
    ).pack(pady=10)

    # Album Data (Title, Description, Color placeholder if image file missing)
    self.photos = [
        {"title": "Sunset View", "desc": "A beautiful golden hour sunset."},
        {"title": "Mountain Peak", "desc": "Snow-capped mountains in winter."},
        {"title": "Green Forest", "desc": "Lush green trees and nature trail."},
    ]
    self.current_index = 0

    # Image Canvas/Label
    self.image_label = tk.Label(
        root, bg="#cbd5e1", width=350, height=220, text="[ Image Area ]"
    )
    self.image_label.pack(pady=10)

    # Caption Label
    self.caption_label = tk.Label(
        root,
        text=self.photos[self.current_index]["title"],
        font=("Segoe UI", 13, "bold"),
        bg="#f0f4f8",
    )
    self.caption_label.pack(pady=5)

    # Navigation Controls Frame
    nav_frame = tk.Frame(root, bg="#f0f4f8")
    nav_frame.pack(pady=10)

    tk.Button(
        nav_frame,
        text="◀ Previous",
        command=self.prev_photo,
        width=10,
        bg="#2b6cb0",
        fg="white",
    ).grid(row=0, column=0, padx=10)
    tk.Button(
        nav_frame,
        text="Next ▶",
        command=self.next_photo,
        width=10,
        bg="#2b6cb0",
        fg="white",
    ).grid(row=0, column=1, padx=10)

    # Action Buttons Frame
    action_frame = tk.Frame(root, bg="#f0f4f8")
    action_frame.pack(pady=10)

    tk.Button(
        action_frame,
        text="View Details (Toplevel)",
        command=self.open_details_window,
        bg="#319795",
        fg="white",
        font=("Segoe UI", 10, "bold"),
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        action_frame,
        text="Album Info Popup",
        command=self.show_album_info,
        bg="#4a5568",
        fg="white",
        font=("Segoe UI", 10),
    ).grid(row=0, column=1, padx=5)

    self.load_current_photo()

  def load_current_photo(self):
    photo_info = self.photos[self.current_index]
    self.caption_label.config(text=photo_info["title"])

    # Attempt to load or generate image preview
    try:
      # If you have local images, specify image path here
      img = Image.new("RGB", (350, 220), color=(100 + self.current_index * 50, 140, 200))
      photo = ImageTk.PhotoImage(img)
      self.image_label.config(image=photo, text="")
      self.image_label.image = photo  # Keep reference
    except Exception as e:
      self.image_label.config(text=f"Photo: {photo_info['title']}")

  def next_photo(self):
    self.current_index = (self.current_index + 1) % len(self.photos)
    self.load_current_photo()

  def prev_photo(self):
    self.current_index = (self.current_index - 1) % len(self.photos)
    self.load_current_photo()

  def show_album_info(self):
    messagebox.showinfo(
        "Album Information",
        f"Photo Album App v1.0\nTotal Photos: {len(self.photos)}\nCurrent View: #{self.current_index + 1}",
    )

  def open_details_window(self):
    # Open Toplevel Window
    detail_win = tk.Toplevel(self.root)
    detail_win.title("Photo Details")
    detail_win.geometry("300x200")
    detail_win.config(bg="#ffffff")

    photo = self.photos[self.current_index]

    tk.Label(
        detail_win,
        text="Detailed Photo Information",
        font=("Segoe UI", 11, "bold"),
        bg="#ffffff",
        fg="#2d3748",
    ).pack(pady=10)
    tk.Label(
        detail_win,
        text=f"Title: {photo['title']}",
        font=("Segoe UI", 10, "bold"),
        bg="#ffffff",
    ).pack(anchor="w", padx=20, pady=2)
    tk.Label(
        detail_win,
        text=f"Description: {photo['desc']}",
        font=("Segoe UI", 10),
        bg="#ffffff",
        wraplength=250,
        justify="left",
    ).pack(anchor="w", padx=20, pady=5)

    tk.Button(
        detail_win,
        text="Close Window",
        command=detail_win.destroy,
        bg="#e53e3e",
        fg="white",
    ).pack(pady=15)


if __name__ == "__main__":
  root = tk.Tk()
  app = PhotoAlbumApp(root)
  root.mainloop()