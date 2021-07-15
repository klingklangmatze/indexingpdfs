import numpy as np
import matplotlib.pyplot as plt
import mplstereonet

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='equal_angle_stereonet')
ax.set_azimuth_ticks(range(0, 360, 30))


ax.text(0.491, 0.491, '$c$', transform=ax.transAxes, color='grey', zorder=3)
ax.text(0.491, 0.559, 'e', transform=ax.transAxes, color='lightgrey')
ax.text(0.492, 0.59, '2', transform=ax.transAxes, color='grey')
ax.text(0.492, 0.635, '3', transform=ax.transAxes, color='grey')
ax.text(0.490, 0.733, '4', transform=ax.transAxes, color='grey')
ax.text(0.492, 0.975, '5', transform=ax.transAxes, color='grey')
ax.text(0.603, 0.68, '6', transform=ax.transAxes, color='grey')
ax.text(0.656, 0.768, '7', transform=ax.transAxes, color='grey')
ax.text(0.622, 0.844, '8', transform=ax.transAxes, color='grey')
ax.text(0.568, 0.918, '9', transform=ax.transAxes, color='grey')
ax.text(0.724, 0.907, '10', transform=ax.transAxes, color='grey')
ax.text(0.686, 0.836, '11', transform=ax.transAxes, color='lightgrey')
ax.text(0.61, 0.892, '12', transform=ax.transAxes, color='lightgrey', fontsize=7)
ax.text(0.484, 0.902, '13', transform=ax.transAxes, color='lightgrey')
ax.text(0.576, 0.972, '14', transform=ax.transAxes, color='lightgrey', fontsize=7)


textstr = '     $2 \Rightarrow \{10\overline{1}3\}$  $3 \Rightarrow \{10\overline{1}2\}$  $4 \Rightarrow \{10\overline{1}1\} ' \
          '$  $5 \Rightarrow \{10\overline{1}0\}$  $6 \Rightarrow \{11\overline{2}2\}$  $7 \Rightarrow \{11\overline{2}1\} ' \
          '$  $8 \Rightarrow \{21\overline{3}1\}$\n$9 \Rightarrow \{51\overline{6}1\}$  $10 \Rightarrow \{11\overline{2}0\} ' \
          '$  $11 \Rightarrow \{22\overline{4}1\}$  $12 \Rightarrow \{31\overline{4}1\}$  $13 \Rightarrow \{40\overline{4}1\} ' \
          '$  $14 \Rightarrow \{51\overline{6}0\}$  $e \Rightarrow \{10\overline{1}4\}$'

ax.text(0.01, -0.13, textstr, transform=ax.transAxes, fontsize=8, color='grey')

# PDF e {10-14}
for ang in range(0, 360, 60):
    ax.cone(90-17.62, ang, 5, zorder=2, color='white', edgecolor='lightgrey')

# PDF 11 {22-41}
for ang in range(30, 360, 60):
    ax.cone(90-77.2, ang, 5, zorder=2, color='white', edgecolor='lightgrey')

# PDF 12 {31-41}
for ang in range(15, 360, 30):
    ax.cone(90-77.91, ang, 5, zorder=2, color='white', edgecolor='lightgrey')

# PDF 13 {40-11}
for ang in range(0, 360, 60):
    ax.cone(90-78.87, ang, 5, zorder=2, color='white', edgecolor='lightgrey')

# PDF 14
ax.cone(0, 10, 5, zorder=2, facecolor='white', edgecolors='lightgrey')
ax.cone(0, 50, 5, zorder=2, facecolor='white', edgecolors='lightgrey')
ax.cone(0, 70, 5, zorder=2, facecolor='white', edgecolors='lightgrey')
ax.cone(0, 110, 5, zorder=2, facecolor='white', edgecolors='lightgrey')
ax.cone(0, 130, 5, zorder=2, facecolor='white', edgecolors='lightgrey')
ax.cone(0, 170, 5, zorder=2, facecolor='white', edgecolors='lightgrey')
ax.cone(0, 190, 5, zorder=2, facecolor='white', edgecolors='lightgrey')
ax.cone(0, 230, 5, zorder=2, facecolor='white', edgecolors='lightgrey')
ax.cone(0, 250, 5, zorder=2, facecolor='white', edgecolors='lightgrey')
ax.cone(0, 290, 5, zorder=2, facecolor='white', edgecolors='lightgrey')
ax.cone(0, 310, 5, zorder=2, facecolor='white', edgecolors='lightgrey')
ax.cone(0, 350, 5, zorder=2, facecolor='white', edgecolors='lightgrey')

