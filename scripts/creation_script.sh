#!/bin/bash

# Create main directory structure
mkdir -p rice
cd rice || exit 1
mkdir -p themes icons configs

# Define arrays
distros=("MINT" "UBUNTU" "DEBIAN" "MANJARO" "ARCH" "FEDORA")
environments=("GNOME" "KDE_PLASMA" "XFCE" "CINNAMON" "MATE" "LXQT" "BUDGIE" "LXDE" "DDE" "PANTHEON")

# Define compatibility matrix
declare -A compatibility
compatibility["GNOME"]="1 2 2 2 2 1"
compatibility["KDE_PLASMA"]="1 2 2 2 2 1"
compatibility["XFCE"]="2 2 2 2 2 1"
compatibility["CINNAMON"]="2 0 0 1 1 1"
compatibility["MATE"]="2 2 1 1 2 1"
compatibility["LXQT"]="0 2 1 1 2 1"
compatibility["BUDGIE"]="0 1 0 0 0 1"
compatibility["LXDE"]="0 0 1 0 0 1"
compatibility["DDE"]="0 0 0 0 0 1"
compatibility["PANTHEON"]="0 0 0 0 0 1"

# Function to create tracker message
get_tracker_message() {
    local component_type=$1
    local env=$2
    local distro=$3
    local comp_value=$4
    
    if [ "$component_type" == "global" ]; then
        echo "# R.I.C.E. Project Global Development Tracker
Created: $(date '+%Y-%m-%d')

This file tracks the overall development progress of the R.I.C.E. (Race Inspired Cosmetic Enhancements) project.

## Status
- Initial setup completed
- Directory structure generated
- Compatibility matrix implemented

## Next Steps
- Begin development of themes, icons, and configs
- Test compatibility across distributions
- Document customization procedures"
        return
    fi
    
    case "$component_type" in
        "themes"|"icons"|"configs")
            if [ -z "$env" ] && [ -z "$distro" ]; then
                echo "# ${component_type^} Development Tracker
Created: $(date '+%Y-%m-%d')

This file tracks the development and testing of $component_type across environments and distributions.

## Status
- Directory structure initialized
- Ready for development"
                return
            elif [ -n "$env" ] && [ -z "$distro" ]; then
                echo "# ${component_type^} Development Tracker for $env
Created: $(date '+%Y-%m-%d')

This file tracks the development of $component_type for the $env desktop environment.

## Status
- Directory structure initialized
- Ready for $env-specific development"
                return
            elif [ -n "$env" ] && [ -n "$distro" ]; then
                local comp_text=""
                case $comp_value in
                    2) comp_text="Default/Official Support";;
                    1) comp_text="Community/Available Support";;
                    0) comp_text="Available via Package Manager";;
                esac
                
                echo "# ${component_type^} Development Tracker: $env on $distro
Created: $(date '+%Y-%m-%d')

## Compatibility Status
- Level: $comp_value ($comp_text)

## Development Status
- Directory structure initialized
- Ready for testing and customization"
                return
            fi
            ;;
    esac
}

# Function to validate if a value exists in an array
value_in_array() {
    local value="$1"
    shift
    local array=("$@")
    for item in "${array[@]}"; do
        if [[ "$item" == "$value" ]]; then
            return 0
        fi
    done
    return 1
}

# Function to get compatibility value
get_compatibility() {
    local env=$1
    local distro_index=$2
    local values=(${compatibility[$env]})
    echo ${values[$distro_index]}
}

# Function to create directory structure and trackers
create_single_route() {
    local env=$1
    local distro=$2
    local base_dirs=("themes" "icons" "configs")

    local distro_index=$(printf "%s\n" "${distros[@]}" | grep -nx "$distro" | cut -d: -f1)
    local comp_value=$(get_compatibility "$env" $((distro_index - 1)))

    for dir in "${base_dirs[@]}"; do
        mkdir -p "$dir/$env/$distro"

        touch "$dir/$dir-tracker.md"
        get_tracker_message "$dir" > "$dir/$dir-tracker.md"

        touch "$dir/$env/$dir-$env-tracker.md"
        get_tracker_message "$dir" "$env" > "$dir/$env/$dir-$env-tracker.md"

        touch "$dir/$env/$distro/$dir-$env-$distro-tracker-$comp_value.md"
        get_tracker_message "$dir" "$env" "$distro" "$comp_value" > "$dir/$env/$distro/$dir-$env-$distro-tracker-$comp_value.md"
    done
}

# Function to handle interactive input
get_user_input() {
    while true; do
        echo "Enter environment and distro (format: ENVIRONMENT/DISTRO) or type 'all' to generate full structure:"
        read -r input

        if [[ "$input" == "all" ]]; then
            for env in "${environments[@]}"; do
                for distro in "${distros[@]}"; do
                    create_single_route "$env" "$distro"
                done
            done
            break
        fi

        IFS='/' read -r env distro <<< "$input"
        if value_in_array "$env" "${environments[@]}" && value_in_array "$distro" "${distros[@]}"; then
            create_single_route "$env" "$distro"
            break
        else
            echo "Invalid input. Available environments: ${environments[*]}"
            echo "Available distributions: ${distros[*]}"
        fi
    done
}

# Main Execution Logic
if [ $# -eq 0 ]; then
    get_user_input
elif [ "$1" == "all" ]; then
    for env in "${environments[@]}"; do
        for distro in "${distros[@]}"; do
            create_single_route "$env" "$distro"
        done
    done
else
    IFS='/' read -r env distro <<< "$1"
    if value_in_array "$env" "${environments[@]}" && value_in_array "$distro" "${distros[@]}"; then
        create_single_route "$env" "$distro"
    else
        echo "Invalid input. Usage: $0 [all | environment/distro]"
    fi
fi

# Create global tracker
touch "global-tracker.md"
get_tracker_message "global" >> "global-tracker.md"

