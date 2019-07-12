# lyrics
A Python application for analyzing music lyrics and repetitions. The project idea is to obtain the Brazil's radios top 100 songs lyrics and analyze them for repetitions. It might include analysis by genre as well.

This application was conveived as the final task for (CMP264/INF01071) Data Visualization course at UFRGS. 
It was heavily inspired in Colin Morris' work, which can be found at https://youtu.be/_tjFwcmHy5M.

## Environment
To install the needed modules, you might need the Pip3 package manager. If you don't have it yet, I suggest you install it using the following command:

    $ sudo apt-get install python3-pip

You can use other package managers, but it's not guaranteed they'll have the `vagalume` module, needed to get the lyrics.
The needed libraries are `numpy`, `matplotlib` and `vagalume`, which can be installed using:

    $ pip3 install numpy matplotlib vagalume colorama

If you already have one or more of these modules, you can just ignore the respective ones.

## Usage
Create an `<name>.txt` file with the `name` you want. 
Then, fill it up with songs in the following format:

`<artist name> -> <song name>`

To run the script, just execute the `lyrics` bash file:

    $ ./lyrics <name>

The results will be saved in a directory called `<name>_dir`, depending on the `name` you chose.
You can remove all results running the `./clean` script.

## API References & links
The Vagalume API reference can be found at https://api.vagalume.com.br/docs/

The Vagalume Python API reference can be found at https://github.com/diegoteixeir4/python-vagalume
