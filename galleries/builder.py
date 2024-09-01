import os

def build_html(path):
    file = path.split("/")[1].split(".avif")[0]
    return f"""
<a class="spotlight" href="{file}.avif" data-description="">
    <picture>
        <source srcset="{file}_thumb_s.avif" media="(max-width: 775px)">
        <img src="{file}_thumb.avif" loading="lazy" alt="" />
    </picture>
</a>"""

def find_avif_files(directory):
    avif_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.avif') and '_thumb' not in file and 'cover' not in file:
                avif_files.append(os.path.join(root, file))
    avif_files.sort()
    return avif_files

# Example usage
avif_files = find_avif_files('acadia')
print(avif_files)

for avif_file in avif_files:
    print(build_html(avif_file))