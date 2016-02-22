import pandas as pd
import Quandl


class CSVDataSource:
    """
    Loads a CSV into a pandas dataframe
    """

    def __init__(self, fname, fields):
        """
        loads the CSV
        :param fname: csv file name
        :param fields: header names
        """
        self.data = pd.read_csv(fname, names=fields, parse_dates=True)

    def parse_timestamp_column(self, label, unit, set_index=True):
        """
        Convert (if necessary) a given column into a pandas timestamp type to allow handling of time series
        :param label: column to check
        :param unit: if column is already a timestamp, i.e. an integer, whats the time unit.
        :return:
        """
        if isinstance(self.data[label][0], pd.tslib.Timestamp):
            if set_index:
                self.data.set_index(label, inplace=True)
            return
        self.data[label] = pd.to_datetime(self.data[label], unit=unit)
        if set_index:
            self.data.set_index(label, inplace=True)
