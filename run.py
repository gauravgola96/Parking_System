import os, sys
import logging
import argparse
from helper import Helper
from parking_system.exceptions import InvalidParams
from parking_system.main import RunParkingSystem

logger = logging.getLogger(__name__)


class CommandExecutor:
    def __init__(self):
        self.command = RunParkingSystem()

    def run_single_command(self, cmd):
        """Run with single command"""
        inputs = cmd.split()
        command = inputs[0]
        input_param = inputs[1:]
        input_values = Helper.fetch_input_values(command, input_param)
        if not input_values:
            logger.debug("Something wrong with input")
            return
        required_param_name = Helper.fetch_required_param_name(cmd=command)
        self.command.run(command=command, **dict(zip(required_param_name, input_values)))

    def run_from_file(self, file):
        """Run with filepath"""
        if not os.path.exists(file):
            logger.debug(f"File {file} doesn't exist")
            return None
        file_obj = open(file)
        try:
            while True:
                line = next(file_obj)
                if line.endswith('\n'):
                    line = line[:-1]
                if line == '':
                    continue
                self.run_single_command(line)
        except StopIteration:
            file_obj.close()
        except Exception as e:
            logger.debug(f"Exception occured : {e}")

    def run_interactive(self):
        """Run in interactive mode in terminal"""
        try:
            while True:
                std_in = input("Enter command for Parking system: \n")
                self.run_single_command(std_in)
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            logger.debug(f"Something undefined occur while STD_IN \n Traceback: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run parking lot system algorithm either with file or \
                                                                                            interactive mode')
    parser.add_argument('--filepath', metavar='path', help='Enter input filepath', required=False)
    parser.add_argument('--interactive', default=False, action='store_true', help='Interactive mode in terminal',
                        required=False)
    args = parser.parse_args()
    command_executor = CommandExecutor()

    if args.filepath and args.interactive:
        error_msg = f'Cannot take params interactive mode and open {args.filepath} together'
        raise InvalidParams(error_msg)

    if args.interactive:
        command_executor.run_interactive()

    if args.filepath:
        command_executor.run_from_file(args.filepath)
    else:
        logger.debug("filepath in null")
