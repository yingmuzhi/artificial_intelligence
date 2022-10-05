"""
utils function
"""
import  torch
from    matplotlib import pyplot as plt


def plot_curve(data):
    """draw loss function

    Args:
        data (_type_): _description_
    """
    fig = plt.figure()
    plt.plot(range(len(data)), data, color = "blue")
    plt.legend(["value"], loc = "upper right")
    plt.xlabel("step")
    plt.ylabel("value")
    plt.show()

def plot_image(img, label, name):
    """show result

    Args:
        img (_type_): _description_
        label (_type_): _description_
        name (_type_): _description_
    """
    fig = plt.figure()
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.tight_layout()
        plt.imshow(img[i][0] * 0.3081 + 0.1307, cmap = "gray", interpolation = "none")
        plt.title("{}: {}".format(name, label[i].item()))
        plt.xticks([])
        plt.yticks([])
    plt.show()

def one_hot(label, depth = 10):
    """one hot

    Args:
        label (_type_): _description_
        depth (int, optional): _description_. Defaults to 10.

    Returns:
        _type_: _description_
    """
    out = torch.zeros(label.size(0), depth)
    idx = torch.LongTensor(label).view(-1, 1)
    out.scatter_(dim = 1, index = idx, value = 1)
    return out
