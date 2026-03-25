# UI Architecture and Implementation Plan

## Project Context for AI Assistant
This project, "Philosophy Visualized", is an NLP and visualization tool. It takes text (e.g., philosophical books), parses the grammatical sentence structures into dependency grammar trees using Stanford Stanza (`tree8.py`), and then renders these trees into a "pixel art forest" PNG image (`treeviz-a.py`) where each sentence is a tree and each word is a node.

Currently, the process is manual via the CLI:
1. `python tree8.py <input.txt>` outputs `<output.json>`
2. `python treeviz-a.py [options] <output.json> <output.png>`

The objective is to build a beautiful, modern, interactive User Interface around this pipeline.

## Proposed Stack
- **Backend API**: FastAPI (Python) to wrap the existing parsing and rendering scripts (`tree8.py` and `treeviz-a.py`) for easy web consumption.
- **Frontend SPA**: Vite + React, utilizing vanilla CSS for a highly customized, premium design system.

## UI/UX Design Aesthetics (CRITICAL)
- **Visuals**: The UI must have a serious "Wow" factor. Implement a sleek dark mode with glassmorphism effects for the input panels and main layout to feel extremely premium.
- **Typography & Colors**: Use modern layout typography (e.g., Inter, Roboto, or Outfit from Google Fonts). Avoid generic colors; use curated, harmonious color palettes with smooth gradients (e.g., deep purples, blues, and forest greens to match the "tree forest" aesthetic).
- **Interactivity**: The user should feel the interface is dynamic and alive. Include micro-animations for button hovers, loading states while Stanza parses the models (which takes several seconds), and a smooth expansion animation when the PNG is finally generated and displayed.
- **Form Controls**: Custom-styled dropdowns and range sliders for the formatting options.

## Core Features
1. **Input Area**: A large text area that supports pasting text directly or uploading a `.txt` file via a stylized drag-and-drop "Dropzone".
2. **Options Panel**: Let the user tweak parameters sent to `treeviz-a.py`:
   - Sort by (Depth, Width, Size)
   - Layout Configuration (Columns per row, Node Size, Padding between trees)
3. **Action Button**: A prominent, modern, dynamically-lit "Generate Forest" button with clear state indicators (Idle, Parsing, Rendering, Done).
4. **Result Box**: A responsive image viewer for the final PNG with zoom/pan capabilities, accompanied by a "Download Image" button.

## Next Steps for the AI Developer
1. Create a `server.py` FastAPI app with endpoints for `/parse` and `/render`. Link these to the existing logic in `tree8.py` and `treeviz-a.py`.
2. Spin up a new Vite React app in a `frontend/` directory (`npx -y create-vite@latest ./frontend --template react`). Do not use Tailwind unless the user specifically overrides. Use vanilla CSS.
3. Build the styled components according to the aesthetics requirements by writing extensive, modern CSS.
4. Hook the frontend state into the API and handle the file lifecycle and rendering results smoothly.
