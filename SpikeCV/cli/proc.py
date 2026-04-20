import typer
from argparse import Namespace

try:
    from spikecv.examples import test_snntracker as snn_tracker
except ImportError:
    snn_tracker = None

app = typer.Typer(name="proc", 
                  help="Commands related to spkProc in SpikeCV.", 
                  no_args_is_help=True)


@app.command(name="track", 
             help="Run the tracking module of SpikeCV. Using SNNTracker as default.", 
             short_help="Run tracking module",
             no_args_is_help=True)
def track(
    algorithm: str = typer.Option("snn_tracker", "--algorithm", "-a", help="Tracking algorithm to use. Currently only 'snn_tracker' is supported."),
    scene_idx: int = typer.Option(0, "--scene-idx", "-s", 
                                  help="Index of the test scene. 0: spike59, 1: rotTrans, 2: cplCam, 3: cpl1, 4: ball, 5: badminton, 6: pingpong"),
    attention_size: int = typer.Option(15, "--attention-size", "-attn_size", help="Size of attention window"),
    data_path: str = typer.Option("motVidarReal2020/", "--data-path", "-d", help="Path to dataset root"),
    label_type: str = typer.Option("tracking", "--label-type", "-l", help="Label type"),
    metrics: bool = typer.Option(False, "--metrics", "-m", help="Enable quantitative metrics (requires GT)"),
):
    """
    Run the tracking module of SpikeCV. Using SNNTracker as default.
    """
    
    if algorithm != "snn_tracker":
        typer.echo(f"Error: Unsupported algorithm '{algorithm}'. Currently only 'snn_tracker' is supported.", err=True)
        raise typer.Exit(1)
    
    typer.echo("Running the tracking module of SpikeCV...")
    
    if snn_tracker is None:
        typer.echo("Error: Could not import snn_tracker from spikecv.examples.test_snntracker", err=True)
        raise typer.Exit(1)
    if metrics and scene_idx not in [0,1]:
        typer.echo("Error: Metrics can only be enabled for scenes with ground truth (0: spike59 and 1: rotTrans).", err=True)
        raise typer.Exit(1)

    args = Namespace(
        scene_idx=scene_idx,
        attention_size=attention_size,
        data_path=data_path,
        label_type=label_type,
        metrics=metrics,
    )
    try:
        snn_tracker.main(args)
    except Exception as e:
        typer.echo(f"Error while running the tracking module: {e}", err=True)
        raise typer.Exit(1)
    
    
