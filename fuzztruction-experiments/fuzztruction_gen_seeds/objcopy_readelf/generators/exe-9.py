import threading
import time

def thread_init_data():
    """
    Function to simulate thread-specific data initialization.
    This function acts as a placeholder for what would be the TLS callback
    in a lower-level implementation.
    """
    thread_name = threading.current_thread().name
    print(f"[{thread_name}] Initializing thread-specific data...")
    # Simulate some initialization delay
    time.sleep(1)
    print(f"[{thread_name}] Thread-specific data initialized.")

def worker():
    """
    Worker function for the thread, calls the initialization.
    """
    thread_init_data()
    # Your thread's main functionality would go here
    print(f"[{threading.current_thread().name}] Doing some work...")

def main():
    """
    Main function to start threads.
    """
    print("Main: Starting threads...")
    threads = [threading.Thread(target=worker, name=f"Worker-{i}") for i in range(2)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Main: All threads have finished execution.")

if __name__ == "__main__":
    main()

# To compile this script into an executable using PyInstaller, run the following command in your terminal:
# pyinstaller --onefile tls_callback_example.py --distpath ./tmp/