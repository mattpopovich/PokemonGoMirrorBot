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
        print(f"Clicking at {coordinates}")
        return self.run_command(f"c:{x},{y}")

    def double_click(self, coordinates):
        """Double-click at the given [x, y] coordinates."""
        x, y = coordinates
        print(f"Double-clicking at {coordinates}")
        return self.run_command(f"dc:{x},{y}")

    def start_drag(self, coordinates):
        """Start a drag at the given [x, y] coordinates."""
        x, y = coordinates
        # print(f"Starting drag at {coordinates}")
        return self.run_command(f"dd:{x},{y}")

    def continue_drag(self, coordinates):
        """Continue a drag to the given [x,y] coordinates."""
        x, y = coordinates
        # print(f"Continuing drag to {coordinates}")
        return self.run_command(f"dm:{x},{y}")

    def release_drag(self, coordinates):
        """Release a drag at the given [x,y] coordinates."""
        x, y = coordinates
        # print(f"Releasing drag at {coordinates}")
        return self.run_command(f"du:{x},{y}")

    # This sends a screenshot notification to pokemon go
    # def get_color(self, coordinates):
    #     """Get the color of the pixel at the given [x,y] coordinates."""
    #     x, y = coordinates
    #     return self.run_command(f"cp:{x},{y}")
