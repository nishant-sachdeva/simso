#!/usr/bin/python3

"""
Example of a script that uses SimSo.
"""

import re
import random
import sys
from simso.core import Model
from simso.configuration import Configuration
import simso.generator.task_generator as task_generator


schedulers = [
"simso.schedulers.RM",
"simso.schedulers.LB_P_EDF",
"simso.schedulers.P_EDF2",
"simso.schedulers.EDHS",
"simso.schedulers.P_EDF",
]

        # configuration.add_task(name="T1", identifier=1, period=7,activation_date=0, wcet=3, deadline=7)
        # configuration.add_task(name="T2", identifier=2, period=12,activation_date=0, wcet=3, deadline=12)
        # configuration.add_task(name="T3", identifier=3, period=20,activation_date=0, wcet=5, deadline=20)
        # configuration.add_task(name="T4", identifier=4, period=20,activation_date=0, wcet=3, deadline=20)
        # configuration.add_task(name="T5", identifier=5, period=20,activation_date=0, wcet=1, deadline=20)
        # configuration.add_task(name="T6", identifier=6, period=20,activation_date=0, wcet=6, deadline=20)
        # configuration.add_task(name="T7", identifier=7, period=20,activation_date=0, wcet=3, deadline=20)
        # configuration.add_task(name="T8", identifier=8, period=20,activation_date=0, wcet=1, deadline=20)
        # configuration.add_task(name="T9", identifier=9, period=20,activation_date=0, wcet=2, deadline=20)
        # configuration.add_task(name="T10", identifier=10, period=20,activation_date=0, wcet=4, deadline=20)

def generateTaskSet(numberOfTaskSets):
    # choice here is between the inbuit schedulers and manual figures
    numberOfTasks = int(random.uniform(1,10)*10)
    maximumUtilization = random.uniform(0.5,1)
    taskSet = task_generator.StaffordRandFixedSum(numberOfTasks, maximumUtilization, numberOfTaskSets)

    # - `min_`: Period min.
    # - `max_`: Period max.
    T_min = 20
    T_max = 50
    periods = task_generator.gen_periods_uniform(numberOfTasks, numberOfTaskSets, T_min, T_max , round_to_int=False)

    taskSet = task_generator.gen_tasksets(taskSet, periods)
    return taskSet


def main(argv):
    # Manual configuration:
    processorUtilizations = {}
    averageProcessorUtilizations = {}
    numberOfTaskSets = int(input("How many Sets do you wish to run > "))
    
    taskSet = generateTaskSet(numberOfTaskSets)
    
    for taskSetNum, exp_set in enumerate(taskSet):
        print(taskSetNum)
        for scheduler in schedulers:
            configuration = Configuration()
            configuration.duration = 100 * configuration.cycles_per_ms
            
            for order, (wcet, per) in enumerate(exp_set):
                configuration.add_task(
                    name="task " + str(order),
                    identifier= order,
                    period = per,
                    activation_date=0,
                    wcet=wcet,
                    deadline = per,
                    abort_on_miss = True
                )

            
            minProcSoFar = 0
            configuration.scheduler_info.clas = scheduler
            configuration.add_processor(name="CPU 1", identifier=1)

            for numberOfProc in range(2, 30):
                procName = "CPU " + str(numberOfProc)            
                configuration.add_processor(name=procName, identifier=numberOfProc)

                # print(scheduler , numberOfProc)
                # Check the config before trying to run it.
                canExit = True
                configuration.check_all()

                try:

                    # Init a model from the configuration.
                    model = Model(configuration)

                    # Execute the simulation.
                    model.run_model()

                    if model.logs is not None:
                        for log in model.logs:
                            if re.search("Preempted", str(log)) is not None:
                                # print("Job has not happened" , numberOfProc)
                                canExit = False
                                break

                except Exception as e:
                    # print(e)
                    # print("Could not run with given configuration")
                    # print(minProcSoFar)
                    canExit = False
                    
                if canExit:
                    break
                minProcSoFar = numberOfProc
                

            if minProcSoFar is not 0:
                processorUtilizations[scheduler] = 1/minProcSoFar
                if scheduler not in averageProcessorUtilizations:
                    averageProcessorUtilizations[scheduler] = processorUtilizations[scheduler]
                else:
                    averageProcessorUtilizations[scheduler] += processorUtilizations[scheduler]


        for proc in processorUtilizations:
            print(proc, processorUtilizations[proc])

    print("\n\nFinal Averages \n")
    for proc in averageProcessorUtilizations:
        print(proc, averageProcessorUtilizations[proc]/numberOfTaskSets)
main(sys.argv)
