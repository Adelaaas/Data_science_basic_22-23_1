a = np.array([-0.5, -12, 2.4, -0.1, 0], float)

z = np.ceil((a > 0) * a) + np.floor((a < 0) * a)
print(z)

