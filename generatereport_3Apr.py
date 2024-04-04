#!/usr/bin/python3


import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
import os
#import mgrs
#import utc

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        uic.loadUi('class_project.ui',self)
        self.report_text_output.setReadOnly(True)
        self.txrx_checkbox.stateChanged.connect(self.master)
        self.classification_combobox.currentIndexChanged.connect(self.master)
        self.dateTimeEdit.dateTimeChanged.connect(self.master)
        ##self.ui.browse_1.clicked.connect(self.browsebutton_Function)
        self.genname.clicked.connect(self.report_output)
        self.txrx_checkbox.stateChanged.connect(self.master)
        self.tx_freq_input.valueChanged.connect(self.master)
        self.tx_freq_input.valueChanged.connect(self.master)
        self.tx_callsign_input.textChanged.connect(self.master)
        self.rx_callsign_input.textChanged.connect(self.master)
        self.tx_freq_input.valueChanged.connect(self.master)
        self.tx_callsign_input.textChanged.connect(self.master)
        self.rx_callsign_input.textChanged.connect(self.master)
        self.talk_group_input.textChanged.connect(self.master)
        self.color_code_input.textChanged.connect(self.master)
        self.tx_radio_id_input.textChanged.connect(self.master)
        self.rx_radio_id_input.textChanged.connect(self.master)
        self.encryption_input.textChanged.connect(self.master)
        self.tech_input.textChanged.connect(self.master)
        self.radio_type_input.textChanged.connect(self.master)
        self.location_input.textChanged.connect(self.master)
        self.gist_input.textChanged.connect(self.master)
        
        #self.title = "Image Viewer"
        #self.setWindowTitle(self.title)
        #f_jack = QLabel(self.f_jack)
        #pixmap = QPixmap('PNG.png')
        #f_jack.setPixmap(pixmap)
        #f_jack.setScaledContents(True)
        #self.setCentralWidget(f_jack)
        #self.resize(pixmap.width(), pixmap.height())

        #self.f_jack.displayText()
        #f_jack = QLabel(self.f_jack)
        #pixmap = QPixmap('PNG.png')
        #f_jack.setPixmap(pixmap)

        self.show()

        #master method that prints inputs to the preview textbox
    def master(self):
        classification = self.classification_combobox.currentText()
        dt_edit = self.dateTimeEdit.dateTime()
        dt_string = dt_edit.toString("yyyyMMdd HHmm")
        tx_freq = self.tx_freq_input.value()
        rx_freq = self.rx_freq_input.value()
        state = self.txrx_checkbox.checkState()
        if state:
            self.rx_freq_input.setValue(tx_freq)
        elif not state:
            self.rx_freq_input.setValue(rx_freq)
        tx_call_sign_box = self.tx_callsign_input.displayText()
        rx_call_sign_box = self.rx_callsign_input.displayText()
        tg_input = self.talk_group_input.displayText()
        cc_input = self.color_code_input.displayText()
        txrid_input = self.tx_radio_id_input.displayText()
        rxrid_input = self.rx_radio_id_input.displayText()
        encr_input = self.encryption_input.displayText()
        tech_input = self.tech_input.displayText()
        type_input = self.radio_type_input.displayText()
        loc_input = self.location_input.displayText()
        gist = self.gist_input.toPlainText()

        preview = str(f"Classification: {classification}\n"
                     f"Location {loc_input}\nD&T: {dt_string}"
                     f"\nTxFreq: {tx_freq}Mhz // Tx Callsign: {tx_call_sign_box}  //  TxRID: {txrid_input}"
                     f"\nRxFreq: {rx_freq}  // Rx Callsign: {rx_call_sign_box}  //  Rx RID: {rxrid_input}"
                     f"\nTalkGroup: {tg_input}  //  ColorCode: {cc_input}  //  RadioType: {type_input}"
                     f"  //  Technology: {tech_input}  //  Encryption: {encr_input}\n\n"
                     f"Gist: {gist}")

        self.report_text_output.setText(preview)

        file = open("SIGINT Report.txt", "w")
        file.write(str(preview))
        file.close()


    def tx_output(self):
        tx_call_sign_box = self.tx_callsign_input.displayText()
        self.report_text_output.setText(str(tx_call_sign_box))

    def browsebutton_Function(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if file:
            self.ui.lineEdit.setText(str(file))

    def textFileOutput(self):
        output_DIR = self.ui.lineEdit.text()

        with open("Output.txt", "w") as text_file:
            print(f" Output Directory = {output_DIR}", file=text_file)

    def report_output(self):
        dt_edit = self.dateTimeEdit.dateTime()
        dt_string = dt_edit.toString("yyyyMMdd HHmm")

        report_data = {"Date Time": dt_string,
                       "Tx Freq": str(self.tx_freq_input.value()),
                       "Rx Freq": str(self.tx_freq_input.value()),
                       "Tx Call sign": self.tx_callsign_input.displayText(),
                       "Rx Call sign": str(self.rx_callsign_input.displayText()),
                       "Tx Radio ID": str(self.tx_radio_id_input.displayText()),
                       "Rx Radio ID": str(self.rx_radio_id_input.displayText()),
                       "Talk Group": str(self.talk_group_input.displayText()),
                       "Color_Code": str(self.color_code_input.displayText()),
                       "Radio Type": str(self.radio_type_input.displayText()),
                       "Technology": str(self.tech_input.displayText()),
                       "Encryption": str(self.encryption_input.displayText()),
                       "MGRS": str(self.location_input.displayText()),
                       "GIST": str(self.gist_input.toPlainText()),
                       }

        if not os.path.exists("dict_to_csv.csv"):
            with open("dict_to_csv.csv", "w") as csvout:
                csvout.write(",".join(report_data.keys()))
                csvout.write("\n")

        with open("dict_to_csv.csv", "a") as csvout:
            csvout.write(",".join(report_data.values()))
            csvout.write("\n")
    #def freq_generator(self):

'''    def report_generator(self):
        F_JACK = self.F_JACK.text()
        tx_freq = self.tx_freq_input(float(self.tx_freq_input))
        tx_callsign = self.tx_callsign_input.textChanged.connect(self.report_text_output)
        tx_radio_id = self.tx_radio_id_input.text()
        rx_freq = self.tx_freq_input()
        rx_callsign = self.rx_callsign_input.text()
        rx_radio_id = self.rx_radio_id_input.text()
        talk_group = self.talk_group_input.text()
        color_code = self.color_code_input.text()
        self.rx_freq_input.setValue(float(tx_freq))
        report_text_output = f'callsign:{tx_callsign}'
        self.report_text.Insertplaintext.connect(self.report_generator)
        self.report_text_output.textChanged[str].connect(self.report_text_output)
        self.report_text_output.setText(report_text_output)
'''





app = QtWidgets.QApplication(sys.argv)
windows = Ui()
app.exec_()

