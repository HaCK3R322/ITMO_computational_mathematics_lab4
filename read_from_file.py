def read(file_path):
    with open(file_path, 'r') as file:
        line = file.readline()
        number_of_points = int(line)
        matrix = [[0, 0] for y in range(number_of_points)]
        if number_of_points == 0:
            return

        for i in range(number_of_points):
            line = file.readline()
            matrix[i][0] = float(line.split()[0])
            matrix[i][1] = float(line.split()[1])

        xarr = []
        yarr = []
        for i in range(number_of_points):
            xarr.append(matrix[i][0])
            yarr.append(matrix[i][1])

        return {'xarr': xarr, 'yarr': yarr}