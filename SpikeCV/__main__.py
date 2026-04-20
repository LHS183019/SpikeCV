import typer
from cli import proc

# 创建主 CLI 应用
app = typer.Typer(
    name="SpikeCV", 
    help="SpikeCV: An open-source framework for Spiking Computer Vision.",
    epilog="Use 'spikecv [COMMAND] --help' for more information on a command.",
    short_help="SpikeCV CLI",
    no_args_is_help=True
    )

# 加载子命令
app.add_typer(proc.app) # spkProc 相关命令

if __name__ == "__main__":
    app()