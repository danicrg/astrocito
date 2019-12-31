import numpy as np
import math
from numpy.random import randint as random
from random import sample, choice
from tqdm import tqdm


def getDirectionArray(direction):
    up = 1 * (direction[0] >= 0) + -1 * (direction[0] < 0)
    right = 1 * (direction[1] >= 0) + -1 * (direction[1] < 0)
    return [(up, 0), (up, right), (0, right)]


def inBoundaries(point, matrix):
    return point[0] == 0 or point[0] == matrix.shape[0] or point[1] == 0 or point[1] == matrix.shape[1]


def getZeroNeighbours(point, direction, matrix):
    r = point[0]
    c = point[1]
    m, n = matrix.shape

    coords = []
    for i, j in getDirectionArray(direction):
        if 0 <= r + i < m and 0 <= c + j < n:
            if matrix[r + i, c + j] == 0:
                coords.append((r + i, c + j))
    return coords


def generateSeedMatrix(frame_size):
    neuron = (np.random.randint(frame_size / 4, 3 * frame_size / 4), np.random.randint(frame_size / 4, 3 * frame_size / 4))
    generator_matrix = np.zeros((frame_size, frame_size))
    generator_matrix[neuron] = 1

    r, c = np.where(generator_matrix)
    r = r[0]
    c = c[0]
    m, n = generator_matrix.shape

    coords = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= r + i < m and 0 <= c + j < n:
                if generator_matrix[r + i, c + j] == 0:
                    coords.append((r + i, c + j))

    n_tails = random(4, len(coords))
    for sampl in sample(coords, n_tails):
        generator_matrix[sampl] = 2

    for step in range(2, int(frame_size / math.sqrt(2))):
        r, c = np.where(generator_matrix == step)
        m, n = generator_matrix.shape
        points = []

        for point in zip(r, c):
            direction = (point[0] - neuron[0], point[1] - neuron[1])
            zeroNeighbours = getZeroNeighbours(point, direction, generator_matrix)
            if len(zeroNeighbours) > 0:
                sam = choice(zeroNeighbours)
                generator_matrix[sam] = step + 1

    return generator_matrix


def generateVideo(n_frames, frame_size):
    video = []
    video_size = (n_frames, frame_size, frame_size)

    video = np.random.randint(8, size=video_size)
    neuron_frame = np.random.randint(n_frames - int(frame_size / math.sqrt(2)))
    generator_matrix = generateSeedMatrix(frame_size)
    final_video = []
    for i, frame in enumerate(video):
        points = 1 * (generator_matrix != 0) * 9 * (generator_matrix == (i - neuron_frame) + 1)
        final = frame + points
        final_video.append(np.where(final > 10, 10, final))

    return final_video


#
sizes = [(5, 600), (7, 600), (20, 600), (150, 600), (500, 600)]

for i, size in enumerate(tqdm(sizes)):
    out = open('input%i.txt' % i, 'w+')
    out.write('%i %i %i \n' % (size[0], size[0], size[1]))
    for frame in tqdm(generateVideo(size[1], size[0])):
        for row in frame:
            out.write(' '.join([str(r) for r in row]) + '\n')
    out.close()

print('Done')
