import subprocess

class Cliclick:
    def __init__(self, executable="cliclick"):
        self.executable = executable

    def run_command(self, *args):
        """Run a cliclick command with given arguments."""
        command = [self.executable] + list(args)
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr.strip()}")
            raise

    def move(self, coordinates):
        """Move the mouse to the given [x, y] coordinates."""
        x, y = coordinates
        return self.run_command(f"m:{x},{y}")

    def click(self, coordinates):
        """Click at the given [x, y] coordinates."""
        x, y = coordinates
        return self.run_command(f"c:{x},{y}")
