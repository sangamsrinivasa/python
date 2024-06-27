import os
import subprocess

def create_user(username, password):
    subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash", username])
    subprocess.run(["echo", f"{username}:{password}", "|", "sudo", "chpasswd"])
    print(f"User {username} created.")


if __name__ == "__main__":
    create_user("new_user", "password123")

