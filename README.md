# Cow Detection and Tracking Project

This project contains implementations for cow detection and tracking using YOLO, along with pathfinding algorithms (A* and D* Lite) for visualization purposes.

## Project Structure

```
Cow_detection_tracking/
├── Cow.ipynb                  # Jupyter notebook for cow detection and tracking
├── a_star_algorithm.py        # A* pathfinding without obstacles
├── a_star_obstacle.py         # A* pathfinding with obstacles
├── d_star_algorithm.py        # D* Lite pathfinding algorithm
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

### Step 1: Create Virtual Environment (Recommended for Python Scripts)

For running the pathfinding algorithms (a_star_algorithm.py, a_star_obstacle.py, d_star_algorithm.py), it's recommended to use a virtual environment:

#### On Windows:
```bash
# Navigate to project directory
cd d:\Workspace\Cow_detection_tracking

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

#### On Linux/macOS:
```bash
# Navigate to project directory
cd /path/to/Cow_detection_tracking

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 2: Install Python Dependencies

Once the virtual environment is activated (you should see `(venv)` in your terminal), install the required packages:

For pathfinding algorithms only:
```bash
pip install pygame
```

For cow detection and tracking (if running locally):
```bash
pip install ultralytics opencv-python ipython jupyter
```

Or install all dependencies at once:
```bash
pip install pygame ultralytics opencv-python ipython jupyter
```

### Step 3: Deactivate Virtual Environment (When Done)

After you're finished working, deactivate the virtual environment:
```bash
deactivate
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

#### Option B: Run Locally with Jupyter
1. Activate virtual environment (if created):
```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

2. Install Jupyter (if not already installed):
```bash
pip install jupyter
```

3. Launch Jupyter Notebook:
```bash
jupyter notebook
```

4. Open `Cow.ipynb` in the browser
5. Run cells sequentially from top to bottom

#### Option C: Run with VS Code
1. Open the notebook in VS Code
2. Select Python kernel (choose the venv interpreter if using virtual environment)
3. Run cells sequentially

### 2. A* Algorithm (No Obstacles)

Make sure your virtual environment is activated, then run:

```bash
# Activate venv first (Windows)
venv\Scripts\activate

# Or on Linux/macOS
source venv/bin/activate

# Run the script
python a_star_algorithm.py
```

Controls:
- Press SPACE to start the A* algorithm animation
- Press R to restart
- Press ESC or Q to quit

### 3. A* Algorithm (With Obstacles)

With virtual environment activated:

```bash
python a_star_obstacle.py
```

Controls:
- Press SPACE to start the A* algorithm animation
- Press R to restart after completion
- Press ESC or Q to quit

### 4. D* Lite Algorithm

With virtual environment activated:

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

## Quick Start Summary

### For Pathfinding Algorithms:
```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/macOS

# 2. Install dependencies
pip install pygame

# 3. Run any script
python a_star_algorithm.py
python a_star_obstacle.py
python d_star_algorithm.py

# 4. Deactivate when done
deactivate
```

### For Jupyter Notebook:
```bash
# Option 1: Upload to Google Colab and run directly
# Option 2: Run locally with Jupyter
venv\Scripts\activate
pip install jupyter ultralytics opencv-python ipython
jupyter notebook
# Open Cow.ipynb and run cells
```

## Notes

- Ensure all input files (images, videos, model weights) are in the same directory as the scripts
- For the notebook, cells should be run in order
- The YOLO model will automatically download if not present
- Pathfinding algorithms use pygame for visualization and require a display
- Always activate the virtual environment before running Python scripts
- The virtual environment folder `venv/` should be added to `.gitignore` if using version control

## Troubleshooting

### Issue: Module not found
Solution: Make sure virtual environment is activated and dependencies are installed using pip

### Issue: Virtual environment not activating
Solution: 
- Windows: Try `venv\Scripts\Activate.ps1` for PowerShell or `venv\Scripts\activate.bat` for Command Prompt
- Check if Python is properly installed and added to PATH

### Issue: YOLO model not loading
Solution: Ensure `yolo11m.pt` is in the correct directory or let ultralytics download it automatically

### Issue: Pygame window not responding
Solution: Make sure you have a proper display environment. On some systems, you may need to install additional graphics libraries

### Issue: Video codec error
Solution: Install ffmpeg:
- Windows: Download from ffmpeg.org
- Linux: `sudo apt-get install ffmpeg`
- macOS: `brew install ffmpeg`

### Issue: Permission denied when creating venv
Solution: Run terminal as administrator or check Python installation permissions

## License

This project is for educational and research purposes.
