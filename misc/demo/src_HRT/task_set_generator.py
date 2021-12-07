import simso.generator.task_generator as task_generator

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