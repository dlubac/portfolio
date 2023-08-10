for jpg_file in *.jpg; do
    img_tag="<img src=\"./$jpg_file\" alt=\"\" />"
    echo "$img_tag"
done
