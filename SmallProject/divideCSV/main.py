import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os


class FileSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Splitter")

        self.label = tk.Label(root, text="Select a file to split (CSV or XLSX):")
        self.label.grid(row=0, column=0)

        self.file_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.file_button.grid(row=0, column=1)

        self.label_chunks = tk.Label(root, text="Enter number of rows per chunk:")
        self.label_chunks.grid(row=1)

        self.chunk_entry = tk.Entry(root)
        self.chunk_entry.grid(row=2)

        self.sheet_option = tk.StringVar(value="name")

        self.label_sheet_option = tk.Label(root, text="Select sheet option:")
        self.label_sheet_option.grid(row=3)

        self.radio_name = tk.Radiobutton(
            root, text="Sheet Name", variable=self.sheet_option, value="name"
        )
        self.radio_name.grid(row=4)

        self.radio_index = tk.Radiobutton(
            root, text="Sheet Index", variable=self.sheet_option, value="index"
        )
        self.radio_index.grid(row=4, column=1)

        self.label_sheet = tk.Label(root, text="Enter sheet name or index (for XLSX):")
        self.label_sheet.grid(row=5)

        self.sheet_entry = tk.Entry(root)
        self.sheet_entry.grid(row=6)

        self.label_start_row = tk.Label(root, text="Enter start row (0-indexed):")
        self.label_start_row.grid(row=7)

        self.start_row_entry = tk.Entry(root)
        self.start_row_entry.grid(row=8)

        self.label_end_row = tk.Label(
            root, text="Enter end row (0-indexed, inclusive):"
        )
        self.label_end_row.grid(row=9)

        self.end_row_entry = tk.Entry(root)
        self.end_row_entry.grid(row=10)

        self.label_start_col = tk.Label(root, text="Enter start column (0-indexed):")
        self.label_start_col.grid(row=11)

        self.start_col_entry = tk.Entry(root)
        self.start_col_entry.grid(row=12)

        self.label_end_col = tk.Label(
            root, text="Enter end column (0-indexed, inclusive):"
        )
        self.label_end_col.grid(row=13)

        self.end_col_entry = tk.Entry(root)
        self.end_col_entry.grid(row=14)

        self.split_button = tk.Button(root, text="Split File", command=self.split_file)
        self.split_button.grid(row=15)

        self.status = tk.Label(root, text="", fg="red")
        self.status.grid(row=16)

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )
        self.status.config(text=f"Selected file: {self.file_path}")

    def split_file(self):
        try:
            rows_per_chunk = int(self.chunk_entry.get())
            if rows_per_chunk <= 0:
                raise ValueError("Number of rows must be greater than 0")

            sheet_value = self.sheet_entry.get()
            if self.sheet_option.get() == "index":
                sheet_value = int(sheet_value)

            start_row = (
                int(self.start_row_entry.get()) if self.start_row_entry.get() else None
            )
            end_row = (
                int(self.end_row_entry.get()) if self.end_row_entry.get() else None
            )
            start_col = (
                int(self.start_col_entry.get()) if self.start_col_entry.get() else None
            )
            end_col = (
                int(self.end_col_entry.get()) if self.end_col_entry.get() else None
            )

            self.split(
                self.file_path,
                rows_per_chunk,
                sheet_value,
                start_row,
                end_row,
                start_col,
                end_col,
            )
            self.status.config(text="File split successfully!", fg="green")
        except Exception as e:
            self.status.config(text=str(e), fg="red")

    def split(
        self,
        file_path,
        rows_per_chunk,
        sheet_value,
        start_row,
        end_row,
        start_col,
        end_col,
    ):
        file_name, file_extension = os.path.splitext(file_path)
        dir_name = os.path.dirname(file_path)
        base_name = os.path.basename(file_name)
        chunk_count = 0

        if file_extension == ".csv":
            reader = pd.read_csv(file_path, chunksize=rows_per_chunk)
            for chunk in reader:
                chunk = self.extract_chunk(
                    chunk, start_row, end_row, start_col, end_col
                )
                chunk_count += 1
                output_file = os.path.join(
                    dir_name, f"{base_name}_part{chunk_count}{file_extension}"
                )
                chunk.to_csv(output_file, index=False)
        elif file_extension == ".xlsx":
            data = pd.read_excel(file_path, sheet_name=sheet_value)
            data = self.extract_chunk(data, start_row, end_row, start_col, end_col)
            total_rows = len(data)
            for start_row_chunk in range(0, total_rows, rows_per_chunk):
                chunk = data.iloc[start_row_chunk : start_row_chunk + rows_per_chunk]
                chunk_count += 1
                output_file = os.path.join(
                    dir_name, f"{base_name}_part{chunk_count}{file_extension}"
                )
                chunk.to_excel(output_file, index=False, engine="openpyxl")
        else:
            raise ValueError("Unsupported file format")

    def extract_chunk(self, data, start_row, end_row, start_col, end_col):
        if start_row is not None and end_row is not None:
            data = data.iloc[start_row : end_row + 1]
        if start_col is not None and end_col is not None:
            data = data.iloc[:, start_col : end_col + 1]
        return data


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSplitterApp(root)
    root.mainloop()
