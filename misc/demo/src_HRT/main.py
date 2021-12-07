from simulator import simulate_run
from task_set_generator import generateTaskSet
from plotting import plotAndPrintComparisons

def start_simulation():
    numberOfTaskSets = 10
    schedulers = ['GRMS', 'FIRST_FIT']
    # processorUtilizations = []
    performanceTotal = []
    for scheduler in schedulers:
        # processorUtilizationForCurrentScheduler = []
        performanceCurrent = []

        task_set = generateTaskSet(numberOfTaskSets)
        abortedJobs = simulate_run(scheduler, task_set)
        performanceCurrent.append(abortedJobs)
        performanceTotal.append(performanceCurrent)
        # processorUtilization = simulate_run(scheduler, task_set)
        # processorUtilizationForCurrentScheduler.append(processorUtilization)
        # processorUtilizations[scheduler] = processorUtilizationForCurrentScheduler

    # return processorUtilizations
    return performanceTotal

if __name__ == '__main__':
    # 1000 task runs
    # generate Task set for each run
    # send for running GRMS :: Admission control :: Execution :: Processor Utilization :: Collect Average over 1000 runs
    # Send for runnign FF-RB :: Admission Control :: Execution :: Processor Utilization :: Collect Average over 1000 runs
    # Plot relevant graphs
    # Print out average processor utilization
    processorUtilizations = start_simulation()
    for item in processorUtilizations:
        print(item)
    # plotAndPrintComparisons(processorUtilizations)

