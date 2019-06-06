# lyrics
A Python application for analyzing music lyrics and repetitions. The project idea is to obtain the Brazil's radios top 100 songs lyrics and analyze them for repetitions. It might include analysis by genre as well.

This application was conveived as the final task for (CMP264/INF01071) Data Visualization course at UFRGS. 
It was heavily inspired in Colin Morris' work, which can be found at https://youtu.be/_tjFwcmHy5M.

## Environment
Install the `vagalume` lib using:

    $ pip3 install vagalume

For the graphics, you'll might also need the `matplotlib`, which can be obtained via:

    $ pip3 install matplotlib

## Usage
Put the desired songs in the `songs.txt` file respecting the following format:

`<artist name> -> <song name>`

And don't forget to leave a blank line at the end of the file!

The code can be executed with the following steps:

    $ ./lyrics

To clean the results, simply do:

    $ ./clean

## API References & links
The Vagalume API reference can be found at https://api.vagalume.com.br/docs/

The Python API usage can be found at https://github.com/diegoteixeir4/python-vagalume
