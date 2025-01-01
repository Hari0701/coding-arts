#projectile motion
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# --- Set up the initial figure and axes ---
fig, ax = plt.subplots(2, 2, figsize=(12, 8))
plt.subplots_adjust(left=0.1, bottom=0.35, right=0.9, top=0.9, wspace=0.3, hspace=0.4)

# --- Global Constants ---
g = 9.8  # Gravitational acceleration (m/s^2)
v0 = 20  # Initial velocity (m/s)
theta_deg = 45  # Launch angle (degrees)
theta_rad = np.radians(theta_deg)

# --- Calculations for projectile motion ---
def projectile_params(v0, theta, g):
    t_flight = 2 * v0 * np.sin(theta) / g  # Total time of flight
    t = np.linspace(0, t_flight, 500)  # Time array
    x = v0 * np.cos(theta) * t  # Horizontal distance
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2  # Vertical distance
    R = (v0**2 * np.sin(2 * theta)) / g  # Range
    H = (v0**2 * (np.sin(theta)**2)) / (2 * g)  # Maximum height
    return t, x, y, R, H

# --- Initial computation ---
t, x, y, R, H = projectile_params(v0, theta_rad, g)

# --- Plot the Trajectory (Top Left) ---
ax[0, 0].plot(x, y, color='blue', label="Trajectory")
ax[0, 0].set_title("Projectile Motion: Trajectory")
ax[0, 0].set_xlabel("Horizontal Distance (m)")
ax[0, 0].set_ylabel("Vertical Distance (m)")
ax[0, 0].legend()
ax[0, 0].grid()

# --- Plot Range vs. Angle (Top Right) ---
angles = np.linspace(0, np.pi / 2, 100)  # Angles from 0 to 90 degrees
ranges = (v0**2 * np.sin(2 * angles)) / g  # Range as a function of angle
ax[0, 1].plot(np.degrees(angles), ranges, color='red', label="Range vs Angle")
ax[0, 1].set_title("Range vs Launch Angle")
ax[0, 1].set_xlabel("Angle (degrees)")
ax[0, 1].set_ylabel("Range (m)")
ax[0, 1].legend()
ax[0, 1].grid()

# --- Plot Height vs Time (Bottom Left) ---
ax[1, 0].plot(t, y, color='green', label="Height vs Time")
ax[1, 0].set_title("Height vs Time")
ax[1, 0].set_xlabel("Time (s)")
ax[1, 0].set_ylabel("Height (m)")
ax[1, 0].legend()
ax[1, 0].grid()

# --- Placeholder for dynamic text or future interactive graphs (Bottom Right) ---
ax[1, 1].text(0.5, 0.5, "Adjust sliders to see changes!", fontsize=12, ha='center', va='center')
ax[1, 1].set_title("Interactive Info Panel")
ax[1, 1].axis("off")

# --- Add sliders for interactivity ---
ax_slider_angle = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor="lightgoldenrodyellow")
ax_slider_velocity = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor="lightgoldenrodyellow")
ax_slider_gravity = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")

slider_angle = Slider(ax_slider_angle, "Angle (°)", 0, 90, valinit=theta_deg, valstep=1)
slider_velocity = Slider(ax_slider_velocity, "Velocity (m/s)", 5, 50, valinit=v0, valstep=1)
slider_gravity = Slider(ax_slider_gravity, "Gravity (m/s²)", 1, 20, valinit=g, valstep=0.5)

# --- Reset button ---
reset_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
reset_button = Button(reset_ax, 'Reset', color='lightblue', hovercolor='skyblue')

# --- Update function ---
def update(val):
    global v0, theta_rad, g
    v0 = slider_velocity.val
    theta_deg = slider_angle.val
    g = slider_gravity.val
    theta_rad = np.radians(theta_deg)
    
    # Update projectile motion parameters
    t, x, y, R, H = projectile_params(v0, theta_rad, g)
    
    # Clear and replot the trajectory
    ax[0, 0].cla()
    ax[0, 0].plot(x, y, color='blue', label="Trajectory")
    ax[0, 0].set_title("Projectile Motion: Trajectory")
    ax[0, 0].set_xlabel("Horizontal Distance (m)")
    ax[0, 0].set_ylabel("Vertical Distance (m)")
    ax[0, 0].legend()
    ax[0, 0].grid()
    
    # Clear and replot range vs angle
    angles = np.linspace(0, np.pi / 2, 100)
    ranges = (v0**2 * np.sin(2 * angles)) / g
    ax[0, 1].cla()
    ax[0, 1].plot(np.degrees(angles), ranges, color='red', label="Range vs Angle")
    ax[0, 1].set_title("Range vs Launch Angle")
    ax[0, 1].set_xlabel("Angle (degrees)")
    ax[0, 1].set_ylabel("Range (m)")
    ax[0, 1].legend()
    ax[0, 1].grid()
    
    # Clear and replot height vs time
    ax[1, 0].cla()
    ax[1, 0].plot(t, y, color='green', label="Height vs Time")
    ax[1, 0].set_title("Height vs Time")
    ax[1, 0].set_xlabel("Time (s)")
    ax[1, 0].set_ylabel("Height (m)")
    ax[1, 0].legend()
    ax[1, 0].grid()
    
    # Update the info panel
    ax[1, 1].cla()
    ax[1, 1].text(0.5, 0.8, f"Max Height: {H:.2f} m", fontsize=12, ha='center')
    ax[1, 1].text(0.5, 0.6, f"Range: {R:.2f} m", fontsize=12, ha='center')
    ax[1, 1].text(0.5, 0.4, f"Time of Flight: {2 * t[-1]:.2f} s", fontsize=12, ha='center')
    ax[1, 1].text(0.5, 0.2, "Adjust sliders to explore!", fontsize=12, ha='center')
    ax[1, 1].set_title("Interactive Info Panel")
    ax[1, 1].axis("off")
    
    fig.canvas.draw_idle()

# --- Reset function ---
def reset(event):
    slider_angle.reset()
    slider_velocity.reset()
    slider_gravity.reset()

# --- Connect sliders and reset button ---
slider_angle.on_changed(update)
slider_velocity.on_changed(update)
slider_gravity.on_changed(update)
reset_button.on_clicked(reset)

plt.show()
