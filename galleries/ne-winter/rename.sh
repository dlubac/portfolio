prefix="ne_winter"
counter=1

for file in *.jpg; do
    if [ -f "$file" ]; then
        new_name="${prefix}_${counter}.jpg"
        mv "$file" "$new_name"
        echo "Renamed $file to $new_name"
        ((counter++))
    fi
done