    R = np.zeros((3, 3), dtype=np.float64)
    cv2.Rodrigues(rvecs, R)
    rvecs = np.zeros((1, 1, 3), dtype=np.float64)
    rvecs,_ = cv2.Rodrigues(R, rvecstmp)