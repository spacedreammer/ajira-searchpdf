import tkinter as tk
from tkinter import scrolledtext, ttk
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pdfplumber
import io
import threading

# --------------------------
# Core search function
# --------------------------
def search_name_in_pdf_url(pdf_url, name_to_search, output_box):
    try:
        r = requests.get(pdf_url, timeout=15)
        file_like = io.BytesIO(r.content)

        found = False
        last_mamlaka = ""
        last_kada = ""

        with pdfplumber.open(file_like) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        if row and len(row) >= 5:
                            cleaned_row = [str(cell).strip() if cell else "" for cell in row]

                            if cleaned_row[1]:
                                last_mamlaka = cleaned_row[1]
                            if cleaned_row[2]:
                                last_kada = cleaned_row[2]

                            if name_to_search.lower() in cleaned_row[4].lower():
                                start_index = output_box.index(tk.END)

                                output_box.insert(tk.END, f"\n✅ 🎉🎉🎉🎉🎉🎉Found in {pdf_url} (Page {page_number}) 🎉🎉🎉🎉\n")
                                output_box.insert(tk.END, f"   MAMLAKA YA AJIRA: {last_mamlaka}\n")
                                output_box.insert(tk.END, f"   KADA: {last_kada}\n")
                                output_box.insert(tk.END, f"  🎉Hongera🎉🎉 JINA: {cleaned_row[4]} 🎉🎉\n\n")

                                end_index = output_box.index(tk.END)
                                output_box.tag_add("highlight", start_index, end_index)

                                found = True
        if not found:
            output_box.insert(tk.END, f"❌ '{name_to_search}' not found in {pdf_url}\n\n")
    except Exception as e:
        output_box.insert(tk.END, f"⚠️ Error reading {pdf_url}: {e}\n\n")


# --------------------------
# Worker Thread
# --------------------------
def run_search(name_to_search, num_pdfs, output_box, progress):
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, f"🔎 Searching for '{name_to_search}' in {num_pdfs} PDF(s)...\n\n")

    # Scrape Ajira homepage
    base_url = "https://www.ajira.go.tz"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    pdf_links = []
    for links in soup.find_all('a', href=True):
        href = links['href']
        if href.lower().endswith('.pdf') and "/baseattachments/placementsattachments/" in href:
            full_url = urljoin(base_url, href)
            pdf_links.append(full_url)

    pdf_links = pdf_links[:num_pdfs]

    progress["value"] = 0
    progress["maximum"] = len(pdf_links)

    for i, pdf_url in enumerate(pdf_links, start=1):
        output_box.insert(tk.END, f"📂 Checking: {pdf_url}\n")
        output_box.see(tk.END)

        search_name_in_pdf_url(pdf_url, name_to_search, output_box)

        progress["value"] = i
        progress.update()

    output_box.insert(tk.END, "\n✅ Search completed!\n")
    output_box.see(tk.END)


# --------------------------
# Start Search
# --------------------------
def start_search():
    name_to_search = entry.get().strip()
    try:
        num_pdfs = int(pdf_limit.get())
    except ValueError:
        output_box.insert(tk.END, "⚠️ Please enter a valid number of PDFs.\n")
        return

    if not name_to_search:
        output_box.insert(tk.END, "⚠️ Please enter a name first.\n")
        return

    threading.Thread(target=run_search, args=(name_to_search, num_pdfs, output_box, progress), daemon=True).start()


# --------------------------
# Tkinter GUI Setup
# --------------------------
root = tk.Tk()
root.title("Ajira PDF Name Search Tool")

# Name input
tk.Label(root, text="Enter Name:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# PDF limit input
tk.Label(root, text="Number of PDFs to search:").pack(pady=5)
pdf_limit = tk.Entry(root, width=10)
pdf_limit.insert(0, "5")
pdf_limit.pack(pady=5)

# Search button
search_button = tk.Button(root, text="Search", command=start_search, bg="lightblue")
search_button.pack(pady=5)

# Progress bar
progress = ttk.Progressbar(root, length=400, mode="determinate")
progress.pack(pady=5)

# Results box
output_box = scrolledtext.ScrolledText(root, width=100, height=30, wrap=tk.WORD)
output_box.pack(pady=10)

# Configure text highlighting style
output_box.tag_configure("highlight", foreground="blue", font=("Helvetica", 13, "bold"))

# Run GUI
root.mainloop()





















