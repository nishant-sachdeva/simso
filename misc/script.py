#!/usr/bin/python3

"""
Example of a script that uses SimSo.
"""

import re

import sys
from simso.core import Model
from simso.configuration import Configuration

schedulers = [
"simso.schedulers.RM",
"simso.schedulers.LB_P_EDF",
"simso.schedulers.P_EDF2",
"simso.schedulers.EDHS",
"simso.schedulers.P_EDF",
]
def main(argv):
    if len(argv) == 2:
        # Configuration load from a file.
        configuration = Configuration(argv[1])
    else:
        # Manual configuration:
        configuration = Configuration()

        configuration.duration = 420 * configuration.cycles_per_ms

        # Add tasks:
        n = 12
        for i in range(n):
            taskName = "T" + str(i)
            configuration.add_task(name=taskName, identifier=i, period=20,activation_date=0, wcet=3, deadline=20)


        # Add a processor:
        configuration.add_processor(name="CPU 1", identifier=1)
        configuration.add_processor(name="CPU 2", identifier=2)
        configuration.add_processor(name="CPU 3", identifier=3)
        # configuration.add_processor(name="CPU 4", identifier=4)
        # configuration.add_processor(name="CPU 5", identifier=5)
        # configuration.add_processor(name="CPU 6", identifier=6)
        # configuration.add_processor(name="CPU 7", identifier=7)
        # Add a scheduler:

        # configuration.scheduler_info.filename = "../simso/schedulers/RM.py"
        configuration.scheduler_info.clas = "simso.schedulers.RM"
        

    # Check the config before trying to run it.
    configuration.check_all()

    # Init a model from the configuration.
    model = Model(configuration)

    # Execute the simulation.
    model.run_model()

    # Print logs.
    for log in model.logs:
        print(log)

main(sys.argv)
