#!/usr/bin/env python3

"""A simple python script template.
"""

import os
import sys
import argparse
import json

# From https://unix.stackexchange.com/a/343974
CROSS = '\u274c'
TICK = '\u2714'

def main(arguments):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))

    args = parser.parse_args(arguments)

    analysis = json.load(args.infile)

    # Whether the app is vulnerable
    is_vulnerable = False

    # check Wordpress version
    print(f"[+] Wordpress version ({analysis['version']['number']}): ", end="")
    if analysis["version"]["status"] == "insecure":
        is_vulnerable = True
        print(f"Insecure {CROSS}")
    else:
        print(f"Secure {TICK}")

    # Check if this version has vulnerabilities
    nb_vulnerabilities = len(analysis["version"]["vulnerabilities"])
    print(f"[+] Wordpress vulnerabilities detected: {nb_vulnerabilities} ", end="")
    if nb_vulnerabilities == 0:
        print(f"{TICK}")
    else:
        print(f"{CROSS}")
        is_vulnerable = True
    
    for vulnerability in analysis["version"]["vulnerabilities"]:
        print(f"   - {vulnerability['title']}")

    # Check if the installation has vulnerable plugins
    vulnerable_plugins = [plugin for plugin in analysis["plugins"].values() if len(plugin["vulnerabilities"]) != 0]
    print(f"[+] Vulnerable plugins detected: {len(vulnerable_plugins)} ", end="")
    if len(vulnerable_plugins) == 0:
        print(f"{TICK}")
    else:
        print(f"{CROSS}")
        is_vulnerable = True
    
    for plugin in vulnerable_plugins:
        print(f"   - {plugin['slug']}")

    # Check the theme
    if analysis["main_theme"] != None:
        print(f"[+] Vulnerable template detected: ", end="")
        if len(analysis["main_theme"]["vulnerabilities"]) == 0:
            print(f"{TICK}")
        else:
            print(f"{CROSS}")
            is_vulnerable = True

    return 1 if is_vulnerable else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))