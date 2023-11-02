import os
def check_reboot():
    return os.path.exists("/run/reboot-required")
print(check_reboot())