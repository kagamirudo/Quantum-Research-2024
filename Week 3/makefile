# Makefile to manage lydon.py and booth.py

# Variables
PYTHON = python3
LYDON = lydon.py
BOOTH = booth.py
INPUT_FILE = words_109583.txt
OUTPUT_FILES = booth.txt lydon.txt

# Default target
all: run

# Run both scripts: booth first, then lydon
run: booth lydon

# Target to run booth.py
booth: $(BOOTH)
	@echo "Running Booth's algorithm..."
	$(PYTHON) $^
	@echo "----------------------------"

# Target to run lydon.py
lydon: $(LYDON)
	@echo "Running Lydon script..."
	$(PYTHON) $^
	@echo "----------------------------"

# Clean target to remove output files
clean:
	@echo "Cleaning up output files..."
	rm -f $(OUTPUT_FILES)

# Help target to display usage
help:
	@echo "Makefile commands:"
	@echo "  make           Run the booth.py and lydon.py scripts."
	@echo "  make clean     Remove output files: $(OUTPUT_FILES)."
	@echo "  make help      Display this help message."

.PHONY: all run booth lydon clean help
