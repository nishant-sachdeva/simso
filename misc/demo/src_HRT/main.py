from simulator import simulate_run
from task_set_generator import generateTaskSet
from plotting import plotAndPrintComparisons

def start_simulation():
    numberOfRuns = 1000
    schedulers = ['GRMS', 'FIRST_FIT']
    processorUtilizations = []
    for scheduler in schedulers:
        processorUtilizationForCurrentScheduler = []
        for i in range(numberOfRuns):
            task_set = generateTaskSet()
            processorUtilization = simulate_run(scheduler, task_set)
            processorUtilizationForCurrentScheduler.append(processorUtilization)
        processorUtilizations[scheduler] = processorUtilizationForCurrentScheduler
    return processorUtilizations

if __name__ == '__main__':
    # 1000 task runs
    # generate Task set for each run
    # send for running GRMS :: Admission control :: Execution :: Processor Utilization :: Collect Average over 1000 runs
    # Send for runnign FF-RB :: Admission Control :: Execution :: Processor Utilization :: Collect Average over 1000 runs
    # Plot relevant graphs
    # Print out average processor utilization
    processorUtilizations = start_simulation()
    plotAndPrintComparisons(processorUtilizations)

