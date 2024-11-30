# Hockey CV Analysis System

## Assignment Achievements
- **Problem 1**: Entity Detection (Hockey Players, Referee, Puck, Goalpost, Scoreboard)
- **Problem 4**: Commentary Generation

## System Overview
This system is a comprehensive hockey video analysis tool that leverages YOLO for object detection and includes advanced features like player tracking, jersey color analysis, and AI-generated commentary.

## Prerequisites
- Python 3.8+
- Required API Keys:
  - Roboflow API Key
  - Gemini API Key
  - Eleven Labs AI Key
- Pre-trained YOLO model

## Installation
1. Clone the repository
2. Download the pre-trained YOLO model from the [Google Drive link](https://drive.google.com/file/d/1ZT1WK2jCKyJFSKZ1A7VvFftWF4hm7jkb/view?usp=sharing) and place it in the root directory of the project.
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure
```
hockey-cv-project/
│
├── main.py                 # Main pipeline execution
├── inference.py            # Default model inference
├── commentary_demo.ipynb   # Commentary generation demo
│
├── hockey_yolo.ipynb       # Model training notebook
│  
├── llm_commentary/
│   └── llm_commentary.py   # LLM commentary generation script
│
├── input_videos/           # Input video files
├── output_videos/          # Processed video outputs (AVI format)
├── output_commentary/      # Generated commentary audio files
├── output_stubs/           # Stub files
├── team_assigner/          # Team assignment logic
├── trackers/               # Player tracking components
└── utils/                  # Utility scripts and functions
```

## Configuration

### API Key Setup
1. Open `llm_commentary/llm_commentary.py`
2. Add your API keys( Gemini and ElevenLabs)
3. In `hockey_yolo.ipynb`, add your Roboflow API key:
  

## Running the System

### Commentary Generation
Open and run `commentary_demo.ipynb` to test the AI-generated commentary.

### Full Pipeline
```bash
python main.py
```
- Processes input hockey videos
- Detects players, referee, puck, etc.
- Generates colored markers with player numbers
- Creates video output in `output_videos/`

### Inference
```bash
python inference.py
```
- Runs inference on the pre-trained YOLO model
- Displays all detected entities (players, goalpost, scoreboard)
- Prints output video save location



## Key Features
- YOLO-based object detection
- Player number and jersey color tracking
- AI-generated commentary
- Voice-synthesized commentary audio

## Output Details
- Video Output: AVI format (recommended player: VLC)
- Commentary: MP3 format
- Markers: Colored based on average jersey color
- Player markers include player numbers

## Troubleshooting
- Ensure all API keys are correctly set
- Check Python and dependency versions
- Verify video input format compatibility

