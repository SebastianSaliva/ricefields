def print_compatibility_matrix():
    # Data
    distributions = ["MINT", "UBUNTU", "DEBIAN", "MANJARO", "FEDORA", "ARCH"]
    environments = [
        "GNOME",
        "KDE_PLASMA",
        "XFCE",
        "CINNAMON",
        "MATE",
        "LXQT",
        "BUDGIE",
        "LXDE",
        "DDE",
        "PANTHEON",
    ]

    compatibility = {
        "GNOME": [1, 2, 2, 2, 2, 1],
        "KDE_PLASMA": [1, 2, 2, 2, 2, 1],
        "XFCE": [2, 2, 2, 2, 2, 1],
        "CINNAMON": [2, 0, 0, 1, 1, 1],
        "MATE": [2, 2, 1, 1, 2, 1],
        "LXQT": [0, 2, 1, 1, 2, 1],
        "BUDGIE": [0, 1, 0, 0, 0, 1],
        "LXDE": [0, 0, 1, 0, 0, 1],
        "DDE": [0, 0, 0, 0, 0, 1],
        "PANTHEON": [0, 0, 0, 0, 0, 1],
    }

    # Print title and legend
    print("\nDesktop Environment Compatibility Matrix")
    print("=" * 50)
    print("\nLegend:")
    print("2 = Default/Official Support")
    print("1 = Community/Available Support")
    print("0 = Available via Package Manager")
    print("\n")

    # Calculate column widths
    env_width = max(len("DE / Distro"), max(len(env) for env in environments))
    dist_width = max(len(dist) for dist in distributions)

    # Print header
    header = f"{'DE / Distro':<{env_width}} |"
    for dist in distributions:
        header += f" {dist:^{dist_width}} |"
    print("| ", end="")
    print(header)

    print("| :---: " * (len(distributions) + 1) + "|")

    # Print matrix
    for env in environments:
        row = f"{env:<{env_width}} |"
        for value in compatibility[env]:
            row += f" {value:^{dist_width}} |"
        print("| ", end="")
        print(row)

    # Print bottom border
    print("-" * (len(header) + 2 - 7))


if __name__ == "__main__":
    print_compatibility_matrix()
