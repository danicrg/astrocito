import numpy as np
from tqdm import tqdm


def solveNeuron(input_file, output_file):
    input_f = open(input_file, 'r')

    sizes = input_f.readline().rsplit(' ')

    width = int(sizes[0])
    height = int(sizes[1])
    frames = int(sizes[2])

    video_size = (frames, width, height)
    video = []

    # Generate numpy matrixes

    print('Generating np matrix...')
    for frame in tqdm(range(frames)):
        matrix = []
        for _ in range(height):
            row = [int(i) for i in input_f.readline().rsplit(' ')]
            matrix.append(row)
        my_frame = np.matrix(matrix)
        video.append(my_frame)

    # Get max value

    threshold = 9

    # Get region
    region = np.zeros((width, height))
    for frame in video:
        region = 1 * (region > 0) + 1 * (frame >= threshold)
    out_f = open(output_file, 'w+')
    for row in region.tolist():
        out_f.write(' '.join([str(i) for i in row]) + '\n')
    out_f.close()


for i in range(5):
    input_file = 'input%i.txt' % i
    output_file = 'output%i.txt' % i
    solveNeuron(input_file, output_file)
    print('Input %s done!' % i)
