#!/usr/bin/env python
# ex: set shiftwidth=4 tabstop=4 expandtab:
import subprocess


def get_temp():
    """ Function to get the Raspberry Pi's CPU temperature """
    cmd = '/opt/vc/bin/vcgencmd measure_temp'
    try:
        output = run_cmd(cmd)
        cel = output.split("'")[0]
        flt_cel = float(cel)
        temp = ((flt_cel * 9) / 5) + 32
    except:
        temp = 'Could not determine CPU temperature'

    return temp


def run_cmd(cmd):
	return subprocess.check_output(cmd.split()).strip().split('=')[1]


def main():
    print(get_temp())


if __name__ == '__main__':
	main()
