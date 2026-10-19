import shutil
import logging
from pathlib import Path
from categories import get_file_category

logger = logging.getLogger(__name__)

def move_file(file_path, target_folder, dry_run):
    """Moves a file to the target folder, handling existing files and dry runs."""
    target_folder.mkdir(parents=True, exist_ok=True)
    destination = target_folder / file_path.name
    
    if destination.exists():
        logger.warning("Skip: %s already exists in %s", file_path.name, target_folder.name)
        return

    if dry_run:
        logger.info("[DRY RUN] Would move %s to %s/", file_path.name, target_folder.name)
    else:
        try:
            shutil.move(file_path, destination)
            logger.info("Moved %s to %s/", file_path.name, target_folder.name)
        except Exception as e:
            logger.error("Failed to move %s: %s", file_path.name, e)

def organize_directory(directory_path, dry_run):
    """Iterates through a directory and organizes files into categorized subfolders."""
    if not directory_path.exists() or not directory_path.is_dir():
        logger.error("Directory '%s' does not exist or is not a directory.", directory_path)
        return

    logger.debug("Starting organization for directory: %s", directory_path)
    
    for item in directory_path.iterdir():
        if item.is_file():
            category = get_file_category(item.suffix)
            target_folder = directory_path / category
            logger.debug("Categorized %s as %s", item.name, category)
            move_file(item, target_folder, dry_run)
            
    logger.debug("Finished organization for directory: %s", directory_path)
