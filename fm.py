import pyaudio
import numpy as np

# Constants
SAMPLE_RATE = 44100    # Sample rate of the audio stream
FREQ_DEV = 75e3        # Maximum frequency deviation of FM signal
FREQ_STEP = 10         # Frequency step size for tuning
CHANNELS = 1           # Number of audio channels (mono)
CHUNK_SIZE = 1024      # Number of samples per audio chunk

# Create PyAudio stream object
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paFloat32,
                    channels=CHANNELS,
                    rate=SAMPLE_RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK_SIZE)

# Function to generate FM demodulation coefficients
def fm_coeffs(frequency):
    omega = 2.0 * np.pi * frequency / SAMPLE_RATE
    return np.array([np.sin(omega * n) for n in range(CHUNK_SIZE)])

# Function to tune to a specific frequency
def tune_frequency(frequency):
    global demod_coeffs
    demod_coeffs = fm_coeffs(frequency)
    print(f"Tuned to {frequency/1000:.1f} kHz")

# Initialize frequency and demodulation coefficients
frequency = 89.1e6    # Starting frequency
demod_coeffs = fm_coeffs(frequency)

# Main loop
while True:
    # Read audio chunk from sound card
    data = np.frombuffer(stream.read(CHUNK_SIZE), dtype=np.float32)
    
    # Apply FM demodulation
    demod_data = np.abs(np.convolve(data, demod_coeffs))
    
    # Play audio chunk to sound card
    stream.write(demod_data.tobytes())
    
    # Check for frequency changes
    key = input()
    if key == 'q':    # Quit program
        break
    elif key == 'up':    # Increase frequency
        frequency += FREQ_STEP
        tune_frequency(frequency)
    elif key == 'down':    # Decrease frequency
        frequency -= FREQ_STEP
        tune_frequency(frequency)
        
# Clean up
stream.stop_stream()
stream.close()
audio.terminate()
