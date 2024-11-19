#!/usr/bin/env python3
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

# Define arrays
DISTROS = ["MINT", "UBUNTU", "DEBIAN", "MANJARO", "ARCH", "FEDORA"]
ENVIRONMENTS = [
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

# Define compatibility matrix
COMPATIBILITY = {
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


class Messages:

    def get_global_msg():
        return f"""# R.I.C.E. Project Global Development Tracker
Created: {datetime.now().strftime('%Y-%m-%d')}

This file tracks the overall development progress of the R.I.C.E. (Race Inspired Cosmetic Enhancements) project.

## Status
- Initial setup completed
- Directory structure generated
- Compatibility matrix implemented

## Next Steps
- Begin development of themes, icons, and configs
- Test compatibility across distributions
- Document customization procedures"""

    def get_not_env_and_not_distro(component_type):
        return f"""# {component_type.capitalize()} Development Tracker
Created: {datetime.now().strftime('%Y-%m-%d')}

This file tracks the development and testing of {component_type} across environments and distributions.

## Status
- Directory structure initialized
- Ready for development"""

    def get_env_and_not_distro(component_type, env):
        return f"""# {component_type.capitalize()} Development Tracker for {env}
Created: {datetime.now().strftime('%Y-%m-%d')}

This file tracks the development of {component_type} for the {env} desktop environment.

## Status
- Directory structure initialized
- Ready for {env}-specific development"""

    def get_env_and_distro(component_type, env, distro, comp_value):
        comp_text = {
            2: "Default/Official Support",
            1: "Community/Available Support",
            0: "Available via Package Manager",
        }[comp_value]

        return f"""# {component_type.capitalize()} Development Tracker: {env} on {distro}
Created: {datetime.now().strftime('%Y-%m-%d')}

## Compatibility Status
- Level: {comp_value} ({comp_text})

## Development Status
- Directory structure initialized
- Ready for testing and customization"""


def get_tracker_message(
    component_type: str,
    env: Optional[str] = None,
    distro: Optional[str] = None,
    comp_value: Optional[int] = None,
) -> str:
    """Generate tracker message based on component type and parameters."""

    if component_type == "global":
        return Messages.get_global_msg()

    if component_type in ["themes", "icons", "configs"]:
        if not env and not distro:
            return Messages.get_not_env_and_not_distro(component_type)

        elif env and not distro:
            return Messages.get_env_and_not_distro(component_type, env)

        elif env and distro:
            return Messages.get_env_and_distro(component_type, env, distro, comp_value)

    return ""


def value_in_array(value: str, array: List[str]) -> bool:
    """Check if a value exists in an array."""
    return value in array


def get_compatibility(env: str, distro_index: int) -> int:
    """Get compatibility value for environment and distro combination."""
    return COMPATIBILITY[env][distro_index]


def create_single_route(env: str, distro: str) -> None:
    """Create directory structure and trackers for a single environment/distro combination."""
    base_dirs = ["themes", "icons", "configs"]
    distro_index = DISTROS.index(distro)
    comp_value = get_compatibility(env, distro_index)

    for dir_name in base_dirs:
        # Create directory structure
        full_path = os.path.join("rice", dir_name, env, distro)
        os.makedirs(full_path, exist_ok=True)

        # Create tracker files
        with open(os.path.join("rice", dir_name, f"{dir_name}-tracker.md"), "w") as f:
            f.write(get_tracker_message(dir_name))

        with open(
            os.path.join("rice", dir_name, env, f"{dir_name}-{env}-tracker.md"), "w"
        ) as f:
            f.write(get_tracker_message(dir_name, env))

        with open(
            os.path.join(
                full_path, f"{dir_name}-{env}-{distro}-tracker-{comp_value}.md"
            ),
            "w",
        ) as f:
            f.write(get_tracker_message(dir_name, env, distro, comp_value))


def get_user_input() -> None:
    """Handle interactive user input."""
    while True:
        print(
            "Enter environment and distro (format: ENVIRONMENT/DISTRO) or type 'all' to generate full structure:"
        )
        user_input = input().strip()

        if user_input == "all":
            for env in ENVIRONMENTS:
                for distro in DISTROS:
                    create_single_route(env, distro)
            break

        try:
            env, distro = user_input.split("/")
            if value_in_array(env, ENVIRONMENTS) and value_in_array(distro, DISTROS):
                create_single_route(env, distro)
                break
            else:
                print(
                    f"Invalid input. Available environments: {' '.join(ENVIRONMENTS)}"
                )
                print(f"Available distributions: {' '.join(DISTROS)}")
        except ValueError:
            print("Invalid format. Use ENVIRONMENT/DISTRO format or 'all'")


def main() -> None:
    """Main execution logic."""
    # Create main directory structure
    os.makedirs("rice", exist_ok=True)
    os.makedirs("rice/themes", exist_ok=True)
    os.makedirs("rice/icons", exist_ok=True)
    os.makedirs("rice/configs", exist_ok=True)

    if len(sys.argv) == 1:
        get_user_input()
    elif sys.argv[1] == "all":
        for env in ENVIRONMENTS:
            for distro in DISTROS:
                create_single_route(env, distro)
    else:
        try:
            env, distro = sys.argv[1].split("/")
            if value_in_array(env, ENVIRONMENTS) and value_in_array(distro, DISTROS):
                create_single_route(env, distro)
            else:
                print("Invalid input. Usage: script.py [all | environment/distro]")
        except ValueError:
            print("Invalid format. Use environment/distro format")

    # Create global tracker
    with open("rice/global-tracker.md", "w") as f:
        f.write(get_tracker_message("global"))


if __name__ == "__main__":
    main()
