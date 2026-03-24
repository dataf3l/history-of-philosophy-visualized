import json
import sys
import argparse
from PIL import Image, ImageDraw

def get_tree_coordinates(node, depth=0, x_offset=0):
    """
    Recursively calculates (x, y) coordinates for each node.
    Returns a list of (x, y, is_root) and the total width used.
    """
    nodes = []
    is_root = (depth == 0)
    # Current node position
    nodes.append((x_offset, depth, is_root))
    
    current_x = x_offset
    max_child_x = x_offset
    
    for i, child in enumerate(node.get('children', [])):
        # If it's the first child, it stays in the same X column
        # Subsequent children move to the right
        child_x = current_x if i == 0 else max_child_x + 1
        child_nodes, last_x = get_tree_coordinates(child, depth + 1, child_x)
        nodes.extend(child_nodes)
        max_child_x = max(max_child_x, last_x)
        
    return nodes, max_child_x

def draw_forest(input_json, output_png, grid_cols=None):
    with open(input_json, 'r', encoding='utf-8') as f:
        forest_data = json.load(f)

    processed_trees = []
    max_w, max_h = 0, 0

    # 1. Calculate relative coordinates for every tree
    for tree_json in forest_data:
        coords, width = get_tree_coordinates(tree_json)
        # Calculate bounding box for this specific tree
        w = (width + 1)
        h = max([c[1] for c in coords]) + 1
        processed_trees.append({'coords': coords, 'w': w, 'h': h})
        max_w = max(max_w, w)
        max_h = max(max_h, h)

    # 2. Layout Logic (Grid)
    num_trees = len(processed_trees)
    if not grid_cols:
        grid_cols = int(num_trees**0.5) + 1
    
    grid_rows = (num_trees // grid_cols) + (1 if num_trees % grid_cols != 0 else 0)

    # Each node is 3x3 pixels. 
    # Let's add 1 extra pixel of padding between trees in the grid
    cell_w = (max_w * 3) + 3
    cell_h = (max_h * 3) + 3
    
    img_w = grid_cols * cell_w
    img_h = grid_rows * cell_h

    # 3. Render PNG
    img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    for idx, tree in enumerate(processed_trees):
        row = idx // grid_cols
        col = idx % grid_cols
        
        # Calculate the top-left corner of this tree's grid cell
        base_x = col * cell_w
        base_y = row * cell_h

        for x, y, is_root in tree['coords']:
            # Calculate pixel position (3x3 grid)
            px = base_x + (x * 3)
            py = base_y + (y * 3)
            
            color = (255, 0, 0) if is_root else (0, 0, 0)
            
            # Draw the 2x2 core within the 3x3 space
            draw.rectangle([px, py, px + 1, py + 1], fill=color)

    img.save(output_png)
    print(f"Forest rendered: {output_png} ({img_w}x{img_h} px)")
    print(f"Max Tree Size: {max_w} nodes wide, {max_h} nodes deep")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render NLP trees as a pixel forest.")
    parser.add_argument("input", help="Path to the JSON trees file")
    parser.add_argument("output", help="Name of the output PNG file")
    parser.add_argument("--cols", type=int, help="Number of columns in the grid (default: auto)")
    
    args = parser.parse_args()
    
    try:
        draw_forest(args.input, args.output, args.cols)
    except Exception as e:
        print(f"Error: {e}")
