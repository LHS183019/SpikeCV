# SNNTracker (spikecv track) Skill

要检查是否安装了 tracking 的依赖包
确保路径在SpikeCV

下载数据
pip install -U openi -i https://pypi.tuna.tsinghua.edu.cn/simple



This skill provides an interface to the `SNNTracker` algorithm for tracking objects in spike camera data.

## Features
- Calibrates motion using STP filters.
- Tracks multiple objects based on spike density and Saccade-inspired attention.
- Outputs trajectory data in JSON and MOT-style text formats.

## Parameters for `track` command

| Parameter | Alias | Default | Description |
|-----------|-------|---------|-------------|
| `--data_path` | `-d` | (Required) | Path to the spike data file (e.g., `.dat`) or directory. |
| `--algorithm` | | `snntracker` | Tracking algorithm. Currently only `snntracker` is supported. |
| `--attention_size` | `-attn` | `15` | Size of the attention window (pixels). |
| `--calibration_time`| `-calib`| `150` | Number of frames used for initial motion calibration. |
| `--block_len` | `-len` | `1000` | Total number of spike frames to process. |
| `--scale` | | `1` | Downscale factor for input spikes (integers > 1). |
| `--output_dir` | `-o` | `results` | Directory where results will be stored. |
| `--label_type` | `-l` | `tracking` | Type of metadata/label to load for the dataset. |
| `--cpu` | | `False` | Force execution on CPU even if CUDA is available. |

## Response Format
The tool returns a JSON object:
```json
{
  "status": "success",
  "result": {
    "tracking_file": "path/to/result_snn.txt",
    "output_dir": "path/to/results",
    "parameters": { ... }
  },
  "message": "Tracking completed successfully."
}
```

## Example Usage

### Tracking a specific scene
```bash
python spikecv_cli.py track -d path/to/dataset/scene_name -len 2000 -attn 20
```

### Forcing CPU execution
```bash
python spikecv_cli.py track -d path/to/data -cpu
```
