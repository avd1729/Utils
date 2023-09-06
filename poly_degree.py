from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


curve = pd.read_csv("curve.csv")
curve.head()

# Split the dataset into 60:40 split into training and test set
train_X, test_X, train_y, test_y = train_test_split(curve.x,
                                                    curve.y,
                                                    test_size=0.40,
                                                    random_state=100)
# Define the dataframe store degree and rmse for training and test set
rmse_df = pd.DataFrame(columns=["degree", "rmse_train", "rmse_test"])
# Define a method to return the rmse given actual and predicted values.


def get_rmse(y, y_fit):
    return np.sqrt(mean_squared_error(y, y_fit))


# Iterate from degree 1 to 15
for i in range(1, 15):
    # fitting model
    p = np.polyfit(train_X, train_y, deg=i)
    # storing model degree and rmse on train and test set
    rmse_df.loc[i-1] = [i,
                        get_rmse(train_y, np.polyval(p, train_X)),
                        get_rmse(test_y, np.polyval(p, test_X))]
print(rmse_df)
