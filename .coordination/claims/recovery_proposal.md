import json
import logging
from typing import Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpportunitiesLedger:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> Dict[str, Any]:
        """Load JSON data from the specified file."""
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            logger.error(f"File not found: {self.file_path}")
            raise e
        except json.JSONDecodeError as e:
            logger.error("Error decoding JSON data.")
            raise e

    def validate_data(self) -> None:
        """Validate the loaded data for integrity."""
        if not isinstance(self.data, dict):
            logger.error("Data is not a valid dictionary.")
            raise ValueError("Invalid data format.")
        
        expected_keys = {'record_count', 'distinct_keys', 'last_run'}
        if not expected_keys.issubset(self.data.keys()):
            logger.error("Missing expected keys in data.")
            raise KeyError(f"Expected keys: {expected_keys}, found: {self.data.keys()}")

    def check_record_count(self) -> None:
        """Check for discrepancies in record counts."""
        current_count = self.data.get('record_count', 0)
        distinct_keys = self.data.get('distinct_keys', 0)

        if current_count != distinct_keys:
            logger.warning(f"Record count mismatch: current={current_count}, distinct={distinct_keys}")
            self.propose_correction(current_count, distinct_keys)

    def propose_correction(self, current_count: int, distinct_keys: int) -> None:
        """Propose a correction for the record count discrepancy."""
        logger.info("Proposing correction for record count discrepancy.")
        difference = abs(current_count - distinct_keys)
        logger.info(f"Difference in counts: {difference}")

        # Adjust the record count to match distinct keys if necessary
        if current_count < distinct_keys:
            logger.info("Adjusting record count to match distinct keys.")
            self.data['record_count'] = distinct_keys
            self.save_data()

    def save_data(self) -> None:
        """Save the updated data back to the file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.data, file, indent=4)
            logger.info("Data saved successfully.")
        except Exception as e:
            logger.error("Failed to save data.")
            raise e

def main() -> None:
    ledger_path = '/opt/PROD/overdrive/opportunities.json'  # Adjust the path as necessary
    ledger = OpportunitiesLedger(ledger_path)

    try:
        ledger.validate_data()
        ledger.check_record_count()
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()