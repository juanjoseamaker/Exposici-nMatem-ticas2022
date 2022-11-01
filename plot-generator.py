import csv
import matplotlib.pyplot as plt
import numpy as np

SUBJECTS = ("español", "matemáticas", "sociales", "naturales", "ingles")
AVERAGES_M = []
AVERAGES_E = []


def read_data():
    with open('promedios-jornada-mañana.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            AVERAGES_M.append(row)
    with open('promedios-jornada-tarde.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            AVERAGES_E.append(row)

    AVERAGES_M.reverse()  # debe estar en orden cronológico
    AVERAGES_E.reverse()


def generate_plots_for_each_subject_averages_m():
    for s in range(5):
        year = 2011
        xpoints = []
        ypoints = []

        for y in range(len(AVERAGES_M)):
            xpoints.append(year)
            ypoints.append(float(AVERAGES_M[y][s]))
            year += 1

        plt.ylabel("Promedio jornada de la mañana en " + SUBJECTS[s])
        plt.xlabel("Año")
        plt.plot(np.array(xpoints), np.array(ypoints))
        plt.savefig('M_' + str(s) + '.png')
        plt.close()


def generate_plots_averages_m():
    year = 2011
    xpoints = []
    ypoints = []

    for y in range(len(AVERAGES_M)):
        average = 0
        for s in range(5):
            average += float(AVERAGES_M[y][s])
        average /= 5

        xpoints.append(year)
        ypoints.append(average)
        year += 1

    plt.ylabel("Promedio jornada de la mañana en total")
    plt.xlabel("Año")
    plt.plot(np.array(xpoints), np.array(ypoints))
    plt.savefig('M_T.png')
    plt.close()

    for s in range(5):
        year = 2011
        xpoints = []
        ypoints = []

        for y in range(len(AVERAGES_M)):
            xpoints.append(year)
            ypoints.append(float(AVERAGES_M[y][s]))
            year += 1

        plt.plot(np.array(xpoints), np.array(ypoints))

    plt.ylabel("Promedio jornada de la mañana")
    plt.xlabel("Año")
    plt.savefig('M.png')
    plt.close()

def generate_plots_for_each_subject_averages_e():
    for s in range(5):
        year = 2012
        xpoints = []
        ypoints = []

        for y in range(len(AVERAGES_E)):
            xpoints.append(year)
            ypoints.append(float(AVERAGES_E[y][s]))
            year += 1

        plt.ylabel("Promedio jornada de la tarde en " + SUBJECTS[s])
        plt.xlabel("Año")
        plt.plot(np.array(xpoints), np.array(ypoints))
        plt.savefig('T_' + str(s) + '.png')
        plt.close()


def generate_plots_averages_e():
    year = 2012
    xpoints = []
    ypoints = []

    for y in range(len(AVERAGES_E)):
        average = 0
        for s in range(5):
            average += float(AVERAGES_E[y][s])
        average /= 5

        xpoints.append(year)
        ypoints.append(average)
        year += 1

    plt.ylabel("Promedio jornada de la tarde en total")
    plt.xlabel("Año")
    plt.plot(np.array(xpoints), np.array(ypoints))
    plt.savefig('T_T.png')
    plt.close()

    for s in range(5):
        year = 2012
        xpoints = []
        ypoints = []

        for y in range(len(AVERAGES_E)):
            xpoints.append(year)
            ypoints.append(float(AVERAGES_E[y][s]))
            year += 1

        plt.plot(np.array(xpoints), np.array(ypoints))

    plt.ylabel("Promedio jornada de la tarde")
    plt.xlabel("Año")
    plt.savefig('T.png')
    plt.close()

def main():
    read_data()
    generate_plots_for_each_subject_averages_m()
    generate_plots_averages_m()
    generate_plots_for_each_subject_averages_e()
    generate_plots_averages_e()

if __name__ == '__main__':
    main()
