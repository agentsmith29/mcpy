class UIBase(object):
    def __init__(self, parent, logger):
        self._x = None
        self._y = None
        self.parent = parent
        self.logger = logger
        self.layout = None
        self.figure = None
        self.canvas = None

    def generate_ui(self):
        raise NotImplementedError

    def generate_plot(self):
        self.logger.debug("Generating plot for normal distribution")

        try:
            # import the necessary widgets
            from PySide6 import QtWidgets, QtCore
            from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
            from matplotlib.figure import Figure
            from matplotlib import pyplot as plt
            from matplotlib.ticker import ScalarFormatter

        except ImportError as e:
            self.logger.error("Unable to import necessary modules for generating plot")
            raise e
        plt.rcParams.update({'font.size': 8})

        if self.layout is None:
            self.layout = QtWidgets.QVBoxLayout()

        if self.figure is None:
            self.figure = plt.figure(figsize=(3, 10))

        if self.canvas is None:
            self.canvas = FigureCanvas(self.figure)

        self.layout.addWidget(self.canvas)

        # Generate data points for the rectangular distribution (implemented by the subclass)
        self._x, self._y = self._plot_points()

        # Clear the existing plot and plot the new data
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        self._set_axis(ax)  # Set the axis formatting (implemented by the subclass)
        self._show_confidence_interval(ax)  # Show the confidence interval (implemented by the subclass)

        # PLot the data
        self._plot(ax)
        y_formatter = ScalarFormatter(useOffset=True)
        ax.yaxis.set_major_formatter(y_formatter)

        self._set_labels(ax)  # Set the labels (x-axis, y-axis and title) for the plot (implemented by the subclass)
       # self.figure.tight_layout()

        self.canvas.draw()
        return self.layout

    def _plot(self, ax):
        ax.plot(self._x, self._y, linewidth=1)

    def _plot_points(self):
        '''
        Defines the x and y plot points for the distribution. Must be
        implemented by the subclass
        :return:
        '''
        raise NotImplementedError("This method must be implemented by the subclass")

    def _set_axis(self, ax):
        '''
        Sets the axis labels for the plot. Must be implemented by the subclass
        :param ax:
        :return:
        '''
        raise NotImplementedError("This method must be implemented by the subclass")

    def _show_confidence_interval(self, ax):
        '''
        Shows the confidence interval on the plot. Must be implemented by the subclass
        :param ax:
        :return:
        '''
        raise NotImplementedError("This method must be implemented by the subclass")

    def _set_labels(self, ax):
        '''
        Sets the labels (x-axis, y-axis and title) for the plot. Must be implemented by the subclass
        :param ax:
        :return:
        '''
        raise NotImplementedError("This method must be implemented by the subclass")
