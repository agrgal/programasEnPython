import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
ax1.add_patch(
    patches.Ellipse(
        (0.5, 0.5),   # (x,y)
        0.6,          # width
        0.5,          # height
    )
)

# fig1.savefig('ellipse1.png', dpi=90, bbox_inches='tight')
plt.show()
