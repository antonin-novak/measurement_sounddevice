This is a simple Python script named `example_sounddevice_sine_wave.py` that generates a sinusoidal signal, sends it to the soundcard output, records the inputs, and plots them.  
  
## Prerequisites  
  
Ensure you have installed the following Python libraries:  
  
- numpy  
- matplotlib  
- sounddevice  
  
You can install the sounddevice from from PyPI:  
```sh  
python3 -m pip install sounddevice 
```
(for more details see [https://python-sounddevice.readthedocs.io/en/0.4.0/installation.html?highlight=asio#installation](https://python-sounddevice.readthedocs.io/en/0.4.0/installation.html?highlight=asio#installation)

## How to Use

To use this script, follow these steps:

1. Run the script using Python:

```sh
python example_sounddevice_sine_wave.py  
```

2. Upon running, the script will print a list of sound devices available on your system. This is done using 

```python
print(sd.query_devices()).
```

3. The script sets the sound device input and output using 
```python
sd.default.device = (1, 3)
```
Here, 1 is the input device number and 3 is the output device number. These device numbers should correspond to the numbers of your desired input and output devices from the printed list. Adjust these numbers according to your specific setup.

4. The script will then generate a sine signal with a frequency of 500 Hz and a duration of 2 seconds.

5. The script plays the generated sine signal and simultaneously records inputs from channels 1 and 2 of your sound device. The output is sent to output channel 1.
In the given script, the output is being sent to output channel 1 (output_mapping=(1)) and the inputs are being recorded from input channels 1 and 2 (input_mapping=(1, 2)).
To change these, simply replace the numbers in the parentheses with the numbers of the desired channels. For example, if you want to send the output to channel 2 and record from channels 3 and 4, you would modify the lines to be:
```python
output_mapping=(2),  # output channel 2  
input_mapping=(3, 4),  # input channels 3 and 4  
```

6. Lastly, the script plots the recorded signals from the input channels over time.


## Author
 
Antonin Novak
Le Mans University, FRANCE

## License
 
This project is licensed under the MIT License.
