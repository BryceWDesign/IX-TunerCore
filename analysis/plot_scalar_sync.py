import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('scalar_convergence_test_log.csv')

# Convert timestamp to seconds
def to_seconds(t):
    m, s = t.split(':')
    return int(m)*60 + float(s)

df['Seconds'] = df['Timestamp'].apply(to_seconds)

# Extract individual node data
nodes = df['Node_ID'].unique()

# Set up figure
plt.figure(figsize=(12, 8))
colors = ['tab:red', 'tab:blue', 'tab:green']

for i, node in enumerate(nodes):
    sub_df = df[df['Node_ID'] == node]

    # Plot Phase Error
    plt.subplot(2, 2, 1)
    plt.plot(sub_df['Seconds'], sub_df['Phase_Error_deg'], label=f'Node {node}', color=colors[i])
    plt.title('Phase Error Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Phase Error (°)')
    plt.grid(True)

    # Plot Magnetic Field
    plt.subplot(2, 2, 2)
    plt.plot(sub_df['Seconds'], sub_df['Mag_Field_T'], label=f'Node {node}', color=colors[i])
    plt.title('Magnetic Field Strength')
    plt.xlabel('Time (s)')
    plt.ylabel('Field (T)')
    plt.grid(True)

    # Plot Optical Voltage
    plt.subplot(2, 2, 3)
    plt.plot(sub_df['Seconds'], sub_df['Optical_V'], label=f'Node {node}', color=colors[i])
    plt.title('Optical Sensor Output')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.grid(True)

    # Plot Temperature
    plt.subplot(2, 2, 4)
    plt.plot(sub_df['Seconds'], sub_df['Temp_C'], label=f'Node {node}', color=colors[i])
    plt.title('Temperature Stability')
    plt.xlabel('Time (s)')
    plt.ylabel('°C')
    plt.grid(True)

# Final legend
plt.tight_layout()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)
plt.suptitle('IX-TunerCore: Scalar Convergence Test Results', fontsize=16, y=1.03)
plt.show()
