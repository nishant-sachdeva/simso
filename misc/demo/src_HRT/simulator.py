import sys
from simso.core import Model
from simso.configuration import Configuration

schedulerDict = {
    "GRMS" : "simso.schedulers.RM",
    "FIRST_FIT" : 
}


def simulate_run(scheduler, taskSet):
    # Manual configuration:
    configuration = Configuration()

    configuration.duration = 420 * configuration.cycles_per_ms

    # Add tasks:
    configuration.add_task(name="T1", identifier=1, period=7,
                            activation_date=0, wcet=3, deadline=7)
    configuration.add_task(name="T2", identifier=2, period=12,
                            activation_date=0, wcet=3, deadline=12)
    configuration.add_task(name="T3", identifier=3, period=20,
                            activation_date=0, wcet=5, deadline=20)

    # Add a processor:
    configuration.add_processor(name="CPU 1", identifier=1)

    # Add a scheduler:
    #configuration.scheduler_info.filename = "../simso/schedulers/RM.py"
    configuration.scheduler_info.clas = 

    # Check the config before trying to run it.
    configuration.check_all()

    # Init a model from the configuration.
    model = Model(configuration)

    # Execute the simulation.
    model.run_model()

    # Print logs.
    for log in model.logs:
        print(log)
