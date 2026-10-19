import argparse
import logging
from pathlib import Path
from organizer import organize_directory

def setup_logging(verbose):
    """Configures the logging level based on the verbose flag."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def setup_arguments():
    """Parses command-line arguments for the tool."""
    parser = argparse.ArgumentParser(
        description="A command-line tool to organize files in a directory by extension.",
        epilog="Example: python main.py ./downloads --verbose --dry-run"
    )
    parser.add_argument(
        "target_dir", 
        type=str, 
        help="Relative or absolute path to the directory to organize."
    )
    parser.add_argument(
        "--dry-run", 
        action="store_true", 
        help="Simulate the organization without moving any files."
    )
    parser.add_argument(
        "-v", "--verbose", 
        action="store_true", 
        help="Enable detailed diagnostic logging (DEBUG level)."
    )
    return parser.parse_args()

def main():
    """Main execution entry point."""
    args = setup_arguments()
    setup_logging(args.verbose)
    
    target_dir = Path(args.target_dir)
    app_logger = logging.getLogger("main")
    
    app_logger.info("Starting file organizer tool.")
    organize_directory(target_dir, args.dry_run)
    app_logger.info("File organization process complete.")

if __name__ == "__main__":
    main()
