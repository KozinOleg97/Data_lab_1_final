from random import randrange

from scipy import io
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Dataset:

    def __init__(self, filename):
        mat = io.loadmat(filename)
        self.examples = mat["examples"][0]
        self.size = self.examples.size

    def showKeypointRnd(self):
        index = randrange(self.size)
        example = self.examples[index]
        keypoints = example[2].T
        filename = example[3][0]

        img = mpimg.imread("FLIC/images/" + filename)
        imgplot = plt.imshow(img)

        for x, y in filter(lambda value: 0 <= value[0], keypoints):
            circle = plt.Circle((x, y), radius=2, color="red")
            ax = plt.gca()
            ax.add_patch(circle)

        plt.show()

    def showKeypoint(self, index):
        example = self.examples[index]
        keypoints = example[2].T
        filename = example[3][0]

        img = mpimg.imread("FLIC/images/" + filename)
        imgplot = plt.imshow(img)

        for x, y in filter(lambda value: 0 <= value[0], keypoints):
            circle = plt.Circle((x, y), radius=2, color="red")
            ax = plt.gca()
            ax.add_patch(circle)

        plt.show()

        # image = Image.open("FLIC/images/" + filename)
        # draw = ImageDraw.Draw(image)
        # for x, y in filter(lambda value: 0 <= value[0], keypoints):
        #    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(255, 0, 0))

        # image.show()


flic = Dataset("FLIC/examples.mat")

#flic.showKeypoint(1202)
flic.showKeypointRnd()
