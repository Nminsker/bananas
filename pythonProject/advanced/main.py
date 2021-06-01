# from dates import *
# from deco import *
#
#
# def to_date(date):
#     d, m, y = filter(lambda x: x != '.', date.split('.'))
#     d, m, y = int(d), int(m), int(y)
#     if not isinstance(d, int) or not isinstance(m, int) or not isinstance(y, int):
#         raise ValueError("Date must be a number")
#     return Date(d, m, y)
#
#
# def calender():
#     with open("eventLog.txt", "r") as f:
#         events = f.read()
#
#     cal = Calender()
#
#     for line in events.split('\n'):
#         t = line.split(' ')
#         try:
#             cal.add_event(t[0], to_date(t[1]))
#         except ValueError as e:
#             print("Skipped the event {0}: {1}".format(t, e))
#
#     cal.print_calender()
#     print(cal.get_all_events_in_month(7))

import cv2
import pytesseract
import context
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


if __name__ == '__main__':
    context.parse()