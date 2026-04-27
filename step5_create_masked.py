import numpy as np

def create_masked_stipple(stipple_img: np.ndarray, mask_img: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    result = np.where(mask_img < threshold, 1.0, stipple_img)
    return result
    