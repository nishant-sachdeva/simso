import sys
from simso.core import Model
from simso.configuration import Configuration


def simulate_run(scheduler, taskSet):
    # print(taskSet)
    schedulerDict = {'GRMS':'simso.schedulers.P_RM', 'FIRST_FIT':'simso.schedulers.P_EDF_WF'}

    configuration = Configuration()
    configuration.duration = 1000 * configuration.cycles_per_ms
    
    # Add a processor:
    numberOfProcessors = 1
    for i in range(numberOfProcessors):
        processorName = "CPU " + str(i)
        configuration.add_processor(name=processorName, identifier=i)
    
    # Add tasks:
    for i, exp_set in enumerate(taskSet):
        while configuration.task_info_list:
            del configuration.task_info_list[0]
        
        for order, (wcet, period) in enumerate(exp_set):
            configuration.add_task(
                name="task",
                identifier=order,
                period = period,
                activation_date=0,
                wcet=wcet,
                deadline = period,
                abort_on_miss = True
            )
    
    # Add a scheduler:
    # configuration.scheduler_info.filename = "../simso/schedulers/RM.py"
    # configuration.scheduler_info.clas = schedulerDict[scheduler]
    configuration.scheduler_info.clas = "simso.schedulers.P_RM"

    # Check the config before trying to run it.
    configuration.check_all()

    # Init a model from the configuration.
    model = Model(configuration)

    # Execute the simulation.
    model.run_model()
    abortedJobs = sum(model.results.tasks[task].exceeded_count for task in model.task_list)
    return abortedJobs