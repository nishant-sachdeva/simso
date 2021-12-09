from simulator import simulate_run
from task_set_generator import generateTaskSet
from plotting import plotAndPrintComparisons

def startSimulation():
    numberOfTaskSets = 1000
    schedulers = ['GRMS', 'FIRST_FIT']
    processorUtilizations = []
    for scheduler in schedulers:
        processorUtilizationForCurrentScheduler = []

        task_set = generateTaskSet(numberOfTaskSets)
        processorUtilization = simulate_run(scheduler, task_set)
        processorUtilizationForCurrentScheduler.append(processorUtilization)
        processorUtilizations[scheduler] = processorUtilizationForCurrentScheduler

    return processorUtilizations

if __name__ == '__main__':
    processorUtilizations = startSimulation()
    for item in processorUtilizations:
        print(item)
    plotAndPrintComparisons(processorUtilizations)

