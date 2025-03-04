import numpy as np
from sklearn.linear_model import LinearRegression


def linear_imputation(data):
    """
    Impute missing values using linear regression.

    Args:
        data (np.ndarray): 2D array with missing values (NaN)

    Returns:
        np.ndarray: Imputed data array
    """
    data_imputed = data.copy()
    n_samples, n_features = data.shape

    for col in range(n_features):
        # Check for missing values in current column
        if np.isnan(data_imputed[:, col]).any():
            other_cols = [c for c in range(n_features) if c != col]

            # Get valid training rows (no missing in current or other columns)
            valid_mask = ~np.isnan(data_imputed[:, col]) & ~np.isnan(data_imputed[:, other_cols]).any(axis=1)
            if valid_mask.sum() < 2:  # Need at least 2 samples for linear regression
                raise ValueError(f"Not enough training data for column {col}")

            # Train model
            X_train = data_imputed[valid_mask][:, other_cols]
            y_train = data_imputed[valid_mask, col]
            model = LinearRegression().fit(X_train, y_train)

            # Predict missing values where other features exist
            missing_mask = np.isnan(data_imputed[:, col])
            pred_mask = missing_mask & ~np.isnan(data_imputed[:, other_cols]).any(axis=1)
            if pred_mask.any():
                X_pred = data_imputed[pred_mask][:, other_cols]
                data_imputed[pred_mask, col] = model.predict(X_pred)

    return data_imputed


if __name__ == "__main__":
    # Test case
    test_data = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [np.nan, 10, 11],  # Missing in column 0
        [12, np.nan, 14]  # Missing in column 1
    ], dtype=float)

    print("Original data:\n", test_data)
    imputed_data = linear_imputation(test_data)
    print("\nImputed data:\n", np.round(imputed_data, 2))
