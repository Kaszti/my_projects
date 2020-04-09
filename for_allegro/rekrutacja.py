import numpy as np


class Model:

  def fit(self, X: np.ndarray, y: np.ndarray) -> None:
    pass

  def predict(self, X: np.ndarray) -> np.ndarray:
    pass

  @staticmethod
  def evaluate(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    # calculate accuracy
    pass
