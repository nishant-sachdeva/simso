import simso.generator.task_generator as task_generator

'''
Following are the requirements for this task generator

1. GRMS - OPT :: No task should fail a deadline in the time range LCM(Ti) + max(Ti) seconds
2. GRMS - A :: Only select tasks that satisfy the bound given in the paper
3. FF-RB :: Take any generic first fit algorithm. // 
    The issue here is that we don't know what bound is being used for this algo//
    So performance comparisons seem to be unfair

'''



def generateTaskSet(numberOfTaskSets):
    # choice here is between the inbuit schedulers and manual figures
    numberOfTasks = 10
    maximumUtilization = 10
    taskSet = task_generator.StaffordRandFixedSum(numberOfTasks, maximumUtilization, numberOfTaskSets)

    # - `min_`: Period min.
    # - `max_`: Period max.
    T_min = 1
    T_max = 10
    periods = task_generator.gen_periods_uniform(numberOfTasks, numberOfTaskSets, T_min, T_max , round_to_int=True)

    taskSet = task_generator.gen_tasksets(taskSet, periods)
    return taskSet