from slmigrate import constants
import subprocess


def stop_sl_service(service):
    if service.require_service_restart:
        print("Stopping " + service.service_to_restart + " service")
        subprocess.run(constants.slconf_cmd_stop_service + service.service_to_restart + " wait")
        subprocess.run(constants.slconf_cmd_stop_all)


def stop_all_sl_services():
    print("Stopping all SystemLink services...")
    subprocess.run(constants.slconf_cmd_stop_all)


def start_all_sl_services():
    print("Starting all SystemLink services")
    subprocess.run(constants.slconf_cmd_start_all)
