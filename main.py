#!/usr/bin/env python
import argparse
from time import sleep
from pprint import pprint
import os.path
from util import print_log
from leads_dup import LeadsDups

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Let's do a Challenge!!!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    reg_grp = parser.add_argument_group()
    reg_grp.add_argument("-c", "--changes", action="store_true", 
                        default=False,
                        help="Changes: from/to")
    reg_grp.add_argument("--cli", action=argparse.BooleanOptionalAction,
                       default=False)
    reg_grp.add_argument("-u", "--username", nargs="+",
                           help="Set current ", default ="Sudha")

    mode_opts = reg_grp.add_mutually_exclusive_group(required=False)
    mode_opts.add_argument("-x", "--all",  action="store_true", 
                        default=False, help= "all the Records")
    mode_opts.add_argument("-a", "--apps", nargs="+",
                           help="App mode: No duplicates")
    mode_opts.add_argument("-l", "--list", action="store_true", default=False,
                           help="List mode: show records")
    mode_opts.add_argument("-s", "--status", action="store_true", default=False,
                           help="Status mode: show current status of apps")

    parser.add_argument("--dry-run",
                       action=argparse.BooleanOptionalAction,
                       default=False)

    args = parser.parse_args()
    print_log("\n---- args ----", output=True)
    pprint(args)
    if args.apps or args.list:
        ## TODO
        #if not validate_args(args.apps):
        exit(0)

    if not os.path.exists("leads.json"):
        print_log("ALERT : leads.json not found..Exiting the application")
        exit(0)
            
    try:
        if args.cli:
            output = True  
        else: 
            output = False  
        
        print_log("Results of the application", output)

        if args.changes:
            if args.dry_run:
                print_log(f"[DRY_RUN]  Changes to check {args.changes}", output)
            else:
                print_log(f"changes set to:  {args.changes}", output)
            ld = LeadsDups()
            ld.changes()

        if args.apps:
            if args.dry_run:
                print_log(f"[DRY_RUN] Apps mode", output)
            else:
                print_log(f"[FULL_RUN] Apps mode", output)   

        if args.list:
            if args.dry_run:
                print_log(f"[DRY_RUN] list mode", output)
            else:
                print_log(f"[FULL RUN] list mode")

        if args.status:
            if args.dry_run:
                print_log(f"[DRY_RUN] status of app {args.apps}", output)
            else:
                print_log(f"[FULL RUN] Status", output)

            if args.all:
                if args.dry_run:
                    print_log(f"[DRY_RUN] ", output)
                else:
                    print_log(f"[FULL RUN] all mode", output)
    except Exception as err:
        print_log(f"Unexpected {err=}, {type(err)=}", output)


