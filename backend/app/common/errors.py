import traceback
import logging

def error_logger(error: Exception, error_id: str):
    tb = traceback.extract_tb(error.__traceback__)
    
    # Log full error path
    error_path = " -> ".join(frame.name for frame in tb)

    frame = tb[-1]
    logging.error(f"\nERROR: {str(error)}")
    logging.error(f"   path:  {error_path}")
    logging.error(f"   file:  {frame.filename}")
    logging.error(f"   line:  {frame.lineno}")
    logging.error(f"   func:  {frame.name}")
    logging.error(f"   code:  {frame.line}")
    logging.error(f"   id:    {error_id}\n")