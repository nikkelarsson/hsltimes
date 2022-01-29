"""Download public transport timetables."""

__program__: str = "freshtables"

import os
import pathlib
import requests
import subprocess
import sys

import dbugging


class Timetables:
    """Represents a downloader that fetches the transport timetables."""

    def __init__(self) -> None:
        """Initializes Timetables class."""
        self.url: str = "https://infopalvelut.storage.hsldev.com/gtfs/hsl.zip"
        self.home: str = str(pathlib.Path.home())
        self.suffix: str = "/.local/share/hsltimes"
        self.location: str = "".join([self.home, self.suffix])
        os.makedirs(self.location, exist_ok=True)

    @dbugging.verbose("Downloading timetables...")
    def download(self, chunk_size: int=128) -> None:
        """
        Downloads the transport timetable zip file.

        Parameters:
            save.......... Where to save the timetables zip file.
            chunk_size.... Chunk size to write per iteration.
        """
        response: object = requests.get(self.url, stream=True)
        filename: str = "".join([self.location, "/timetables.zip"])
        with open(filename, "wb") as fd:
            for chunk in response.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    @dbugging.verbose(f"Extracting timetables...")
    def unzip(self) -> None:
        """Unzips the downloaded transport timetables zip -file."""
        src: str = "".join([self.location, "/timetables.zip"])
        dst: str = "".join([self.location, "/timetables"])
        subprocess.run(["unzip", src, "-d", dst])

    @dbugging.verbose("Cleaning up...")
    def clean(self) -> None:
        """Removes the zip file after it's not needed anymore."""
        os.remove("".join([self.location, "/timetables.zip"]))


def main(argc: int=len(sys.argv), argv: list=sys.argv) -> None:
    """Main function."""

    if argc > 1:
        sys.exit(f"{__program__} doesn't accept any command line arguments")

    timetables: object = Timetables()

    # Download timetables
    timetables.download()

    # Unzip timetables
    timetables.unzip()

    # Remove timetables.zip
    timetables.clean()


if __name__ == "__main__":
    main()
