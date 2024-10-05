import argparse

print("""
 ██████╗ ██╗███╗   ███╗██████╗ ██╗     ███████╗███████╗
██╔════╝ ██║████╗ ████║██╔══██╗██║     ██╔════╝██╔════╝
██║  ███╗██║██╔████╔██║██████╔╝██║     █████╗  █████╗  
██║   ██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══╝  
╚██████╔╝██║██║ ╚═╝ ██║██║     ███████╗███████╗███████╗
 ╚═════╝ ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚══════╝
                   Made by Anton Hrlić                                    
""")

parser = argparse.ArgumentParser(description="A simple program that prints help when -h is used.")
args = parser.parse_args()
print("Run the script with -h to display the help message.")
print("I will dig your mama")
