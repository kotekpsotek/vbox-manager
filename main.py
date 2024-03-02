import time
from os import getenv
import virtualbox
import dotenv

# Load envs
dotenv.load_dotenv()

# Create VMBox instance
vbox = virtualbox.VirtualBox()

# Create Instance of Session
session = virtualbox.Session()

# Find specific machine
machine_name = ""
machine = vbox.find_machine(machine_name)

# For virtualbox API 6_1 and above (VirtualBox 6.1.2+), use the following:
progress = machine.launch_vm_process(session, "gui", [])
progress.wait_for_completion()

time.sleep(35)
