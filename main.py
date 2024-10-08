import matplotlib.pyplot as plt
import numpy as np

# Set up the figure for plotting
fig, axs = plt.subplots(8, 1, figsize=(10, 16))
fig.subplots_adjust(hspace=0.6)

# Simulate time points
time = np.arange(1, 21)

# Irregular Data for Sensor 1
sensor_1 = np.array([np.nan, 1, np.nan, np.nan, np.nan, 2, 3, np.nan, np.nan, np.nan,
                    np.nan, 4, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
axs[0].plot(time, sensor_1, 'bo-', label='Sensor 1 (Irregular)')
axs[0].set_title('Sensor 1: Irregular Data')
axs[0].set_ylabel('Value')
axs[0].set_xlabel('Time')
axs[0].legend()

# Missing Data for Sensor 2
sensor_2 = np.array([np.nan, 1, np.nan, np.nan, 2, np.nan, np.nan, 3, np.nan, np.nan,
                    np.nan, np.nan, np.nan, 4, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
axs[1].plot(time, sensor_2, 'go-', label='Sensor 2 (Missing)')
axs[1].set_title('Sensor 2: Missing Data')
axs[1].set_ylabel('Value')
axs[1].set_xlabel('Time')
axs[1].legend()

# Inaccurate Data for Sensor 3
sensor_3 = np.ones(20)
sensor_3[5] = np.nan  # Faulty data points
sensor_3[10] = np.nan
axs[2].plot(time, sensor_3, 'ro-', label='Sensor 3 (Inaccurate)')
axs[2].set_title('Sensor 3: Inaccurate Data')
axs[2].set_ylabel('Value')
axs[2].set_xlabel('Time')
axs[2].legend()

# Noisy Data for Sensor 4
sensor_4 = np.sin(time / 2) + np.random.normal(0,
                                               0.1, len(time))  # Sine wave + noise
axs[3].plot(time, sensor_4, 'mo-', label='Sensor 4 (Noisy)')
axs[3].set_title('Sensor 4: Noisy Data')
axs[3].set_ylabel('Value')
axs[3].set_xlabel('Time')
axs[3].legend()

# Delayed Data for Sensor 5 (shifted)
sensor_5 = np.array([np.nan, np.nan, 1, 2, 3, 4, 5, np.nan, np.nan, np.nan, np.nan,
                    np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
axs[4].plot(time, sensor_5, 'co-', label='Sensor 5 (Delayed)')
axs[4].set_title('Sensor 5: Delayed Data')
axs[4].set_ylabel('Value')
axs[4].set_xlabel('Time')
axs[4].legend()

# Inconsistent Data for Sensor 6
sensor_6_format_1 = np.array([1, np.nan, 1.5, np.nan, 2, np.nan, np.nan, np.nan, np.nan,
                             np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
sensor_6_format_2 = np.array([np.nan, 10, np.nan, 20, np.nan, 30, np.nan, np.nan, np.nan,
                             np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
axs[5].plot(time, sensor_6_format_1, 'yo-', label='Format 1')
axs[5].plot(time, sensor_6_format_2, 'bo-', label='Format 2')
axs[5].set_title('Sensor 6: Inconsistent Data')
axs[5].set_ylabel('Value')
axs[5].set_xlabel('Time')
axs[5].legend()

# Sensor Drift for Sensor 7
sensor_7 = np.linspace(1, 3, 20) + np.random.normal(0,
                                                    0.05, 20)  # Gradual drift
axs[6].plot(time, sensor_7, 'ko-', label='Sensor 7 (Sensor Drift)')
axs[6].set_title('Sensor 7: Sensor Drift')
axs[6].set_ylabel('Value')
axs[6].set_xlabel('Time')
axs[6].legend()

# Clock Skew for Sensor 8
sensor_8 = np.array([np.nan, 1, 2, 3, 4, 5, np.nan, np.nan, np.nan, np.nan, np.nan,
                    np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
axs[7].plot(time, sensor_8, 'ro-', label='Sensor 8 (Clock Skew)')
axs[7].set_title('Sensor 8: Clock Skew')
axs[7].set_ylabel('Value')
axs[7].set_xlabel('Time')
axs[7].legend()

plt.show()