# PDF 2 {10-13}
for ang in range(0, 360, 60):
    ax.cone(90-22.95, ang, 5, zorder=2, color='white', edgecolor='grey')

# PDF 3 {10-12}
for ang in range(0, 360, 60):
    ax.cone(90-32.42, ang, 5, zorder=2, color='white', edgecolor='grey')

# PDF 4 {10-11}
for ang in range(0, 360, 60):
    ax.cone(90-51.79, ang, 5, zorder=2, color='white', edgecolor='grey')

# PDF 5 {10-10}
for ang in range(0, 360, 60):
    ax.cone(90-90, ang, 5, zorder=2, color='white', edgecolor='grey')

# PDF 6 {11-22}
for ang in range(30, 360, 60):
    ax.cone(90-47.73, ang, 5, zorder=2, color='white', edgecolor='grey')

# PDF 7 {11-21}
for ang in range(30, 360, 60):
    ax.cone(90-65.56, ang, 5, zorder=2, color='white', edgecolor='grey')

# PDF 8 {21-31}
for ang in range(20, 60, 20):
    ax.cone(90-73.71, ang, 5, zorder=2, color='white', edgecolor='grey')
for ang in range(80, 120, 20):
    ax.cone(90-73.71, ang, 5, zorder=2, color='white', edgecolor='grey')
for ang in range(140, 180, 20):
    ax.cone(90-73.71, ang, 5, zorder=2, color='white', edgecolor='grey')

for ang in range(200, 240, 20):
    ax.cone(90-73.71, ang, 5, zorder=2, color='white', edgecolor='grey')
for ang in range(260, 300, 20):
    ax.cone(90-73.71, ang, 5, zorder=2, color='white', edgecolor='grey')
for ang in range(320, 360, 20):
    ax.cone(90-73.71, ang, 5, zorder=2, color='white', edgecolor='grey')

# PDF 9 {21-31}
for ang in range(10, 90, 40):
    ax.cone(90-82.07, ang, 5, zorder=2, color='white', edgecolor='grey')
for ang in range(190, 270, 40):
    ax.cone(90-82.07, ang, 5, zorder=2,  color='white', edgecolor='grey')

ax.cone(90-82.07, 70, 5, zorder=2,  color='white', edgecolor='grey')
ax.cone(90-82.07, 110, 5, zorder=2,  color='white', edgecolor='grey')
ax.cone(90-82.07, 130, 5, zorder=2,  color='white', edgecolor='grey')
ax.cone(90-82.07, 170, 5, zorder=2,  color='white', edgecolor='grey')
ax.cone(90-82.07, 250, 5, zorder=2,  color='white', edgecolor='grey')
ax.cone(90-82.07, 290, 5, zorder=2,  color='white', edgecolor='grey')
ax.cone(90-82.07, 310, 5, zorder=2,  color='white', edgecolor='grey')
ax.cone(90-82.07, 350, 5, zorder=2,  color='white', edgecolor='grey')

# PDF 10 {11-20}
for ang in range(30, 360, 60):
    ax.cone(90-90, ang, 5, zorder=2,  color='white', edgecolor='grey')



def sph2cart(lon, lat):
    x = np.cos(lat)*np.cos(lon)
    y = np.cos(lat)*np.sin(lon)
    z = np.sin(lat)
    return x, y, z


