# Cow Detection and Tracking Project

This project contains implementations for cow detection and tracking using YOLO,BoT-SORT, along with pathfinding algorithms (A* and D* ) for visualization purposes.

## Project Structure

```
Cow_detection_tracking/
├── Cow.ipynb                  # Jupyter notebook for cow detection and tracking
├── a_star_algorithm.py        # A* pathfinding without obstacles
├── a_star_obstacle.py         # A* pathfinding with obstacles
├── d_star_algorithm.py        # D* pathfinding algorithm
├── yolo11m.pt                 # YOLO model weights
├── cow_video.mp4              # Input video for tracking
├── 1.png, 2.png, 3.png        # Sample images for detection
└── README.md                  # This file
```

## Requirements

### For Cow Detection (Cow.ipynb)
- Python 3.8+
- ultralytics
- opencv-python
- IPython (for notebook display)

### For Pathfinding Algorithms
- Python 3.8+
- pygame

## Installation

### Step 1: Install Python Dependencies



For pathfinding algorithms:
```bash
pip install pygame
```

Or install all dependencies at once:
```bash
pip install ultralytics opencv-python ipython pygame
```

## Running Instructions

### 1. Cow Detection and Tracking (Cow.ipynb)

#### Option A: Run in Google Colab (Recommended)
1. Upload the notebook file `Cow.ipynb` to Google Colab
2. Upload required files:
   - `yolo11m.pt` (model weights)
   - `cow_video.mp4` (for video tracking)
   - `1.png`, `2.png`, `3.png` (for image detection)
3. Run cells sequentially from top to bottom
4. The notebook will automatically install dependencies in the first cell


#### Option B: Run with VS Code
1. Open the notebook in VS Code
2. Select Python kernel
3. Run cells sequentially

### 2. A* Algorithm (No Obstacles)

Run the basic A* pathfinding visualization:
```bash
python a_star_algorithm.py
```

Controls:
- Press SPACE to start the A* algorithm animation
- Press R to restart
- Press ESC or Q to quit

### 3. A* Algorithm (With Obstacles)

Run A* pathfinding with obstacles:
```bash
python a_star_obstacle.py
```

Controls:
- Press SPACE to start the A* algorithm animation
- Press R to restart after completion
- Press ESC or Q to quit

### 4. D* Lite Algorithm

Run the D* Lite pathfinding algorithm:
```bash
python d_star_algorithm.py
```

Controls:
- Press SPACE to run D* Lite algorithm
- Press R to restart
- Press ESC to quit

## Features

### Cow Detection and Tracking
- Detects cows in images using YOLO11m model
- Tracks multiple cows in video with BoTSORT tracker
- Draws bounding boxes with confidence scores
- Saves annotated output images and videos

### Pathfinding Algorithms
- Visual demonstration of A* algorithm (with and without obstacles)
- Visual demonstration of D* Lite algorithm
- Real-time animation showing algorithm progression
- Color-coded visualization:
  - Blue: Start point
  - Yellow: Goal point
  - Green: Open set (being explored)
  - Red: Closed set (already processed)
  - Purple: Final path
  - Black: Obstacles (walls)

## Output

### Cow Detection
- Annotated images saved in `output_images/` directory
- Tracked video saved as `cow_tracked_output.mp4` (in runs folder)

### Pathfinding
- Real-time visualization in pygame window
- No file output (visualization only)

## Notes

- Ensure all input files (images, videos, model weights) are in the same directory as the scripts
- For the notebook, cells should be run in order
- The YOLO model will automatically download if not present
- Pathfinding algorithms use pygame for visualization and require a display

## Troubleshooting

### Issue: Module not found
Solution: Install the required dependencies using pip

### Issue: YOLO model not loading
Solution: Ensure `yolo11m.pt` is in the correct directory or let ultralytics download it automatically

### Issue: Pygame window not responding
Solution: Make sure you have a proper display environment. On some systems, you may need to install additional graphics libraries

### Issue: Video codec error
Solution: Install ffmpeg:
- Windows: Download from ffmpeg.org
- Linux: `sudo apt-get install ffmpeg`
- macOS: `brew install ffmpeg`

## License

This project is for educational and research purposes.
