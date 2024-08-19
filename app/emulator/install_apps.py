import subprocess


apk_files = [
    'C:\Python Projects\Alpha-Finance-Tracker\Finance-Tracker-Service\kaufland.apk',
    'C:\Python Projects\Alpha-Finance-Tracker\Finance-Tracker-Service\lidl.apk'
]
import subprocess
import time
import os



avd_name = 'emulator-5554'
emulator_path = 'C:\\Users\\user\\AppData\\Local\\Android\\Sdk\\emulator\\emulator.exe'
#
# def start_emulator(avd_name):
#     try:
#         # Start the emulator
#         subprocess.Popen([emulator_path, '-avd', avd_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         print(f"Starting emulator: {avd_name}")
#         # Give the emulator some time to start up
#         time.sleep(90)  # Adjust time if needed
#     except Exception as e:
#         print(f"Exception occurred while starting emulator: {e}")

def install_apk(apk_path):
    try:
        # Run adb install command
        result = subprocess.run(['adb', 'install', apk_path], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully installed: {apk_path}")
        else:
            print(f"Failed to install: {apk_path}")
            print("Error:", result.stderr)
    except Exception as e:
        print(f"Exception occurred while installing {apk_path}: {e}")

def main():
    # Start the emulator
    # start_emulator(avd_name)

    # Check if adb is running and devices are connected
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    if 'device' not in result.stdout:
        print("No devices or emulators found. Please ensure your emulator or device is running.")
        return

    # Install each APK
    for apk in apk_files:
        if os.path.exists(apk):
            install_apk(apk)
        else:
            print(f"APK file does not exist: {apk}")

main()