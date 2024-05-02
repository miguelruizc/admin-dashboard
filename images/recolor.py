import xml.etree.ElementTree as ET

def recolor_svg(svg_file_path, output_file_path, new_fill_color):
    # Parse the SVG file
    tree = ET.parse(svg_file_path)
    root = tree.getroot()
    
    # Define the SVG namespace
    namespace = "{http://www.w3.org/2000/svg}"
    
    # Find all elements with 'fill' attribute
    for elem in root.iter(namespace + "path"):
        # Modify fill attribute to new color
        elem.set("fill", new_fill_color)
    
    # Save the modified SVG to a new file
    tree.write(output_file_path)

# Usage example
recolor_svg("tasks.svg", "white/tasks.svg", "white")
