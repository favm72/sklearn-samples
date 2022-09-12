import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, x_max]x[y_min, y_max].
# step size in the mesh


def hex_to_dec_color(hex_str):
    return tuple(int(hex_str[i:i+2], 16)/255 for i in (0, 2, 4))


def do_plot(X, y, predict):
    h = .02  # step size in the mesh
    cmap_light = LinearSegmentedColormap.from_list(
        "mymap", [hex_to_dec_color(x) for x in ["FA8EA4", "7CFFB9", "9F98FF"]], N=100)
    cmap_bold = LinearSegmentedColormap.from_list(
        "dotmap", [hex_to_dec_color(x) for x in ["F0375C", "59B584", "473BEE"]], N=100)

    x_min, x_max = X[:, 0].min() - 0.2, X[:, 0].max() + 0.2
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.2
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    fig = plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, cmap=cmap_light)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    fig.axes[0].set_title('Classifier')
    fig.axes[0].set_xlabel('Length')
    fig.axes[0].set_ylabel('Width')
