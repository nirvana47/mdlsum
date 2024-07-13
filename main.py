import typer
from pathlib import Path
from mdlsum.download import download_video
from mdlsum.transcribe import transcribe_audio
from mdlsum.summarize import summarize_text

app = typer.Typer()

@app.command()
def process_video(video_url: str):
    """
    Download, transcribe, and summarize a YouTube video.
    """
    try:
        # Download video
        audio_file = download_video(video_url)
        
        # Transcribe audio
        transcript = transcribe_audio(audio_file)
        
        # Summarize transcript
        summary = summarize_text(transcript)
        
        # Save summary to file
        output_file = Path(audio_file).with_suffix('.txt')
        with open(output_file, 'w') as f:
            f.write(summary)
        
        # Display summary in terminal
        typer.echo(f"Summary saved to: {output_file}")
        typer.echo("\nSummary:")
        typer.echo(summary)
    
    except Exception as e:
        typer.echo(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app()