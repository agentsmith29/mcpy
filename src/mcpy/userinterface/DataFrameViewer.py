import numpy as np
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QTableView, QMainWindow, QTableWidgetItem, QVBoxLayout, QWidget, QTableWidget


class DataFrameViewer(QMainWindow):
    def __init__(self, data):
        super().__init__()

        self.setWindowTitle("NumPy Array Table View")
        self.setGeometry(100, 100, 600, 400)

        # Create a QTableWidget to display the data
        self.table_widget = QTableWidget(self)
        if isinstance(data, list):
            data = np.array(data).reshape((len(data), 1))
        self.set_data(data.reshape((len(data), 1)))

        # Set the table as the central widget
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def set_data(self, data):
        # Check if the input is a NumPy array
        if not isinstance(data, np.ndarray):
            raise ValueError(f"Input must be a NumPy array, got {type(data)}")

        # Get the dimensions of the array
        num_rows, num_cols = data.shape

        # Set the number of rows and columns in the table
        self.table_widget.setRowCount(num_rows)
        self.table_widget.setColumnCount(num_cols)

        # Fill the table with data from the NumPy array
        for row in range(num_rows):
            for col in range(num_cols):
                item = QTableWidgetItem(str(data[row, col]))
                self.table_widget.setItem(row, col, item)