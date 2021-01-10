import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
ax1.add_patch(
    patches.Circle(
        (0.5, 0.5),   # (x,y)
        0.4,          # radius
    )
)

# fig1.savefig('circle1.png', dpi=90, bbox_inches='tight')
plt.show()
