import os, time

def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

def loading_animation():
    animation = "|/-\\"
    total_iteration = 50
    i = 0
    while i < total_iteration:
        progress = "█" * (i % total_iteration) + "-" * (total_iteration - (i % total_iteration))
        print(f"Loading [{progress}] {animation[i % len(animation)]}", end="\r")
        i += 1
        time.sleep(0.1)