def cart2sph(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    lat = np.arcsin(z/r)
    lon = np.arctan2(y, x)
    return lon, lat


def indexing(az, dip, dir, label, symbol, color, edgecolor, size, uv_n, theta, rot_angle):

    # U-state data to Az, Dip
    if dir in ['E', 'e']:
        az = 360 - az
    elif az < 180:
        az = 180 - az
    else:
        az = 360-(az-180)

    # Sphere coordinates to Cartesian coord.
    vector = np.asarray(sph2cart(np.radians(az), np.radians(dip)))
    vector_n = vector / np.linalg.norm(vector)

    # Rotation matrix * vector
    z1 = (np.cos(theta) * (np.cross(uv_n, vector_n)))
    rm = uv_n * (np.dot(uv_n, vector_n)) + np.cross(z1, uv_n) + (np.sin(theta) * (np.cross(uv_n, vector_n)))
    rm_n = rm / np.linalg.norm(rm)

    v_x, v_y, v_z = rm_n
    vector_rot_deg = np.degrees(cart2sph(v_x, v_y, v_z))

    az, dip = vector_rot_deg

    if az > 0:
        if dip < 0:
            az = az + 180
            dip = abs(dip)
        else:
            az = az
            dip = abs(dip)
    elif dip < 0:
        az = az + 180
        dip = abs(dip)
    else:
        az = az + 360
        dip = abs(dip)

    ax.pole(az + rot_angle + 90, 90 - dip, symbol, markersize=size, label=label, zorder=3, markeredgecolor=edgecolor, markerfacecolor=color, markeredgewidth=1.1)

    return az, dip


# Rotation axis based on C_AXIS
#The respective C-axis of the quartz grain must be entered here
caa, cad, dir = 125, 23, 'e'
if dir in ['E', 'e']:
    caa = 360 - caa
elif caa < 180:
    caa = 180 - caa
else:
    caa = 360-(caa-180)

ca_a = caa
ca_d = cad

if ca_a in range(0, 90):
    vz = -1
    ra_a = ca_a + 90
if ca_a in range(270, 360):
    vz = -1
    ra_a = ca_a + 90
if ca_a in range(90, 180):
    vz = 1
    ra_a = ca_a - 90
if ca_a in range(180, 270):
    vz = 1
    ra_a = ca_a - 90

rot_ax = np.asarray(sph2cart(np.radians(ra_a), np.radians(0)))
v_nu = rot_ax / np.linalg.norm(rot_ax)
theta = np.radians(vz * (90 - ca_d))


#Here you can finally rotate the measuring points
rot_angle = 0

if rot_angle > 0:
    ax.text(0.85, 0.075, 'Rotation: \nClockwise '+ str(rot_angle) + '°', transform=ax.transAxes, color='grey', zorder=2, fontsize=7)
elif rot_angle < 0:
    ax.text(0.85, 0.075, 'Rotation: \nCounterclockwise ' + str(np.abs(rot_angle)) + '°', transform=ax.transAxes, color='grey', zorder=2,
            fontsize=7)
else:
    ax.text(0.85, 0.075, 'Unrotated data', transform=ax.transAxes, color='grey', zorder=2,
            fontsize=7)


#Enter the measured values at this point
indexing(15, 12, 'w', 'PDF1', '+', 'g', 'g', '8', v_nu, theta, rot_angle)
indexing(255, 8, 'e', 'PDF2', '+', 'b', 'b', '8', v_nu, theta, rot_angle)
indexing(2, 6, 'w', 'PDF3', '+',  'r', 'r', '8', v_nu, theta, rot_angle)
indexing(56, 10, 'w', 'PDF3', '+',  'r', 'r', '8', v_nu, theta, rot_angle)
indexing(56, 10, 'w', 'PDF3', '+',  'r', 'r', '8', v_nu, theta, rot_angle)


ax.legend(title='$\mathbf{RA-16}$\n   $\mathit{Grain}-1b2$', loc='best', frameon=True, fancybox=True, edgecolor='dimgrey',
          labelspacing=0.25, borderpad=0.25)

circle1 = plt.Circle((0, 0), 0.09, linewidth=1, facecolor='white', ls='solid', ec='dimgrey', zorder=2)
ax.add_artist(circle1)
ax.grid(color='lightgrey', zorder=0, ls='--')

#fig.savefig("ustage_meas_RA16_g1b2.svg", bbox_inches='tight', format='svg')
#fig.savefig("ustage_meas_RA16_g1b2.pdf", bbox_inches='tight', format='pdf')
# fig.savefig("ustage_meas_035_g1.png", bbox_inches='tight', format='png', dpi=300)

plt.show()
