import pandas as pd
import fitz
import PyPDF2
import os

from psc_gui import Ui_PSC_GUI
from dataframe_model import PandasModel

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc

class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.file_names = None
        self.df_o = None
        self.ui = Ui_PSC_GUI()
        self.ui.setupUi(self)

#   Buttons
        self.ui.open_file_button.clicked.connect(self.select_file)
        self.ui.run_button.clicked.connect(self.sign_search)
        self.ui.save_button.clicked.connect(self.save_data_as_xlsx)
        self.ui.save_who_button.clicked.connect(self.save_tidy_data_as_xlsx)
        

    def sign_search(self):

        def sign_check(file):
            who = "-"
            who_list = "-"
            has_v = []
            size = []
            file = str(file)
            if fitz.open(file).get_sigflags() == 3:
                ff = PyPDF2.PdfFileReader(file, strict=False).getFields()
                sigs = list(ff)
                for i in range(len(ff)):
                    has_v.append("/V" in ff[sigs[i]])
                    size.append(len(ff[list(ff)[i]]))
                test = all(elem == True for elem in has_v)
                if test == True:
                    result = "All Signed"
                else:
                    result = "Missing Signatures"
                    output = [i for i, x in enumerate(has_v) if not (x)]
                    who_list = []
                    for i in output:
                        who_list.append(list(ff)[i])
                    who = ", ".join(who_list)
            else:
                result = "No Signatures"
            return result, who, who_list

        def loop_sign_check(filenames):
            result = [sign_check(i) for i in filenames]
            df = pd.DataFrame(result, columns=["results", "missing_who", "missing_signature"])
            df["file_name"] = filenames
            df["file"] = df["file_name"].apply(os.path.basename)
            return df

        self.df_raw = loop_sign_check(self.file_names)
        self.df_tidy = self.df_raw.explode("missing_signature")
        self.df_tidy = self.df_tidy[["file", "results", "missing_signature"]]
        self.df_o = self.df_raw[["file", "results", "missing_who"]]
        
        self.model = PandasModel(self.df_o)
        self.proxymodel = qtc.QSortFilterProxyModel()
        self.proxymodel.setSourceModel(self.model)
        self.proxymodel.setFilterKeyColumn(-1)
        self.ui.pandas_table.setModel(self.proxymodel)

    def select_file(self):
        # open file dialog
        self.file_names, _ = qtw.QFileDialog.getOpenFileNames(
            self, "Open File", "", "pdf (*.pdf)"
        )
        self.ui.file_confirm.setText(f"{str(len(self.file_names))} file/s selected")


    def save_data_as_xlsx(self):
        name = qtw.QFileDialog.getSaveFileName(self, "Save File", filter="*.xlsx")
        if name[0] == "":
            pass
        else:
            self.df_o.to_excel(name[0], index=False)

    def save_tidy_data_as_xlsx(self):
        name = qtw.QFileDialog.getSaveFileName(self, "Save File", filter="*.xlsx")
        if name[0] == "":
            pass
        else:
            self.df_tidy.to_excel(name[0], index=False)

if __name__ == "__main__":
    app = qtw.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
