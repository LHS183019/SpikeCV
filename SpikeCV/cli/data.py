import typer

app = typer.Typer(name="data", 
                  help="Commands related to data handling in SpikeCV.", 
                  no_args_is_help=True)


@app.command(name="download",
             help="Download datasets for SpikeCV.",
             short_help="Download datasets",
             no_args_is_help=True)
def download(
    dataset: str = typer.Option("motVidarReal2020", "--dataset", "-d", help="Dataset to download. Currently only 'motVidarReal2020'(dataset for tracking) is supported.")
):
    url = {
        "motVidarReal2020": "https://github.com/Zyj061/snnTracker/raw/main/datasets/motVidarReal2020.zip"
    }
    typer.echo("Downloading datasets for SpikeCV...")