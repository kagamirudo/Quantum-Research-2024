import matplotlib.pyplot as plt
import numpy as np


def LMSR1(s):
    s = s + s
    n = len(s) // 2
    f = [-1] * n
    k = 0

    for j in range(1, n):
        i = f[j - k - 1]
        while i != -1 and s[k + i + 1] != s[j]:
            if s[j] < s[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if s[k + i + 1] != s[j]:
            if s[j] < s[k]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k


def LMSR(s):
    n = len(s)
    res = 0
    l = 0
    while l < n:
        res = l
        r = l
        p = l + 1
        while r < n:
            c = s[p] if p < n else s[p - n]
            if s[r] > c:
                break
            if s[r] < c:
                r = l - 1
            r += 1
            p += 1
        l = max(r, l + p - r)
    return res


def detect(chain):
    chain_r = "".join(reversed(chain))
    i = LMSR(chain)
    i_r = LMSR(chain_r)

    n = len(chain)
    chain = chain + chain

    return min(chain[i : i + n], chain[i_r : i_r + n])


def visualize_benzenoid(chain):
    # Define the coordinates for the benzene ring (hexagon)
    angles = np.linspace(0, 2 * np.pi, 7)[:-1]  # 6 points for benzene
    x = np.cos(angles)
    y = np.sin(angles)

    # Convert BEC to zero-based index (BEC digits - 1)
    bec = [int(char) - 1 for char in chain]  # Adjusting to zero-based indexing

    # Reorder BEC to start from the lowest-left and clockwise
    # First, find the lowest-left (smallest angle, i.e., smallest x-coordinate)
    start_index = np.argmin(x)  # Find the index of the lowest-left atom

    # Adjust the BEC so it starts from the correct position
    bec = bec[bec.index(start_index) :] + bec[: bec.index(start_index)]

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(5, 5))

    # Plot the carbon atoms (6 vertices for benzene)
    ax.scatter(x, y, c="black", s=100, label="Carbon Atoms", zorder=3)

    # Start traversing the boundary as per BEC
    for i in range(len(bec)):
        start = bec[i]  # Get the starting index of boundary traversal
        end = bec[(i + 1) % len(bec)]  # Wrap around for boundary continuity

        # Draw boundary edge based on BEC
        ax.plot(
            [x[start], x[end]],
            [y[start], y[end]],
            "r-",
            lw=3,
            alpha=0.9,
            label="Boundary Edge" if i == 0 else "",
        )

    # Formatting
    ax.set_aspect("equal")
    ax.set_title(f"Benzene Visualization with BEC ({chain})", fontsize=12)
    ax.axis("off")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    chain = "4142123351123111521"
    visualize_benzenoid(chain)

    print(detect(chain))
