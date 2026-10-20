import json
import logging
from typing import Dict, Any, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpportunitiesLedger:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data: List[Dict[str, Any]] = self.load_data()

    def load_data(self) -> List[Dict[str, Any]]:
        """Load opportunities data from JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                logger.info("Successfully loaded data from %s", self.file_path)
                return data
        except FileNotFoundError as e:
            logger.error("File not found: %s", e)
            raise
        except json.JSONDecodeError as e:
            logger.error("Error decoding JSON: %s", e)
            raise

    def get_record_count(self) -> int:
        """Return the number of records in the ledger."""
        return len(self.data)

    def get_distinct_keys_count(self) -> int:
        """Return the count of distinct keys in the records."""
        distinct_keys = {key for record in self.data for key in record.keys()}
        return len(distinct_keys)

    def validate_integrity(self) -> None:
        """Validate the integrity of the ledger data."""
        record_count = self.get_record_count()
        distinct_keys_count = self.get_distinct_keys_count()
        
        logger.info("Current record count: %d", record_count)
        logger.info("Distinct keys in records: %d", distinct_keys_count)

        if record_count != distinct_keys_count:
            logger.warning("Discrepancy detected: %d records vs %d distinct keys", record_count, distinct_keys_count)
            # Additional logic to handle discrepancies can be added here

class OverdriveState:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.state_data: Dict[str, Any] = self.load_state()

    def load_state(self) -> Dict[str, Any]:
        """Load state data from JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                state = json.load(file)
                logger.info("Successfully loaded state from %s", self.file_path)
                return state
        except FileNotFoundError as e:
            logger.error("File not found: %s", e)
            raise
        except json.JSONDecodeError as e:
            logger.error("Error decoding JSON: %s", e)
            raise

    def check_state_transition(self) -> bool:
        """Check if there has been a state transition."""
        state_changed = self.state_data.get("state_changed", False)
        logger.info("State changed: %s", state_changed)
        return state_changed

def main():
    # Paths to the JSON files (update these paths based on the repo structure)
    opportunities_path = '.coordination/overdrive/opportunities.json'
    state_path = '.coordination/overdrive/state.json'

    # Initialize ledger and state objects
    ledger = OpportunitiesLedger(opportunities_path)
    state = OverdriveState(state_path)

    # Validate integrity of the opportunities ledger
    ledger.validate_integrity()

    # Check for state transitions
    if not state.check_state_transition():
        logger.warning("No state transition detected in the latest execution window.")

if __name__ == "__main__":
    main()