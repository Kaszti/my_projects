import numpy as np
import os
import codecs
import pickle


class Prime_numbers:
  #pierwsze

  def fit(self, X: np.ndarray, y: np.ndarray) -> None:
    pass

  def predict(self, X: np.ndarray) -> np.ndarray:
    pass

  @staticmethod
  def evaluate(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    # calculate accuracy
    pass


class Complex_numbers:
  #złożone

  def fit(self, X: np.ndarray, y: np.ndarray) -> None:
    pass

  def predict(self, X: np.ndarray) -> np.ndarray:
    pass

  @staticmethod
  def evaluate(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    # calculate accuracy
    pass


datapath = r'Data\\MNISTdata\\'
files = os.listdir(datapath)

def get_int(b):
  return int(codecs.encode(b, 'hex'), 16)

# data_dict = {}
# for file in files:
#   if file.endswith('ubyte'):
#     print(f'Reading {file}')
#     with open (datapath + file, 'rb') as f:
#       data = f.read()
#       type = get_int(data[:4])
#       length = get_int(data[4:8])
#       if type == 2051:
#         category = 'images'
#         num_rows = get_int(data[8:12])
#         num_columns = get_int(data[12:16])
#         parsed = np.frombuffer(data, dtype = np.uint8, offset = 16)
#         parsed = parsed.reshape(length, num_rows, num_columns)
#       elif type == 2049:
#         category = 'labels'
#         parsed = np.frombuffer(data, dtype = np.uint8, offset = 8)
#         parsed = parsed.reshape(length)
#       if length == 10000:
#         set = 'test'
#       elif length == 60000:
#         set ='train'
#       data_dict[set + '_' + category] = parsed

# with open(datapath + 'MNISTData.pkl', 'wb') as fp:
#   pickle.dump(data_dict, fp)

with open(datapath + 'MNISTData.pkl', 'rb') as fp:
  new_dict = pickle.load(fp)

print(new_dict['test_labels'][0])