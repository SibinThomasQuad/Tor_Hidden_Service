import os
import stem.process

def start_tor():
    tor_process = stem.process.launch_tor_with_config(
        config={
            'SocksPort': '9050',
            'HiddenServiceDir': '/tmp/hidden_service',
            'HiddenServicePort': '80 127.0.0.1:80'
        },
        take_ownership=True
    )
    return tor_process

def get_onion_address():
    with open('/tmp/hidden_service/hostname', 'r') as f:
        return f.read().strip()

if __name__ == '__main__':
    tor_process = start_tor()
    onion_address = get_onion_address()
    print(f"Your Tor hidden service is available at: http://{onion_address}")
    try:
        input("Press Enter to stop Tor...\n")
    except KeyboardInterrupt:
        pass
    finally:
        print("Shutting down...")
        tor_process.kill()
