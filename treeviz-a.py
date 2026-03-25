import json
import sys
import argparse
from PIL import Image, ImageDraw

def get_tree_coordinates(node, depth=0, x_offset=0):
    nodes = []
    is_root = (depth == 0)
    nodes.append((x_offset, depth, is_root))
    
    current_x = x_offset
    max_child_x = x_offset
    
    for i, child in enumerate(node.get('children', [])):
        child_x = current_x if i == 0 else max_child_x + 1
        child_nodes, last_x = get_tree_coordinates(child, depth + 1, child_x)
        nodes.extend(child_nodes)
        max_child_x = max(max_child_x, last_x)
        
    return nodes, max_child_x

def draw_forest(args):
    with open(args.input, 'r', encoding='utf-8') as f:
        forest_data = json.load(f)

    processed_trees = []
    
    # 1. Calculate relative coordinates
    for tree_json in forest_data:
        coords, width = get_tree_coordinates(tree_json)
        w = (width + 1)
        h = max([c[1] for c in coords]) + 1
        # Add 'size' (total nodes) for another sorting option
        processed_trees.append({
            'coords': coords, 
            'w': w, 
            'h': h, 
            'size': len(coords)
        })

    # 2. Sorting Logic
    if args.sort_depth:
        processed_trees.sort(key=lambda t: t['h'])
    elif args.sort_width:
        processed_trees.sort(key=lambda t: t['w'])
    elif args.sort_size:
        processed_trees.sort(key=lambda t: t['size'])

    # 3. Layout Logic
    max_w = max(t['w'] for t in processed_trees)
    max_h = max(t['h'] for t in processed_trees)
    
    num_trees = len(processed_trees)
    grid_cols = args.cols if args.cols else int(num_trees**0.5) + 1
    grid_rows = (num_trees // grid_cols) + (1 if num_trees % grid_cols != 0 else 0)

    # Use node_size for the grid. A node_size of 3 means 2x2 active + 1px border.
    n = args.node_size
    pad = args.padding
    cell_w = (max_w * n) + pad
    cell_h = (max_h * n) + pad
    
    img_w = grid_cols * cell_w
    img_h = grid_rows * cell_h

    # 4. Render
    img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    for idx, tree in enumerate(processed_trees):
        row = idx // grid_cols
        col = idx % grid_cols
        
        base_x = col * cell_w
        base_y = row * cell_h

        for x, y, is_root in tree['coords']:
            px = base_x + (x * n)
            py = base_y + (y * n)
            
            color = (255, 0, 0) if is_root else (0, 0, 0)
            # Draw core (node_size - 1 to leave that 1px white border)
            draw.rectangle([px, py, px + (n-2), py + (n-2)], fill=color)

    img.save(args.output)
    print(f"Forest rendered to {args.output}")
    print(f"Stats: {num_trees} trees | Grid: {grid_cols}x{grid_rows} | Max Depth: {max_h}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render NLP trees as a pixel forest.")
    parser.add_argument("input", help="Path to the JSON trees file")
    parser.add_argument("output", help="Name of the output PNG file")
    
    # Layout and Sorting
    parser.add_argument("--cols", type=int, help="Grid columns")
    parser.add_argument("--sort-depth", action="store_true", help="Sort by tree height")
    parser.add_argument("--sort-width", action="store_true", help="Sort by tree breadth")
    parser.add_argument("--sort-size", action="store_true", help="Sort by total node count")
    
    # Rendering Parameters
    parser.add_argument("--node-size", type=int, default=3, help="Pixels per node (default 3)")
    parser.add_argument("--padding", type=int, default=3, help="Pixels between trees (default 3)")
    
    args = parser.parse_args()
    draw_forest(args)