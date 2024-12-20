#!/bin/bash
# Generate Preview Images
#
# Dependencies:
#   - hyprshot
#   - cwebp
#   - catppuccin-catwalk (as catwalk executable in PATH)
#
# Important notes:
#   - This script will only work on Wayland on Linux
#   - This script assumes installation through Toolbox which, at the time
#     of writing, is the only possible way to install Fleet. If this changes
#     in the future, the script will need updating
set -euo pipefail
IFS=$'\n\t'

FLEET_TOOLBOX_BIN="$HOME/.local/share/JetBrains/Toolbox/apps/fleet/bin/Fleet"

SCRIPT_PATH="$(dirname "$0")"
OUTPUT_DIR="$SCRIPT_PATH/../assets"
TMP_DIR="/tmp/catppuccin-theme-preview"
CATPPUCCIN_THEMES_DIR="$SCRIPT_PATH/../catppuccin-theme/frontendImpl/src/jvmMain/resources"
FLEET_THEME_DIR="$HOME/.config/JetBrains/Fleet/themes"
DEMO_THEME="{\"meta\": {\"theme.name\": \"DEMO THEME (SELECT ME!)\",\"theme.kind\": \"Dark\",\"theme.version\": 1},\"colors\": {},\"textAttributes\": {},\"palette\": {}}"

if [[ ! -f "$FLEET_TOOLBOX_BIN" ]]; then
    echo "Fleet binary not found in Toolbox directory. If installed through another mean, please file an issue"
    exit 1
fi

# Clone test repository
rm -rf "$TMP_DIR"
git clone https://github.com/catppuccin/catppuccin "$TMP_DIR" --depth 1

# Place the demo theme so that it can be selected and later replaced
echo -n "$DEMO_THEME" > "$FLEET_THEME_DIR/demo_theme.json"

# Launch instance of fleet in the background
"$FLEET_TOOLBOX_BIN" "$TMP_DIR/samples/kotlin.kt" --projectDir "$TMP_DIR" &> /dev/null &
pid=$!

# Inform the user of the next steps
echo "Once Fleet launches, select the 'DEMO THEME' and then come back here and press enter."
echo "Hyprshot will launch every 3 seconds and then you will need to capture the Fleet window"
read

for theme_path in $(find "$CATPPUCCIN_THEMES_DIR" -type f); do
    # Replace the demo theme contents with the new ones
    cp "$theme_path" "$FLEET_THEME_DIR/demo_theme.json"
    # Give it some time for Fleet to update
    sleep 3

    # For some reason, hyprshot exists with code 1 even on success, so ignore it
    png_path=$(hyprshot --mode window --silent -o "/tmp" -- echo || true)
    output_file="$(basename "$theme_path" | sed -e "s/^catppuccin-//" -e "s/\.json$//").webp"

    cwebp -q 100 -o "$OUTPUT_DIR/$output_file" "$png_path" &> /dev/null
done

catwalk --layout stacked --directory assets/

# Cleanup
kill "$pid"
rm "$FLEET_THEME_DIR/demo_theme.json"
