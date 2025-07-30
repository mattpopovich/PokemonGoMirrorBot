import subprocess

from functions.utils import randomize_location


class Cliclick:
    def __init__(self, executable="cliclick"):
        self.executable = executable

    def run_command(self, *args):
        """Run a cliclick command with given arguments."""
        command = [self.executable] + list(args)
        try:
            result = subprocess.run(
                command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr.strip()}")
            raise

    def move(self, coordinates: list[int]):
        """Move the mouse to the given [x, y] coordinates."""
        x, y = coordinates
        return self.run_command(f"m:{x},{y}")

    def click(self, coordinates: list[int]):
        """Click at the given [x, y] coordinates."""
        x, y = coordinates
        # print(f"Clicking at {coordinates}")
        return self.run_command(f"c:{x},{y}")

    def random_click(self, coordinates: list[int], pixel_randomness: int):
        """Click at the given [x,y] coordinates within a specified pixel_randomness range"""
        return self.click(randomize_location(coordinates, pixel_randomness))

    def double_click(self, coordinates: list[int]):
        """Double-click at the given [x, y] coordinates."""
        x, y = coordinates
        # print(f"Double-clicking at {coordinates}")
        return self.run_command(f"dc:{x},{y}")

    def start_drag(self, coordinates: list[int]):
        """Start a drag at the given [x, y] coordinates."""
        x, y = coordinates
        # print(f"Starting drag at {coordinates}")
        return self.run_command(f"dd:{x},{y}")

    def continue_drag(self, coordinates: list[int]):
        """Continue a drag to the given [x,y] coordinates."""
        x, y = coordinates
        # print(f"Continuing drag to {coordinates}")
        return self.run_command(f"dm:{x},{y}")

    def release_drag(self, coordinates: list[int]):
        """Release a drag at the given [x,y] coordinates."""
        x, y = coordinates
        # print(f"Releasing drag at {coordinates}")
        return self.run_command(f"du:{x},{y}")

    # This sends a screenshot notification to pokemon go
    # def get_color(self, coordinates):
    #     """Get the color of the pixel at the given [x,y] coordinates."""
    #     x, y = coordinates
    #     return self.run_command(f"cp:{x},{y}")
